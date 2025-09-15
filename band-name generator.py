#!/usr/bin/env python3
"""
Band Name Generator
A simple program that generates a band name based on user input.
"""

import time


def main():
    """Main function to run the band name generator."""
    # Display welcome message
    print("🎸 Welcome to the Band Name Generator! 🥁")
    print("Let's create an awesome name for your band.\n")

    # Get user input
    city = input("What's the name of the city you grew up in?\n> ")
    pet = input("What's the name of your first pet?\n> ")

    # Generate band name
    band_name = f"{city} {pet}"

    # Display result with animation
    print("\nGenerating your band name", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    print(f"\n\n🎶 Your band name could be: {band_name}! 🎶")

    # Ask if user wants to generate another name
    while True:
        again = input("\nGenerate another name? (y/n): ").lower()
        if again == 'y':
            print("\n" + "=" * 40 + "\n")
            main()  # Restart the program
            break
        elif again == 'n':
            print("\nThanks for using the Band Name Generator! Rock on! 🤘")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()