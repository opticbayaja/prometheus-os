# Basic specifications for the Micro E-mini S&P 500 futures contract

symbol = "MES"
index_price = 6000.0
multiplier = 5.0
tick_size = 0.25

# Hypothetical trade
entry_price = 6000.0
stop_price = 5988.0
contracts = 2

# Calculations
tick_value = tick_size * multiplier
notional_value = index_price * multiplier
stop_distance = abs(entry_price - stop_price)
risk_per_contract = stop_distance * multiplier
total_risk = risk_per_contract * contracts

# Results
print(f"Contract: {symbol}")
print(f"Notional value: ${notional_value:,.2f}")
print(f"Tick value: ${tick_value:,.2f}")
print(f"Stop distance: {stop_distance:.2f} points")
print(f"Risk per contract: ${risk_per_contract:,.2f}")
print(f"Total risk: ${total_risk:,.2f}")