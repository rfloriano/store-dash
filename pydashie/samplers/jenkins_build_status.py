from pydashie.dashie_sampler import DashieSampler

import requests

JENKINS_URI = "http://j.appdev.globoi.com/api/json?pretty=true"


class JenkinsSampler(DashieSampler):
    def name(self):
        return 'jenkinsBuildStatus'

    def sample(self):
        failed_jobs = []
        jobs = requests.get(JENKINS_URI).json()['jobs']

        for job in jobs:
            if job['color'] in ['disabled', 'notbuilt', 'blue', 'blue_anime']:
                continue

            if job['color'] in ['yellow', 'yellow_anime']:
                job_status = requests.get(job['url'] + 'lastUnstableBuild/api/json').json()
            else:
                job_status = requests.get(job['url'] + 'lastFailedBuild/api/json').json()

            culprits = []
            for culprit in job_status['culprits']:
                culpritName = culprit.get('fullName', '')
                if culpritName != '':
                    culpritName = culpritName.split('<')[0]
                culprits.append(culpritName)

            failed_jobs.append({
                'label': job['name'],
                'value': ', '.join(culprits)
            })

        return {
            'failedJobs': failed_jobs,
            'succeededJobs': [],
            'failed': len(failed_jobs) > 0
        }
