from typing import List
from pydantic import BaseModel

class CommentPredictionRequest(BaseModel):
        # comment_id: str
        text: str
