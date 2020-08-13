# -*- coding: utf-8 -*-
from ocds.contenttypes.content.o_c_d_s_item import IOCDSItem  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class OCDSItemIntegrationTest(unittest.TestCase):

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

    def test_ct_o_c_d_s_item_schema(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Item')
        schema = fti.lookupSchema()
        self.assertEqual(IOCDSItem, schema)

    def test_ct_o_c_d_s_item_fti(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Item')
        self.assertTrue(fti)

    def test_ct_o_c_d_s_item_factory(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Item')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IOCDSItem.providedBy(obj),
            u'IOCDSItem not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_o_c_d_s_item_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='OCDS Item',
            id='o_c_d_s_item',
        )

        self.assertTrue(
            IOCDSItem.providedBy(obj),
            u'IOCDSItem not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('o_c_d_s_item', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('o_c_d_s_item', parent.objectIds())

    def test_ct_o_c_d_s_item_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='OCDS Item')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_o_c_d_s_item_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='OCDS Item')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'o_c_d_s_item_id',
            title='OCDS Item container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
