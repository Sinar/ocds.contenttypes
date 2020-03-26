# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ocds.contenttypes


class OcdsContenttypesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=ocds.contenttypes)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ocds.contenttypes:default')


OCDS_CONTENTTYPES_FIXTURE = OcdsContenttypesLayer()


OCDS_CONTENTTYPES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(OCDS_CONTENTTYPES_FIXTURE,),
    name='OcdsContenttypesLayer:IntegrationTesting',
)


OCDS_CONTENTTYPES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(OCDS_CONTENTTYPES_FIXTURE,),
    name='OcdsContenttypesLayer:FunctionalTesting',
)


OCDS_CONTENTTYPES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        OCDS_CONTENTTYPES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='OcdsContenttypesLayer:AcceptanceTesting',
)
