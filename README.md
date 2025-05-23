# Router Access Automator

Automates login and password update tasks on WiFi routers via Selenium. 

## 🔧 Features

- Fingerprints router services and banners.
- Tries default credentials for login.
- Automates login via Selenium.
- Changes router admin and guest passwords automatically.

## ⚠️ Disclaimer

> This tool is built strictly for **educational and research purposes**. Unauthorised access or modification of network hardware/software is illegal. Use **only on devices you own or have permission to test**. Using this you can get access to the dashboard of your router service, but doing any changes to it is at your own risk. 

## 🚀 Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/aryancodesit/router-access-automator.git
   cd Roter Access Automator
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Place ```chromedriver.exe``` in the ```router_tasks/``` folder or specify its path in the script.

## 🧪 Usage

Run modules as needed:

- Fingerprint router:
  ```bash
  python router_fingerprint.py

- Try default logins:
  ```bash
  python router_login.py

- Automate router login and change password:
  ```bash
  python router_auto_ops.py

## 📝 Requirements

- Python 3.7+

- Google Chrome (for Selenium)

- Chromedriver (version must match your Chrome)

## 📂 Folder Structure

  ```
    router_tasks/
  ├── chromedriver.exe
  ├── router_fingerprint.py
  ├── router_login.py
  ├── router_auto_ops.py
  └── requirements.txt
  ```

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first. This is a very basic Project... It has a lot of scope of improvement, so please contribute to it. Thank you! Jai Hind 🇮🇳
