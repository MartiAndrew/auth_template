from fastapi.routing import APIRouter
from tmpauth.web.api.auth.router import auth_router
from tmpauth.web.api.docs import router as docs_router
from tmpauth.web.api.internal.router import internal_router
from tmpauth.web.api.monitoring.router import monitoring_router
from tmpauth.web.api.public.router import public_router
from tmpauth.web.api.users.router import users_router

api_router = APIRouter()
api_router.include_router(monitoring_router)
api_router.include_router(auth_router, prefix="/tmpauth/auth", tags=["authetication"])
api_router.include_router(users_router, prefix="/tmpauth/users", tags=["users"])
api_router.include_router(internal_router, prefix="/internal", tags=["internal"])
api_router.include_router(
    public_router,
    prefix="/tmpauth/public",
    tags=["public"],
)
api_router.include_router(docs_router)
