# -*- coding: utf-8 -*-

from ocds.contenttypes import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider
from plone.autoform import directives
from plone.app.z3cform.widget import SelectFieldWidget


class IDocumentTypeMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IDocumentType(model.Schema):
    """
    """

    directives.widget(DocumentType=SelectFieldWidget)
    DocumentType = schema.List(
                title=_(u'Document Type'),
                description=_(u'''
                OCDS classification of the document
                '''),

                default=[],
                value_type=schema.Choice(
                    vocabulary='ocds.DocumentType'
                    ),
                required=False,
                )


@implementer(IDocumentType)
@adapter(IDocumentTypeMarker)
class DocumentType(object):
    def __init__(self, context):
        self.context = context

    @property
    def DocumentType(self):
        if safe_hasattr(self.context, 'DocumentType'):
            return self.context.DocumentType
        return None

    @DocumentType.setter
    def DocumentType(self, value):
        self.context.DocumentType = value
