import time

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Player and game state variables
player = {
    "name": "Joel Miller",
    "health": 100,
    "inventory": [],
    "location": "village"
}

locations = {
    "village": "You are in a peaceful village. There's a path to the forest.",
    "forest": "You are in a dense forest. It's dark and eerie. There's a path to the mountain.",
    "mountain": "You are at the base of a towering mountain. The artifact is rumored to be at the peak."
}

events = [
    # Village events
    {"location": "village", "description": "You meet a wise old man. He offers you a potion. Do you accept it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You gain 20 health.", "2": "You move on."}},
    {"location": "village", "description": "A merchant offers you a sword for 10 gold. Do you buy it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You don't have enough gold.", "2": "You move on."}},
    {"location": "village", "description": "A villager asks for your help to find his lost dog. Do you help?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You find the dog and gain a friend.", "2": "You move on."}},
    {"location": "village", "description": "You see a child crying. Do you comfort them?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "The child gives you a charm.", "2": "You move on."}},
    {"location": "village", "description": "A blacksmith offers to repair your armor for 5 gold. Do you agree?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You don't have enough gold.", "2": "You move on."}},
    
    # Forest events
    {"location": "forest", "description": "You find a fork in the path. Do you go left or right?", "choices": {"1": "Left", "2": "Right"}, "outcome": {"1": "You encounter a wild animal.", "2": "You find a hidden treasure."}},
    {"location": "forest", "description": "You come across a river. Do you swim across or walk along the bank?", "choices": {"1": "Swim", "2": "Walk"}, "outcome": {"1": "You are attacked by a crocodile.", "2": "You find a bridge."}},
    {"location": "forest", "description": "A strange plant catches your eye. Do you investigate?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "The plant releases poisonous spores.", "2": "You move on."}},
    {"location": "forest", "description": "You find an abandoned hut. Do you enter?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You find supplies.", "2": "You move on."}},
    {"location": "forest", "description": "You hear rustling in the bushes. Do you check it out?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You are ambushed by bandits.", "2": "You move on."}},
    {"location": "forest", "description": "You find a map on the ground. Do you take it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You gain a map of the forest.", "2": "You move on."}},
    {"location": "forest", "description": "You find a glowing stone. Do you pick it up?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "The stone grants you magical powers.", "2": "You move on."}},
    {"location": "forest", "description": "You see a deer stuck in a trap. Do you free it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "The deer leads you to a hidden grove.", "2": "You move on."}},
    {"location": "forest", "description": "You find a mysterious chest. Do you open it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You find gold.", "2": "You move on."}},
    
    # Mountain events
    {"location": "mountain", "description": "You encounter a steep cliff. Do you climb it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You reach the top safely.", "2": "You find another path."}},
    {"location": "mountain", "description": "A snowstorm begins. Do you seek shelter or press on?", "choices": {"1": "Shelter", "2": "Press on"}, "outcome": {"1": "You find a cave.", "2": "You are caught in the storm."}},
    {"location": "mountain", "description": "You see a distant figure. Do you approach?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "The figure is a friendly hermit.", "2": "You move on."}},
    {"location": "mountain", "description": "You find a mysterious door in the rock. Do you open it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You discover an ancient temple.", "2": "You move on."}},
    {"location": "mountain", "description": "You are feeling tired. Do you rest?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You regain some health.", "2": "You press on."}},
    {"location": "mountain", "description": "You find a strange artifact. Do you examine it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "It grants you a vision.", "2": "You move on."}},
    {"location": "mountain", "description": "You hear a distant roar. Do you investigate?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You find a dragon's lair.", "2": "You move on."}},
    {"location": "mountain", "description": "You find a hidden path. Do you follow it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "It leads to the artifact.", "2": "You move on."}},
    {"location": "mountain", "description": "You find a chest. Do you open it?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You find valuable items.", "2": "You move on."}},
    {"location": "mountain", "description": "You meet a traveler who offers to trade. Do you trade?", "choices": {"1": "Yes", "2": "No"}, "outcome": {"1": "You gain useful items.", "2": "You move on."}},
]

def main_menu():
    while True:
        print_with_delay("\n--- Main Menu ---")
        print_with_delay("1. Start New Game")
        print_with_delay("2. Instructions")
        print_with_delay("3. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            start_new_game()
        elif choice == '2':
            show_instructions()
        elif choice == '3':
            print_with_delay("Exiting game. Goodbye!")
            break
        else:
            print_with_delay("Invalid choice. Please enter a number from 1 to 4.")

def start_new_game():
    player["health"] = 100
    player["inventory"] = []
    player["location"] = "village"
    print_with_delay("\nStarting a new game...")
    game_loop()



def show_instructions():
    print_with_delay("\n--- Instructions ---")
    print_with_delay("1. Navigate through different locations.")
    print_with_delay("2. Encounter events and make decisions.")
    print_with_delay("3. Try to find the magical artifact and return safely.")
    print_with_delay("4. Manage your health and inventory.")
    print_with_delay("5. Have fun!\n")

def game_loop():
    while True:
        if player["health"] <= 0:
            print_with_delay("You have perished. Game over.")
            break

        print_with_delay(f"\nCurrent location: {player['location']}")
        print_with_delay(locations[player['location']])
        print_with_delay("1. Move")
        print_with_delay("2. Check Inventory")
        print_with_delay("3. Encounter Event")
        print_with_delay("4. Quit to Main Menu")

        choice = input("Please select an option: ")

        if choice == '1':
            move()
        elif choice == '2':
            check_inventory()
        elif choice == '3':
            encounter_event()
        elif choice == '4':
            print_with_delay("Returning to Main Menu...")
            break
        else:
            print_with_delay("Invalid choice. Please enter a number from 1 to 4.")

def move():
    if player['location'] == 'village':
        player['location'] = 'forest'
        print_with_delay("You move to the forest.")
    elif player['location'] == 'forest':
        player['location'] = 'mountain'
        print_with_delay("You move to the mountain.")
    elif player['location'] == 'mountain':
        print_with_delay("You have reached the mountain peak. The artifact is here!")
        event_artifact()

def check_inventory():
    if player["inventory"]:
        print_with_delay(f"Your inventory: {', '.join(player['inventory'])}")
    else:
        print_with_delay("Your inventory is empty.")

def encounter_event():
    current_location = player['location']
    available_events = [event for event in events if event["location"] == current_location]
    if available_events:
        event = available_events.pop(0)
        print_with_delay(f"\n{event['description']}")
        for key, choice in event['choices'].items():
            print_with_delay(f"{key}. {choice}")
        
        player_choice = input("Choose an option: ")
        if player_choice in event['choices']:
            print_with_delay(event['outcome'][player_choice])
        else:
            print_with_delay("Invalid choice. You miss the opportunity.")
    else:
        print_with_delay("There are no more events here.")

def event_artifact():
    print_with_delay("You found the magical artifact! Your quest is complete!")
    print_with_delay("Congratulations, you won the game!")
    player["inventory"].append("Magical Artifact")
    player["location"] = "village"
    print_with_delay("You return to the village victorious.")

# Entry point of the game
if __name__ == "__main__":
    main_menu()
