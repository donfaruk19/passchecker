import subprocess
import sys
import os
import platform
import re
import math
import getpass # For masked password input
from colorama import init, Fore, Style

# Define the virtual environment directory name
VENV_DIR = ".venv"
# List of required packages
REQUIRED_PACKAGES = ["colorama"]

# --- Self-Setup Virtual Environment and Dependencies (Corrected) ---
def setup_environment():
    """
    Checks if running in a venv and if packages are installed within that venv.
    Creates venv and installs packages if necessary, then re-executes.
    """
    in_venv = (sys.prefix != sys.base_prefix)

    venv_path = os.path.join(os.getcwd(), VENV_DIR)
    if platform.system() == "Windows":
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")
        pip_executable = os.path.join(venv_path, "Scripts", "pip.exe")
    else: # Linux or macOS
        python_executable = os.path.join(venv_path, "bin", "python")
        pip_executable = os.path.join(venv_path, "bin", "pip")

    if not in_venv:
        print(f"{Fore.CYAN}--- Setting up environment ---{Style.RESET_ALL}")

        if not os.path.exists(venv_path) or not os.path.exists(python_executable):
            print(f"{Fore.YELLOW}Creating virtual environment at '{venv_path}'...{Style.RESET_ALL}")
            try:
                subprocess.check_call([sys.executable, "-m", "venv", venv_path])
                print(f"{Fore.GREEN}Virtual environment created.{Style.RESET_ALL}")
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Error creating virtual environment: {e}{Style.RESET_ALL}")
                print(f"{Fore.RED}Please ensure 'python3 -m venv' is available on your system.{Style.RESET_ALL}")
                sys.exit(1)
            except Exception as e:
                print(f"{Fore.RED}An unexpected error occurred while creating venv: {e}{Style.RESET_ALL}")
                sys.exit(1)
        else:
            print(f"{Fore.YELLOW}Virtual environment already exists at '{venv_path}'.{Style.RESET_ALL}")

        print(f"{Fore.YELLOW}Ensuring required packages are installed in the virtual environment...{Style.RESET_ALL}")
        try:
            install_command = [pip_executable, "install"] + REQUIRED_PACKAGES
            subprocess.check_call(install_command)
            print(f"{Fore.GREEN}All required packages installed in virtual environment.{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error installing packages into venv: {e}{Style.RESET_ALL}")
            print(f"{Fore.RED}Please try installing manually within the venv: '{pip_executable} install {' '.join(REQUIRED_PACKAGES)}'{Style.RESET_ALL}")
            sys.exit(1)
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred while installing packages: {e}{Style.RESET_ALL}")
            sys.exit(1)
        
        print(f"{Fore.BLUE}Relaunching script in virtual environment...{Style.RESET_ALL}")
        try:
            os.execv(python_executable, [python_executable] + sys.argv)
        except Exception as e:
            print(f"{Fore.RED}Error relaunching script: {e}{Style.RESET_ALL}")
            sys.exit(1)
    else: # in_venv is True
        all_packages_installed_in_current_venv = True
        for package in REQUIRED_PACKAGES:
            try:
                __import__(package.lower().replace('-', '_'))
            except ImportError:
                all_packages_installed_in_current_venv = False
                break
        
        if not all_packages_installed_in_current_venv:
            print(f"{Fore.YELLOW}Installing missing packages in current virtual environment: {', '.join(REQUIRED_PACKAGES)}...{Style.RESET_ALL}")
            try:
                install_command = [sys.executable, "-m", "pip", "install"] + REQUIRED_PACKAGES
                subprocess.check_call(install_command)
                print(f"{Fore.GREEN}All required packages installed in current virtual environment.{Style.RESET_ALL}")
            except subprocess.CalledProcessError as e:
                print(f"{Fore.RED}Error installing packages in current venv: {e}{Style.RESET_ALL}")
                sys.exit(1)
            except Exception as e:
                print(f"{Fore.RED}An unexpected error occurred while installing packages in current venv: {e}{Style.RESET_ALL}")
                sys.exit(1)
        else:
            print(f"{Fore.YELLOW}All required packages are already installed in current virtual environment.{Style.RESET_ALL}")
    
    return 

