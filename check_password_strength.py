import re

def check_password_strength(password):
    if len(password) < 8:
        return "❌ Too short (min 8 chars)"
    
    # Single pass check with compiled regex for efficiency
    patterns = [
        (r'[A-Z]', "❌ Need uppercase letter"),
        (r'[a-z]', "❌ Need lowercase letter"), 
        (r'\d', "❌ Need digit"),
        (r'[!@#$%^&*(),.?":{}|<>]', "❌ Need special character")
    ]
    
    for pattern, msg in patterns:
        if not re.search(pattern, password):
            return msg
    
    return "✅ Strong password!"

if __name__ == "__main__":
    result = check_password_strength(input("Enter password: "))
    print(result)