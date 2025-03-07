# Proyecto: CRUD de PDFs con Vue.js y Django

Este proyecto es una aplicación web que permite gestionar archivos PDF con permisos diferenciados. Usa **Vue.js** en el frontend y **Django** en el backend, con autenticación mediante correo electrónico, contraseña y **2FA con Google Authenticator**.

## Tecnologías Utilizadas

### Backend (Django + Django REST Framework)
- Django
- Django REST Framework
- django-otp (para 2FA con Google Authenticator)
- PyOTP
- PyQRCode (para generar códigos QR del 2FA)

### Frontend (Vue.js)
- Vue.js 3
- Vue Router
- Pinia (para el estado global)
- Fetch API para llamadas al backend

## Características del Proyecto
- **Autenticación segura** con correo y contraseña
- **2FA con Google Authenticator** para mejorar la seguridad
- **CRUD de archivos PDF** con permisos diferenciados:
  - Un usuario puede **subir, ver y solicitar edición/eliminación** de PDFs
  - Otro usuario tiene permisos para **aprobar o rechazar** solicitudes
- **Almacenamiento de PDFs** en el servidor
- **Protección de rutas según roles de usuario**

## Instalación y Configuración

### Configurar el Backend (Django)
```bash
# Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Migrar la base de datos
python manage.py migrate

# Crear un superusuario (opcional)
python manage.py createsuperuser

# Ejecutar el servidor de Django
python manage.py runserver
```

### Configurar el Frontend (Vue.js)
```bash
cd frontend
npm install  # Instalar dependencias de Vue.js
npm run dev  # Iniciar el servidor de desarrollo
```

## Uso de la Aplicación
1. **Registro**: Los usuarios pueden registrarse con correo y contraseña.
2. **Inicio de sesión**: Deben ingresar sus credenciales y luego ingresar el código de **Google Authenticator**.
3. **Gestión de PDFs**:
   - Un usuario puede **subir, ver y solicitar cambios** en archivos PDF.
   - Un usuario con permisos de aprobación puede **aceptar o rechazar solicitudes**.

## Rutas HTTP de la Aplicación
- **Frontend:** `http://localhost:5173/`
- **Backend:** `http://localhost:8000/`
- **API Base:** `http://localhost:8000/api/`
- **Dashboard (después de iniciar sesión):** `http://localhost:5173/dashboard`

## API Endpoints Principales
| Método | Endpoint          | Descripción |
|---------|-----------------|-------------|
| `POST`  | `/api/register/` | Registro de usuarios |
| `POST`  | `/api/login/`    | Inicio de sesión + 2FA |
| `GET`   | `/api/qr-code/`  | Genera el QR para 2FA |
| `POST`  | `/api/pdfs/`     | Subir un PDF |
| `GET`   | `/api/pdfs/`     | Listar PDFs |
| `DELETE` | `/api/pdfs/{id}/` | Eliminar PDF (si se aprueba) |

## Explicación de los Módulos
- **`users/`**: Maneja la autenticación, registro y 2FA.
- **`pdfs/`**: Implementa el CRUD de archivos PDF.
- **`frontend/`**: Contiene la aplicación Vue.js.
- **`api/`**: Define las rutas del backend y la API REST.

## Errores Conocidos
- **Problema con la validación del 2FA**: A veces los códigos generados no coinciden correctamente.
- **Error 400 en inicio de sesión**: Vue.js no envía correctamente los datos al backend.
- **Error 405 al subir PDF**: El método `POST` no está permitido en `/api/pdfs/`.

---

**Autor:** Santiago Torres Rincón

