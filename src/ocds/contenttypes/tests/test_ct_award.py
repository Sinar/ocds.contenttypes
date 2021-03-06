# -*- coding: utf-8 -*-
from ocds.contenttypes.content.award import IAward  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class AwardIntegrationTest(unittest.TestCase):

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

    def test_ct_award_schema(self):
        fti = queryUtility(IDexterityFTI, name='Award')
        schema = fti.lookupSchema()
        self.assertEqual(IAward, schema)

    def test_ct_award_fti(self):
        fti = queryUtility(IDexterityFTI, name='Award')
        self.assertTrue(fti)

    def test_ct_award_factory(self):
        fti = queryUtility(IDexterityFTI, name='Award')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IAward.providedBy(obj),
            u'IAward not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_award_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Award',
            id='award',
        )

        self.assertTrue(
            IAward.providedBy(obj),
            u'IAward not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('award', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('award', parent.objectIds())

    def test_ct_award_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Award')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_award_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Award')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'award_id',
            title='Award container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
