# vds_rutrack_app

Este módulo Odoo (`vds_rutrack_app`) ha sido desarrollado para realizar ajustes y añadir funcionalidades específicas en modelos base de Odoo, con el objetivo de integrar y soportar la aplicación de Rutrack.

## Funcionalidades y Campos Añadidos:

### Modelo: `account.payment` (Pagos)
*   **`pago_app` (Booleano):** Indica si un pago se ha originado desde la aplicación móvil. Campo de solo lectura, útil para auditoría y seguimiento.

### Modelo: `res.partner` (Contactos)
*   **`saldo_vencido` (Flotante):** Muestra el saldo pendiente que un contacto tiene vencido. Campo de solo lectura, visible en la cabecera del contacto.
*   **`objetivo` (Texto):** Permite registrar un objetivo específico relacionado con el contacto. Editable, se encuentra en la pestaña de venta del formulario del contacto.

### Modelo: `sale.order` (Ventas)
*   **`venta_credito` (Booleano):** Indica si una venta se ha realizado a crédito. Campo de solo lectura, visible en la cabecera del pedido de venta.

### Modelo: `product.template` (Productos)
*   **`imagen_app` (Binario):** Campo para subir una imagen del producto que será utilizada en la aplicación. La imagen se almacena en formato Base64 en la base de datos y tiene un límite de tamaño de 2MB para optimizar el rendimiento de la aplicación.

## Instalación y Actualización:
Para aplicar los cambios de este módulo, asegúrate de actualizar el módulo `vds_rutrack_app` en tu instancia de Odoo.
