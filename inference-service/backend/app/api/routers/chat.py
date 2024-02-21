from typing import List

from fastapi import APIRouter, HTTPException, status
from llama_index.core.llms import MessageRole
from pydantic import BaseModel
from nemoguardrails import LLMRails, RailsConfig

chat_router = r = APIRouter()

class _Message(BaseModel):
    role: MessageRole
    content: str

class _ChatData(BaseModel):
    messages: List[_Message]


@r.post("")
async def chat(data: _ChatData):
    # check preconditions and get last message
    if len(data.messages) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No messages provided",
        )
    lastMessage = data.messages.pop()
    if lastMessage.role != MessageRole.USER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Last message must be from user",
        )

    # Load a guardrails configuration from the specified path.
    config = RailsConfig.from_path("./app/config")
    rails = LLMRails(config)

    # call generate_async
    response = await rails.generate_async(prompt=lastMessage.content)

    return response
