from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import answer_question
from explanation_module import get_explanation
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"result": None})

@app.post("/qa")
def qa_route(request: Request, question: str = Form(...)):
    result = answer_question(question)
    return templates.TemplateResponse(request=request, name="index.html", context={"result": result})

@app.post("/explain")
def explain_route(request: Request, concept: str = Form(...)):
    result = get_explanation(concept)
    return templates.TemplateResponse(request=request, name="index.html", context={"result": result})

@app.post("/quiz")
def quiz_route(request: Request, topic: str = Form(...)):
    result = generate_quiz(topic)
    return templates.TemplateResponse(request=request, name="index.html", context={"result": result})

@app.post("/summarize")
def summarize_route(request: Request, text: str = Form(...)):
    result = summarize_text(text)
    return templates.TemplateResponse(request=request, name="index.html", context={"result": result})

@app.post("/learn")
def learn_route(request: Request, topic: str = Form(...)):
    result = get_learning_recommendations(topic)
    return templates.TemplateResponse(request=request, name="index.html", context={"result": result})