from pyrogram import Client
from pytgcalls import PyTgCalls

from TamilBots.config import API_HASH, API_ID, SESSION_NAME
from TamilBots.services.queues import queues

client = Client(SESSION_NAME, API_ID, API_HASH)
pytgcalls = PyTgCalls(client)


@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, chat_id: int) -> None:
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(chat_id, queues.get(chat_id)["file"])


run = pytgcalls.start
