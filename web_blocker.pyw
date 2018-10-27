"""WebSite Block with .pyw extension,
 run as administrator """
import time
from datetime import datetime as dt


hosts_path = "C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
web_to_block = ["www.facebbok.com", "facebbok.com", "www.instagram.com","instagram.com"]
hosts_temp = "hosts"

while True:
    """check if the time is between the two values(10, 18)"""
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        """"""
        print("Working hours...")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for web in web_to_block:
                """checking if the websites already in file"""
                if web in content:
                    pass
                else:
                    """writing the web to block"""
                    file.write(redirect + " " + web + "\n")
    else:
        """unblock the sites"""
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in web_to_block):
                    file.write(line)
            file.truncate()
        print("fun time")
    time.sleep(5)
