import os

from samplers.omni_versions import OmniVersions
from samplers.trello_sampler import TrelloSampler
from samplers.jenkins_build_status import JenkinsSampler
from samplers.backstage_store_versions import BackstageStoreVersions
from samplers.healthcheck import Healthcheck
from samplers.holmes_versions import HolmesVersions
from samplers.holmes_reviews import HolmesReviews
from samplers.quarter_days import QuarterDays
from samplers.quarter_goals import QuarterGoals


MINUTE = 60
HOUR = 60 * MINUTE


def run(app, xyzzy):
    samplers = [
        OmniVersions(xyzzy, 5 * MINUTE),
        BackstageStoreVersions(xyzzy, 5 * MINUTE),
        TrelloSampler(xyzzy, 10 * MINUTE),
        JenkinsSampler(xyzzy, MINUTE),
        Healthcheck(xyzzy, 1 * MINUTE),
        HolmesVersions(xyzzy, 5 * MINUTE),
        HolmesReviews(xyzzy, 5 * MINUTE),
        QuarterDays(xyzzy, 5 * MINUTE),
        QuarterGoals(xyzzy, 5 * MINUTE),
        # SynergySampler(xyzzy, 3),
        # BuzzwordsSampler(xyzzy, 2), # 10
        # ConvergenceSampler(xyzzy, 1),
    ]

    reload = os.environ.get('RELOAD', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', '5000'))

    try:
        app.run(debug=True,
                host='0.0.0.0',
                port=port,
                threaded=True,
                use_reloader=reload,
                use_debugger=True
                )
    finally:
        print "Disconnecting clients"
        xyzzy.stopped = True

        print "Stopping %d timers" % len(samplers)
        for (i, sampler) in enumerate(samplers):
            sampler.stop()

    print "Done"
