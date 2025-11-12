"""Представления для рендеринга шаблонов."""
from fastapi import APIRouter
from tmpauth.services.authentication.views.home import router as home_router
from tmpauth.services.authentication.views.verification import (
    router as verification_router,
)

router = APIRouter()

router.include_router(home_router)
router.include_router(verification_router)
