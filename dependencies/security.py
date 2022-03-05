from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from config import API_KEY
from starlette.status import HTTP_403_FORBIDDEN

api_key_header = APIKeyHeader(name="x-api-key", auto_error=True)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Unauthorized"
            )
        return api_key