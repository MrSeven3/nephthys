from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from nephthys.utils.env import env

jobstores = {
    "default":SQLAlchemyJobStore(url=env.database_url)
}

scheduler = AsyncIOScheduler(jobstores=jobstores, timezone="Europe/London")