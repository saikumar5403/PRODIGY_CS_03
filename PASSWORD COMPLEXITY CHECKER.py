import re
import random
import string


def assess_password_strength(password):
    """
    Assess the strength of a given password based on length, 
    presence of uppercase, lowercase, digits, and special characters.

    Args:
        password (str): The password to evaluate.

    Returns:
        dict: A dictionary with the strength, score, and improvement suggestions.
    """
    # Define criteria
    min_length = 8
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Check length
    length_ok = len(password) >= min_length

    # Calculate score
    score = sum([length_ok, has_uppercase, has_lowercase, has_digit, has_special])

    # Determine strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # Generate improvement suggestions
    suggestions = []
    if not length_ok:
        suggestions.append(f"Increase the length to at least {min_length} characters.")
    if not has_uppercase:
        suggestions.append("Add at least one uppercase letter (A-Z).")
    if not has_lowercase:
        suggestions.append("Add at least one lowercase letter (a-z).")
    if not has_digit:
        suggestions.append("Include at least one digit (0-9).")
    if not has_special:
        suggestions.append("Use at least one special character (!@#$%^&*(),.?\":{}|<>).")

    return {
        "strength": strength,
        "score": score,
        "suggestions": suggestions
    }

def generate_suggested_password():
    """
    Generate a strong password suggestion.

    Returns:
        str: A randomly generated strong password.
    """
    length = random.randint(12, 16)  # Randomize password length between 12 and 16
    characters = (
        random.choices(string.ascii_uppercase, k=2) +
        random.choices(string.ascii_lowercase, k=4) +
        random.choices(string.digits, k=2) +
        random.choices("!@#$%^&*(),.?\":{}|<>", k=2)
    )
    random.shuffle(characters)
    return ''.join(characters[:length])

if __name__ == "__main__":
    print("Password Complexity Checker")
    password = input("Enter a password to evaluate: ")

    # Assess password
    result = assess_password_strength(password)

    # Output results
    print(f"\nPassword Strength: {result['strength']}")
    print(f"Score: {result['score']}/5")

    if result['suggestions']:
        print("\nSuggestions to improve your password:")
        for suggestion in result['suggestions']:
            print(f"- {suggestion}")

        # Provide a strong password suggestion
        suggested_password = generate_suggested_password()
        print(f"\nSuggested Strong Password: {suggested_password}")
    else:
        print("Great job! Your password is strong.")