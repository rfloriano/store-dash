import os
from example_samplers import *
from samplers.trello_sampler import TrelloSampler
from samplers.jenkins_build_status import JenkinsSampler


MINUTE = 60
HOUR = 60 * MINUTE


def run(app, xyzzy):
    samplers = [
        OmniVersions(xyzzy, HOUR),
        TrelloSampler(xyzzy, 10 * MINUTE),
        JenkinsSampler(xyzzy, MINUTE),
        # SynergySampler(xyzzy, 3),
        # BuzzwordsSampler(xyzzy, 2), # 10
        # ConvergenceSampler(xyzzy, 1),
    ]

    reload = os.environ.get('RELOAD', 'False').lower() == 'true'

    try:
        app.run(debug=True,
                host='0.0.0.0',
                port=5000,
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
