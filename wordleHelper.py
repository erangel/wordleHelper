#!/usr/bin/python

import sys, argparse, re


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w", "--wordle", help="Wordle current state. Use '.' to mark unknows."
    )
    parser.add_argument("-e", "--exclude", help="letters that can be excluded")

    args = parser.parse_args()

    include = "^" + args.wordle + "$"
    exclude = "^[^" + args.exclude + "]{5}$"

    print("wordle guess: " + include)
    print("excluding chars: " + exclude)

    # Read word file
    dictFile = open("/usr/share/dict/words")
    words = [word.strip() for word in dictFile.readlines() if len(word.strip()) == 5]
    dictFile.close

    prog = re.compile(include, re.RegexFlag.IGNORECASE)
    prog_exclude = re.compile(exclude, re.RegexFlag.IGNORECASE)
    by_guess_1 = list(filter(lambda w: prog.match(w), words))
    by_guess_2 = list(filter(lambda w: prog_exclude.match(w), by_guess_1))
    print(len(by_guess_2))
    print(by_guess_2)


if __name__ == "__main__":
    main(sys.argv[1:])
