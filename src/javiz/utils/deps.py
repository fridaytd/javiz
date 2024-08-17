import os

from fastapi import Depends, Request, HTTPException
from typing import Annotated, Final
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from javiz.utils.logger import get_logger

logger = get_logger("deps")


async def __validate_security_header(request: Request):
    try:
        PUBLIC_KEY: Final = os.getenv("APPLICATION_PUBLIC_KEY", "")
        verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

        signature = request.headers["X-Signature-Ed25519"]
        timestamp = request.headers["X-Signature-Timestamp"]

        body = (await request.body()).decode("utf-8")
        verify_key.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
    except Exception:
        logger.error("Verify fail")
        raise HTTPException(
            status_code=401,
            detail="Nono",
        )
    logger.info("Verify sucess")
    return await request.json()


ValidateDep = Annotated[dict, Depends(__validate_security_header)]
