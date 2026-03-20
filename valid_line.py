from send_test import send_kansu
import secrets
import string
def secret_str():
    return "".join(secrets.choice(string.digits)for _ in range(4))

TEISU_DOMAIN="@g.sugiyama-u.ac.jp"
def check_send(target_email,auth_code):
    if target_email.endswith(TEISU_DOMAIN):
        print(f"{TEISU_DOMAIN}のアドレス確認済み")
        send_kansu(target_email,auth_code)
    else:
        print(f"{target_email}は大学のアドレスではありません")
random_code=secret_str()
check_send("a25dc002am@g.sugiyama-u.ac.jp",random_code)