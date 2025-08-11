from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_products():
    return [
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Smartphone"}
    ]
