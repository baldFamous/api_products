# Gestor de Inventario para Almacenes

Este proyecto es una **API backend** desarrollada en Django y Django REST Framework para la gestión de inventarios en almacenes. La API permite realizar operaciones CRUD sobre productos y proveedores, además de gestionar y controlar el stock de inventario. También incluye autenticación y autorización con JWT, generación de reportes y monitoreo de errores.

## Requisitos del Proyecto

### 1. Configuración del Entorno de Desarrollo
Configura el entorno de desarrollo de Django y Django REST Framework con PostgreSQL como base de datos.

**Pasos a realizar:**
- Instala Django y Django REST Framework.
- Configura la base de datos PostgreSQL.
- Configura las variables de entorno usando una librería como `django-environ` para asegurar la información sensible.

**Documentación:**
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Configuración de PostgreSQL en Django](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes)
- [django-environ para variables de entorno](https://django-environ.readthedocs.io/en/latest/)

---

### 2. Gestión de Productos
Implementa los endpoints CRUD para manejar productos en el sistema. Cada producto debe tener los siguientes atributos:
   - `nombre`: nombre del producto.
   - `descripción`: descripción del producto.
   - `precio`: precio del producto.
   - `categoría`: categoría a la que pertenece el producto.
   - `proveedor`: ID del proveedor asociado.
   - `cantidad en stock`: número de unidades en inventario.
   - `fecha de expiración`: fecha de expiración, opcional.

**Endpoints:**
   - `POST /api/productos/`: Crear un nuevo producto.
   - `GET /api/productos/`: Obtener lista de productos (con filtros por categoría, proveedor, etc.).
   - `GET /api/productos/{id}/`: Obtener detalles de un producto.
   - `PUT /api/productos/{id}/`: Actualizar un producto.
   - `DELETE /api/productos/{id}/`: Eliminar un producto.

**Documentación:**
- [Django Models y Queries](https://docs.djangoproject.com/en/4.0/topics/db/models/)
- [Serializers en Django REST Framework](https://www.django-rest-framework.org/api-guide/serializers/)
- [Views en Django REST Framework](https://www.django-rest-framework.org/tutorial/3-class-based-views/)

---

### 3. Control de Inventario
Implementa los endpoints para ajustar la cantidad en stock de cada producto y registra un historial de movimientos de inventario para cada ajuste.

**Endpoints:**
   - `POST /api/inventario/ajustar/`: Ajustar la cantidad en stock (entrada/salida).
   - `GET /api/inventario/historial/`: Consultar historial de movimientos (opcionalmente filtrado por fecha, tipo de movimiento).

**Documentación:**
- [Serializers para Validación de Datos](https://www.django-rest-framework.org/api-guide/serializers/#validation)
- [Consultas Avanzadas en Django ORM](https://docs.djangoproject.com/en/4.0/topics/db/queries/)

---

### 4. Gestión de Proveedores
Desarrolla endpoints para crear, leer, actualizar y eliminar proveedores, permitiendo asociarlos a los productos.

**Endpoints:**
   - `POST /api/proveedores/`: Crear un nuevo proveedor.
   - `GET /api/proveedores/`: Obtener lista de proveedores.
   - `GET /api/proveedores/{id}/`: Obtener detalles de un proveedor.
   - `PUT /api/proveedores/{id}/`: Actualizar un proveedor.
   - `DELETE /api/proveedores/{id}/`: Eliminar un proveedor.

**Documentación:**
- [Relaciones en Django ORM](https://docs.djangoproject.com/en/4.0/topics/db/examples/)
- [Serializers para Relaciones](https://www.django-rest-framework.org/api-guide/relations/)

---

### 5. Autenticación y Autorización
Configura autenticación basada en tokens JWT y define roles de usuario (por ejemplo, "Administrador" y "Operador") para controlar el acceso a diferentes funcionalidades.

**Endpoints:**
   - `POST /api/auth/registrarse/`: Registro de usuarios.
   - `POST /api/auth/login/`: Login de usuario y generación de token JWT.
   - Control de permisos según roles para endpoints críticos.

**Documentación:**
- [Simple JWT para Django REST Framework](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Permisos y Roles en Django REST Framework](https://www.django-rest-framework.org/api-guide/permissions/)

---

### 6. Generación de Reportes
Implementa endpoints que generen reportes de inventario y que puedan ser descargados en formato PDF o CSV. Los reportes deben incluir:
   - Productos con bajo stock.
   - Productos más vendidos.
   - Reportes por proveedor.

**Endpoints:**
   - `GET /api/reportes/inventario/`: Generar reporte en PDF o CSV.

**Documentación:**
- [Generación de PDFs en Django](https://docs.djangoproject.com/en/4.0/howto/outputting-pdf/)
- [Exportación a CSV en Django](https://docs.djangoproject.com/en/4.0/howto/outputting-csv/)

---

### 7. Logs y Monitoreo de Errores
Implementa logs de cada operación importante y configura un sistema de monitoreo para capturar errores en producción usando una herramienta como Sentry.

**Configuración:**
   - Añade logs para operaciones CRUD y ajustes de inventario.
   - Configura Sentry para el monitoreo de errores.

**Documentación:**
- [Logging en Django](https://docs.djangoproject.com/en/4.0/topics/logging/)
- [Sentry para Monitoreo de Errores en Django](https://sentry.io/for/django/)

---

### 8. Documentación de la API
Usa Swagger para documentar la API de manera que cualquier usuario pueda probar y entender cada endpoint. Asegúrate de que cada endpoint esté documentado con ejemplos de solicitudes y respuestas.

**Documentación:**
- [drf-yasg para Documentación Swagger en Django](https://drf-yasg.readthedocs.io/en/stable/readme.html)

---

### 9. Despliegue en Producción
Despliega el backend en un servicio de hosting como Heroku o Railway. Configura la base de datos en producción y asegúrate de que los ajustes de seguridad estén en su lugar.

**Pasos:**
   - Configura el entorno de producción en Django.
   - Configura la base de datos en el servidor.
   - Ajusta la configuración de seguridad (como `ALLOWED_HOSTS` y `DEBUG=False`).

**Documentación:**
- [Despliegue de Django en Heroku](https://devcenter.heroku.com/articles/deploying-python)
- [Documentación de Railway](https://docs.railway.app/)

---

### Bonus Opcional

#### 10. Sistema de Notificaciones
Implementa un sistema que envíe notificaciones por correo cuando el stock esté bajo. Puedes usar la API de correo electrónico de SendGrid o SMTP de Gmail.

**Documentación:**
- [Django y SendGrid](https://sendgrid.com/docs/for-developers/sending-email/django/)
- [Django y SMTP](https://docs.djangoproject.com/en/4.0/topics/email/)

#### 11. Automatización de Backups
Configura backups automáticos de la base de datos con una frecuencia diaria para proteger los datos.

**Documentación:**
- [Backups de PostgreSQL](https://www.postgresql.org/docs/)