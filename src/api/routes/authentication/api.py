from fastapi import APIRouter

from src.api.routes.authentication import auth_jwt
router = APIRouter()

router.include_router(auth_jwt.router, prefix="/auth")