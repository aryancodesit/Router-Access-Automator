import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# === Load credentials from config.json ===
try:
    with open("config.json", "r") as f:
        config = json.load(f)
        ROUTER_IP = config.get("router_ip", "http://192.168.29.1")
        USERNAME = config.get("username", "admin")
        PASSWORD = config.get("password", "Secure@123")
except FileNotFoundError:
    print("[!] config.json not found. Please create it with router_ip, username, and password.")
    exit(1)

# === Setup ChromeDriver ===
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keep browser open after script ends

service = Service('./chromedriver.exe')  # Ensure chromedriver.exe is in the same folder
driver = webdriver.Chrome(service=service, options=chrome_options)

# === Open Router Login Page ===
print(f"[~] Opening router login page at {ROUTER_IP}")
driver.get(ROUTER_IP)

# === Auto-fill Login Credentials ===
try:
    user_input = driver.find_element(By.ID, "tf1_userName")
    pass_input = driver.find_element(By.ID, "tf1_password")
    login_button = driver.find_element(By.NAME, "button.login.users.dashboard")

    user_input.send_keys(USERNAME)
    pass_input.send_keys(PASSWORD)
    login_button.click()

    print("[+] Login form submitted successfully.")
except Exception as e:
    print("[!] Error during login automation:", e)
