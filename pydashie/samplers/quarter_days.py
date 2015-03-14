#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

from pydashie.dashie_sampler import DashieSampler

URL = 'http://dash.appdev.globoi.com:8000/quarter/goals/'


class QuarterDays(DashieSampler):
    def name(self):
        return 'quarter-days'

    def sample(self):
        resp = requests.get(URL)
        data = resp.json()
        quarter = data['quarters'][0]
        title = quarter.get('name', 'err') + ' days'
        return {
            'current': quarter.get('remaining_days', 'err'),
            'moreinfo': 'in {0}'.format(title)
        }
