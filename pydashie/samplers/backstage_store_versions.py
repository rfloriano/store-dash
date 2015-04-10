#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests

from pydashie.dashie_sampler import DashieSampler


class BackstageStoreVersions(DashieSampler):
    def name(self):
        return 'backstage-store-versions'

    def sample(self):
        data = [
            ('QA-API', 'http://api.store-qa.backstage.globoi.com/api/version/'),
            ('QA-Web', 'http://store-qa.backstage.globoi.com/version'),
            ('Prod-API', 'http://api.store.backstage.globoi.com/api/version/'),
            ('Prod-Web', 'http://store.backstage.globoi.com/version'),
        ]

        items = []
        for label, url in data:
            resp = requests.get(url)
            try:
                version = resp.json().get('version', '')
            except:
                version = ''
            items.append({'label': label, 'value': version})

        return {'items': items}
