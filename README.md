# API de Skype con FastAPI
![](https://img.shields.io/badge/Python-3.12.0-blue)
![](https://img.shields.io/badge/skPy-0.10.6-blue)
![](https://img.shields.io/badge/fastapi-0.108.0-green)


## Descripción General
Esta API proporciona una interfaz simple y efectiva para interactuar con Skype utilizando FastAPI. Permite a los usuarios recuperar información de los grupos de chat de Skype y enviar mensajes a través de la API. La API está diseñada para ser intuitiva y fácil de usar, enfocándose en las operaciones esenciales de Skype.

## Características
- **Recuperación de Grupos de Chat de Skype**: Permite a los usuarios obtener una lista de sus grupos de chat recientes en Skype, incluyendo detalles como los mensajes y participantes de cada grupo.
- **Envío de Mensajes**: Ofrece la posibilidad de enviar mensajes a un chat de Skype específico, proporcionando una manera efectiva de comunicarse a través de la API.

## Endpoints
La API consta de dos endpoints principales:

1. **POST /recuperar_grupos**
    - Recupera información sobre los grupos de chat de Skype del usuario.
    - Parámetros de entrada: `username` (nombre de usuario de Skype), `password` (contraseña de Skype).
    - Respuesta: Un listado de los chats recientes, cada uno con su respectiva información detallada.

2. **POST /enviar_mensaje**
    - Permite enviar un mensaje a un chat específico en Skype.
    - Parámetros de entrada: `username` (nombre de usuario de Skype), `password` (contraseña de Skype), `id_chat` (identificador del chat de destino), `message` (mensaje a enviar).
    - Respuesta: Confirmación del envío del mensaje.

## Manejo de Errores
- En caso de cualquier fallo durante la ejecución de las operaciones, la API proporciona mensajes de error descriptivos para facilitar la depuración y el manejo de excepciones.

## Implementación Técnica
La API está construida utilizando FastAPI, lo que garantiza un rendimiento rápido y una fácil integración con otros sistemas. Utiliza `skpy` para interactuar con los servicios de Skype. La ejecución del servidor se realiza a través de `uvicorn`, asegurando una gestión eficiente del servidor asíncrono.

## Ejemplo de Uso
Para iniciar el servidor, ejecute el siguiente comando:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
