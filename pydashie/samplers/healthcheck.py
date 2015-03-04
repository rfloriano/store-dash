#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests

from pydashie.dashie_sampler import DashieSampler


class Healthcheck(DashieSampler):
    def name(self):
        return 'healthcheck'

    def sample(self):
        data = [
            ('QA-API', 'http://api.store-qa.backstage.globoi.com/healthcheck/'),
            ('QA-Web', 'http://store-qa.backstage.globoi.com/healthcheck/'),
            ('Prod-API', 'http://api.store.backstage.globoi.com/healthcheck/'),
            ('Prod-Web', 'http://store.backstage.globoi.com/healthcheck/'),
        ]

        items = []
        failed = False
        for label, url in data:
            resp = requests.get(url)
            if 'WORKING' not in resp:
                failed = True
            items.append({'label': label, 'value': resp.text})

        return {'items': items, 'failed': failed}
