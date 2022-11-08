from src.jchess.pgn.parser import file, chessmove
from os import listdir
import pytest

test_case_dir = "resources/"

def test_all_test_cases():
    for filename in [x for x in listdir(test_case_dir) if x.endswith('.pgn')]:
        with open(f"{test_case_dir}{filename}", 'r') as f:
            try:
                parsedoutput = file.parse(f.read()).or_die()
                for game in parsedoutput:
                    assert len(game["game"]["turns"]) > 0
                    assert len(game["annotations"]) > 0
                    for move in game["game"]["turns"]:
                        assert "movenumber" in move.keys() and "whitemove" in move.keys()
                        assert "annotations" in move["whitemove"].keys()
            except:
                pytest.fail(f"Failed on {filename}")


def test_simple_thing():
    try:
        move = chessmove.parse("r3").or_die()
    except Exception as e:
        print(e.__class__)
    # print(move)
