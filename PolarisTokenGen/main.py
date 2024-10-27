import random
import string
import base64
from colorama import Fore, init

# Initialize colorama for colored output
init(autoreset=True)

# ASCII Art with colors for menu
def display_ascii():
    ascii_art = f"""
{Fore.GREEN}██████╗  ██████╗ ██╗      █████╗ ██████╗ ██╗███████╗     ██████╗ ███████╗███╗   ██╗
{Fore.CYAN}██╔══██╗██╔═══██╗██║     ██╔══██╗██╔══██╗██║██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
{Fore.BLUE}██████╔╝██║   ██║██║     ███████║██████╔╝██║███████╗    ██║  ███╗█████╗  ██╔██╗ ██║
{Fore.MAGENTA}██╔═══╝ ██║   ██║██║     ██╔══██║██╔══██╗██║╚════██║    ██║   ██║██╔══╝  ██║╚██╗██║
{Fore.YELLOW}██║     ╚██████╔╝███████╗██║  ██║██║  ██║██║███████║    ╚██████╔╝███████╗██║ ╚████║
{Fore.RED}╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
"""
    print(ascii_art)

# Menu display
def menu():
    display_ascii()
    print(f"{Fore.CYAN}[{Fore.YELLOW}1{Fore.CYAN}] {Fore.GREEN}Token Gen")
    print(f"{Fore.CYAN}[{Fore.YELLOW}2{Fore.CYAN}] {Fore.RED}Exit")

# Function to generate a Discord-style token
def generate_token():
    # Part 1: Base64-encoded user ID (18-digit numeric ID)
    user_id = ''.join(random.choices(string.digits, k=18))
    user_id_encoded = base64.urlsafe_b64encode(user_id.encode()).decode().rstrip('=')

    # Part 2: Base64-encoded token (32 random characters)
    token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    token_encoded = base64.urlsafe_b64encode(token.encode()).decode().rstrip('=')

    # Part 3: Base64-encoded signature (27 random characters)
    signature = ''.join(random.choices(string.ascii_letters + string.digits, k=27))
    signature_encoded = base64.urlsafe_b64encode(signature.encode()).decode().rstrip('=')

    return f"{user_id_encoded}.{token_encoded}.{signature_encoded}"

# Function to handle token generation and save tokens to a txt file
def token_generation_menu():
    try:
        count = int(input(f"\n{Fore.CYAN}How Many Tokens: {Fore.YELLOW}"))
        tokens = []
        for _ in range(count):
            token = generate_token()
            print(f"{Fore.YELLOW}[INFO] {Fore.GREEN}{token}")
            tokens.append(token)

        # Save generated tokens to a text file
        save_tokens_to_file(tokens)
    except ValueError:
        print(f"{Fore.RED}Invalid input! Please enter a number.")

# Function to save tokens into a txt file
def save_tokens_to_file(tokens):
    token_file = "generated_tokens.txt"
    with open(token_file, 'w') as file:
        for token in tokens:
            file.write(f"{token}\n")
    print(f"\n{Fore.GREEN}[INFO] Tokens saved to {Fore.YELLOW}{token_file}")

# Main program loop
def main():
    while True:
        menu()
        choice = input(f"\n{Fore.CYAN}Enter your choice: {Fore.YELLOW}")
        if choice == '1':
            token_generation_menu()
        elif choice == '2':
            print(f"{Fore.RED}Exiting...")
            break
        else:
            print(f"{Fore.RED}Invalid choice, please try again.")

if __name__ == "__main__":
    main()
