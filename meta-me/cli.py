import argparse
from metasearch import metasearch

def main():
    parser = argparse.ArgumentParser(
        description="A metacritic search tool"
    )
    parser.add_argument(
        "search_term", type = str,
        help="The name of the game/movie/tv show"
    )
    args = parser.parse_args()
    results = metasearch(args.search_term)

if __name__ == "__main__":  
    main()