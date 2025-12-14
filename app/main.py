from fastapi import FastAPI, Request
from core.logger import setup_logger
import time
import uuid
import json


logger = setup_logger()

app = FastAPI(title="FastAPI Scalable Backend")

@app.get("/")
async def root():
    return {"message":"Hello FastAPI"}

@app.middleware("http")
async def logging_middleware(request : Request, call_next):
    request_id =  str(uuid.uuid4())
    start_time = time.perf_counter()
    
    response = await call_next(request)

    duration = round((time.perf_counter() - start_time) * 1000, 2)

    log_data = {
        "timestamp":time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "level": " INFO",
        "request_id":request_id,
        "method": request.method,
        "path":request.url.path,
        "query_params": dict(request.query_params),
        "client_ip": request.client.host if request.client else None,
        "user_agent":request.headers.get("user-agent"),
        "status_code":response.status_code,
        "duration":duration
    }

    logger.info(json.dumps(log_data))
    response.headers["X-Request-ID"] = request_id
    return response
