import os

hosts_path = "/etc/hosts"

def unblock_websites():
    websites_to_unblock = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com", "youtube.com", "www.youtube.com","chess.com","www.chess.com"]
    with open(hosts_path, 'r+') as hosts_file:
        lines = hosts_file.readlines()
        hosts_file.seek(0)
        for line in lines:
            if not any(website in line for website in websites_to_unblock):
                hosts_file.write(line)
        hosts_file.truncate()
    print("Websites freigegeben: ", websites_to_unblock)

if __name__ == "__main__":
    unblock_websites()
