# tasks.py is for asynchronous when invoices get paid

import asyncio

from lnbits.core.models import Payment
from lnbits.helpers import get_current_extension_name
from lnbits.tasks import register_invoice_listener
from loguru import logger


async def wait_for_paid_invoices():
    invoice_queue = asyncio.Queue()
    register_invoice_listener(invoice_queue, get_current_extension_name())

    while True:
        payment = await invoice_queue.get()
        await on_invoice_paid(payment)


async def on_invoice_paid(payment: Payment) -> None:
    if (
        payment.extra.get("tag") != "example"
    ):  # Will grab any payment with the tag "example"
        logger.debug(payment)
        # Do something
    return
