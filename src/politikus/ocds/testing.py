# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import politikus.ocds


class PolitikusOcdsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=politikus.ocds)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'politikus.ocds:default')


POLITIKUS_OCDS_FIXTURE = PolitikusOcdsLayer()


POLITIKUS_OCDS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(POLITIKUS_OCDS_FIXTURE,),
    name='PolitikusOcdsLayer:IntegrationTesting',
)


POLITIKUS_OCDS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(POLITIKUS_OCDS_FIXTURE,),
    name='PolitikusOcdsLayer:FunctionalTesting',
)


POLITIKUS_OCDS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        POLITIKUS_OCDS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='PolitikusOcdsLayer:AcceptanceTesting',
)
