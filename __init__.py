import asyncio

from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer
from lnbits.tasks import catch_everything_and_restart

db = Database("ext_decoder")

decoder_ext: APIRouter = APIRouter(prefix="/decoder", tags=["decoder"])

decoder_static_files = [
    {
        "path": "/decoder/static",
        "name": "decoder_static",
    }
]


def decoder_renderer():
    return template_renderer(["decoder/templates"])


from .tasks import wait_for_paid_invoices
from .views import *  # noqa: F401,F403
from .views_api import *  # noqa: F401,F403


def decoder_start():
    loop = asyncio.get_event_loop()
    loop.create_task(catch_everything_and_restart(wait_for_paid_invoices))
