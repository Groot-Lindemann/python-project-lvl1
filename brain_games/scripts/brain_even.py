#!/usr/bin/evn python3

"""Running module for Brain Even."""

from brain_games import engine
from brain_games.games import even


def main():
    """Run Even game"""
    engine.start_game(even)


if __name__ == '__main__':
    main()
