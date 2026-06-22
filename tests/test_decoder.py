import httpx
import pytest
from bolt11 import decode as bolt11_decode
from lnurl import Lnurl, url_decode

from ..views import _load_version

SAMPLE_INVOICE = (
    "LNBC2220N1P4RNXA9PP587AZAHDX7PHQ9LHVY8HWZZ9C7WK3MW2LVXKJ8AMKE3AHVTXEVLESS"
    "P5JVEMH3SHMWKRJXZ8PS4AU0C34UJE9P8NQ4ETRU75YX9A3FCPT0WSXQRRSSNP4QVYNDEAQZMA"
    "N7H898JXM98DZKM0MLRSX36S93SMRUR7H0AZYYUXC5RZJQ25CARZEPGD4VQSYN44JRK85EZRPJ"
    "U92XYRK9APW4CDJH6YRWT5JGQQQQRT49LMTCQQQQQQQQQQQ86QQ9QCQZPUDQ2F38XY6T5WV9QYY"
    "SSQAYYKSWSMM3SSLA72MA0VE3E9V69Z64CW8NCLL5954XAQR60ESXV3ATQQVUFT2ZX7WJ89ZPWD"
    "AC23RSEUHESFEZDF4X46RQDZK0YWVGCQVFSSZE"
)
SAMPLE_LNURL = Lnurl("https://primal.net/.well-known/lnurlp/bitkarrot").bech32
SAMPLE_LIGHTNING_ADDRESS = "bitkarrot@primal.net"


def _strip_lightning_prefix(input_str: str) -> str:
    if input_str.lower().startswith("lightning:"):
        return input_str[10:]
    return input_str


@pytest.mark.asyncio
async def test_bolt11_decode():
    invoice = _strip_lightning_prefix(f"LIGHTNING:{SAMPLE_INVOICE}")
    decoded = bolt11_decode(invoice)
    assert decoded.data["currency"] == "bc"
    assert decoded.data["amount_msat"] == 222000
    assert decoded.data["description"] == "LNbits"
    assert "payment_hash" in decoded.data


@pytest.mark.asyncio
async def test_lnurl_decode():
    url = str(url_decode(SAMPLE_LNURL))
    assert url.startswith("https://")


@pytest.mark.asyncio
async def test_lightning_address_resolution():
    name, domain = SAMPLE_LIGHTNING_ADDRESS.split("@")
    url = f"https://{domain}/.well-known/lnurlp/{name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert "callback" in data
    assert data.get("tag") == "payRequest"


@pytest.mark.asyncio
async def test_lightning_prefix_is_stripped():
    prefixed = f"LIGHTNING:{SAMPLE_INVOICE}"
    assert _strip_lightning_prefix(prefixed) == SAMPLE_INVOICE
    assert _strip_lightning_prefix(SAMPLE_INVOICE) == SAMPLE_INVOICE


@pytest.mark.asyncio
async def test_version_loaded_from_config():
    assert _load_version() == "1.1.2"
