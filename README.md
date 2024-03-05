# Trabajo práctico 5

Prof. Jorge Zapata
Email: jorge.zapata@ulead.ac.cr 
Tel: +506 85592422
Horario: Aula 4, jueves de 4:00 PM a 7:00 PM (hora Costa Rica UTC-6)
Valor: 5 puntos

## Instrucciones

Desarrollar un programa en Python y con FastAPI o cualquier otro framework de APIs las
siguientes APIs:


1. Registro de Usuarios:
Método: POST
Descripción: Crea un endpoint para registrar usuarios.
Ejemplo:
Endpoint: /register
Parámetros: Nombre de usuario, correo electrónico y contraseña.
Respuesta: Mensaje de éxito o error.


2. Obtener Datos de Usuario:
Método: GET
Descripción: Obtiene información de un usuario específico.
Ejemplo:
Endpoint: /user/{id}
Parámetros: ID del usuario.
Respuesta: Devuelve los datos del usuario si existe, de lo contrario, un mensaje
de error.


3. Crear Tareas:
Método: POST
Descripción: Permite a los usuarios crear nuevas tareas.
Ejemplo:
Endpoint: /tasks/create
Parámetros: Título de la tarea, descripción y estado (pendiente, en progreso,
completada).
Respuesta: Confirmación de creación de tarea.


4. Listar Tareas por Usuario:
Método: GET
Descripción: Devuelve todas las tareas asociadas a un usuario.
Ejemplo:
Endpoint: /tasks/{user_id}
Parámetros: ID del usuario.
Respuesta: Lista de tareas del usuario especificado.


Realizarlas en grupos de 2 personas cada una se hará cargo de ciertas características a elegir
y deberá subir el sistema versionado en github. Cada funcionalidad debe tener un branch en la
que se desarrolló y contar con los merge de cada integrante del equipo en ambiente de
desarrollo, staging y producción. Deberá adjuntar el enlace de Github

## Install

pip install fastapi 

pip install uvicorn uvicorn

main:app --reload