import time

# --- 1. Initial Market Setup ---
fair_value = 40.0
initial_algo_bid = 20.0
initial_algo_ask = 100.0  # As per your "100 seller" comment

# The price at which the algo will flip from 'bidding up' to 'selling'
# 20% above fair value
sell_trigger_price = fair_value * (1 + 0.20)  # 40.0 * 1.20 = 48.0

# --- Market State Variables ---
current_algo_bid = initial_algo_bid
current_algo_ask = initial_algo_ask
human_bid = 0.0
human_position = 0
human_cost_basis = 0.0

def print_market_state():
    """Helper function to show the current market."""
    print(f"  Market: Bid ${current_algo_bid:.2f} (Algo) / Ask ${current_algo_ask:.2f} (Algo)")

print("--- START: Illiquid Market ---")
print(f"Option Fair Value is estimated at: ${fair_value:.2f}")
print(f"Algo is setting a wide market to provide 'fake' liquidity.")
print_market_state()
print("-" * 40)
time.sleep(3)


# --- 2. Human Buyer Arrives ---
human_bid = 21.0
print(f"\n--- EVENT 1: Human Buyer Arrives ---")
print(f"Human places a bid to buy at: ${human_bid:.2f}")
print(f"  New Best Bid is: ${human_bid:.2f} (Human)")
time.sleep(2)


# --- 3. The Algo 'Chase' ---
print(f"\n--- EVENT 2: The Algo 'Chase' Begins ---")
print("Algo detects the human bid and starts 'walking up' the price.")

# We simulate the chase, with the algo always bidding 1 tick above the human
chase_prices = [22.0, 25.0, 29.0, 34.0, 38.0, 42.0, 46.0]

for price in chase_prices:
    # Algo outbids the human
    current_algo_bid = price
    print(f"\nAlgo updates its bid to: ${current_algo_bid:.2f}")
    print_market_state()
    time.sleep(1)
    
    # Human gets frustrated and bids higher
    human_bid = price + 1.0
    print(f"Human chases, updates bid to: ${human_bid:.2f}")
    time.sleep(1)

print("-" * 40)
print("The human is now chasing the price far above the fair value of $40.")
time.sleep(2)


# --- 4. The Human Crosses the 'Sell Trigger' ---
print(f"\n--- EVENT 3: The 'Trap' is Sprung ---")
print(f"Algo's hidden 'Sell Trigger' price is: ${sell_trigger_price:.2f}")
human_bid = sell_trigger_price
print(f"Desperate, the human places a final bid at: ${human_bid:.2f}")
time.sleep(2)


# --- 5. The Algo 'Flips' and Sells ---
print(f"\n--- EVENT 4: The Algo Sells ---")
print(f"Algo sees the human bid at ${human_bid:.2f}, which is its trigger price.")
print(f"Algo's original ask was ${initial_algo_ask:.2f}.")

# This is the "flip"
current_algo_ask = human_bid  # Algo drops its ask from 100 to 48
print(f"Algo INSTANTLY changes its ask to ${current_algo_ask:.2f} to fill the human's bid.")
time.sleep(1)

print("\n*** TRANSACTION EXECUTED ***")
print(f"  Human BUYER bought 1 option @ ${human_bid:.2f}")
print(f"  Algo SELLER sold 1 option @ ${current_algo_ask:.2f}")

human_position = 1
human_cost_basis = current_algo_ask
print(f"Human now owns 1 option, with a cost of ${human_cost_basis:.2f}")
print("-" * 40)
time.sleep(3)


# --- 6. The Algo Resets ---
print(f"\n--- EVENT 5: The Algo Resets the Market ---")
print("Immediately after the trade, the algo resets its quotes...")

current_algo_bid = initial_algo_bid
current_algo_ask = initial_algo_ask
human_bid = 0.0  # The human's bid is filled, so it's gone

print(f"NEW Market State:")
print_market_state()
print(f"The spread is wide again: ${current_algo_ask - current_algo_bid:.2f}")
print("-" * 40)
time.sleep(2)


# --- 7. The Outcome (Human's Loss) ---
print(f"\n--- OUTCOME: The Human's Position ---")
print(f"The human buyer is holding the option, which they bought for: ${human_cost_basis:.2f}")
print("The human now looks at the market to see what their option is 'worth'.")
print(f"  Best Bid (the price they can sell for): ${current_algo_bid:.2f}")
print(f"  Best Ask (the price to buy another): ${current_algo_ask:.2f}")

# Calculate the immediate "paper" loss
immediate_loss = human_cost_basis - current_algo_bid

print(f"\nIf the human wants to sell, they must sell to the algo's bid of ${current_algo_bid:.2f}.")
print(f"This represents an immediate loss of: ${human_cost_basis:.2f} (Cost) - ${current_algo_bid:.2f} (Market Bid) = ${immediate_loss:.2f}")
print("The human has been trapped by the algo in an illiquid market.")
