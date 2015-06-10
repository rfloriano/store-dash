#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests

from pydashie.dashie_sampler import DashieSampler


class HolmesVersions(DashieSampler):
    def name(self):
        return 'holmes-versions'

    def sample(self):
        items = []
        try:
            resp = requests.get('http://holmes-api.cloud.globoi.com/version')
            if resp.status_code == 200:
                items.append({'label': 'API', 'value': resp.text})
            else:
                items.append({'label': 'API', 'value': 'Error'})
        except:
            items.append({'label': 'API', 'value': 'Error'})

        try:
            resp = requests.get('http://holmes.cloud.globoi.com/version.txt')
            if resp.status_code == 200:
                items.append({'label': 'Web', 'value': resp.text})
            else:
                items.append({'label': 'Web', 'value': 'Error'})
        except:
            items.append({'label': 'Web', 'value': 'Error'})

        return {'items': items}
