# -*- coding: utf-8 -*-
from ocds.contenttypes.content.contract_process import IContractProcess  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ContractProcessIntegrationTest(unittest.TestCase):

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

    def test_ct_contract_process_schema(self):
        fti = queryUtility(IDexterityFTI, name='Contract Process')
        schema = fti.lookupSchema()
        self.assertEqual(IContractProcess, schema)

    def test_ct_contract_process_fti(self):
        fti = queryUtility(IDexterityFTI, name='Contract Process')
        self.assertTrue(fti)

    def test_ct_contract_process_factory(self):
        fti = queryUtility(IDexterityFTI, name='Contract Process')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IContractProcess.providedBy(obj),
            u'IContractProcess not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_contract_process_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Contract Process',
            id='contract_process',
        )

        self.assertTrue(
            IContractProcess.providedBy(obj),
            u'IContractProcess not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('contract_process', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('contract_process', parent.objectIds())

    def test_ct_contract_process_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contract Process')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_contract_process_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Contract Process')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'contract_process_id',
            title='Contract Process container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
