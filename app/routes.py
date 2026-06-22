from fastapi import APIRouter
from sqlalchemy import text
from app.database import engine

router = APIRouter()

@router.get("/products")
def get_products(
    limit: int = 20,
    category: str = None,
    cursor: str = None
):

    query = """
    SELECT *
    FROM products
    """

    params = {}

    conditions = []

    if category:
        conditions.append("category = :category")
        params["category"] = category

    if cursor:
        conditions.append("updated_at < :cursor")
        params["cursor"] = cursor

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += """
    ORDER BY updated_at DESC
    LIMIT :limit
    """

    params["limit"] = limit

    with engine.connect() as conn:
        rows = conn.execute(
            text(query),
            params
        ).mappings().all()

    next_cursor = None

    if rows:
        next_cursor = str(rows[-1]["updated_at"])

    return {
        "count": len(rows),
        "next_cursor": next_cursor,
        "products": rows
    }