from cafe_booking.web.api.docs import router as docs_router
from cafe_booking.web.api.internal.router import internal_router
from cafe_booking.web.api.monitoring.router import monitoring_router
from cafe_booking.web.api.public.router import public_router
from fastapi.routing import APIRouter

api_router = APIRouter()
api_router.include_router(monitoring_router)
api_router.include_router(internal_router, prefix="/internal", tags=["internal"])
api_router.include_router(
    public_router,
    prefix="/cafe_booking/public",
    tags=["public"],
)
api_router.include_router(docs_router)
