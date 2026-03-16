from abc import ABC, abstractmethod
from src.schemas.chat import ChatRequest, ChatResponse


class BaseAgent(ABC):

    @abstractmethod
    async def run(self, request: ChatRequest) -> ChatResponse:
        pass
