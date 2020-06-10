# -*- coding: utf-8 -*-
from ocds.contenttypes.content.modification import IModification  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ModificationIntegrationTest(unittest.TestCase):

    layer = OCDS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'ContractingProcess',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_modification_schema(self):
        fti = queryUtility(IDexterityFTI, name='Modification')
        schema = fti.lookupSchema()
        self.assertEqual(IModification, schema)

    def test_ct_modification_fti(self):
        fti = queryUtility(IDexterityFTI, name='Modification')
        self.assertTrue(fti)

    def test_ct_modification_factory(self):
        fti = queryUtility(IDexterityFTI, name='Modification')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IModification.providedBy(obj),
            u'IModification not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_modification_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Modification',
            id='modification',
        )

        self.assertTrue(
            IModification.providedBy(obj),
            u'IModification not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('modification', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('modification', parent.objectIds())

    def test_ct_modification_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Modification')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_modification_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Modification')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'modification_id',
            title='Modification container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
