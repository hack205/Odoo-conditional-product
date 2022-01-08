# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplateExtra(models.Model):
    _name       = 'product.template'
    _inherit    = 'product.template'

    # Phone
    iccid = fields.Boolean(string='Iccid', default=True)
    phone = fields.Boolean(string='Phone', default=True)
    imei = fields.Boolean(string='Imei')

    # Rate plan
    phone_plan = fields.Boolean(string='Phone plan',default=True)
    type_activation = fields.Boolean(string='Type of activation')
    account = fields.Boolean(string='Account')

    # Payment conditions
    method_payment = fields.Boolean(string='Method of payment',default=True)
    hitch = fields.Boolean(string='Hitch')
    hitch_phone =  fields.Boolean(string='Hitch phone')

    # Credit note
    nc_document = fields.Boolean(string='CN Document')
    nc_amount =  fields.Boolean(string='Credit note')
    nc_date =  fields.Boolean(string='CN Date',default=True)