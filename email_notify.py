import smtplib
from email.mime.text import MIMEText

# Email config
sender_email = "ashwinikumarmahawar@gmail.com"
receiver_email = "ashwinikumarmahawar@gmail.com"
app_password = "ubos abar wmlf jirt"

# Message body
subject = "📈 Trading Bot Status"
body = "✅ The trading bot ran successfully!"

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)