# Ensure environment is set up before anything else
setup_environment()

# Initialize colorama after potential re-execution
init()

# --- Consistent CLI Header Design ---
ANSI_ESCAPE_PATTERN = re.compile(r'\x1b\[[0-9;]*m')
BORDER_COLOR = Fore.MAGENTA
TITLE_COLOR = Fore.CYAN
SUB_TITLE_COLOR = Fore.LIGHTCYAN_EX
AUTHOR_COLOR = Fore.GREEN
HEADER_WIDTH = 50

def center_header_text(text, width, color=None):
    """Centers text within a given width, accounting for ANSI escape codes."""
    visible_text = ANSI_ESCAPE_PATTERN.sub('', text)
    text_len = len(visible_text)
    
    padding_left = (width - text_len) // 2
    padding_right = width - text_len - padding_left
    
    formatted_text = " " * padding_left + text + " " * padding_right
    
    if color:
        return color + formatted_text + Style.RESET_ALL
    return formatted_text

# --- Helper function for consistent user input and flow control ---
def get_user_choice(prompt_text, valid_options=None, allow_back=False):
    """
    Prompts the user for input with consistent styling and handles 'q' for quit,
    and optionally 'b' for back.
    """
    while True:
        back_option = ", b: Back" if allow_back else ""
        user_input = input(f"{Fore.BLUE}{prompt_text} (q: Quit{back_option}): {Style.RESET_ALL}").strip().lower()

        if user_input == 'q':
            return 'QUIT' # Sentinel value for quitting the entire program
        if allow_back and user_input == 'b':
            return 'BACK' # Sentinel value for going back one step

        if valid_options is None: # No specific validation needed, just return input
            return user_input
        elif user_input in valid_options:
            return user_input
        else:
            print(f"{Fore.RED}Invalid input. Please choose from the valid options: {', '.join(valid_options)}.{Style.RESET_ALL}\n")

# --- ASCII Progress Bar ---
def print_progress_bar(score, max_score=11):
    """Prints a simple ASCII progress bar based on the score."""
    progress = int((score / max_score) * 10)
    bar = Fore.GREEN + "█" * progress + Fore.RESET + "▒" * (10 - progress)
    print(f"Progress: [{bar}] {score}/{max_score}")

# --- Security Feature: Common Weak Passwords ---
COMMON_WEAK_PASSWORDS = [
    "password", "123456", "qwerty", "12345678", "123456789", "111111",
    "password123", "dragon", "p@ssword", "admin", "guest", "iloveyou", "secret",
    "welcome", "abcde", "test", "000000"
]

# --- Security Feature: Session-based Password History ---
checked_passwords_history = []


