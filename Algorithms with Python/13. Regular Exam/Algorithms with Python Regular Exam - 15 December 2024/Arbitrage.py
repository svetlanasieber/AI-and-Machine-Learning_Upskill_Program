import math
from collections import defaultdict


def detect_arbitrage(n, pairs, target_currency):

    currencies = set()
    graph = []
    for from_currency, to_currency, rate in pairs:
        currencies.add(from_currency)
        currencies.add(to_currency)
        weight = -math.log(float(rate))
        graph.append((from_currency, to_currency, weight))


    currency_index = {currency: idx for idx, currency in enumerate(currencies)}
    index_currency = {idx: currency for currency, idx in currency_index.items()}
    num_currencies = len(currency_index)


    distances = [float('inf')] * num_currencies
    predecessors = [-1] * num_currencies
    start = currency_index[target_currency]
    distances[start] = 0


    for _ in range(num_currencies - 1):
        for from_currency, to_currency, weight in graph:
            u = currency_index[from_currency]
            v = currency_index[to_currency]
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u


    arbitrage_path = []
    for from_currency, to_currency, weight in graph:
        u = currency_index[from_currency]
        v = currency_index[to_currency]
        if distances[u] + weight < distances[v]:
            # Negative cycle detected, reconstruct the cycle
            arbitrage_start = v
            for _ in range(num_currencies):
                arbitrage_start = predecessors[arbitrage_start]


            cycle = []
            current = arbitrage_start
            while True:
                cycle.append(current)
                current = predecessors[current]
                if current == arbitrage_start and len(cycle) > 1:
                    break

            arbitrage_path = [index_currency[idx] for idx in reversed(cycle)]
            break


    if arbitrage_path:
        return True, arbitrage_path
    else:
        result = {index_currency[idx]: round(math.exp(-distances[idx]), 3) for idx in range(num_currencies)}
        return False, result


def main():

    n = int(input())
    pairs = []
    print("Enter each trading pair in the format '{from_currency} {to_currency} {price}':")
    for _ in range(n):
        pair = input().strip().split()
        pairs.append((pair[0], pair[1], float(pair[2])))

    target_currency = input().strip()


    arbitrage_possible, output = detect_arbitrage(n, pairs, target_currency)

    if arbitrage_possible:
        print("True")
        print(" ".join(output))
    else:
        print("False")
        for currency, price in output.items():
            print(f"{currency}: {price:.3f}")


if __name__ == "__main__":
    main()
