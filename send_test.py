import smtplib
from email.message import EmailMessage
def send_kansu(target_email,auth_code):
    msg=EmailMessage()
    msg.set_content(f"あなたのコードは{auth_code}です")
    msg["Subject"]="コード送信"
    msg["From"]="miotikusyo@gmail.com"
    msg["To"]="miotikusyo@gmail.com"
    smtp_server="smtp.gmail.com"
    smtp_port=587
    sender_password="bmkc qek w jtvc ydgb"
    try:
        with smtplib.SMTP(smtp_server,smtp_port)as server:
            server.starttls()
            server.login(msg["From"],sender_password)
            server.send_message(msg)
            print(f"{target_email}に送信しました")
    except Exception as e:
            print(f"送信失敗{e}")

send_kansu("miotikusyo@gmail.com","9999")