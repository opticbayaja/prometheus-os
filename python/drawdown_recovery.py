from dataclasses import dataclass


@dataclass(frozen=True)
class DrawdownScenario:
    initial_capital: float
    loss_percentage: float

    def validate(self) -> None:
        if self.initial_capital <= 0:
            raise ValueError("Initial capital must be greater than zero.")

        if not 0 < self.loss_percentage < 100:
            raise ValueError(
                "Loss percentage must be greater than 0 and less than 100."
            )

    @property
    def loss_rate(self) -> float:
        return self.loss_percentage / 100

    @property
    def capital_after_loss(self) -> float:
        return self.initial_capital * (1 - self.loss_rate)

    @property
    def dollars_lost(self) -> float:
        return self.initial_capital - self.capital_after_loss

    @property
    def recovery_percentage(self) -> float:
        return (
            self.initial_capital / self.capital_after_loss - 1
        ) * 100

    @property
    def dollars_to_recover(self) -> float:
        return self.initial_capital - self.capital_after_loss


initial_capital = 10_000.00
loss_percentages = [10, 20, 30, 40, 50]

print("DRAWDOWN RECOVERY REPORT")
print("-" * 72)
print(
    f"{'Loss':>8}"
    f"{'Capital Left':>18}"
    f"{'Dollars Lost':>18}"
    f"{'Recovery Needed':>20}"
)
print("-" * 72)

for loss_percentage in loss_percentages:
    scenario = DrawdownScenario(
        initial_capital=initial_capital,
        loss_percentage=loss_percentage,
    )

    scenario.validate()

    print(
        f"{scenario.loss_percentage:>7.0f}%"
        f"${scenario.capital_after_loss:>16,.2f}"
        f"${scenario.dollars_lost:>16,.2f}"
        f"{scenario.recovery_percentage:>19.2f}%"
    )

print("-" * 72)
print(
    "Principle: Recovery requirements accelerate as drawdowns become larger."
)