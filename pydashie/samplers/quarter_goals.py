#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

from pydashie.dashie_sampler import DashieSampler

URL = 'http://dash.appdev.globoi.com:8000/quarter/goals/'


class QuarterGoals(DashieSampler):
    def name(self):
        return 'quarter-goals'

    def sample(self):
        resp = requests.get(URL)
        data = resp.json()
        quarter = data['quarters'][0]
        items = []
        for goal in quarter.get('goals', []):
            is_done = goal.get('is_done', False)
            mark = '☐'
            if is_done:
                mark = '✔'
            items.append({
                'label': '{0}: {1}'.format(mark, goal.get('name', 'err')),
            })
        return {
            'items': items,
            'title': 'Goals for {0}'.format(quarter.get('name', 'err')),
        }
