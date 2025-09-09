# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from io import BytesIO
from PIL import Image
import base64

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    imagen_app = fields.Binary(string='Imagen para App', attachment=False)
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

    @api.constrains('imagen_app')
    def _check_imagen_app_format(self):
        for record in self:
            if record.imagen_app:
                try:
                    # Odoo almacena binarios como base64, necesitamos decodificarlo para Pillow
                    image_bytes = base64.b64decode(record.imagen_app)
                    image = Image.open(BytesIO(image_bytes))
                    if image.format.upper() != 'PNG':
                        raise ValidationError(_("La imagen para la aplicación debe ser en formato PNG."))
                except (IOError, Image.UnidentifiedImageError):
                    raise ValidationError(_("No se pudo identificar el formato de la imagen. Asegúrate de que sea un archivo de imagen válido."))
