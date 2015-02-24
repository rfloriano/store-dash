from pydashie.dashie_sampler import DashieSampler

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
            items.append({
                'label': app.get('title', 'error'),
                'value': app.get('omni-store', {}).get('version', 'error')
            })
        return {'items': items}
