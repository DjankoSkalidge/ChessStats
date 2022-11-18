import json

from src.jchess.model import File
from src.jchess.pgn.parser import file
from src.jchess.data.data import DataInstance


class DataLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not filepath.endswith('.pgn') and not filepath.endswith('.json'):
            print(".pgn or .json file extension expected. Will try to parse this as a PGN.")

    def load(self):
        if self.filepath.endswith('.json'):
            print(f"Parsing json file {self.filepath}")
            with open(self.filepath, 'r') as f:
                obj = json.load(f)
                data = File(entries=obj["entries"])
        else:
            print(f"Parsing pgn file {self.filepath}")
            with open(self.filepath, 'r') as f:
                data = File(entries=file.parse(f.read()).or_die())
        return DataInstance(data.entries)
