from pydashie.dashie_sampler import DashieSampler

import requests
from requests.exceptions import ConnectionError


class OmniVersions(DashieSampler):
    def __init__(self, *args, **kwargs):
        self.api_url = 'http://api.store.backstage.globoi.com/api/applications/list/'
        DashieSampler.__init__(self, *args, **kwargs)

    def name(self):
        return 'omni-versions'

    def sample(self):
        try:
            resp = requests.get(self.api_url)
        except ConnectionError:
            return {}

        applications = resp.json().get('applications', [])
        items = []
        for app in applications:
            if 'local' in app.get('url')\
               or 'local' in app.get('title', '').lower():
                continue
            items.append({
                'label': app.get('title', 'error'),
                'value': app.get('omni-store', {}).get('version', 'error')
            })
        return {'items': sorted(items, key=lambda k: k['label'].lower())}
