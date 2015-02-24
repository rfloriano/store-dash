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

            proxies = {}
            if 'staging' in app.get('url')\
               or 'staging' in app.get('title', '').lower()\
               or 'stg' in app.get('url')\
               or 'stg' in app.get('title', '').lower():
                proxies = {
                    'http': 'http://proxy.staging.globoi.com:3128',
                    'http': 'http://proxy.staging.globoi.com:3128',
                }
            url = os.path.join(app.get('url'), 'admin/omni-store/version/')
            print 'Getting version from {0}({1})'.format(app.get('title'), url)
            resp = None
            data = {}
            try:
                resp = requests.get(url, timeout=3, proxies=proxies)
                data = resp.json()
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.ReadTimeout, ValueError):
                pass
            if hasattr(resp, 'status_code') and resp.status_code == 404:
                data['version'] = 'none'
            items.append({
                'label': app.get('title', 'error'),
                'value': data.get('version', 'error')
            })
        return {'items': items}
