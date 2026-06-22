import json
from pathlib import Path

from fastapi import APIRouter, Depends
from lnbits.core.views.generic import index
from lnbits.decorators import check_user_exists


def _load_version() -> str:
    config_path = Path(__file__).parent / "config.json"
    try:
        with config_path.open() as f:
            return json.load(f).get("version", "unknown")
    except Exception:
        return "unknown"


__version__ = _load_version()

decoder_generic_router: APIRouter = APIRouter()


decoder_generic_router.add_api_route(
    "/",
    methods=["GET"],
    endpoint=index,
    dependencies=[Depends(check_user_exists)],
)


decoder_generic_router.add_api_route(
    "/api/v1/version",
    methods=["GET"],
    endpoint=lambda: {"version": __version__},
)
