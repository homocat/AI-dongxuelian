import datetime
from fastapi import APIRouter
from fastapi.responses import FileResponse
from gradio_client import Client
from models.messageModel import MessageModel
import SparkApi

#以下密钥信息从控制台获取
appid = "3efb053a"     #填写控制台中获取的 APPID 信息
api_secret = "MzgzMzMwYWMzYjZlMzhiYmM0OWQ2Njc0"   #填写控制台中获取的 APISecret 信息
api_key ="3d73d5b03ccb0cd8834bb87797c45232"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
domain = "general"   # v1.5版本
# domain = "generalv2"    # v2.0版本
#云端环境的服务地址
Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
# Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址
spark_api = APIRouter()

text = []



# length = 0

def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
@spark_api.post("/")
async def index(req: str, current_user: int):
    
    query = MessageModel.select().order_by(MessageModel.index.desc()).limit(1)
    last_message = query.get()
    last_index = last_message.index

    text.clear()
    question = checklen(getText("user", "强制在60字以内回答尽量少的, 要像人一样没有逻辑的回答, 越有趣越好(包括标点符号, 注意精确表达感情): " + req))
    SparkApi.answer =""
    SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
    getText("assistant",SparkApi.answer)
    client = Client("https://www.modelscope.cn/api/v1/studio/xzjosh/Azuma-Bert-VITS2/gradio/")
    result = client.predict(
                str(text[1]["content"]),    # str in 'Text' Textbox component
				"Azuma",	# str (Option from: ['Azuma']) in 'Speaker' Dropdown component
				0.2,	# int | float (numeric value between 0.1 and 1) in 'SDP/DP混合比' Slider component
				0.5,	# int | float (numeric value between 0.1 and 1) in '感情调节' Slider component
				0.9,	# int | float (numeric value between 0.1 and 1) in '音素长度' Slider component
				1,	# int | float (numeric value between 0.1 and 2) in '生成长度' Slider component
				fn_index=0
    )
    new_message = MessageModel(
        user = current_user,
        question = req,
        index = last_index + 1,
        ans = text[1]["content"],
        voice = result[1],
        date = datetime.datetime.now()
    )
    new_message.save()
    return FileResponse(result[1], media_type="audio/wav", filename="main.wav")

@spark_api.post("/history")
def history(id):
    query = MessageModel.select().where(MessageModel.user == id)
    messages = [message for message in query]

    return messages

@spark_api.post("/play")
def play(current_user: int, index: int):
    query = MessageModel.select().where(
            (MessageModel.index == index) & (MessageModel.user == current_user)
        ).first()
    return FileResponse(query.voice, media_type="audio/wav", filename="main.wav")