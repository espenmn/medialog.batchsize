# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from z3c.form import interfaces
from zope import schema
from zope.interface import alsoProvides
from plone.supermodel import model
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('medialog.batchsize')


class IMedialogBatchsizeLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IBatchSettings(model.Schema):
    """Adds settings to medialog.controlpanel"""

    model.fieldset(
        'Batch',
        label=_(u'Batch settings'),
        fields=[
             'batch_size',
             'hide_from_navigation'
        ],
     )

    batch_size = schema.Int (
    	title=_(u"label_batch", default=u"Batch Size"),
        min=3,
        max=500,
        required=True,
    )

    hide_from_navigation = schema.Bool(
     	title=_(u"label_hide_from_navigation", default=u"Dont display items marked hide from navigation"),
        required=False
    )


alsoProvides(IBatchSettings, IMedialogControlpanelSettingsProvider)
