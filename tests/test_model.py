from src.jchess.pgn.parser import file
from src.jchess.model import File
from os import listdir
import pytest
from pydantic import ValidationError
import json

# Run from the tests dir
test_case_dir = "resources/"


def test_all_test_cases():
    for filename in [x for x in listdir(test_case_dir) if x.endswith('.pgn')]:
        with open(f"{test_case_dir}{filename}", 'r') as f:
            try:
                parsedoutput = file.parse(f.read()).or_die()
                pgn = File(entries=parsedoutput)
                for entry in pgn.entries:
                    assert len(entry.game.turns) > 0
                    assert len(entry.annotations) > 0
            except ValidationError as e:
                print(json.dumps(entry))
                pytest.fail(f"Validation Error for {filename}")
            except:
                pytest.fail(f"Failed on {filename}")
            print(f"Succesfully parsed {filename}")
