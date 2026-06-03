# PassChecker

## 🛡️ CLI Password Strength Analyzer 🛡️

A robust command-line tool that assesses the strength and security of passwords with real-time feedback, entropy calculation, and actionable improvement suggestions.

---

## ✨ Features

* **Interactive CLI:** User-friendly command-line interface with clear prompts and color-coded output.
* **Auto-Setup Environment:** Automatically creates a Python virtual environment and installs dependencies for a seamless first-run experience.
* **Masked Password Input:** Protects your privacy by masking password input on the terminal.
* **Comprehensive Strength Assessment:** Evaluates passwords based on multiple criteria:
    * **Length Analysis:** Validates password length against security standards.
    * **Character Type Detection:** Checks for uppercase, lowercase, numbers, and special characters.
    * **Entropy Calculation:** Quantifies password randomness and unpredictability in bits.
    * **Estimated Crack Time:** Provides theoretical estimates of brute-force attack duration in human-readable units.
* **Strength Ratings:** Assigns clear ratings (Very Weak, Weak, Moderate, Strong, Very Strong) with color indicators.
* **Smart Improvement Suggestions:** Offers specific, actionable tips to enhance password security.
* **🔐 Security Checks:**
    * **Common Password Detection:** Flags known weak passwords from common password dictionaries.
    * **Session History Warning:** Alerts you if you re-enter a previously checked password in the same session.
* **Security Best Practices:** Provides important reminders on password safety and management.
* **Custom ASCII Header:** Features a distinctive stylized header for visual appeal.

---

## 🚀 Quick Start

### Prerequisites

* Python 3.x (with `python3` and `python3 -m venv` available)

### Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/donfaruk19/passchecker.git
   cd passchecker
   ```

2. **Run the tool:**
   ```bash
   python3 password_strength_checker.py
   ```
   The script will automatically set up a virtual environment and install dependencies on first run.

### Commands

* `c` or `check` - Check a password's strength
* `h` or `help` - Display detailed information and criteria
* `q` or `quit` - Exit the program

---

## 💡 Example

```
Enter mode (c/check, q/quit, h/help): c
Enter your password: 
████████ (input is masked)

--- Password Strength Assessment ---
Progress: [███████░░░] 7/11
Score: 7/11
Strength: Weak
Entropy: 37.07 bits
Estimated Crack Time: 1.16 minutes

Feedback:
  ✓ Good length (8 characters). Consider making it longer.
  ✓ Contains uppercase letters
  ✓ Contains lowercase letters
  ✗ Add numbers
  ✗ Add special characters
```

---

## 📋 Security Notes

* Never reuse passwords across different accounts
* Use a password manager to generate and store complex, unique passwords
* Estimated crack times are theoretical based on computational power and character combinations
* Long passphrases are generally more secure than short complex passwords (e.g., `CorrectHorseBatteryStaple` > `P@$$w0rd!`)

---

## 📝 License

This project is free to use and modify. Attribution is appreciated but not required.

---

## 👤 Author

Abdullahi Umar Faruk

---

## 🤝 Contributing

Feel free to fork, modify, and submit improvements!
