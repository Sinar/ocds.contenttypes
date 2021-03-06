# -*- coding: utf-8 -*-
from ocds.contenttypes.content.contracting_process import IContractingProcess  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ContractingProcessIntegrationTest(unittest.TestCase):

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

    def test_ct_contracting_process_schema(self):
        fti = queryUtility(IDexterityFTI, name='Contracting Process')
        schema = fti.lookupSchema()
        self.assertEqual(IContractingProcess, schema)

    def test_ct_contracting_process_fti(self):
        fti = queryUtility(IDexterityFTI, name='Contracting Process')
        self.assertTrue(fti)

    def test_ct_contracting_process_factory(self):
        fti = queryUtility(IDexterityFTI, name='Contracting Process')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IContractingProcess.providedBy(obj),
            u'IContractingProcess not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_contracting_process_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Contracting Process',
            id='contracting_process',
        )

        self.assertTrue(
            IContractingProcess.providedBy(obj),
            u'IContractingProcess not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('contracting_process', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('contracting_process', parent.objectIds())

    def test_ct_contracting_process_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contracting Process')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_contracting_process_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contracting Process')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'contracting_process_id',
            title='Contracting Process container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
