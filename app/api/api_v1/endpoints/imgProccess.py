from fastapi import APIRouter, UploadFile, File
from PIL import Image
from fastapi.responses import FileResponse

img_api = APIRouter()
from stitching import Stitcher
stitcher = Stitcher()

@img_api.post()
def index(img1: UploadFile = File(...), img2: UploadFile = File(...)):
    pil_img1 = Image.open(img1.file)
    pil_img2 = Image.open(img2.file)

    # todo opencv 拼接图片
    panorama = stitcher.stitch(["img1.jpg", "img2.jpg", "img3.jpg"])
    result_img = Image.blend(pil_img1, pil_img2, alpha=0.5)

    return FileResponse(panorama, media_type="image/png")