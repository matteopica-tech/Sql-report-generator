import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "business_data.db"


def create_database():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        transaction_date TEXT NOT NULL
    )
    """)

    sample_data = [
        ("Alpha SRL", "Software", 1200.50, "PAID", "2026-05-01"),
        ("Beta SNC", "Consulting", 850.00, "PENDING", "2026-05-02"),
        ("Gamma SPA", "Monitoring", 430.99, "PAID", "2026-05-03"),
        ("Studio Rossi", "Database", 2200.00, "PAID", "2026-05-04"),
        ("Delta Tech", "Automation", 1750.20, "FAILED", "2026-05-05"),
        ("Alpha SRL", "Software", 980.00, "PAID", "2026-05-06"),
        ("Beta SNC", "Consulting", 640.50, "PENDING", "2026-05-07"),
    ]

    cursor.executemany("""
    INSERT INTO sales (
        customer_name,
        category,
        amount,
        status,
        transaction_date
    )
    VALUES (?, ?, ?, ?, ?)
    """, sample_data)

    connection.commit()
    connection.close()

    print(f"Database creato correttamente: {DATABASE_PATH}")


if __name__ == "__main__":
    create_database()