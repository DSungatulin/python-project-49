#!/usr/bin/env python3
from brain_games.games import brain_calc
from brain_games.engine import run_game_engine


def main():
    run_game_engine(brain_calc)


if __name__ == '__main__':
    main()
