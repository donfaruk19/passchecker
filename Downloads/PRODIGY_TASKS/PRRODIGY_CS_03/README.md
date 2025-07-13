# PRODIGY_CS_03: Password Complexity Checker

## 🛡️ PixelShield: CLI Password Strength Analyzer 🛡️

This project, developed as part of the Prodigy Infotech Cybersecurity Internship, implements a robust Command-Line Interface (CLI) tool designed to assess the strength and security of user-provided passwords. It offers detailed analysis, actionable feedback, and incorporates crucial security features to guide users toward creating more secure credentials.

---

## ✨ Features

* **Interactive CLI:** A user-friendly command-line interface with clear prompts and color-coded output.
* **Self-Setup Environment:** Automatically sets up a Python virtual environment and installs necessary dependencies (like `colorama`) for a smooth out-of-the-box experience.
* **Masked Password Input:** Protects user privacy by masking password input on the terminal using `getpass`.
* **Comprehensive Strength Assessment:** Evaluates passwords based on multiple criteria:
    * **Length:** Analyzes password length against recommended standards.
    * **Character Types:** Checks for the presence of uppercase letters, lowercase letters, numbers, and special characters.
    * **Entropy Calculation:** Quantifies the randomness and unpredictability of the password in bits, a key measure of security.
    * **Estimated Crack Time:** Provides a theoretical estimate of how long it might take a brute-force attacker to guess the password, presented in human-readable units (seconds, minutes, hours, days, years).
* **Categorized Strength Feedback:** Assigns a clear strength rating (Very Weak, Weak, Moderate, Strong, Very Strong) with corresponding color indicators.
* **Actionable Improvement Suggestions:** Offers specific, practical tips on how to enhance password strength (e.g., "Add uppercase letters", "Increase length").
* **🔐 Critical Security Checks:**
    * **Common Password Dictionary Check:** Instantly flags and warns if the entered password is a known, easily guessable, and commonly used weak password.
    * **Session-Based History Warning:** Alerts the user if they re-enter a password that has already been checked in the current session, promoting the use of unique passwords.
* **General Security Notes:** Provides important reminders on password best practices, such as avoiding reuse and considering password managers.
* **Unique CLI Header:** Features a custom, stylized ASCII art header for a distinctive visual appeal.

---

## 🚀 How to Use

### Prerequisites

* Python 3.x (Ensure `python3` and `python3 -m venv` are available in your system's PATH).

### Setup and Running the Tool

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/donfaruk19/PRODIGY_CS_03.git](https://github.com/donfaruk19/PRODIGY_CS_03.git)
    ```
    (Replace `donfaruk19/PRODIGY_CS_03.git` with your actual repository URL if different).
2.  **Navigate to the project directory:**
    ```bash
    cd PRODIGY_CS_03
    ```
3.  **Run the script:**
    The script includes an automatic environment setup. Just run it directly.
    ```bash
    python3 password_strength_checker.py
    ```
    * The first time you run it, it will automatically create a virtual environment (`.venv` folder) and install the necessary `colorama` package. It will then relaunch itself within this environment.

### Usage

Once the tool starts, you will see the main menu:

* Enter `c` or `check` to input a password for assessment.
* Enter `h` or `help` to display detailed information about the tool, its features, and criteria.
* Enter `q` or `quit` to exit the program.

---

## 💡 Example Usage

```bash
# Example Run:
aufaruk@AUFaruk-PC:~/PRODIGY_CS_03$ python3 password_strength_checker.py

# ... (Environment setup messages on first run) ...

╔══════════════════════════════════════════════════╗
║* █▀█ ▄▀█ █▀▀ █▀▀ ▀█▀ █▄█  █▀█ █▄█ █▀█ █▀▀ █▀▀ *  ║
║* █▀▄ █▀█ █▄▄ ██▄  █  █ █  █▀▄ █ █ █▀▄ █▄▄ ▀▀█ *  ║
║                                                  ║
║   --- S T R E N G T H   C H E C K E R ---        ║
║                                                  ║
║           By Abdullahi Umar Faruk                ║
║                                                  ║
╚══════════════════════════════════════════════════╝
Task: Password Complexity Checker
Copyright © 2025 Prodigy Infotech. All rights reserved.
WARNING: Unauthorized use or distribution is prohibited.
═════════════════════════════════════════════════════

Enter mode (c/check, q/quit, h/help): c
Enter your password: 
******** (input is masked)

--- Password Strength Assessment ---
Progress: [███████▒▒▒] 7/11
Score: 7/11
Strength: Weak
Entropy: 37.07 bits
Estimated Crack Time: 1.16 minutes (This is a theoretical estimate)

Feedback:
  ✓ Good length (8 characters). Consider making it longer.
  ✓ Contains uppercase letters
  ✓ Contains lowercase letters
  ✗ Add numbers (e.g., add '123' to 'pass').
  ✗ Add special characters (e.g., add '@' to 'pass').
------------------------------------

--- Important Security Notes ---
  - Never reuse passwords across different online accounts.
  - Consider using a reputable password manager to generate and store complex, unique passwords.
  - The 'Estimated Crack Time' is a theoretical estimate based on computational power and character combinations. Real-world cracking can vary due to dictionary attacks, social engineering, or leaked databases.
  - Aim for long passphrases rather than short, complex passwords (e.g., 'CorrectHorseBatteryStaple' is better than 'P@$$w0rd!').
--------------------------------

Enter mode (c/check, q/quit, h/help): c
Enter your password: 
******** (input is masked)

Note: You have already checked this exact password in this session.
      For optimal security, always use unique passwords.

--- Password Strength Assessment ---
Progress: [███████▒▒▒] 7/11
Score: 7/11
Strength: Weak
Entropy: 37.07 bits
Estimated Crack Time: 1.16 minutes (This is a theoretical estimate)

Feedback:
  ✓ Good length (8 characters). Consider making it longer.
  ✓ Contains uppercase letters
  ✓ Contains lowercase letters
  ✗ Add numbers (e.g., add '123' to 'pass').
  ✗ Add special characters (e.g., add '@' to 'pass').
------------------------------------

--- Important Security Notes ---
  - Never reuse passwords across different online accounts.
  - Consider using a reputable password manager to generate and store complex, unique passwords.
  - The 'Estimated Crack Time' is a theoretical estimate based on computational power and character combinations. Real-world cracking can vary due to dictionary attacks, social engineering, or leaked databases.
  - Aim for long passphrases rather than short, complex passwords (e.g., 'CorrectHorseBatteryStaple' is better than 'P@$$w0rd!').
--------------------------------

Enter mode (c/check, q/quit, h/help): c
Enter your password: 
******** (input is masked)

--- Password Strength Assessment ---
Progress: [▒▒▒▒▒▒▒▒▒▒] 0/11
Score: 0/11
Strength: Very Weak
Entropy: 0.00 bits
Estimated Crack Time: Less than a second

Feedback:
  ✗ CRITICAL: This is an extremely common and easily guessable password. Avoid it immediately!
------------------------------------

--- Important Security Notes ---
  - Never reuse passwords across different online accounts.
  - Consider using a reputable password manager to generate and store complex, unique passwords.
  - The 'Estimated Crack Time' is a theoretical estimate based on computational power and character combinations. Real-world cracking can vary due to dictionary attacks, social engineering, or leaked databases.
  - Aim for long passphrases rather than short, complex passwords (e.g., 'CorrectHorseBatteryStaple' is better than 'P@$$w0rd!').
--------------------------------

Enter mode (c/check, q/quit, h/help): q
Exiting Password Complexity Tool. Goodbye!
