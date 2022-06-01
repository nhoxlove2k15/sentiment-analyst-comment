# -*- coding: utf-8 -*-
from fastapi import FastAPI
from dto_request import CommentPredictionRequest
from predict import predict_comment

app = FastAPI()

@app.get("/health_check")
async def health_check():
	return {"message": "ok"}

@app.post("/comment/predictions")
async def oneBookPredict(item:CommentPredictionRequest):
        res = {}
        # res["comment_id"] = item.comment_id
        preds = predict_comment(item.text)
        res["predictions"] =  preds
        return res
