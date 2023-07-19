from get_alpha import get_stock
import matplotlib.pyplot as plt
import talib


def get_macd(start_date, end_date, code):
    df = get_stock(start_date, end_date, code)
    df.index = df['trade_date']
    # print(df)

    df['macd'], df['macdsignal'], df['macdhist'] = talib.MACD(df.close, fastperiod=12, slowperiod=26, signalperiod=9)
    print(df)

    plt.figure(figsize=(16, 8))
    plt.plot(df['close'], label='close')
    plt.plot(df['macd'], label='macd')
    plt.plot(df['macdsignal'], label='macdsignal')
    plt.plot(df['macdhist'], label='macdhist')
    plt.gca().set(title='MACD', xlabel='date', ylabel='price')
    plt.legend()
    plt.show()


def get_boll(start_date, end_date, code):
    df = get_stock(start_date, end_date, code)
    df.index = df['trade_date']
    # print(df)

    df['H_line'], df['M_line'], df['L_line'] = talib.BBANDS(df.close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    print(df)

    plt.figure(figsize=(16, 8))
    plt.plot(df['close'], label='close')
    plt.plot(df['H_line'], label='H_line')
    plt.plot(df['M_line'], label='M_line')
    plt.plot(df['L_line'], label='L_line')
    plt.gca().set(title='Bollinger Bands', xlabel='date', ylabel='price')
    plt.legend()
    plt.show()


def get_kdj(start_date, end_date, code):
    df = get_stock(start_date, end_date, code)
    df.index = df['trade_date']
    # print(df)

    df['K'], df['D'] = talib.STOCH(df.high, df.low, df.close, fastk_period=9, slowk_period=5, slowk_matype=1, slowd_period=5, slowd_matype=1)
    df.loc[:, 'J'] = 3.0 * df.loc[:, 'K'] - 2.0 * df.loc[:, 'D']
    print(df)

    plt.figure(figsize=(16, 8))
    plt.plot(df['high'], label='high')
    plt.plot(df['low'], label='low')
    plt.plot(df['close'], label='close')
    plt.plot(df['K'], label='K')
    plt.plot(df['D'], label='D')
    plt.plot(df['J'], label='J')
    plt.gca().set(title='KDJ', xlabel='date', ylabel='price')
    plt.legend()
    plt.show()


def get_obv(start_date, end_date, code):
    df = get_stock(start_date, end_date, code)
    df.index = df['trade_date']
    # print(df)

    df['obv'] = talib.OBV(df['close'], df['vol'])
    # 自行实现
    '''
    obv = []
    for i in range(0, len(df)):
        if i == 0:
            obv.append(df['vol'].values[i])
        else:
            if df['close'].values[i] > df['close'].values[i-1]:
                obv.append(obv[-1] + df['vol'].values[i])
            if df['close'].values[i] < df['close'].values[i-1]:
                obv.append(obv[-1] - df['vol'].values[i])
            if df['close'].values[i] == df['close'].values[i-1]:
                obv.append(obv[-1])
    df['obv'] = obv
    '''
    print(df)

    fig, ax1 = plt.subplots(1, 1, figsize=(16, 8))
    ax2 = ax1.twinx()
    line1 = ax1.plot(df['close'], label='close', color='royalblue')
    line2 = ax2.plot(df['obv'], label='obv', color='tomato')
    ax1.set_xlabel('date')
    ax1.set_ylabel('price')
    ax2.set_ylabel('obv')
    plt.title('OBV')
    lines = line1 + line2
    labels = [h.get_label() for h in lines]
    plt.legend(lines, labels, loc='upper right')
    plt.show()


# get_macd("2020-01-01", "2023-07-05", "430047.BJ")
# get_boll("2020-01-01", "2023-07-05", "430047.BJ")
# get_kdj("2020-01-01", "2023-07-05", "430047.BJ")
get_obv("2020-01-01", "2023-07-05", "430047.BJ")