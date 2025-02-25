from fastapi import APIRouter
import logging
from app.helpers.datetime_helper import current_datetime
from app.llm_services.intent_service import classify_intent
from app.schema.chat_query import ChatQuery, ChatQueryBaseResponse


logging.basicConfig(level=logging.INFO)
router = APIRouter()


@router.post("/")
def read_root(chat_query: ChatQuery) -> ChatQueryBaseResponse:
    logging.debug("chat_query: %s", chat_query)

    intent = classify_intent(chat_query.message)
    response = ChatQueryBaseResponse(
        chat_id=chat_query.chat_id,
        user_id=chat_query.user_id,
        message=chat_query.message,
        response=intent,
        response_time=current_datetime(),
    )
    return response
