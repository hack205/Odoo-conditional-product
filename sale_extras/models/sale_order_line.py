# -*- coding: utf-8 -*-
from odoo import models, fields

class CustomOrder(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'


    # Phone
    iccid = fields.Boolean(related='product_id.iccid')
    iccid_char = fields.Char(string='Iccid')
    
    phone = fields.Boolean(related='product_id.phone')
    phone_char = fields.Char(string='Phone')
    
    imei = fields.Boolean(related='product_id.imei')
    imei_char = fields.Char(string='Imei')
    
    
    # Rate plan
    phone_plan = fields.Boolean(related='product_id.phone_plan')
    phone_plan_char = fields.Char(string='Phone plan')

    type_activation = fields.Boolean(related='product_id.type_activation')
    type_activation_selection = fields.Selection(string='Type of activation',
    selection = [('1','1')])

    account = fields.Boolean(related='product_id.account')
    account_char = fields.Char(string='Account')


     # Payment conditions
    method_payment = fields.Boolean(related='product_id.method_payment')
    method_payment_selection = fields.Selection(string="Method of payment",
        selection=[
            ('bank_transfer', 'Transferencia Bancaria'),
            ('check', 'Cheque'), 
            ('confirming', 'Confirming')],
        default='bank_transfer')
    
    hitch = fields.Boolean(related='product_id.hitch')
    hitch_char = fields.Char(string='Hitch')
    
    hitch_phone =  fields.Boolean(related='product_id.hitch_phone')
    hitch_phone_char =  fields.Char(string='Hitch phone')


     # Credit note
    nc_document = fields.Boolean(related='product_id.nc_document')
    nc_document_char = fields.Char(string='CN Document')

    nc_amount =  fields.Boolean(related='product_id.nc_amount')
    nc_amount_char =  fields.Char(string='Credit note')
    
    nc_date =  fields.Boolean(related='product_id.nc_date')
    nc_date_date =  fields.Date(string='CN Date')