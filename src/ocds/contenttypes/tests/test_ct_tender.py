# -*- coding: utf-8 -*-
from ocds.contenttypes.content.tender import ITender  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class TenderIntegrationTest(unittest.TestCase):

    layer = OCDS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'OCDS Release',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_tender_schema(self):
        fti = queryUtility(IDexterityFTI, name='Tender')
        schema = fti.lookupSchema()
        self.assertEqual(ITender, schema)

    def test_ct_tender_fti(self):
        fti = queryUtility(IDexterityFTI, name='Tender')
        self.assertTrue(fti)

    def test_ct_tender_factory(self):
        fti = queryUtility(IDexterityFTI, name='Tender')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITender.providedBy(obj),
            u'ITender not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_tender_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Tender',
            id='tender',
        )

        self.assertTrue(
            ITender.providedBy(obj),
            u'ITender not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('tender', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('tender', parent.objectIds())

    def test_ct_tender_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Tender')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_tender_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Tender')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'tender_id',
            title='Tender container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
