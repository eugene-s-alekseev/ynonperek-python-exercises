import argparse
import collections
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", action="store", default=True, type=str)
    args = parser.parse_args()
    with open(args.f) as file:
        words = file.read()
        print(words)
        words = re.split("\W+", words)

    word, count = list(collections.Counter(words).most_common())[0]
    print(word, count)

if __name__ == "__main__":
    main()
