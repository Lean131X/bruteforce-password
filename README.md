# Brute Force Password Cracker

This project implements a simple **controlled brute force** algorithm in Python to understand how password guessing attacks work and to reflect on the importance of using secure passwords.

---

##  How to run the program

1. Clone this repository or download the files.
   ```bash
   git clone https://github.com/Lean131X/bruteforce-password.git
   cd bruteforce-password
2. Make sure you have Python 3 installed.
    Check in the cmd with:
    python --version
3. Run the script:
    python bruteforce.py

Example output:

If the secret password is "yaQ@", the output could be:
Password found: yaQ@
Attempts made: 9339544
Time taken: 0.5667 seconds

Reflection:

Execution time grows significantly when the password is longer or when the alphabet includes more characters (uppercase, numbers, symbols).
Short passwords like "abc" can be found in milliseconds.
A password with 8+ characters including uppercase, lowercase, numbers, and symbols generates billions of possible combinations, making brute force attacks impractical.
This demonstrates the importance of using long, unique, and secure passwords.

Repository files:

bruteforce.py: Main script with the brute force algorithm.

README.md: Documentation with instructions, examples, and reflection.
