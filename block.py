import os

hosts_path = "/etc/hosts"
redirect_ip = "127.0.0.1"

def block_websites():
    websites_to_block = ["www.facebook.com", "facebook.com", "www.instagram.com", "instagram.com", "youtube.com", "www.youtube.com","chess.com","www.chess.com"]
    with open(hosts_path, 'a') as hosts_file:
        for website in websites_to_block:
            hosts_file.write(redirect_ip + " " + website + "\n")
    print("Websites blockiert: ", websites_to_block)

if __name__ == "__main__":
    block_websites()
