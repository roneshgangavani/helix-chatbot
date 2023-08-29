# libraries
import pandas as pd
import numpy as np
from datetime import datetime

from flask import Flask, render_template, request
from bot.mybot import qna_bot
from db.connection import insert_df_into_db,append_df_into_db

def get_dataframe(user_ques,bot_response):
    row={'Date':[datetime.now()],"user_question":[user_ques],"bot_response":[bot_response]}
    df=pd.DataFrame.from_dict(row)
    print(df)
    append_df_into_db("bot_responces",df)


app = Flask(__name__)
# run_with_ngrok(app) 

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    user_question = msg
    if user_question.lower() in ['exit', 'quit', 'bye']:
        print("QnA Bot: Goodbye!")
    answer = qna_bot.get_answer(user_question)
    try:
        get_dataframe(user_question,answer)
    except:
        print("Something wrong with database insertion")
    return answer

if __name__ == "__main__":
    app.run()

