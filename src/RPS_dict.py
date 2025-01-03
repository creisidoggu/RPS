import random
from enum import IntEnum
import json


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: [GameAction.Paper, GameAction.Spock],
    GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Scissors: [GameAction.Rock, GameAction.Spock],
    GameAction.Lizard: [GameAction.Scissors, GameAction.Rock],
    GameAction.Spock: [GameAction.Paper, GameAction.Lizard]
}


def load_save_data(json_route):
    try:
        with open(json_route, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Save file not found, creating...")
        open(json_route, "w")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON file, creating...")
        open(json_route, "w")
        return {}


def write_save_data(json_route, data):
    with open(json_route, "w") as file:
        json.dump(data, file, indent=4)


def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    elif computer_action in Victories[user_action]:
        print(f"{computer_action.name} beats {user_action.name}. You loose!")
        game_result = GameResult.Defeat
        
    else:
        print(f"{user_action.name} beats {computer_action.name}. You win!")
        game_result = GameResult.Victory
        
    return game_result

def get_computer_action(username):
    loaded_data = load_save_data('src/player_data.json')
    elections = loaded_data[username][0]['elections']
    if all(value == 0 for value in elections.values()):
        computer_action = GameAction(random.randint(0, len(GameAction) - 1))
    else:
        most_used_choice = max(elections, key=elections.get)
        computer_action = Victories[GameAction[most_used_choice]][0]
    
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action(game_option):
    # Scalable to more options (beyond rock, paper and scissors...)
    if game_option == 2:
        valid_choices = list(GameAction)
    else:
        valid_choices = list(GameAction)[:3]
    game_choices = [f"{action.name}[{action.value}]" for action in valid_choices]
    game_choices_str = ", ".join(game_choices)
    
    while True:
        try:
            user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
            if user_selection not in [action.value for action in valid_choices]:
                print(f"Invalid choice. Pick a valid option from: {game_choices_str}")
                continue
            user_action = GameAction(user_selection)
            return user_action
        except ValueError:
            print('Invalid input. Enter a number corresponding to your choice.')


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == "y"


def selection_screen():
    while True:
        try:
            choice = int(input('Select a game mode: [0] EXIT [1] RPS [2] RPSLS\n'))
            if choice in [0, 1, 2]:
                return choice
            else:
                print('Invalid choice. Pick a number between 0 and 2')
        except ValueError:
            print('Invalid input. Enter a number')

def main():
    json_route = 'src/player_data.json'
    user = input('Insert a username:\n')
    player_data = load_save_data(json_route)
    
    if user not in player_data:
        player_data[user] = [
            {"elections": {action.name : 0 for action in GameAction}},
            {"history":[]}
        ]
        write_save_data(json_route, player_data)
    while True:
        game_option = selection_screen()
        if game_option==0:
            print('Exiting game. \'Seeya!')
            break
        while True:
            try:
                user_action = get_user_action(game_option)
            except ValueError:
                range_str = f"[0, {len(game_option) - 1}]"
                print(f"Invalid selection. Pick a choice in range {range_str}!")
                continue

            computer_action = get_computer_action(user)
            match_result = assess_game(user_action, computer_action)
            
            election_name = user_action.name
            player_data[user][0]['elections'][election_name] += 1
            player_data[user][1]['history'].append({
                "election": election_name,
                "match_result": match_result.name
            })
            
            write_save_data(json_route, player_data)

            if not play_another_round():
                break


if __name__ == "__main__":
    main()