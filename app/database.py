import asyncpg
import os

DB_URL = os.getenv("DATABASE_URL")

async def init_db():
    conn = await asyncpg.connect(DB_URL)
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id SERIAL PRIMARY KEY,
        question TEXT,
        answer TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    await conn.close()
