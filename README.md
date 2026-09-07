# Telegram Report Bot

A Telegram bot for automated payment analytics reporting using Python and synthetic transaction data.

## Overview

This project demonstrates how analytics and reporting can be integrated into a Telegram bot.

The bot reads transaction data from a CSV file, calculates key payment metrics, generates analytical summaries, and can send an Excel report directly in Telegram.

## Features

- Payment analytics summary
- Top users by payment volume
- Excel report generation
- Excel report delivery through Telegram
- Telegram command menu
- Environment-based token configuration
- Synthetic demo dataset

## Available Commands

- `/start` — start the bot
- `/report` — show payment analytics summary
- `/top_users` — show top users by payment volume
- `/file` — generate and download Excel analytics report
- `/help` — show available commands

## Example Report

The `/report` command returns metrics such as:

- Payment Volume
- Transaction Count
- Successful Transactions
- Success Rate
- Commission Revenue
- Active Users
- Average Transaction Amount

## Dataset

The project uses:

`sample_transactions.csv`

Main fields:

- `transaction_id`
- `user_id`
- `date`
- `category`
- `amount`
- `commission`
- `status`

All data in this repository is synthetic and created specifically for portfolio demonstration purposes.

## Project Structure

- `bot.py` — Telegram bot logic and commands
- `report_generator.py` — analytics and text report generation
- `excel_report.py` — Excel report generator
- `sample_transactions.csv` — synthetic transaction dataset
- `requirements.txt` — Python dependencies
- `.env.example` — environment variable example
- `.gitignore` — prevents secrets from being committed
- `README.md` — project documentation

## Tech Stack

- Python
- Pandas
- python-telegram-bot
- OpenPyXL
- python-dotenv
- Telegram Bot API
- Excel

## How It Works

1. The bot loads synthetic transaction data.
2. Python calculates the main payment KPIs.
3. The user requests analytics through Telegram commands.
4. The bot returns a text summary or generates an Excel report.
5. The Excel report can be downloaded directly from Telegram.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file:

```text
TELEGRAM_BOT_TOKEN=your_real_bot_token
```

Run the bot:

```bash
python bot.py
```

Then open the bot in Telegram and use:

```text
/start
/report
/top_users
/file
/help
```

## Security

The real Telegram bot token is stored locally in `.env`.

The `.env` file is excluded from Git using `.gitignore`.

Only `.env.example` is included in the repository.

Never commit a real Telegram bot token to a public repository.

## Skills Demonstrated

- Python automation
- Telegram Bot API integration
- Analytics reporting
- Payment analytics
- KPI calculation
- Excel report generation
- File delivery automation
- Environment variables
- Secret management
- Modular Python project structure

## Data Privacy

All transaction data used in this project is synthetic.

The repository does not contain confidential, customer, production, or employer data.

## Future Improvements

- Scheduled daily reports
- Date filters
- Category filters
- User access control
- Database integration
- Automated alerts
- Charts sent as images
- Deployment to a cloud server
