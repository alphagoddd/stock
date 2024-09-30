def calculate_position_size(capital, risk_percentage, entry_price, stop_loss_price):
    risk_per_trade = capital * (risk_percentage / 100)
    position_size = risk_per_trade / abs(entry_price - stop_loss_price)
    return position_size

def calculate_risk_reward_ratio(entry_price, target_price, stop_loss_price):
    risk = abs(entry_price - stop_loss_price)
    reward = abs(target_price - entry_price)
    risk_reward_ratio = reward / risk
    return risk_reward_ratio

if __name__ == "__main__":
    capital = 10000  # Total capital in dollars
    risk_percentage = 2  # Risk 2% of capital per trade
    entry_price = 150  # Stock entry price
    stop_loss_price = 145  # Stop-loss price
    target_price = 160  # Target price
    
    position_size = calculate_position_size(capital, risk_percentage, entry_price, stop_loss_price)
    risk_reward_ratio = calculate_risk_reward_ratio(entry_price, target_price, stop_loss_price)
    
    print(f"Position Size: {position_size}")
    print(f"Risk-Reward Ratio: {risk_reward_ratio}")
