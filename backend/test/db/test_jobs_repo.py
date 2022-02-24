from venv import create
from sqlalchemy.orm import Session
from db.repository.jobs import create_new_job, retreive_job
from schemas.jobs import JobCreate
from utils.users import create_random_owner


def test_retreive_job_by_id(db_session:Session):
    title = "test title"
    company = "test company"
    company_url = "testcompanyurl.com"
    location = "test location"
    description = "test description"
    owner = create_random_owner(db=db_session)
    job_schema = JobCreate(title=title, company=company, company_url=company_url, location=location, description=description)
    job = create_new_job(job=job_schema, db=db_session, owner_id=owner.id)
    retreived_job = retreive_job(id=job.id, db=db_session)
    assert retreived_job.id == job.id
    assert retreived_job.title == job.title