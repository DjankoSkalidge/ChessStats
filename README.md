# ChessStats
Stats for a PGN file containing multiple game descriptions.

## Parsing PGN
This repository contains a tool that parses a `.pgn` file into a structured json file. 

### Usage
```
python parse_pgn.py [-h] input output

Positional arguments:
  input       Path of pgn file
  output      Destination of parsed output

```
Alternatively, import the grammar to parse your own files
```python
from pgn_grammar import file

with open(path_to_pgn_file, 'r') as f:
    parsedoutput = file.parse(f.read()).or_die()
```

### Features & Performance
This PGN parser's selling feature over parsers like `chess.pgn`, is that it parses and stores move annotations.

Lichess.org offers a functionality to export chess games with clock information for all the moves. This parser will
parse that clock information and include it in the final json structure.

The parser can parse 10000 games in ~20 seconds.



## Stats