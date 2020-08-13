# -*- coding: utf-8 -*-
from ocds.contenttypes.content.ocds_item import IOcdsItem  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class OcdsItemIntegrationTest(unittest.TestCase):

    layer = OCDS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Award',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_ocds_item_schema(self):
        fti = queryUtility(IDexterityFTI, name='ocds item')
        schema = fti.lookupSchema()
        self.assertEqual(IOcdsItem, schema)

    def test_ct_ocds_item_fti(self):
        fti = queryUtility(IDexterityFTI, name='ocds item')
        self.assertTrue(fti)

    def test_ct_ocds_item_factory(self):
        fti = queryUtility(IDexterityFTI, name='ocds item')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IOcdsItem.providedBy(obj),
            u'IOcdsItem not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_ocds_item_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='ocds item',
            id='ocds_item',
        )

        self.assertTrue(
            IOcdsItem.providedBy(obj),
            u'IOcdsItem not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('ocds_item', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('ocds_item', parent.objectIds())

    def test_ct_ocds_item_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='ocds item')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_ocds_item_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='ocds item')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'ocds_item_id',
            title='ocds item container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
