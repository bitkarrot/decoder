import pytest
from fastapi import APIRouter, FastAPI
from httpx import AsyncClient

from .. import decoder_ext
from ..views import __version__


# just import router and add it to a test router
@pytest.mark.asyncio
async def test_router():
    router = APIRouter()
    router.include_router(decoder_ext)


@pytest.mark.asyncio
async def test_version_endpoint():
    app = FastAPI()
    app.include_router(decoder_ext)
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/decoder/api/v1/version")
    assert response.status_code == 200
    assert response.json() == {"version": __version__}
    assert __version__ == "1.1.3"
