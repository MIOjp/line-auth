from dotenv import load_dotenv
import os
load_dotenv()
sender_password=os.getenv("GMAIL_PASS")
sender_address=os.getenv("GMAIL_ADDRESS")
import smtplib
from email.message import EmailMessage

def send_kansu(target_email,auth_code):
    msg=EmailMessage()
    msg.set_content(f"あなたのコードは{auth_code}です")
    msg["Subject"]="コード送信"
    msg["From"]=sender_address
    msg["To"]="a25dc002am@g.sugiyama-u.ac.jp"
    smtp_server="smtp.gmail.com"
    smtp_port=587
    try:
        with smtplib.SMTP(smtp_server,smtp_port)as server:
            server.starttls()
            server.login(msg["From"],sender_password)
            server.send_message(msg)
            print(f"{target_email}に送信しました")
    except Exception as e:
            print(f"送信失敗{e}")

