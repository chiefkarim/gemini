#TODO: refactor when to close the connection to the db

async def getChatHistory(db):
    chat_history =await db.fetch("SELECT * FROM chat_history;")
    db.close()
    return chat_history 
