# -*- coding: utf-8 -*-
from politikus.ocds.interfaces import IPolitikusOcdsLayer
from politikus.ocds.testing import POLITIKUS_OCDS_FUNCTIONAL_TESTING
from politikus.ocds.testing import POLITIKUS_OCDS_INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.Five.browser import BrowserView
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides
from zope.viewlet.interfaces import IViewletManager

from politikus.ocds.behaviors.document_type import IDocumentTypeMarker
import unittest


class ViewletIntegrationTest(unittest.TestCase):

    layer = POLITIKUS_OCDS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.app = self.layer['app']
        self.request = self.app.REQUEST
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Document', 'other-document')
        api.content.create(self.portal, 'News Item', 'newsitem')

    def test_document_type_viewlet_is_registered(self):
        alsoProvides(self.portal['other-document'], IDocumentTypeMarker)
        view = BrowserView(self.portal['other-document'], self.request)
        manager_name = 'plone.belowcontentbody'
        alsoProvides(self.request, IPolitikusOcdsLayer)
        manager = queryMultiAdapter(
            (self.portal['other-document'], self.request, view),
            IViewletManager,
            manager_name,
            default=None
        )
        self.assertIsNotNone(manager)
        manager.update()
        my_viewlet = [v for v in manager.viewlets if v.__name__ == 'document-type-viewlet']  # NOQA: E501
        self.assertEqual(len(my_viewlet), 1)

    # XXX would be nice to have this test working:
    # def test_document_type_viewlet_is_not_available_on_newsitem(self):
    #     view = BrowserView(self.portal['newsitem'], self.request)
    #     manager_name = 'plone.belowcontentbody'
    #     alsoProvides(self.request, IPolitikusOcdsLayer)
    #     manager = queryMultiAdapter(
    #         (self.portal['newsitem'], self.request, view),
    #         IViewletManager,
    #         manager_name,
    #         default=None
    #     )
    #     self.assertIsNotNone(manager)
    #     manager.update()
    #     my_viewlet = [v for v in manager.viewlets if v.__name__ == 'document-type-viewlet']  # NOQA: E501
    #     self.assertEqual(len(my_viewlet), 0)


class ViewletFunctionalTest(unittest.TestCase):

    layer = POLITIKUS_OCDS_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
