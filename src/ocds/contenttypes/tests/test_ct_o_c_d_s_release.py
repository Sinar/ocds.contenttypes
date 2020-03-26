# -*- coding: utf-8 -*-
from ocds.contenttypes.content.o_c_d_s_release import IOCDSRelease  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class OCDSReleaseIntegrationTest(unittest.TestCase):

    layer = OCDS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_o_c_d_s_release_schema(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Release')
        schema = fti.lookupSchema()
        self.assertEqual(IOCDSRelease, schema)

    def test_ct_o_c_d_s_release_fti(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Release')
        self.assertTrue(fti)

    def test_ct_o_c_d_s_release_factory(self):
        fti = queryUtility(IDexterityFTI, name='OCDS Release')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IOCDSRelease.providedBy(obj),
            u'IOCDSRelease not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_o_c_d_s_release_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='OCDS Release',
            id='o_c_d_s_release',
        )

        self.assertTrue(
            IOCDSRelease.providedBy(obj),
            u'IOCDSRelease not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('o_c_d_s_release', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('o_c_d_s_release', parent.objectIds())

    def test_ct_o_c_d_s_release_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='OCDS Release')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_o_c_d_s_release_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='OCDS Release')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'o_c_d_s_release_id',
            title='OCDS Release container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
