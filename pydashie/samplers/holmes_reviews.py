#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests

from pydashie.dashie_sampler import DashieSampler


class HolmesReviews(DashieSampler):
    def name(self):
        return 'holmes-reviews'

    def sample(self):
        url = 'http://holmes-api.cloud.globoi.com/reviews-in-last-hour/'
        data = requests.get(url).json()
        total = float(data.get('count')) / data.get('ellapsed')
        return {'text': '%.2f por segundo' % total}
