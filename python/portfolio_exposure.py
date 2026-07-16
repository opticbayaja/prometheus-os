from dataclasses import dataclass
from collections import defaultdict


@dataclass(frozen=True)
class Position:
    symbol: str
    direction: str
    risk_dollars: float
    risk_factor: str

    def validate(self) -> None:
        if self.risk_dollars <= 0:
            raise ValueError(
                f"Risk for {self.symbol} must be greater than zero."
            )

        if self.direction not in {"LONG", "SHORT"}:
            raise ValueError(
                f"Direction for {self.symbol} must be LONG or SHORT."
            )


# Simulated positions.
positions = [
    Position(
        symbol="MES",
        direction="LONG",
        risk_dollars=50.00,
        risk_factor="US_EQUITIES",
    ),
    Position(
        symbol="MNQ",
        direction="LONG",
        risk_dollars=50.00,
        risk_factor="US_EQUITIES",
    ),
    Position(
        symbol="M2K",
        direction="LONG",
        risk_dollars=50.00,
        risk_factor="US_EQUITIES",
    ),


]

for position in positions:
    position.validate()


gross_portfolio_risk = sum(
    position.risk_dollars for position in positions
)

risk_by_factor: dict[str, float] = defaultdict(float)

for position in positions:
    risk_by_factor[position.risk_factor] += position.risk_dollars


print("PORTFOLIO EXPOSURE REPORT")
print("-" * 60)

for position in positions:
    print(
        f"{position.symbol:<5} "
        f"{position.direction:<5} "
        f"Risk: ${position.risk_dollars:,.2f} "
        f"Factor: {position.risk_factor}"
    )

print("-" * 60)
print(f"Gross portfolio risk: ${gross_portfolio_risk:,.2f}")

print("\nRISK BY FACTOR")
print("-" * 60)

for factor, factor_risk in risk_by_factor.items():
    concentration = factor_risk / gross_portfolio_risk * 100

    print(f"{factor}: ${factor_risk:,.2f}")
    print(f"Portfolio concentration: {concentration:.2f}%")

print("-" * 60)

largest_factor = max(
    risk_by_factor,
    key=risk_by_factor.get,
)

largest_factor_risk = risk_by_factor[largest_factor]
largest_concentration = (
    largest_factor_risk / gross_portfolio_risk * 100
)

print(f"Largest risk factor: {largest_factor}")
print(f"Largest concentration: {largest_concentration:.2f}%")

if largest_concentration >= 80:
    print("Warning: Portfolio risk is highly concentrated.")
else:
    print("Portfolio risk is distributed across multiple factors.")