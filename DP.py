def get_is_possible(coins, target):
    coins = list(filter(lambda x: x < target, coins))
    is_possible = [False for _ in range(target + 1)]
    for c in coins:
        is_possible[c] = True
    for i in range(target + 1):
        for c in coins:
            if c <= i:
                is_possible[i] |= is_possible[i - c]
    return is_possible[target]


def get_num_possible_ways(coins, target):
    coins = list(filter(lambda x: x < target, coins))
    ways = [0 for _ in range(target + 1)]
    for c in coins:
        ways[c] = 1
    for i in range(target + 1):
        for c in coins:
            if c <= i:
                ways[i] += ways[i - c]
    return ways[target]


if __name__ == '__main__':
    # Coin Change 1
    print(get_is_possible([17, 22, 10], 43))

    # Coin Change 2
    print(get_num_possible_ways([17, 22, 10], 44))
