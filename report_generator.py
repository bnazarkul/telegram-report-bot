import pandas as pd


DATA_FILE = "sample_transactions.csv"


def load_data():
    df = pd.read_csv(DATA_FILE)

    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["commission"] = pd.to_numeric(df["commission"], errors="coerce")

    return df


def get_summary():
    df = load_data()

    total_transactions = len(df)

    successful_df = df[df["status"] == "Success"]

    successful_transactions = len(successful_df)

    success_rate = (
        successful_transactions / total_transactions * 100
        if total_transactions > 0
        else 0
    )

    payment_volume = successful_df["amount"].sum()

    commission_revenue = successful_df["commission"].sum()

    active_users = successful_df["user_id"].nunique()

    average_transaction = (
        successful_df["amount"].mean()
        if successful_transactions > 0
        else 0
    )

    return {
        "total_transactions": total_transactions,
        "successful_transactions": successful_transactions,
        "success_rate": success_rate,
        "payment_volume": payment_volume,
        "commission_revenue": commission_revenue,
        "active_users": active_users,
        "average_transaction": average_transaction,
    }


def generate_report_text():
    summary = get_summary()

    report = (
        "📊 Payment Analytics Report\n\n"
        f"💳 Payment Volume: {summary['payment_volume']:,.0f}\n"
        f"🧾 Transactions: {summary['total_transactions']}\n"
        f"✅ Successful: {summary['successful_transactions']}\n"
        f"📈 Success Rate: {summary['success_rate']:.1f}%\n"
        f"💰 Commission Revenue: {summary['commission_revenue']:,.0f}\n"
        f"👥 Active Users: {summary['active_users']}\n"
        f"📌 Avg Transaction: {summary['average_transaction']:,.2f}"
    )

    return report


def get_top_users(limit=5):
    df = load_data()

    successful_df = df[df["status"] == "Success"]

    top_users = (
        successful_df
        .groupby("user_id")
        .agg(
            payment_count=("transaction_id", "count"),
            payment_volume=("amount", "sum")
        )
        .reset_index()
        .sort_values(
            "payment_volume",
            ascending=False
        )
        .head(limit)
    )

    return top_users


def generate_top_users_text(limit=5):
    top_users = get_top_users(limit)

    lines = ["🏆 Top Users by Payment Volume\n"]

    for _, row in top_users.iterrows():
        lines.append(
            f"{row['user_id']} — "
            f"{row['payment_volume']:,.0f} "
            f"({row['payment_count']} payments)"
        )

    return "\n".join(lines)


if __name__ == "__main__":
    print(generate_report_text())
    print()
    print(generate_top_users_text())
