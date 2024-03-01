from fastapi import APIRouter

router = APIRouter(
    prefix="/info",
    tags=["Info"]
)

@router.get("/version")
def get_version() -> str:
    return "1.0"
