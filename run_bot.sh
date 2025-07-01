#!/bin/bash

echo "🔁 Running the trading bot..."

cd /home/ashwini/trading-bot
source env/bin/activate
python3 bot.py

python3 email_notify.py

if [ $? -eq 0 ]; then
    echo "✅ Trading bot ran successfully at $(date)" | mail -s "Bot Success ✅" ashwinikumarmahawar@gmail.com
else
    echo "❌ Trading bot failed at $(date). Check bot_output.log." | mail -s "Bot Failed ❌" ashwinikumarmahawar@gmail.com
fi

