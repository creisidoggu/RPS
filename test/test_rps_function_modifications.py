from src.RPS_dict import get_computer_action

def test_see_most_used_action():
    assert get_computer_action('fran') == 0