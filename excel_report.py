import pandas as pd

from report_generator import load_data


OUTPUT_FILE = "payment_report.xlsx"


def create_excel_report():
    df = load_data()

    successful_df = df[df["status"] == "Success"].copy()

    summary = pd.DataFrame({
        "metric": [
            "Total Transactions",
            "Successful Transactions",
            "Success Rate (%)",
            "Payment Volume",
            "Commission Revenue",
            "Active Users",
            "Average Transaction"
        ],
        "value": [
            len(df),
            len(successful_df),
            round(len(successful_df) / len(df) * 100, 2) if len(df) else 0,
            successful_df["amount"].sum(),
            successful_df["commission"].sum(),
            successful_df["user_id"].nunique(),
            round(successful_df["amount"].mean(), 2)
            if len(successful_df)
            else 0
        ]
    })

    top_users = (
        successful_df
        .groupby("user_id")
        .agg(
            payment_count=("transaction_id", "count"),
            payment_volume=("amount", "sum")
        )
        .reset_index()
        .sort_values("payment_volume", ascending=False)
    )

    category_summary = (
        successful_df
        .groupby("category")
        .agg(
            transaction_count=("transaction_id", "count"),
            payment_volume=("amount", "sum"),
            commission_revenue=("commission", "sum")
        )
        .reset_index()
        .sort_values("payment_volume", ascending=False)
    )

    with pd.ExcelWriter(
        OUTPUT_FILE,
        engine="openpyxl"
    ) as writer:

        summary.to_excel(
            writer,
            sheet_name="Summary",
            index=False
        )

        category_summary.to_excel(
            writer,
            sheet_name="Categories",
            index=False
        )

        top_users.to_excel(
            writer,
            sheet_name="Top Users",
            index=False
        )

        df.to_excel(
            writer,
            sheet_name="Transactions",
            index=False
        )

    return OUTPUT_FILE


if __name__ == "__main__":
    file_name = create_excel_report()
    print(f"Report created: {file_name}")
