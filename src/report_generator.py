import sqlite3
import csv
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "data" / "business_data.db"
OUTPUT_DIR = BASE_DIR / "output"


def get_sales_data():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    query = """
    SELECT
        customer_name,
        category,
        amount,
        status,
        transaction_date
    FROM sales
    ORDER BY amount DESC
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    connection.close()

    return rows


def generate_csv_report(rows):
    OUTPUT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_file = OUTPUT_DIR / f"sales_report_{timestamp}.csv"

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Customer",
            "Category",
            "Amount",
            "Status",
            "Transaction Date"
        ])

        writer.writerows(rows)

    return output_file


def main():
    print("Recupero dati dal database...")

    rows = get_sales_data()

    print(f"Record trovati: {len(rows)}")

    report_file = generate_csv_report(rows)

    print(f"Report generato: {report_file}")


if __name__ == "__main__":
    main()