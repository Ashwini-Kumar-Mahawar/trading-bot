# 🧠 Algorithmic Trading Bot

An automated trading bot built with Python to fetch stock data, generate trade signals, and run on a schedule using Cron. Ideal for beginners exploring financial data analysis and automation.

---

## 🚀 Features

- 📈 Fetches historical stock data (e.g., AAPL, MSFT) via `yfinance`
- ⚙️ Signal generation using pandas and NumPy
- ⏰ Automates execution using Linux `cron`
- 🪵 Logs output to a file for debugging and performance tracking
- 📧 Optional: Email alerts for trade signals

---

## 📦 Tech Stack

- Python 3
- `pandas`, `NumPy`, `yfinance`
- Shell scripting (`.sh`)
- Linux / WSL
- Cron scheduler
- Optional: `mailutils` for email alerts

---

## 🛠️ Setup Instructions

1. Clone the Repo

    ```bash
    git clone https://github.com/your-username/trading-bot.git
    cd trading-bot
    
---

2. Install Python Environment

    ```bash
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    
- If requirements.txt doesn’t exist, run:

   ```bash
   pip install pandas numpy yfinance
   
---

3. Test It

    ```bash
    python3 bot.py
    
- If working correctly, this should create a signals.csv file with signal data.

---

4. Automate with Cron
- Edit the crontab:
    ```bash
    crontab -e
    
- Example: Run every day at 9:30 AM
    ```bash
    30 9 * * * /home/ashwini/trading-bot/run_bot.sh
    
- Ensure run_bot.sh is executable:
    ```bash
    chmod +x run_bot.sh
    
---

### 📧 (Optional) Email Alerts
- Install mail tools:
    ```bash
    sudo apt install mailutils
    
- Update run_bot.sh or bot.py to send email when a signal is generated
- Requires Gmail App Password (for SMTP)

---

### 🤝 Contributing

- Pull requests are welcome! If you find bugs or want to add improvements, feel free to open an issue or PR.