# --- Password Strength Assessment Function ---
def check_password_strength(password):
    """
    Assesses the strength of a password based on length, character types,
    and estimates entropy and cracking time.
    """
    score = 0
    feedback = []
    
    # Define character sets for entropy calculation
    lower_chars = 26
    upper_chars = 26
    digit_chars = 10
    special_chars_set = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~" # Expanded set
    special_chars_count = len(special_chars_set)

    # --- Initial Check: Common Weak Passwords ---
    if password.lower() in COMMON_WEAK_PASSWORDS:
        score = 0 # Force score to minimum
        strength = "Very Weak"
        strength_color = Fore.RED
        feedback.append(f"{Fore.RED}✗ CRITICAL: This is an extremely common and easily guessable password. Avoid it immediately!{Fore.RESET}")
        return score, strength, feedback, strength_color, 0, "Less than a second"

    # Criteria flags
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special_chars_set for c in password)

    # --- Length Check ---
    length = len(password)
    if length >= 12:
        score += 3
        feedback.append(f"{Fore.GREEN}✓ Excellent length ({length} >= 12 characters){Fore.RESET}")
    elif length >= 8:
        score += 2
        feedback.append(f"{Fore.YELLOW}✓ Good length ({length} characters). Consider making it longer.{Fore.RESET}")
    else:
        score += 1
        feedback.append(f"{Fore.RED}✗ Weak length ({length} < 8 characters). Aim for at least 8, preferably 12+.{Fore.RESET}")

    # --- Character Type Checks and Entropy Contribution ---
    char_set_size = 0
    
    if has_uppercase:
        score += 2
        char_set_size += upper_chars
        feedback.append(f"{Fore.GREEN}✓ Contains uppercase letters{Fore.RESET}")
    else:
        feedback.append(f"{Fore.RED}✗ Add uppercase letters (e.g., change 'pass' to 'Pass').{Fore.RESET}")

    if has_lowercase:
        score += 2
        char_set_size += lower_chars
        feedback.append(f"{Fore.GREEN}✓ Contains lowercase letters{Fore.RESET}")
    else:
        feedback.append(f"{Fore.RED}✗ Add lowercase letters (e.g., change 'PASS' to 'pAss').{Fore.RESET}")

    if has_digit:
        score += 2
        char_set_size += digit_chars
        feedback.append(f"{Fore.GREEN}✓ Contains numbers{Fore.RESET}")
    else:
        feedback.append(f"{Fore.RED}✗ Add numbers (e.g., add '123' to 'pass').{Fore.RESET}")

    if has_special:
        score += 2
        char_set_size += special_chars_count
        feedback.append(f"{Fore.GREEN}✓ Contains special characters{Fore.RESET}")
    else:
        feedback.append(f"{Fore.RED}✗ Add special characters (e.g., add '@' to 'pass').{Fore.RESET}")

    # --- Entropy Calculation (using character set size) ---
    entropy = 0
    if char_set_size > 0 and length > 0:
        entropy = length * math.log2(char_set_size)
    
    # --- Cracking Time Estimation (simplified assumption) ---
    # This is a very simplified model. Real-world cracking time varies greatly.
    # It assumes a brute-force attacker with specific capabilities.
    # A base of 2^40 ops/sec for simplicity. Adjust base as needed for calibration.
    
    crack_time_seconds = 0
    if entropy > 0:
        baseline_for_seconds = 40 # Entropy level that roughly maps to 'seconds' for a modern attacker
        if entropy > baseline_for_seconds:
             crack_time_seconds = 2 ** (entropy - baseline_for_seconds)
        else: # For very low entropy, it's virtually instant
            crack_time_seconds = 2 ** (entropy / 2) if entropy > 0 else 0.01
            
        # Cap crack_time_seconds to a reasonable max to prevent overflow or absurd numbers for display
        if crack_time_seconds > 10**30: 
            crack_time_seconds = float('inf') # Represents 'effectively impossible'
    else:
        crack_time_seconds = 0.01 # Very low or zero entropy

    crack_time_display = "Less than a second"
    if crack_time_seconds == float('inf'):
        crack_time_display = "Effectively impossible (trillions of years+)"
    elif crack_time_seconds >= 1:
        if crack_time_seconds < 60:
            crack_time_display = f"{crack_time_seconds:.2f} seconds"
        elif crack_time_seconds < 3600:  # < 1 hour
            crack_time_display = f"{crack_time_seconds / 60:.2f} minutes"
        elif crack_time_seconds < 86400:  # < 1 day
            crack_time_display = f"{crack_time_seconds / 3600:.2f} hours"
        elif crack_time_seconds < 604800:  # < 1 week
            crack_time_display = f"{crack_time_seconds / 86400:.2f} days"
        elif crack_time_seconds < 2628000:  # < 1 month (approx 30.44 days)
            crack_time_display = f"{crack_time_seconds / 604800:.2f} weeks"
        elif crack_time_seconds < 31536000:  # < 1 year (approx 365.25 days)
            crack_time_display = f"{crack_time_seconds / 2628000:.2f} months"
        else: # More than a year
            crack_time_years = crack_time_seconds / 31536000
            if crack_time_years >= 1_000_000_000_000: # Trillions of years
                crack_time_display = f"{crack_time_years / (10**12):.2f} trillion years"
            elif crack_time_years >= 1_000_000_000: # Billions of years
                crack_time_display = f"{crack_time_years / (10**9):.2f} billion years"
            elif crack_time_years >= 1_000_000: # Millions of years
                crack_time_display = f"{crack_time_years / (10**6):.2f} million years"
            else:
                crack_time_display = f"{crack_time_years:.2f} years"

    # --- Determine overall strength based on score and entropy ---
    if score >= 11 and entropy >= 80:
        strength = "Very Strong"
        strength_color = Fore.GREEN
    elif score >= 8 and entropy >= 60:
        strength = "Strong"
        strength_color = Fore.CYAN 
    elif score >= 5 and entropy >= 40:
        strength = "Moderate"
        strength_color = Fore.YELLOW
    else: # If score is low or entropy is very low
        strength = "Weak"
        strength_color = Fore.RED

    return score, strength, feedback, strength_color, entropy, crack_time_display

