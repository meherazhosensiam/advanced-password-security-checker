---
**Author:** Meheraz Hosen Siam | [GitHub](https://github.com/meherazhosensiam) 🔗
# 🔐 Password Robustness & Data Leak Checker

A Python tool centered on cybersecurity that evaluates password strength and confirms if the password has been involved in recognized data breaches.

This initiative employs password security guidelines and the **Have I Been Pwned API** to assist users in determining if their password is secure.

## 🚀 Characteristics

* Analysis of password strength

* Looks for:

* Length of password

* CAPITAL LETTERS

* small letters

* Digits

* Unique signs

* Identification of data breaches utilizing the Have I Been Pwned database

* SHA-1 cryptographic hashing for secure password verification

* Straightforward command-line interface

Of course! Please provide the text you'd like me to paraphrase.

## 🛠 Tools Utilized

* Python

* Regular expressions

* Requests module

* SHA-1 hash function

* Have I Been Compromised API
## 📦 Setup

# Duplicate the repository:


git clone https://github.com/meherazhosensiam/advanced-password-security-checker.git

Enter the directory:
cd advanced-password-security-checker
# nstall requirements:
pip install requests
## ▶️ Utilization

##: Execute the script
# First of all make the file executable
chmod +x advanced-password-security-checker
# Execute the python file 
python3 advanced-password-security-checker.py


## ⚠️ Safety Alert

This tool does not transmit your complete password to any outside service.

A partial SHA-1 hash prefix is utilized for breach verification through the Have I Been Pwned API employing a **k-anonymity model**.
