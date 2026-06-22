from fastapi import APIRouter
from sqlalchemy import text
from app.database import engine

router = APIRouter()

@router.get("/products")
def get_products(limit: int = 20):

    query = """
    SELECT *
    FROM products
    ORDER BY updated_at DESC
    LIMIT :limit
    """

    with engine.connect() as conn:
        rows = conn.execute(
            text(query),
            {"limit": limit}
        ).mappings().all()

    return rows