# --- Help function ---
def display_help():
    """Displays a detailed help section for the Password Complexity Checker."""
    print(Fore.CYAN + "\n=== Help Section ===")
    print(Fore.GREEN + "About the Tool:")
    print("This Password Complexity Tool assesses the strength of passwords based on various criteria.")
    print("It provides a score, a categorized strength level, an estimated cracking time, and specific tips for improvement.")
    print(Fore.YELLOW + "Author: Abdullahi Umar Faruk")
    print(Fore.RESET + "\nCriteria for Strength Assessment:")
    print(f"  - {Fore.CYAN}Length:{Fore.RESET} Longer passwords are always stronger.")
    print(f"    * Aim for at least 8 characters, preferably 12 or more.")
    print(f"  - {Fore.CYAN}Character Types:{Fore.RESET} Using a mix of:")
    print(f"    * Uppercase letters (A-Z)")
    print(f"    * Lowercase letters (a-z)")
    print(f"    * Numbers (0-9)")
    print(f"    * Special characters ({''.join(filter(str.isprintable, "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"))})") # Display printable chars
    print("    increases the possible combinations, making the password harder to guess.")
    print(f"  - {Fore.CYAN}Entropy:{Fore.RESET} Measured in bits, this indicates the randomness and unpredictability of your password.")
    print("    * Higher entropy means a more secure password.")
    print(f"  - {Fore.CYAN}Estimated Crack Time:{Fore.RESET} A theoretical estimation of how long it might take a brute-force attacker to guess your password.")
    print("    * This is an estimate based on computing power and character set size, not a guarantee.")
    print(Fore.RESET + "\nNew Security Features:")
    print(f"  - {Fore.LIGHTMAGENTA_EX}Common Password Check:{Fore.RESET} Alerts you if your password is on a list of commonly used/weak passwords.")
    print(f"  - {Fore.LIGHTMAGENTA_EX}Session History Warning:{Fore.RESET} Warns if you re-enter a password you've already checked in the current session.")
    
    print(Fore.RESET + "\nMain Menu Options:")
    print("  c/check    - Enter a password to check its strength.")
    print("  h/help     - Display this help message.")
    print("  q/quit     - Exit the program.")
    print(Fore.CYAN + "===================\n")

