import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

from report_generator import (
    generate_report_text,
    generate_top_users_text,
)

from excel_report import create_excel_report


load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    text = (
        "Hello! 👋\n\n"
        "I'm a Telegram analytics bot.\n\n"
        "Available commands:\n"
        "/report — payment analytics summary\n"
        "/top_users — top users by payment volume\n"
        "/file — download Excel analytics report"
    )

    await update.message.reply_text(text)


async def report_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    report = generate_report_text()

    await update.message.reply_text(report)


async def top_users_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    report = generate_top_users_text()

    await update.message.reply_text(report)


async def file_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    file_name = create_excel_report()

    with open(file_name, "rb") as file:
        await update.message.reply_document(
            document=file,
            filename="payment_report.xlsx",
            caption="📊 Payment Analytics Excel Report"
        )


def main():
    if not BOT_TOKEN:
        raise ValueError(
            "TELEGRAM_BOT_TOKEN was not found. "
            "Create a .env file and add your bot token."
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start_command)
    )

    app.add_handler(
        CommandHandler("report", report_command)
    )

    app.add_handler(
        CommandHandler("top_users", top_users_command)
    )

    app.add_handler(
        CommandHandler("file", file_command)
    )

    print("Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
