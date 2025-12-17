from __future__ import annotations
import matplotlib.pyplot as plt

from stock_utils import load_csv, summarize, moving_average

DATA_PATH = "data/stock_dummy.csv"

def main() -> None:
    # Step0: CSV読み込み＋概要確認
    dates, closes = load_csv(DATA_PATH)
    mn, mx = summarize(closes)
    print(f"rows={len(closes)}, min={mn}, max={mx}")

    # Step1: 株価（終値）を描く
    x = list(range(len(closes)))
    plt.plot(x, closes, label="close")

    # Step2: 移動平均（5日）を計算して描く
    ma5 = moving_average(closes, window=5)

    # ma5 の先頭は None なので、描画用に NaN に変換して線を自然に途切れさせる
    ma_y = [v if v is not None else float("nan") for v in ma5]
    plt.plot(x, ma_y, label="5-day average")

    # 仕上げ
    plt.title("Dummy Stock Price + MA5")
    plt.xlabel("day index")
    plt.ylabel("close")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
