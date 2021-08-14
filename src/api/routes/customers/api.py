from fastapi import APIRouter

from src.api.routes.customers import customers_info
router = APIRouter()

router.include_router(customers_info.router, prefix="/customer")