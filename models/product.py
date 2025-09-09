# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    imagen_app = fields.Binary(string='Imagen para App', attachment=True)
    _max_image_size_kb = 2048  # Límite de 2MB (2048 KB)

    @api.constrains('imagen_app')
    def _check_imagen_app_size(self):
        for record in self:
            if record.imagen_app:
                # Odoo almacena binarios como base64, cada 3 bytes se convierten en 4 caracteres base64
                # Multiplicamos por 3/4 para estimar el tamaño original en bytes
                # y luego dividimos por 1024 para obtener KB
                image_size_kb = (len(record.imagen_app) * 3 / 4) / 1024
                if image_size_kb > record._max_image_size_kb:
                    raise ValidationError(_(
                        "La imagen para la aplicación excede el tamaño máximo permitido de %s KB." % record._max_image_size_kb
                    ))
