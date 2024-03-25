import aiofiles
from fastapi import UploadFile


async def download_image(image_file: UploadFile | None) -> str | None:
    if image_file is None:
        return None

    file_path = f'media/{image_file.filename}'
    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await image_file.read()
        await out_file.write(content)

    return file_path