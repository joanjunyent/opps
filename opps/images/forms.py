#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Image
from .widgets import CropExample

from opps.core.widgets import OppsEditor


class ImageModelForm(forms.ModelForm):
    crop_example = forms.CharField(label=_('Crop Example'), required=False,
                                   widget=CropExample())
    crop_x1 = forms.CharField(label=_(u'Crop X1'), required=False,
                              widget=forms.HiddenInput())
    crop_x2 = forms.CharField(label=_(u'Crop X2'), required=False,
                              widget=forms.HiddenInput())
    crop_y1 = forms.CharField(label=_(u'Crop Y1'), required=False,
                              widget=forms.HiddenInput())
    crop_y2 = forms.CharField(label=_(u'Crop Y2'), required=False,
                              widget=forms.HiddenInput())

    class Meta:
        model = Image
        widgets = {'description': OppsEditor()}
