import uuid
from abc import abstractmethod
from typing import Protocol, BinaryIO


def file_path_creator(extension: str = "jpg") -> str:
    return f"{uuid.uuid4()}.{extension}"


class FileManager(Protocol):

    @abstractmethod
    async def save(self, payload: BinaryIO, path: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, path: str) -> None:
        raise NotImplementedError
