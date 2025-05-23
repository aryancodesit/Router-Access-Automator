import socket
import requests
from contextlib import closing
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ROUTER_IP = "192.168.29.1"
COMMON_PORTS = [80, 8080, 443, 8443, 23]  # HTTP, HTTPS, Telnet

def scan_open_ports(ip, ports):
    open_ports = []
    for port in ports:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def grab_banner(ip, port, https=False):
    try:
        proto = "https" if https else "http"
        url = f"{proto}://{ip}:{port}"
        response = requests.get(url, timeout=5, verify=False)
        print(f"\n[+] {'HTTPS' if https else 'HTTP'} Banner from port {port}:")
        print(f"    Status Code: {response.status_code}")
        print(f"    Server Header: {response.headers.get('Server', 'N/A')}")
        print(f"    Title: {response.text.split('<title>')[1].split('</title>')[0] if '<title>' in response.text else 'N/A'}")
    except Exception as e:
        print(f"[!] Failed to get {'HTTPS' if https else 'HTTP'} banner on port {port}: {e}")


def main():
    print(f"[~] Scanning {ROUTER_IP} for open ports...")
    open_ports = scan_open_ports(ROUTER_IP, COMMON_PORTS)

    if not open_ports:
        print("[!] No open ports found. Is the router reachable?")
        return

    print(f"[+] Open ports found: {open_ports}")

    for port in open_ports:
        if port in [80, 8080]:
            grab_banner(ROUTER_IP, port)
        elif port == 443 or port == 8443:
            grab_banner(ROUTER_IP, port, https=True)
        elif port == 23:
            print("[!] Telnet detected. (Consider manual fingerprinting via Telnet client)")

if __name__ == "__main__":
    main()


#explaination of the code:
# This script scans a router for open ports and attempts to grab banners from HTTP/HTTPS services.
# It uses the `socket` library to check for open ports and the `requests` library to fetch banners.
# The script defines a list of common ports (HTTP, HTTPS, and Telnet) and checks each one.
# If an open port is found, it attempts to fetch the banner and prints relevant information.
# The script also handles exceptions to avoid crashing on connection errors.
# The `main` function orchestrates the scanning and banner grabbing process.