# --- Display Main CLI Header ---
def display_main_header():
    """Prints the unique CLI header for the application."""
    print(BORDER_COLOR + "╔" + "═" * HEADER_WIDTH + "╗" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text(TITLE_COLOR + "█▀█ ▄▀█ █▀▀ █▀▀ ▀█▀ █▄█  █▀█ █▄█ █▀█ █▀▀ █▀▀", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text(TITLE_COLOR + "█▀▄ █▀█ █▄▄ ██▄  █  █ █  █▀▄ █ █ █▀▄ █▄▄ ▀▀█", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text(SUB_TITLE_COLOR + "--- C O M P L E X I T Y   C H E C K E R ---", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text(AUTHOR_COLOR + "By Abdullahi Umar Faruk", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
    print(BORDER_COLOR + "╚" + "═" * HEADER_WIDTH + "╝" + Style.RESET_ALL)

    print(Fore.YELLOW + "Task: Password Complexity Checker")
    print(Fore.RED + "Copyright © 2025 Prodigy Infotech. All rights reserved.")
    print("WARNING: Unauthorized use or distribution is prohibited.")
    print(Fore.RESET + "═" * (HEADER_WIDTH + 2) + "\n")


# --- Main program loop ---
def main_program_loop():
    """Main loop for the password checker application."""
    display_main_header() # Display header once at the start

    while True:
        try:
            mode = get_user_choice(f"Enter mode (c/check, h/help)", 
                                  valid_options=['c', 'check', 'h', 'help'], 
                                  allow_back=False) # No 'b' option from main menu

            if mode == 'QUIT':
                print(Fore.CYAN + "Exiting Password Complexity Tool. Goodbye!")
                break
            elif mode in ['h', 'help']:
                display_help()
                continue # Stay in main menu after help
            elif mode in ["c", "check"]:
                # Use getpass for masked input
                password = getpass.getpass(f"{Fore.BLUE}Enter your password: {Fore.RESET}")
                
                if not password:
                    print(f"{Fore.RED}Password cannot be empty. Please try again.{Fore.RESET}\n")
                    continue

                # --- New Feature: Check against session history ---
                if password in checked_passwords_history:
                    print(f"\n{Fore.YELLOW}Note: You have already checked this exact password in this session.{Fore.RESET}")
                    print(f"{Fore.YELLOW}      For optimal security, always use unique passwords.{Fore.RESET}")
                
                # Add to history (only if not already there, or if we want to show warning every time)
                # Adding it here ensures it's recorded after input, before assessment display
                if password not in checked_passwords_history:
                    checked_passwords_history.append(password)


                score, strength, feedback, strength_color, entropy, crack_time = check_password_strength(password)
                
                print(f"\n{Fore.GREEN}--- Password Strength Assessment ---{Fore.RESET}")
                print_progress_bar(score)
                print(f"Score: {score}/11")
                print(f"Strength: {strength_color}{strength}{Fore.RESET}")
                print(f"Entropy: {entropy:.2f} bits")
                print(f"Estimated Crack Time: {crack_time}{Fore.RESET}") # Color added in function
                print("\nFeedback:")
                for comment in feedback:
                    print(f"  {comment}")
                print(f"{Fore.GREEN}------------------------------------{Fore.RESET}\n")

                # --- New Feature: General Security Notes ---
                print(f"{Fore.LIGHTMAGENTA_EX}--- Important Security Notes ---{Fore.RESET}")
                print(f"  - {Fore.YELLOW}Never reuse passwords across different online accounts.{Fore.RESET}")
                print(f"  - {Fore.YELLOW}Consider using a reputable password manager to generate and store complex, unique passwords.{Fore.RESET}")
                print(f"  - {Fore.YELLOW}The 'Estimated Crack Time' is a theoretical estimate based on computational power and character combinations. Real-world cracking can vary due to dictionary attacks, social engineering, or leaked databases.{Fore.RESET}")
                print(f"  - {Fore.YELLOW}Aim for long passphrases rather than short, complex passwords (e.g., 'CorrectHorseBatteryStaple' is better than 'P@$$w0rd!').{Fore.RESET}")
                print(f"{Fore.LIGHTMAGENTA_EX}--------------------------------{Fore.RESET}\n")

            else:
                print(f"{Fore.RED}Invalid mode! Please enter c/check, q/quit, or h/help.\n{Fore.RESET}")
        except EOFError:
            print(f"{Fore.RED}\nError: Script requires an interactive terminal. Exiting.\n{Fore.RESET}")
            break
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}\n{Fore.RESET}")

# --- Entry point of the script ---
if __name__ == "__main__":
    try:
        main_program_loop()
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Operation interrupted by user. Exiting.{Style.RESET_ALL}")
        sys.exit(0)
    finally:
        print(Style.RESET_ALL) # Ensure colors are reset on exit