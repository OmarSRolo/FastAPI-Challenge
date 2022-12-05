from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.middleware.cors import CORSMiddleware

from apps.calc import urls as calc_url
from apps.jokes import urls as jokes_url

app = FastAPI(title="Challenge", default_response_class=UJSONResponse)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(jokes_url.router, prefix="/api/v1")
app.include_router(calc_url.router, prefix="/api/v1")
