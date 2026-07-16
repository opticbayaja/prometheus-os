import math
from collections.abc import Sequence


def pearson_correlation(
    series_a: Sequence[float],
    series_b: Sequence[float],
) -> float:
    """Calculate the Pearson correlation between two return series."""

    if len(series_a) != len(series_b):
        raise ValueError("Both series must contain the same number of values.")

    if len(series_a) < 2:
        raise ValueError("At least two observations are required.")

    mean_a = sum(series_a) / len(series_a)
    mean_b = sum(series_b) / len(series_b)

    numerator = sum(
        (value_a - mean_a) * (value_b - mean_b)
        for value_a, value_b in zip(series_a, series_b)
    )

    squared_deviation_a = sum(
        (value - mean_a) ** 2 for value in series_a
    )

    squared_deviation_b = sum(
        (value - mean_b) ** 2 for value in series_b
    )

    denominator = math.sqrt(
        squared_deviation_a * squared_deviation_b
    )

    if denominator == 0:
        raise ValueError(
            "Correlation is undefined when a series has no variation."
        )

    return numerator / denominator


# Synthetic daily percentage returns.
# These numbers are educational examples, not current market data.

mes_returns = [
    1.29, 1.45, 0.07, -0.76, -1.09,
    0.03, -1.02, -1.44, 0.20, 0.13,
    0.55, -0.91, 0.01, -0.06, -1.51,
    0.54, 0.32, 2.39, 0.20, -0.14,
]

mnq_returns = [
    1.53, 1.30, 0.37, -0.78, -0.85,
    0.39, -0.63, -1.18, -0.21, 0.27,
    0.49, -0.52, 0.08, 0.33, -1.30,
    0.53, 0.51, 1.65, 0.03, -0.30,
]

gold_returns = [
    2.11, 0.05, 0.66, 0.54, -0.39,
    -1.55, 0.86, -0.55, 0.74, -1.29,
    -0.38, 1.17, 1.43, -1.31, -1.48,
    0.01, 0.76, 0.40, 0.32, -1.00,
]


market_pairs = {
    "MES vs MNQ": (mes_returns, mnq_returns),
    "MES vs Gold": (mes_returns, gold_returns),
    "MNQ vs Gold": (mnq_returns, gold_returns),
}


print("CORRELATION ANALYSIS")
print("-" * 50)

for pair_name, return_series in market_pairs.items():
    correlation = pearson_correlation(
        return_series[0],
        return_series[1],
    )

    print(f"{pair_name}: {correlation:.2f}")

print("-" * 50)
print("Important: The data above is synthetic.")
print("Real correlations change through time.")