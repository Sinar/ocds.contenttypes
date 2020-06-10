# -*- coding: utf-8 -*-
from ocds.contenttypes.behaviors.document_type import IDocumentTypeMarker
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class DocumentTypeIntegrationTest(unittest.TestCase):

    layer = OCDS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_document_type(self):
        behavior = getUtility(IBehavior, 'ocds.contenttypes.document_type')
        self.assertEqual(
            behavior.marker,
            IDocumentTypeMarker,
        )
