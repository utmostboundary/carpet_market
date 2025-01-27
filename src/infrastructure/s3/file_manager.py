from boto3 import client
from botocore.client import BaseClient
from botocore.config import Config
from botocore.exceptions import ClientError
from typing_extensions import BinaryIO

from src.application.common.file_manager import FileManager
from src.infrastructure.s3.config import S3Config


class S3FileManager(FileManager):
    def __init__(self, config: S3Config):
        self._config = config

    def _client(self) -> BaseClient:
        return client(
            "s3",
            endpoint_url=self._config.endpoint_url,
            aws_access_key_id=self._config.aws_access_key_id,
            aws_secret_access_key=self._config.aws_secret_access_key,
            config=Config(signature_version="s3v4"),
        )

    async def save(self, payload: BinaryIO, path: str) -> bool:
        s3 = self._client()
        try:
            s3.upload_file(payload, "carpets", path)
            return True
        except ClientError:
            return False

    async def delete(self, path: str) -> None:
        pass
