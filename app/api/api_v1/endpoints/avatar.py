from fastapi.responses import Response
from models.avatar import AvatarModel
from fastapi import APIRouter, UploadFile
from PIL import Image

avatar_api = APIRouter()

@avatar_api.post("/update-avatar/{user_id}")
async def update_avatar(user_id: int, file: UploadFile = UploadFile(...)):
    # 查询头像表中的记录
    avatar = AvatarModel.get_or_none(user_id=user_id)

    # 保存新的头像文件到内存中
    avatar_bytes = await file.read()

    if avatar:
        # 更新头像记录的字节数据
        avatar.file_data = avatar_bytes
        avatar.save()
    else:
        # 创建新的头像记录
        AvatarModel.create(user_id=user_id, file_data=avatar_bytes)
        
    return {"message": "头像上传成功"}

@avatar_api.get("/avatar/{user_id}")
async def get_avatar(user_id: int):
    # 查询头像表中的记录
    avatar = AvatarModel.get_or_none(user_id=user_id)

    return Response(content=avatar.file_data, media_type='image/jpeg')
       