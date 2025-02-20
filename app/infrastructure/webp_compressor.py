from io import BytesIO
from typing import BinaryIO

from PIL import Image
from pillow_heif import register_heif_opener

from app.application.common.file_converter import FileCompressor


class WebpFileCompressor(FileCompressor):

    def compress(self, payload: BinaryIO, quality: int) -> BinaryIO:
        register_heif_opener()
        image = Image.open(fp=payload)
        buffered_image = BytesIO()
        image.save(
            fp=buffered_image,
            format="WEBP",
            optimize=True,
            quality=quality,
        )

        return buffered_image
