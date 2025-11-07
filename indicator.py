import pandas as pd
import numpy as np

def moving_averages(df, short=20, long=50):
    df['MA_short'] = df['Close'].rolling(short).mean()
    df['MA_long'] = df['Close'].rolling(long).mean()
    return df

def volatility_features(df, period=14):
    df['ATR'] = df['High'] - df['Low']
    df['Boll_Width'] = (df['Close'].rolling(period).std()) / df['Close']
    return df

def momentum_indicators(df, period=14):
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    rs = gain.rolling(period).mean() / loss.rolling(period).mean()
    df['RSI'] = 100 - (100 / (1 + rs))
    df['Momentum'] = df['Close'] - df['Close'].shift(period)
    return df
