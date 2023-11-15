from fastapi import APIRouter
from models.QA import QAModel
from datetime import datetime

QA_api = APIRouter()
current_date = datetime.now()

@QA_api.post("/post")
def post_comment(current_user: int, content: str, reply: int):
    new_comment = QAModel.create(
        index=1,
        user=current_user,
        date=current_date,
        content=content,
        reply=reply
    )
    return {"message": "Comment posted successfully"}

@QA_api.get("/get")
def get_all_comments():
    all_comments = QAModel.select()
    comments = []
    for comment in all_comments:
        comments.append({
            "user": comment.user,
            "date": comment.date,
            "content": comment.content,
            "reply": comment.reply
        })
    return comments

@QA_api.delete("/delete")
def delete_comment(index: int, current_user: int):
    try:
        comment = QAModel.get(QAModel.id == index, QAModel.user == current_user)
        comment.delete_instance()
        return {"message": "Comment deleted successfully"}
    except QAModel.DoesNotExist:
        return {"error": "Comment not found"}