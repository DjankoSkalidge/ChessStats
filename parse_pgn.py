import argparse
import json
from pgn_grammar import file


def main():
    args = parse_args()
    with open(args.input, 'r') as f:
        parsedoutput = file.parse(f.read()).or_die()
    with open(args.output, 'w+') as f:
        json.dump(parsedoutput, f)


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input', help='Path of pgn file', type=str)
    parser.add_argument('output', help='Destination of parsed output', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    main()
