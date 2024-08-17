import time
from datetime import datetime, timedelta

hosts_path = "/etc/hosts"
redirect_ip = "127.0.0.1"
websites_to_block = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com"]
block_duration = 2 * 60 * 60  # 2 hours

# Endzeit der Blockierung
end_time = datetime.now() + timedelta(seconds=block_duration)

def block_websites():
    with open(hosts_path, 'r+') as file:
        content = file.read()
        print (content   )
#         for website in websites_to_block:
#             if website not in content:
#                 file.write(redirect_ip + " " + website + "\n")

# def unblock_websites():
#     with open(hosts_path, 'r+') as file:
#         content = file.readlines()
#         file.seek(0)
#         for line in content:
#             if not any(website in line for website in websites_to_block):
#                 file.write(line)
#         file.truncate()

# try:
#     print(f"Webseiten werden blockiert bis {end_time}")
#     block_websites()
#     while datetime.now() < end_time:
#         time.sleep(1)
#     print("Webseiten werden wieder freigegeben.")
# finally:
#     unblock_websites()

if __name__ == "__main__":
    block_websites()
    print("Webseiten werden blockiert.")