import re
import hashlib
import requests


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak Password ❌"
    elif score <= 4:
        return "Medium Password ⚠️"
    else:
        return "Strong Password ✅"


def check_data_breach(password):
    # Convert password to SHA1 hash
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()

    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    hashes = response.text.splitlines()

    for h in hashes:
        hash_suffix, count = h.split(":")
        if hash_suffix == suffix:
            return f"⚠️ Password found in {count} data breaches!"

    return "✅ Password not found in known breaches."


password = input("Enter your password: ")

strength = check_password_strength(password)
breach_status = check_data_breach(password)

print("\nPassword Strength:", strength)
print("Breach Check:", breach_status)