import ollama

from app.config import constants
from app.llm_services.constants import (
    CAR_RECOMMENDATION_AGENT,
    GENERAL_CHAT_AGENT,
)
from app.llm_services.enums import OllamaChatResponseEnum
from app.llm_services.prompts.orchestrator import ORCHESTRATOR_PROMPT_TEMPLATE
from app.schema.ollama_chat import OllamaMessage

INTENTS = [CAR_RECOMMENDATION_AGENT, GENERAL_CHAT_AGENT]


def classify_intent(message):
    prompt = ORCHESTRATOR_PROMPT_TEMPLATE.format(message=message)
    request_message = OllamaMessage(role="user", content=prompt)
    response = ollama.chat(
        model=constants.INTENT_CLASSIFICATION_MODEL,
        messages=[
            dict(request_message),
        ],
    )
    response_body = response[OllamaChatResponseEnum.message.value]
    resp_message = OllamaMessage(
        content=response_body[OllamaChatResponseEnum.content.value],
        role=response_body[OllamaChatResponseEnum.role.value],
    )
    intent = resp_message.content.strip()

    if intent in INTENTS:
        return intent
    return GENERAL_CHAT_AGENT
