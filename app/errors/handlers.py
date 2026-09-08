from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.errors.exceptions import PredictionError

import logging

logger = logging.getLogger(__name__)

async def prediction_error_handler(
        request: Request,
        exc: PredictionError,
        ):

        request_id = request.state.request_id


        logger.error(
                f"Prediction failed request_id={request_id}: {exc}"
                )
        
        return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                        "error": "prediction_failed",
                        "detail": "An internal prediction error occurred.",
                        "request_id": request_id,
                }
        )

