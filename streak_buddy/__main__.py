import argparse
from . import streak


def main():
    parser = argparse.ArgumentParser(prog="streak_buddy")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("mark")
    sub.add_parser("show")
    sub.add_parser("reset")
    args = parser.parse_args()
    if args.cmd == "mark":
        s = streak.mark_today()
        print(f"Streak: {s} days")
    elif args.cmd == "show":
        print(f"Streak: {streak.get_streak()} days")
    elif args.cmd == "reset":
        streak.reset()
        print("Streak reset")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
