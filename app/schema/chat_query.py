import datetime
from pydantic import BaseModel


class ChatQuery(BaseModel):
    chat_id: int
    user_id: int
    message: str


class ChatQueryBaseResponse(ChatQuery):
    response: str
    response_time: datetime.datetime
