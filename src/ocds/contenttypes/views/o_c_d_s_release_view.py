# -*- coding: utf-8 -*-

from ocds.contenttypes import _
from plone.dexterity.browser.view import DefaultView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class OCDSReleaseView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('ocds-release-view.pt')

    def __call__(self):
        # Implement your own actions:
        return super(OCDSReleaseView, self).__call__()
