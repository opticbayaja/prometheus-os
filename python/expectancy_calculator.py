from statistics import mean


# Synthetic results expressed in R multiples.
# Positive numbers are winning trades.
# Negative numbers are losing trades.
trade_results_r = [
    1.50,
    -1.00,
    2.00,
    -1.00,
    1.00,
    -1.00,
    3.00,
    -1.00,
    -1.00,
    2.00,

]

risk_dollars_per_trade = 50.00

winning_trades = [
    result for result in trade_results_r if result > 0
]

losing_trades = [
    result for result in trade_results_r if result < 0
]

total_trades = len(trade_results_r)
number_of_wins = len(winning_trades)
number_of_losses = len(losing_trades)

win_rate = number_of_wins / total_trades
loss_rate = number_of_losses / total_trades

average_win_r = mean(winning_trades) if winning_trades else 0.0
average_loss_r = (
    abs(mean(losing_trades)) if losing_trades else 0.0
)

expectancy_r = (
    win_rate * average_win_r
    - loss_rate * average_loss_r
)

gross_profit_r = sum(winning_trades)
gross_loss_r = abs(sum(losing_trades))

profit_factor = (
    gross_profit_r / gross_loss_r
    if gross_loss_r > 0
    else float("inf")
)

total_result_r = sum(trade_results_r)
expectancy_dollars = expectancy_r * risk_dollars_per_trade
total_result_dollars = total_result_r * risk_dollars_per_trade

print("TRADING EXPECTANCY REPORT")
print("-" * 50)
print(f"Total trades: {total_trades}")
print(f"Winning trades: {number_of_wins}")
print(f"Losing trades: {number_of_losses}")
print(f"Win rate: {win_rate:.2%}")
print(f"Average win: {average_win_r:.2f}R")
print(f"Average loss: {average_loss_r:.2f}R")
print(f"Expectancy: {expectancy_r:.2f}R per trade")
print(f"Profit factor: {profit_factor:.2f}")
print(f"Total result: {total_result_r:.2f}R")
print(f"Expected dollars per trade: ${expectancy_dollars:,.2f}")
print(f"Total simulated result: ${total_result_dollars:,.2f}")

if expectancy_r > 0:
    print("Assessment: Positive simulated expectancy.")
elif expectancy_r < 0:
    print("Assessment: Negative simulated expectancy.")
else:
    print("Assessment: Break-even simulated expectancy.")

print("-" * 50)
print("Warning: This synthetic sample does not prove future profitability.")