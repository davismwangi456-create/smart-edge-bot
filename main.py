import pandas as pd
from indicators import moving_averages, volatility_features, momentum_indicators
from backtest import classify_market_regimes
from visualize import plot_regimes

# Load your data (place a CSV under /data)
df = pd.read_csv('data/sample_data.csv')

# Compute indicators
df = moving_averages(df)
df = volatility_features(df)
df = momentum_indicators(df)

# Classify market regimes
df = classify_market_regimes(df)

# Visualize results
plot_regimes(df)

# Save processed output
df.to_csv('data/processed_output.csv', index=False)
print("✅ Analysis complete! Saved to data/processed_output.csv")
