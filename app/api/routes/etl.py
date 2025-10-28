from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from app.models.etl_models import ETLJob, JobConfiguration
from app.api.dependencies import get_db



router = APIRouter()

@router.get("/jobs", tags=["Jobs"], response_model = List[ETLJob])
def get_jobs(db : Session = Depends(get_db)):
    return db.exec(select(ETLJob)).all()


@router.get("/jobs/{job_id}", response_model=ETLJob)
def get_job(job_id : int, db : Session = Depends(get_db)):
    job = db.exec(select(ETLJob).where(ETLJob.id == job_id)).first()
    
    if not job:
        return HTTPException(404, "Job not found")
    return job 


@router.post("/jobs", response_model=ETLJob)
def create_job(etl_job : ETLJob, db : Session = Depends(get_db)):
    db.add(etl_job)
    db.commit() 
    db.refresh(etl_job)
    return etl_job


@router.get("/jobs/configurations", response_model=List[JobConfiguration])
def get_job_configurations(db : Session = Depends(get_db)):
    return db.exec(select(JobConfiguration)).all()


@router.get("/job/configuration/{configruation_id}", response_model=JobConfiguration)
def get_job_configuration(configuration_id : int, db : Session = Depends(get_db)):
    configuration = db.exec(select(JobConfiguration).where(JobConfiguration.id == configuration_id)).first()

    if not configuration:
        return HTTPException(404, "Job configuration not found")
    
    return configuration


@router.post("/job/configuration", response_model=JobConfiguration)
def create_job_configuration(configuration : JobConfiguration, db : Session = Depends(get_db)):
    db.add(configuration)
    db.commit() 
    db.refresh(configuration)
    return configuration