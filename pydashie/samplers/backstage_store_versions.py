#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests

from pydashie.dashie_sampler import DashieSampler


class BackstageStoreVersions(DashieSampler):
    def name(self):
        return 'backstage-store-versions'

    def sample(self):
        data = [
            ('QA', 'http://api.store-qa.backstage.globoi.com/api/version/'),
            ('Prod', 'http://api.store.backstage.globoi.com/api/version/'),
        ]

        items = []
        for label, url in data:
            resp = requests.get(url)
            version = resp.json().get('version', '')
            items.append({'label': label, 'value': version})

        return {'items': items}
