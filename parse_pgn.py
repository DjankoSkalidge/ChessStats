import argparse
import json
from pgn_grammar import file
import pandas as pd


def to_csv(parsedoutput: dict) -> pd.DataFrame:
    columns = ['event', 'white', 'black', 'time_control', 'datetime', 'moves', 'result', 'termination', 'white_rating', 'black_rating', 'opening']
    df = pd.DataFrame(columns=columns)
    for game in parsedoutput:
        df = pd.concat([df, pd.DataFrame([{'event': game["annotations"].get("Event", "unknown"),
                         'white': game["annotations"].get("White", "unknown"),
                         'black': game["annotations"].get("Black", "unknown"),
                         'time_control': game["annotations"].get("TimeControl", "unknown"),
                         'datetime': f"{game['annotations'].get('UTCDate')} {game['annotations'].get('UTCTime')}",
                         'moves': json.dumps(game["game"]["moves"]),
                         'result': game["game"]["outcome"],
                         'termination': game["annotations"].get("Termination", "unknown"),
                         'white_rating': game["annotations"].get("WhiteElo", "unknown"),
                         'black_rating': game["annotations"].get("BlackElo", "unknown"),
                         'opening': game["annotations"].get("Opening", "unknown")
                         }])],axis=0, ignore_index=True)
    return df

def main():
    args = parse_args()
    if args.output_format == 'mp4':
        print("Wat dacht jezelf?")
        exit()
    with open(args.input, 'r') as f:
        parsedoutput = file.parse(f.read()).or_die()
    if args.output_format == 'json':
        with open(args.output, 'w+') as f:
            json.dump(parsedoutput, f)
    elif args.output_format == 'csv':
        to_csv(parsedoutput).to_csv(args.output)



def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('input', help='Path of pgn file', type=str)
    parser.add_argument('output', help='Destination of parsed output', type=str)
    parser.add_argument('--output-format', choices=['csv', 'json', 'mp4'], type=str, default='json')

    return parser.parse_args()


if __name__ == '__main__':
    main()
