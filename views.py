from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from lnbits.helpers import template_renderer
from lnbits.core.models import User
from lnbits.decorators import check_user_exists
from starlette.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")


def decoder_renderer():
    return template_renderer(["decoder/templates"])

decoder_generic_router: APIRouter = APIRouter()

@decoder_generic_router.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    user: User = Depends(check_user_exists),
):
    return decoder_renderer().TemplateResponse(
        "decoder/index.html", {"request": request, "user": user.dict()}
    )
