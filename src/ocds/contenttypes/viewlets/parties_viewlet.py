# -*- coding: utf-8 -*-

from plone.app.layout.viewlets import ViewletBase
from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
from zc.relation.interfaces import ICatalog
from zope.schema.interfaces import IVocabularyFactory


class PartiesViewlet(ViewletBase):

    def backrefs(self, attribute_name, portal_type):
        """
        Return back references from source object on specified attribute_name
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)

        source_object = self.context
        result = []

        for rel in catalog.findRelations(
            dict(to_id=intids.getId(aq_inner(source_object)),
                 from_attribute=attribute_name)
              ):

            obj = intids.queryObject(rel.from_id)

            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == portal_type:

                    # Temporary workaround for broken objects
                    if obj.absolute_url():
                        result.append(obj)

        return result

    def infra(self, attribute_name, portal_type='Infrastructure Project'):
        return self.backrefs(attribute_name, portal_type)

    # untested
    def release(self, attribute_name, portal_type='OCDS Release'):
        return self.backrefs(attribute_name, portal_type)

    def render(self):
        return super(PartiesViewlet, self).render()
