from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.jobs import *
from sqlalchemy.orm import Session
from db.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def home(request:Request, db:Session=Depends(get_db)):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse("jobs/homepage.html", {"request": request, "jobs": jobs})


@router.get("/details/{id}")
def job_detail(id:int, request:Request, db:Session=Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return templates.TemplateResponse("jobs/detail.html", {"request":request, "job":job})