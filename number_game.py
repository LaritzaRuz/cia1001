#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A fun number guessing game where the player needs to guess
a random number between 1 and 100.
"""

import random
import time
from colorama import init, Fore, Style

# Initialize colorama for Windows
init()

def print_colored(text, color=Fore.WHITE, style=Style.NORMAL, end='\n'):
    """Print text with color and style."""
    print(f"{style}{color}{text}{Style.RESET_ALL}", end=end)

def get_player_name():
    """Get the player's name and welcome them."""
    print_colored("\n╔══════════════════════════════════════╗", Fore.CYAN)
    print_colored("║  Welcome to the Number Guessing Game! ║", Fore.CYAN)
    print_colored("╚══════════════════════════════════════╝\n", Fore.CYAN)
    name = input(f"{Fore.YELLOW}What's your name? {Style.RESET_ALL}").strip()
    return name

def play_game():
    """Main game logic."""
    name = get_player_name()
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print_colored(f"\nHi {name}! 🎮", Fore.GREEN)
    print_colored("I'm thinking of a number between 1 and 100.", Fore.WHITE)
    print_colored(f"Can you guess it in {max_attempts} attempts? 🤔\n", Fore.WHITE)
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"{Fore.YELLOW}Enter your guess: {Style.RESET_ALL}"))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print_colored("⚠️  Please guess a number between 1 and 100!", Fore.RED)
                continue
                
            if guess == secret_number:
                print_colored(f"\n🎉 Congratulations {name}! You got it in {attempts} attempts! 🎉", Fore.GREEN, Style.BRIGHT)
                return True
            elif guess < secret_number:
                print_colored("📈 Too low! Try a higher number.", Fore.BLUE)
            else:
                print_colored("📉 Too high! Try a lower number.", Fore.MAGENTA)
                
            remaining = max_attempts - attempts
            print_colored(f"Attempts remaining: {remaining} {'🎯' * remaining}\n", Fore.YELLOW)
            
        except ValueError:
            print_colored("⚠️  Please enter a valid number!", Fore.RED)
            
    print_colored(f"\n💫 Game Over! The number was {secret_number}.", Fore.RED)
    return False

def main():
    """Main game loop with play again feature."""
    while True:
        won = play_game()
        
        if won:
            print_colored("\n🏆 You're a great guesser! 🌟", Fore.GREEN, Style.BRIGHT)
        else:
            print_colored("\n😅 Better luck next time! 🍀", Fore.YELLOW)
            
        play_again = input(f"\n{Fore.CYAN}Would you like to play again? (yes/no): {Style.RESET_ALL}").lower().strip()
        if play_again != 'yes':
            print_colored("\nThanks for playing! Goodbye! 👋✨", Fore.GREEN)
            break

if __name__ == "__main__":
    main() 