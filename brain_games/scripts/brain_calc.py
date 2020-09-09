#!/usr/bin/env python3

"""Running module for Brain Calc."""

from brain_games import engine
from brain_games.games import calc


def main():
    """Run Calc game."""
    engine.start_game(calc)


if __name__ == '__main__':
    main()
