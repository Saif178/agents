from decimal import Decimal, getcontext


def compute_pi_like_series(terms: int = 1_000_000) -> Decimal:
    # Set precision high enough to capture the result accurately
    getcontext().prec = 30

    total = Decimal(0)
    sign = 1

    for i in range(terms):
        denominator = 2 * i + 1
        term = Decimal(sign) / Decimal(denominator)
        total += term
        sign *= -1

    return total * 4


if __name__ == "__main__":
    result = compute_pi_like_series()
    print(result)
