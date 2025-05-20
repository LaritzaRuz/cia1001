#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fantasy Quest - A text-based adventure game
"""

import random
import time
from colorama import init, Fore, Style
import os

# Initialize colorama for Windows
init()

class Player:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.max_health = 100
        self.inventory = ["Health Potion"]
        
        # Class-specific starting stats
        if character_class == "Warrior":
            self.strength = 15
            self.magic = 5
            self.inventory.append("Rusty Sword")
        elif character_class == "Mage":
            self.strength = 5
            self.magic = 15
            self.inventory.append("Wooden Staff")
        else:  # Ranger
            self.strength = 10
            self.magic = 10
            self.inventory.append("Short Bow")

    def use_potion(self):
        if "Health Potion" in self.inventory:
            self.inventory.remove("Health Potion")
            heal_amount = 30
            self.health = min(self.max_health, self.health + heal_amount)
            print_colored(f"\n🧪 You used a Health Potion and recovered {heal_amount} health!", Fore.GREEN)
            print_colored(f"Current Health: {self.health}/{self.max_health} ❤️", Fore.RED)
        else:
            print_colored("\n❌ You don't have any Health Potions!", Fore.RED)

def print_colored(text, color=Fore.WHITE, style=Style.NORMAL, end='\n'):
    """Print text with color and style."""
    print(f"{style}{color}{text}{Style.RESET_ALL}", end=end)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the game header."""
    clear_screen()
    print_colored("\n╔═══════════════════════════════════╗", Fore.CYAN)
    print_colored("║         Fantasy Quest              ║", Fore.CYAN)
    print_colored("╚═══════════════════════════════════╝\n", Fore.CYAN)

def get_player_info():
    """Get player name and class."""
    print_header()
    name = input(f"{Fore.YELLOW}Enter your hero's name: {Style.RESET_ALL}").strip()
    
    print_colored("\nChoose your class:", Fore.CYAN)
    print_colored("1. Warrior (High Strength, Low Magic)", Fore.RED)
    print_colored("2. Mage (High Magic, Low Strength)", Fore.BLUE)
    print_colored("3. Ranger (Balanced Strength and Magic)", Fore.GREEN)
    
    while True:
        choice = input(f"\n{Fore.YELLOW}Enter your choice (1-3): {Style.RESET_ALL}").strip()
        if choice == "1":
            return name, "Warrior"
        elif choice == "2":
            return name, "Mage"
        elif choice == "3":
            return name, "Ranger"
        else:
            print_colored("Invalid choice! Please choose 1, 2, or 3.", Fore.RED)

def combat(player, enemy_name, enemy_health):
    """Handle combat encounters."""
    print_colored(f"\n⚔️  A {enemy_name} appears! ⚔️", Fore.RED)
    enemy_current_health = enemy_health
    
    while enemy_current_health > 0 and player.health > 0:
        print_colored(f"\nYour Health: {player.health}/{player.max_health} ❤️", Fore.RED)
        print_colored(f"{enemy_name}'s Health: {enemy_current_health}/{enemy_health} 👿\n", Fore.MAGENTA)
        
        print_colored("What would you like to do?", Fore.CYAN)
        print_colored("1. Attack", Fore.RED)
        print_colored("2. Use Magic", Fore.BLUE)
        print_colored("3. Use Health Potion", Fore.GREEN)
        
        choice = input(f"\n{Fore.YELLOW}Enter your choice (1-3): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            damage = random.randint(5, 10) + player.strength // 2
            enemy_current_health -= damage
            print_colored(f"\n⚔️  You dealt {damage} damage to the {enemy_name}!", Fore.RED)
        elif choice == "2":
            damage = random.randint(5, 10) + player.magic // 2
            enemy_current_health -= damage
            print_colored(f"\n✨ You cast a spell for {damage} damage!", Fore.BLUE)
        elif choice == "3":
            player.use_potion()
            continue
        
        if enemy_current_health > 0:
            enemy_damage = random.randint(5, 15)
            player.health -= enemy_damage
            print_colored(f"💥 The {enemy_name} hits you for {enemy_damage} damage!", Fore.RED)
        
        time.sleep(1)
    
    return player.health > 0

def play_game():
    """Main game loop."""
    print_header()
    name, character_class = get_player_info()
    player = Player(name, character_class)
    
    print_colored(f"\nWelcome, {player.name} the {player.character_class}!", Fore.GREEN)
    print_colored("Your journey begins in the mystical land of Eldoria...", Fore.CYAN)
    time.sleep(2)
    
    # First choice
    print_colored("\nYou stand at a crossroads. Which path will you take?", Fore.CYAN)
    print_colored("1. The Dark Forest 🌲", Fore.GREEN)
    print_colored("2. The Ancient Ruins 🏛️", Fore.YELLOW)
    
    path = input(f"\n{Fore.YELLOW}Choose your path (1-2): {Style.RESET_ALL}").strip()
    
    if path == "1":
        print_colored("\nYou enter the Dark Forest...", Fore.GREEN)
        time.sleep(1)
        if not combat(player, "Forest Troll", 50):
            return False
        print_colored("\n🎉 You defeated the Forest Troll!", Fore.GREEN)
        player.inventory.append("Magic Ring")
        print_colored("You found a Magic Ring! 💍", Fore.YELLOW)
    else:
        print_colored("\nYou explore the Ancient Ruins...", Fore.YELLOW)
        time.sleep(1)
        if not combat(player, "Stone Golem", 60):
            return False
        print_colored("\n🎉 You defeated the Stone Golem!", Fore.GREEN)
        player.inventory.append("Ancient Scroll")
        print_colored("You found an Ancient Scroll! 📜", Fore.YELLOW)
    
    # Final battle
    print_colored("\nYou've reached the final challenge!", Fore.RED)
    time.sleep(1)
    if not combat(player, "Dragon", 100):
        return False
    
    print_colored("\n🎉 Congratulations! You've completed your quest!", Fore.GREEN)
    print_colored("Your final inventory:", Fore.YELLOW)
    for item in player.inventory:
        print_colored(f"  • {item}", Fore.CYAN)
    return True

def main():
    """Main game loop with play again feature."""
    while True:
        if play_game():
            print_colored("\n🏆 You are a true hero! 🌟", Fore.GREEN, Style.BRIGHT)
        else:
            print_colored("\n💀 Game Over! Better luck next time! 🍀", Fore.RED)
            
        play_again = input(f"\n{Fore.CYAN}Would you like to play again? (yes/no): {Style.RESET_ALL}").lower().strip()
        if play_again != 'yes':
            print_colored("\nThank you for playing Fantasy Quest! Farewell, brave hero! 👋✨", Fore.GREEN)
            break

if __name__ == "__main__":
    main() 