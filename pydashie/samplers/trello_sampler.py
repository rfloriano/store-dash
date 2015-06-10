from pydashie.dashie_sampler import DashieSampler

import trello


class TrelloSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        key = '00ca4ffbe198c58151dc431f8443b94f'
        token = 'ffda4648a2ea629a706e6e3fc938bb7f3d967fe6db3736b3c10ed33677313ad6'
        try:
            self.api = trello.TrelloApi(key)
            self.api.set_token(token)
            DashieSampler.__init__(self, *args, **kwargs)
        except:
            self.api = None

    def name(self):
        return 'trello'

    def sample(self):
        if self.api is None:
            return {}

        cards = self.api.lists.get_card('543c0dd47693971e54abf1c2')
        items = []
        for card in cards:
            members = []
            for member_id in card.get('idMembers', []):
                members.append(self.api.members.get(member_id))

            members = ', '.join([member.get('fullName', 'undef').split(' ')[0]
                                for member in members])
            items.append({
                'label': '%s: %s ' % (members, card.get('name', 'undef'))
            })
        return {'items': items}
