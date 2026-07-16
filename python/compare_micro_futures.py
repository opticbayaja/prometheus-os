from dataclasses import dataclass


@dataclass(frozen=True)
class FuturesContract:
    symbol: str
    name: str
    multiplier: float
    tick_size: float

    @property
    def tick_value(self) -> float:
        return self.multiplier * self.tick_size

    def risk_per_contract(self, stop_distance: float) -> float:
        if stop_distance <= 0:
            raise ValueError("Stop distance must be greater than zero.")

        return stop_distance * self.multiplier


contracts = [
    FuturesContract(
        symbol="MES",
        name="Micro E-mini S&P 500",
        multiplier=5.00,
        tick_size=0.25,
    ),
    FuturesContract(
        symbol="MNQ",
        name="Micro E-mini Nasdaq-100",
        multiplier=2.00,
        tick_size=0.25,
    ),
    FuturesContract(
        symbol="M2K",
        name="Micro E-mini Russell 2000",
        multiplier=5.00,
        tick_size=0.10,
    ),
    FuturesContract(
        symbol="MYM",
        name="Micro E-mini Dow",
        multiplier=0.50,
        tick_size=1.00,
    ),
]

stop_distances = {
    "MES": 10.0,
    "MNQ": 25.0,
    "M2K": 10.0,
    "MYM": 100.0,
}

print("MICRO E-MINI FUTURES COMPARISON")
print("-" * 75)

for contract in contracts:
    stop_distance = stop_distances[contract.symbol]
    risk = contract.risk_per_contract(stop_distance)

    print(f"Symbol: {contract.symbol}")
    print(f"Name: {contract.name}")
    print(f"Multiplier: ${contract.multiplier:,.2f} per point")
    print(f"Tick size: {contract.tick_size:.2f} points")
    print(f"Tick value: ${contract.tick_value:,.2f}")
    print(f"Example stop: {stop_distance:,.2f} points")
    print(f"Risk per contract: ${risk:,.2f}")
    print("-" * 75)