import random
import string
import sys

def get_valid_length():
    """Prompts the user for a valid password length (integer > 0)."""
    while True:
        try:
            length_input = input("Enter desired password length (e.g., 12): ")
            length = int(length_input)
            if length > 0:
                return length
            else:
                print("🚨 Length must be a positive integer.")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")

def get_char_types():
    """Prompts the user to select character types for the password."""
    print("\n--- Character Sets ---")
    
    # Character sets from the 'string' module
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    char_sets = {
        'l': letters,
        'n': numbers,
        's': symbols
    }
    
    # User selection loop
    while True:
        selected_chars = ""
        
        use_letters = input("Include *Letters* (a-z, A-Z)? (y/n): ").lower() == 'y'
        use_numbers = input("Include *Numbers* (0-9)? (y/n): ").lower() == 'y'
        use_symbols = input("Include *Symbols* (!@#$%, etc.)? (y/n): ").lower() == 'y'
        
        if not (use_letters or use_numbers or use_symbols):
            print("⚠ You must select at least one character type. Please try again.")
            continue
            
        if use_letters:
            selected_chars += char_sets['l']
        if use_numbers:
            selected_chars += char_sets['n']
        if use_symbols:
            selected_chars += char_sets['s']
            
        return selected_chars

def generate_password(length, char_set):
    """Generates a random password using the given length and character set."""
    if not char_set:
        print("❌ Error: Character set is empty.")
        return None
        
    # Uses random.choice to pick characters from the set 'length' times
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    print("✨ Welcome to the Python Command-Line Password Generator! ✨")
    print("----------------------------------------------------------")

    # 1. User Input and Validation
    password_length = get_valid_length()
    
    # 2. Character Set Selection
    character_set = get_char_types()
    
    # 3. Password Generation
    final_password = generate_password(password_length, character_set)

    # 4. Output
    if final_password:
        print("\n✅ *Generated Password:*")
        print(f"   {final_password}")
        print(f"   Length: {len(final_password)}")
        print(f"   Character Set Size: {len(character_set)}")

if __name__== "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye! 👋")
        sys.exit(0)