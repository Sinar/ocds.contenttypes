# -*- coding: utf-8 -*-
from politikus.ocds.behaviors.related_awards import IRelatedAwardsMarker
from politikus.ocds.testing import POLITIKUS_OCDS_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class RelatedAwardsIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_OCDS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_related_awards(self):
        behavior = getUtility(IBehavior, 'politikus.ocds.related_awards')
        self.assertEqual(
            behavior.marker,
            IRelatedAwardsMarker,
        )
