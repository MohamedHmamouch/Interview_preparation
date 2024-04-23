
def max_price(n, m, price):
    sum_val = 0

    for i in range(n):
        now_max = max(price)
        sum_val += now_max

        for j in range(len(price)):
            if price[j] == now_max:
                if (price[j] - 1) == 0:
                    price.pop(j)
                    break
                else:
                    price[j] -= 1
                break

    return sum_val


def min_price(n, m, price):
    sum_val = 0

    for i in range(n):
        now_min = min(price)
        sum_val += now_min

        for j in range(len(price)):
            if price[j] == now_min:
                if (price[j] - 1) == 0:
                    price.pop(j)
                    break
                else:
                    price[j] -= 1
                break

    return sum_val


def main():
    n, m = map(int, input().split())
    price = list(map(int, input().split()))

    a = max_price(n, m, price.copy())
    b = min_price(n, m, price.copy())

    print(a, b)


if __name__ == "__main__":
    main()
