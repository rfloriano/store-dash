from dashie_sampler import DashieSampler

import os
import random
import collections
import requests


class OmniVersions(DashieSampler):
    def __init__(self, *args, **kwargs):
        self.api_url = 'http://local.globoi.com:2369/api/applications/list/'
        DashieSampler.__init__(self, *args, **kwargs)

    def name(self):
        return 'omni-versions'

    def sample(self):
        resp = requests.get(self.api_url)
        applications = resp.json().get('applications', [])
        items = []
        for app in applications:
            url = os.path.join(app.get('url'), 'admin/omni-store/version/')
            data = requests.get(url).json()
            items.append({
                'label': app.get('title', 'undef'),
                'value': data.get('version', 'undef')
            })
        return {'items': items}


class SynergySampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        self._last = 0
        DashieSampler.__init__(self, *args, **kwargs)

    def name(self):
        return 'synergy'

    def sample(self):
        s = {'value': random.randint(0, 100),
             'current': random.randint(0, 100),
             'last': self._last}
        self._last = s['current']
        return s


class BuzzwordsSampler(DashieSampler):
    def name(self):
        return 'buzzwords'

    def sample(self):
        my_little_pony_names = ['Rainbow Dash',
                                'Blossomforth',
                                'Derpy',
                                'Fluttershy',
                                'Lofty',
                                'Scootaloo',
                                'Skydancer']
        items = [{'label': pony_name, 'value': random.randint(0, 20)} for pony_name in my_little_pony_names]
        random.shuffle(items)
        return {'items': items}


class ConvergenceSampler(DashieSampler):
    def name(self):
        return 'convergence'

    def __init__(self, *args, **kwargs):
        self.seedX = 0
        self.items = collections.deque()
        DashieSampler.__init__(self, *args, **kwargs)

    def sample(self):
        self.items.append({'x': self.seedX,
                           'y': random.randint(0, 20)})
        self.seedX += 1
        if len(self.items) > 10:
            self.items.popleft()
        return {'points': list(self.items)}
