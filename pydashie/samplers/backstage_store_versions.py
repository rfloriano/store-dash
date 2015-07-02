#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from distutils.version import LooseVersion

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
            try:
                resp = requests.get(url)
                version = resp.json().get('version', '')
            except:
                version = ''
            items.append({'label': label, 'value': version})

        data = [
            ('OmniStore', True, 'http://artifactory.globoi.com/artifactory/api/storage/pypi-local/omnistore'),
            ('OmniInstaller', False, 'http://artifactory.globoi.com/artifactory/api/storage/pypi-local/omni-installer'),
        ]

        for label, aux, url in data:
            try:
                resp = requests.get(url)
                versions = resp.json().get('children')
                versions = [x['uri'].replace('/', '') for x in versions]
                aux_version = ''
                if aux:
                    branch_version = [x for x in versions if x.startswith('0.4')]
                    branch_version.sort(key=LooseVersion)
                    items.append({'label': 'OmniStore 0.4', 'value': branch_version[-1]})
                versions.sort(key=LooseVersion)
                version = "%s%s" % (versions[-1], aux_version)
            except:
                version = ''
            items.append({'label': label, 'value': version})

        return {'items': items}
