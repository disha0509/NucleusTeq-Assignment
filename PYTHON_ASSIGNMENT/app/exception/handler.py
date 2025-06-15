from fastapi import HTTPException, Request
from app.logging_config import logger
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error": True,
            "message": "An unexpected error occurred.",
            "code": 500
        },
    )


async def custom_http_exception_handler(request: Request,exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "message": exc.detail,
            "code": exc.status_code
},
    )


async def custom_validation_exception_handler(request: Request,exc: RequestValidationError):
    for error in exc.errors():
        loc = error.get("loc", [])
        msg = error.get("msg", "Invalid input.")
        
        # ✅ Specific case for email
        if "email" in loc:
            return JSONResponse(
                status_code=HTTP_400_BAD_REQUEST,
                content={
                    "error": True,
                    "message": "Invalid email format.",
                    "code": HTTP_400_BAD_REQUEST
                }
            )
