from dataclasses import dataclass
from typing import BinaryIO


@dataclass(frozen=True)
class FileMetadata:
    payload: BinaryIO
    extension: str = "jpg"
