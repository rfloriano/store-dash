#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from requests.exceptions import ConnectionError


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

        failed = False
        items = []
        for label, url in data:
            try:
                resp = requests.get(url)
                value = 'WORKING'
                if 'WORKING' not in resp.text:
                    value = 'Failed'
                    failed = True
                items.append({'label': label, 'value': value})
            except ConnectionError:
                items.append({'label': label, 'value': 'Failed'})
                failed = True

        return {'items': items, 'failed': failed}
