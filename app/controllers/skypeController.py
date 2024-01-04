def serialize_skype_chat(chat):
    chat_data = {
        "id": chat.id,
        "alerts": chat.alerts,
        "userIds": chat.userIds,
    }

    # Comprueba si es una SkypeGroupChat y agrega el atributo 'topic' y 'creatorId'
    if hasattr(chat, 'topic'):
        chat_data["topic"] = chat.topic
        chat_data["creatorId"] = chat.creatorId
    
    return chat_data