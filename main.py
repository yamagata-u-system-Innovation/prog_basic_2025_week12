from __future__ import annotations
import matplotlib.pyplot as plt

from stock_utils import read_stock_csv, moving_average, calc_buy_signals, summarize

DATA_PATH = "data/stock_dummy.csv"

def main() -> None:
    # 1) CSV読み込み
    dates, closes = read_stock_csv(DATA_PATH)

    # 2) サマリ表示
    mn, mx = summarize(closes)
    print(f"rows={len(closes)}, min={mn}, max={mx}")

    # 3) 移動平均
    ma5 = moving_average(closes, window=5)

    # 4) 買いシグナル
    signals = calc_buy_signals(dates, closes, ma5)
    print("buy signals:")
    for idx in signals[:10]:
        print(f"  {dates[idx]} close={closes[idx]} ma5={ma5[idx]}")

    # 5) グラフ表示
    x = list(range(len(closes)))

    # TODO: 終値の折れ線
    # TODO: 移動平均（Noneは飛ばして描く工夫：例として y_ma = [v if v is not None else float('nan') for v in ma5]）
    # TODO: signals の点にマーカー（scatter）

    plt.title("Dummy Stock Price + MA5 + Buy Signals")
    plt.xlabel("day index")
    plt.ylabel("close")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
