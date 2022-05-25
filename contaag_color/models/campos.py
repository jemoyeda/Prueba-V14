from odoo import models, fields 

#creando campos del modulo
class producto(models.Model):
    _inherit = 'product.template'

    color_id = fields.Many2one(comodel_name='colores', string='Color')

class informe(models.Model):
    _inherit = 'stock.quant'

    color_id_in = fields.Many2one(string='Color', related='product_id.color_id')