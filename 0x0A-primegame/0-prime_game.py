#!/usr/bin/python3
"""Module defining the isWinner function for the Prime Game."""

def isWinner(x, nums):
    """Determines the winner of the prime game after x rounds.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers where each integer represents the
                     maximum number for that round.

    Returns:
        str: The name of the player that won the most rounds. If the winner
             cannot be determined, returns None.
    """
    maria_wins_count = 0
    ben_wins_count = 0

    for num in nums:
        rounds_set = list(range(1, num + 1))
        primes_set = primes_in_range(1, num)

        if not primes_set:
            ben_wins_count += 1
            continue

        is_maria_turn = True

        while True:
            if not primes_set:
                if is_maria_turn:
                    ben_wins_count += 1
                else:
                    maria_wins_count += 1
                break

            smallest_prime = primes_set.pop(0)
            rounds_set.remove(smallest_prime)
            rounds_set = [x for x in rounds_set if x % smallest_prime != 0]

            is_maria_turn = not is_maria_turn

    if maria_wins_count > ben_wins_count:
        return "Maria"

    if maria_wins_count < ben_wins_count:
        return "Ben"

    return None

def is_prime(n):
    """Determines if a number is a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Generates a list of prime numbers within a specified range.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.

    Returns:
        list: A list of prime numbers between start and end (inclusive).
    """
    return [n for n in range(start, end + 1) if is_prime(n)]

# Example usage
if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
