# -*- coding: utf-8 -*-
from ocds.contenttypes.content.infrastructure_project import IInfrastructureProject  # NOQA E501
from ocds.contenttypes.testing import OCDS_CONTENTTYPES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class InfrastructureProjectIntegrationTest(unittest.TestCase):

    layer = OCDS_CONTENTTYPES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_infrastructure_project_schema(self):
        fti = queryUtility(IDexterityFTI, name='Infrastructure Project')
        schema = fti.lookupSchema()
        self.assertEqual(IInfrastructureProject, schema)

    def test_ct_infrastructure_project_fti(self):
        fti = queryUtility(IDexterityFTI, name='Infrastructure Project')
        self.assertTrue(fti)

    def test_ct_infrastructure_project_factory(self):
        fti = queryUtility(IDexterityFTI, name='Infrastructure Project')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IInfrastructureProject.providedBy(obj),
            u'IInfrastructureProject not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_infrastructure_project_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Infrastructure Project',
            id='infrastructure_project',
        )

        self.assertTrue(
            IInfrastructureProject.providedBy(obj),
            u'IInfrastructureProject not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('infrastructure_project', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('infrastructure_project', parent.objectIds())

    def test_ct_infrastructure_project_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Infrastructure Project')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_infrastructure_project_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Infrastructure Project')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'infrastructure_project_id',
            title='Infrastructure Project container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
