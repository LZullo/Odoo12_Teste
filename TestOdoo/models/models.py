# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TestOdoo_Customer(models.Model):
    _inherit = 'res.partner'

    units_number= fields.Integer(string="Quantidade de unidades",default=0)
    blocks_number= fields.Integer(string="Quantidade de blocos",default=0)
    residents_number= fields.Integer(string="Quantidade de moradores",default=0)
    gate_type= fields.Selection([('propria', 'Própria'), ('terceirizada', 'Terceirizada')],default='propria',string='Tipo de portaria')
    gate_hour=fields.Selection([('twentyfour', '24H'), ('twelve', '12H')],default='twentyfour',string='Horário da portaria')

    @api.constrains('units_number','blocks_number','residents_number')
    def constraint_validity_quantitynumbers(self):
        for rec in self:
            if rec.units_number < 0:
                raise ValidationError('A quantidade de unidades deve ser positiva')
            if rec.blocks_number < 0:
                raise ValidationError('A quantidade de blocos deve ser positiva')
            if rec.residents_number < 0:
                raise ValidationError('A quantidade de moradores deve ser positiva')


class TestOdoo_Lead(models.Model):
    _inherit = "crm.lead"

     selectable_fields = ['units_number', 'partner_id', 'blocks_number', 'residents_number', 'gate_type','gate_hour']
    
     @api.model
     def fields_get(self, allfields=None, attributes=None):
         res = super(TestOdoo_Lead, self).fields_get(allfields, attributes=attributes)
         not_selectable_fields = set(self._fields.keys()) - set(self.selectable_fields)
         for field in not_selectable_fields:
             res[field]['selectable'] = False
         return res

    units_number= fields.Integer(related='partner_id.units_number',string="Quantidade de unidades")
    blocks_number= fields.Integer(related='partner_id.blocks_number',string="Quantidade de blocos")
    residents_number= fields.Integer(related='partner_id.residents_number',string="Quantidade de moradores")
    gate_type= fields.Selection(related='partner_id.gate_type',string='Tipo de portaria')
    gate_hour=fields.Selection(related='partner_id.gate_hour',string='Horário da portaria')

