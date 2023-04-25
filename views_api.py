# views_api.py is for you API endpoints that could be hit by another service

# add your dependencies here

from http import HTTPStatus

from fastapi import Depends
from lnbits.decorators import check_admin
from loguru import logger

from . import example_ext, scheduled_tasks

# add your endpoints here


@example_ext.get("/api/v1/test/{test_data}")
async def api_example(test_data: str):
    return {
        "test_data": test_data,
    }


@example_ext.delete(
    "/api/v1",
    status_code=HTTPStatus.OK,
    dependencies=[Depends(check_admin)],
    description="Stop the extension.",
)
async def api_stop():
    for t in scheduled_tasks:
        try:
            t.cancel()
        except Exception as ex:
            logger.warning(ex)

    return {"success": True}
