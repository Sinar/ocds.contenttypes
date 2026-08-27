# -*- coding: utf-8 -*-
from politikus.ocds.behaviors.related_o_c_d_s_releases import IRelatedOCDSReleasesMarker
from politikus.ocds.testing import POLITIKUS_OCDS_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class RelatedOCDSReleasesIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_OCDS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_related_o_c_d_s_releases(self):
        behavior = getUtility(IBehavior, 'politikus.ocds.related_o_c_d_s_releases')
        self.assertEqual(
            behavior.marker,
            IRelatedOCDSReleasesMarker,
        )
