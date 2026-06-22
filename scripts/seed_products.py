from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

query = """
INSERT INTO products
(
id,
name,
category,
price,
created_at,
updated_at
)
SELECT
gen_random_uuid()::text,
'Product ' || gs,
(
ARRAY[
'Electronics',
'Books',
'Fashion',
'Sports',
'Home'
]
)[floor(random()*5+1)],
round((random()*1000)::numeric,2),
NOW() - (random()*365 || ' days')::interval,
NOW() - (random()*365 || ' days')::interval
FROM generate_series(1,200000) gs;
"""

with engine.begin() as conn:
    conn.execute(text(query))

print("Seeded 200000 products!")