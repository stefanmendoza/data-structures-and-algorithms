# Problem: Given a value N and a list of coins L, find the least amount of
# coins from L required to reach value N.

# T(n) = O(N) * O(L) = O(N)
def compute(target_sum, available_coins):
    results = [None] * (target_sum + 1)

    if target_sum in available_coins:
        return [target_sum]

    for value in range(1, target_sum + 1):
        # The minimum coins to get to the value is 1 (itself)
        if value in available_coins:
            results[value] = [value]
            continue

        # The value is smaller than the smallest coin we have
        # so it's impossible to get to this value
        if value < min(available_coins):
            continue

        smallest_list = []
        smallest_list_length = target_sum + 1
        for coin in available_coins:
            if results[value - coin] is not None:
                # The smallest possible list for each coin will be the smallest list for the
                # value of [target value - coin] with the given coin added. This may or may
                # not result in the optimal length list or even a list that sums up to the
                # target value
                current_list = results[value - coin] + [coin]

                if sum(current_list) <= value and len(current_list) < smallest_list_length:
                    smallest_list = current_list
                    smallest_list_length = len(current_list)

        if sum(smallest_list) == value:
            results[value] = smallest_list

    return results[target_sum]
