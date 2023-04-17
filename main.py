import argparse
from spotify_data_scraper import SpotifyData, SpotifyAudioLoader
from pathlib import Path
def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root","-r", required=True, type=Path,
                        help="Path to store json data")
    parser.add_argument("--client_id", "-i", type=str, required=True,
                        help="Client ID")
    parser.add_argument("--client_secret", "-s", type=str, required=True)
    parser.add_argument("--show_id", type=str, default="27XP61URSuKu9oeWR793D6")
    args = parser.parse_args()
    return args

def main():
    args = cli()
    data = SpotifyData(args.root, args.client_id, args.client_secret)
    data.fetch_episodes(show_id=args.show_id)


if __name__=="__main__":
    main()