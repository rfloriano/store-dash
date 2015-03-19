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
        for label, url in data:
            resp = requests.get(url)
            value = 'WORKING'
            if 'WORKING' not in resp.text:
                value = 'Failed'
            items.append({'label': label, 'value': value})

        return {'items': items}
