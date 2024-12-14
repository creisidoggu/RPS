import random
from enum import IntEnum
import json


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock,
}


def load_save_data(json_route):
    try:
        with open(json_route, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Save file not found, creating...")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON file, creating...")
        return {}


def write_save_data(json_route, data):
    with open(json_route, "w") as file:
        json.dump(data, file, indent=4)


def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    return game_result

def get_computer_action(username):
    loaded_data = load_save_data('src/player_data.json')
    print(loaded_data)
    if loaded_data[username][0]['elections'] == {}:
        computer_selection = random.randint(0, len(GameAction) - 1)
        computer_action = GameAction(computer_selection)
    else:
        elections = loaded_data[username][0]['elections']
        most_used_choice = max(elections, key=elections.get)
        computer_action = Victories[GameAction[most_used_choice]]
    
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [
        f"{game_action.name}[{game_action.value}]" for game_action in GameAction
    ]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == "y"


def main():
    json_route = 'src/player_data.json'
    user = input('Inserte un usuario...')
    player_data = load_save_data(json_route)
    
    if user not in player_data:
        player_data[user] = [
            {"elections": {"Rock":0, "Paper":0, "Scissors":0}},
            {"history":[]}
        ]
    
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(user)
        match_result = assess_game(user_action, computer_action)
        print(match_result)
        
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