from fastapi import APIRouter

from src.schemas.system_info import HealthCheck

router = APIRouter()


@router.get(
    "/health",
    tags=["health"],
    summary="Information about the system health.",
    description="Check if the system is up.",
    response_model=HealthCheck,
)
def health_check():
    return HealthCheck(status="ok")
