# -*- coding: utf-8 -*-
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class OCDSDocumentIntegrationTest(unittest.TestCase):

    layer = OCDS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Infrastructure Project',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_o_c_d_s_document_schema(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Document')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('OCDS Document')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_o_c_d_s_document_fti(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Document')
        self.assertTrue(fti)

    def test_ct_o_c_d_s_document_factory(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Document')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_o_c_d_s_document_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='OCDS Document',
            id='o_c_d_s_document',
        )


        parent = obj.__parent__
        self.assertIn('o_c_d_s_document', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('o_c_d_s_document', parent.objectIds())

    def test_ct_o_c_d_s_document_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='OCDS Document')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
