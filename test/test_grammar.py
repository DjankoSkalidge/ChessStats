from src.pgn_grammar import file
from os import listdir
import pytest

test_case_dir = "test/resources/"

def test_all_test_cases():
    for filename in [x for x in listdir(test_case_dir) if x.endswith('.pgn')]:
        with open(f"{test_case_dir}{filename}", 'r') as f:
            try:
                parsedoutput = file.parse(f.read()).or_die()
                for game in parsedoutput:
                    assert len(game["game"]["moves"]) > 0
                    assert len(game["annotations"]) > 0
                    for move in game["game"]["moves"]:
                        assert "movenumber" in move.keys() and "whitemove" in move.keys()
                        assert "annotations" in move["whitemove"].keys()
            except:
                pytest.fail(f"Failed on {filename}")
