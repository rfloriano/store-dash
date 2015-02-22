from pydashie.dashie_sampler import DashieSampler

import os
import requests


class OmniVersions(DashieSampler):
    def __init__(self, *args, **kwargs):
        self.api_url = 'http://api.store.backstage.globoi.com/api/applications/list/'
        DashieSampler.__init__(self, *args, **kwargs)

    def name(self):
        return 'omni-versions'

    def sample(self):
        resp = requests.get(self.api_url)
        applications = resp.json().get('applications', [])
        items = []
        for app in applications:
            if 'local' in app.get('url')\
               or 'local' in app.get('title', '').lower():
                continue
            url = os.path.join(app.get('url'), 'admin/omni-store/version/')
            print 'Getting version from {0}({1})'.format(app.get('title'), url)
            try:
                data = requests.get(url, timeout=3).json()
            except Exception:
                data = {}
            items.append({
                'label': app.get('title', 'undef'),
                'value': data.get('version', 'undef')
            })
        return {'items': items}
