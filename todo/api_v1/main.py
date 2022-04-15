from fastapi import FastAPI


app = FastAPI(title="Todo API", openapi_url="/api/v1/openapi.json",
              docs_url="/api/v1/docs", redoc_url="/api/v1/redoc",
              version="1.0.0")
