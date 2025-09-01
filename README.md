# Instagram Follow Bot 🚀

An automated Instagram bot built with **Python** and **Selenium** that logs in to your Instagram account and follows followers of a chosen target account.

---

## ⚡ Features

* Logs in to Instagram automatically.
* Navigates to the target account's followers list.
* Scrolls and clicks "Follow" buttons automatically.
* Handles click interception gracefully.

---

## 🛠️ Requirements

* Python 3.10+
* Google Chrome (latest version)
* ChromeDriver (matching your Chrome version)

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/achintya-goyal/Instagram-Follow-Bot.git
   cd instagram-follow-bot
   ```

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows
   source venv/bin/activate   # On Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install selenium
   ```

4. **Download ChromeDriver**

   * Find your Chrome version:
     Go to `chrome://settings/help` in Chrome.
   * Download the matching driver: [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
   * Place `chromedriver.exe` in your PATH or the project folder.

---

## 🔑 Setup

1. Open `main.py`.
2. Replace these with your Instagram credentials:

   ```python
   USERNAME = "your_username"
   PASSWORD = "your_password"
   ```
3. Change the target account:

   ```python
   ACCOUNT = "leomessi"
   ```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

The bot will:

1. Open Instagram login page.
2. Log in with your credentials.
3. Open the target account's followers list.
4. Attempt to follow users automatically.

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. Automating Instagram actions may violate Instagram's Terms of Service. Use at your own risk.

⚠️ **Note:** Instagram’s front-end and back-end are constantly changing. This means:

* Paths, classes, or XPaths used in this bot may stop working without notice.
* Instagram may introduce additional authentication steps (like 2FA, email verification, or CAPTCHA).
* You may need to update the script accordingly to keep it functional.
