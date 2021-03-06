# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import medialog.batchsize


class MedialogBatchsizeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=medialog.batchsize)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.batchsize:default')


MEDIALOG_BATCHSIZE_FIXTURE = MedialogBatchsizeLayer()


MEDIALOG_BATCHSIZE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEDIALOG_BATCHSIZE_FIXTURE,),
    name='MedialogBatchsizeLayer:IntegrationTesting',
)


MEDIALOG_BATCHSIZE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEDIALOG_BATCHSIZE_FIXTURE,),
    name='MedialogBatchsizeLayer:FunctionalTesting',
)


MEDIALOG_BATCHSIZE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEDIALOG_BATCHSIZE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MedialogBatchsizeLayer:AcceptanceTesting',
)
