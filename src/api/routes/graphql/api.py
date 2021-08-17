from fastapi import APIRouter

from src.api.routes.graphql import graph_ql
router = APIRouter()

router.include_router(graph_ql.router, prefix="/graph")