#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def play_game(n):
    """
    Stimulate a single game from 1 to n.
    Returns True if Maria wins, False if Ben wins.
    """

    # available numbers set
    available = set(range(1, n + 1))
    maria_turn = True

    while True:
        primes = [p for p in available if is_prime(p)]

        if not primes:
            return not maria_turn

        prime = min(primes)

        to_remove = {p for p in available if p % prime == 0}
        available -= to_remove
        # next palyer turn
        maria_turn = not maria_turn


def isWinner(x, nums):
    """
    Overall winner across x rounds.

    Args:
    x (int): Number of rounds
    nums (list): Set of n for each round

    Returns:
    str: Name of the player who won most rounds, or None
    """

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
