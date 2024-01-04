from fastapi import FastAPI, HTTPException
from skpy import Skype
from app.controllers.skypeController import serialize_skype_chat

app = FastAPI()

@app.post("/recuperar_grupos")
async def recuperar_grupos(username: str, password: str):
    try:
        # Inicia sesión en Skype
        skype = Skype(username, password)

        skype_data = skype.chats.recent()
        serialized_data = {key: serialize_skype_chat(value) for key, value in skype_data.items()}

        # Devuelve los datos en un formato más legible
        response_data = {
            "data": serialized_data,
            "total_count": len(serialized_data)
        }

        return response_data
    except Exception as e:
        return {"error": str(e)}
    
@app.post("/enviar_mensaje")
async def enviar_mensaje(username: str, password: str, id_chat: str, message: str):
    try:
        skype = Skype(username, password)

        contact = skype.chats[id_chat]

        contact.sendMsg(message)
        return {"mensaje": "Mensaje enviado correctamente"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="No se pudo enviar el mensaje")


if __name__ == "__main__":
    import uvicorn

    # Ejecuta el servidor con UVicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
