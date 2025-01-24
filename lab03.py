import random

# Define Variables
numLives = 10           # Number of player's lives remaining
mNumLives = 12          # Number of monster's lives remaining
diceOptions = list(range(1, 7))  # Create a list of dice values [1, 2, 3, 4, 5, 6]

# Get user input for combat strength
combatStrength = int(input("Enter your combat strength (Number between 1-6): "))
while combatStrength < 1 or combatStrength > 6:
    print("Input must be an integer between 1-6.")
    combatStrength = int(input("Enter your combat strength: "))

mCombatStrength = int(input("Enter the monster's combat strength (Number between 1-6): "))
while mCombatStrength < 1 or mCombatStrength > 6:
    print("Input must be an integer between 1-6.")
    mCombatStrength = int(input("Enter the monster's combat strength: "))

# Define weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Display available weapons
print("\nAvailable Weapons:")
for i, weapon in enumerate(weapons, start=1):
    print(f"{i}. {weapon}")

# Simulate 10 rounds of battle
print("\nStarting the battle sequence!\n")
for round_num in range(1, 20, 2):  # Simulate rounds 1, 3, 5, ..., 19
    if round_num == 11:
        print("Battle Truce declared in Round 11. Game Over!")
        break

    # Roll dice for hero and monster
    hero_roll = random.choice(diceOptions)
    monster_roll = random.choice(diceOptions)

    # Add dice rolls to combat strengths
    hero_total_strength = combatStrength + hero_roll
    monster_total_strength = mCombatStrength + monster_roll

    # Determine selected weapons based on dice rolls
    hero_weapon = weapons[hero_roll - 1]  # Subtract 1 for zero-based indexing
    monster_weapon = weapons[monster_roll - 1]

    # Announce the round and results
    print(f"Round {round_num}: Hero rolled {hero_roll}, Monster rolled {monster_roll}.")
    print(f"Hero selected: {hero_weapon}, Monster selected: {monster_weapon}.")
    print(f"Hero Total Strength: {hero_total_strength}, Monster Total Strength: {monster_total_strength}.")

    # Determine the winner of the round
    if hero_total_strength > monster_total_strength:
        print("Hero wins the round!\n")
    elif hero_total_strength < monster_total_strength:
        print("Monster wins the round!\n")
    else:
        print("It's a tie!\n")

print("Battle sequence complete!")