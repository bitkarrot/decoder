from fastapi import APIRouter
from lnbits.db import Database

from .views import decoder_generic_router

db = Database("ext_decoder")

decoder_ext: APIRouter = APIRouter(prefix="/decoder", tags=["decoder"])
decoder_ext.include_router(decoder_generic_router)

decoder_static_files = [
    {
        "path": "/decoder/static",
        "name": "decoder_static",
    }
]
