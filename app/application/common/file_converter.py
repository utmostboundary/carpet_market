from typing import Protocol, BinaryIO


class FileCompressor(Protocol):

    def compress(self, payload: BinaryIO, quality: int) -> BinaryIO:
        raise NotImplementedError
