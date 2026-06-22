\# CodeVector Backend Task



\## Overview



This project is a backend service built using FastAPI and PostgreSQL to efficiently browse a large catalog of approximately 200,000 products.



The API supports:



\* Product listing

\* Category filtering

\* Cursor-based pagination

\* Fast querying on large datasets



\## Tech Stack



\* FastAPI

\* PostgreSQL (Neon)

\* SQLAlchemy

\* Render



\## Features



\### Product Listing



Retrieve products ordered by latest updated products first.



Endpoint:



GET /products



\### Category Filtering



Filter products by category.



Example:



GET /products?category=Books



\### Cursor Pagination



Efficient cursor-based pagination using updated\_at timestamps.



Example:



GET /products?cursor=2026-06-22T10:00:00



\### Why Cursor Pagination?



\* Faster than OFFSET pagination on large datasets

\* Prevents duplicate and missing records while data changes

\* Scales efficiently with growing data



\## Database Schema



Each product contains:



\* id

\* name

\* category

\* price

\* created\_at

\* updated\_at



A seed script generates approximately 200,000 products.



\## Live Deployment



Backend URL:



https://codevector-task-hqqe.onrender.com



API Documentation:



https://codevector-task-hqqe.onrender.com/docs



\## GitHub Repository



https://github.com/jukantilohith-19/codevector-task



\## Improvements With More Time



\* Composite cursor using (updated\_at, id)

\* Automated testing

\* Docker deployment

\* Response caching

\* Simple frontend UI



\## AI Usage



AI tools were used to accelerate implementation, debugging, and deployment setup.



All generated code was reviewed, tested, understood, and modified where necessary.



