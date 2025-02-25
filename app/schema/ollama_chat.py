from pydantic import BaseModel


class OllamaMessage(BaseModel):
    content: str
    role: str


class OllamaChatResponse(BaseModel):
    message: OllamaMessage
