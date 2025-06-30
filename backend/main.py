from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import get_db

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
async def db_check(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        return {"db": "connected", "result": result.scalar()}
    except Exception as e:
        return {"db": "error", "detail": str(e)} 