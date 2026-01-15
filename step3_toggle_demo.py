from __future__ import annotations
import matplotlib.pyplot as plt

from stock_utils import load_csv, moving_average

DATA_PATH = "data/stock_dummy.csv"

# ====== ここをON/OFFして比較 ======
USE_BELOW_MA = True     # 条件1：平均より安い？
USE_V_BOTTOM = True     # 条件2：下がってから上がった？（V字の底）
WINDOW = 5              # 移動平均の期間（5→10などで比較も可）
# ==================================

def find_signals(closes: list[float], ma: list[float | None]) -> list[int]:
    """条件のON/OFFに応じてシグナル（インデックス）を返す"""
    signals: list[int] = []

    for i in range(1, len(closes) - 1):
        # 条件1：平均より安い？
        cond_below_ma = False
        if USE_BELOW_MA:
            if ma[i] is None:
                continue  # 平均がない日は判定しない
            cond_below_ma = closes[i] < ma[i]
        else:
            cond_below_ma = True  # OFFなら常にOK扱い

        # 条件2：下がってから上がった？（V字の底）
        cond_v = False
        if USE_V_BOTTOM:
            cond_v = (closes[i - 1] > closes[i]) and (closes[i] < closes[i + 1])
        else:
            cond_v = True  # OFFなら常にOK扱い

        if cond_below_ma and cond_v:
            signals.append(i)

    return signals


def main() -> None:
    dates, closes = load_csv(DATA_PATH)

    # 移動平均
    ma = moving_average(closes, WINDOW)

    # シグナル検出
    signals = find_signals(closes, ma)

    # 結果表示
    print("=== SETTINGS ===")
    print(f"USE_BELOW_MA={USE_BELOW_MA}, USE_V_BOTTOM={USE_V_BOTTOM}, WINDOW={WINDOW}")
    print(f"signals_count={len(signals)}")
    if signals:
        print("first 10 signals:")
        for idx in signals[:10]:
            print(f"  {dates[idx]} close={closes[idx]} ma={ma[idx]}")

    # 描画
    x = list(range(len(closes)))
    plt.plot(x, closes, label="close")

    # None は描画できないので NaN に変換
    ma_y = [v if v is not None else float("nan") for v in ma]
    plt.plot(x, ma_y, label=f"MA{WINDOW}")

    # シグナル点
    sx = signals
    sy = [closes[i] for i in signals]
    plt.scatter(sx, sy, label="signals")

    plt.title("Step3 Toggle Demo: Rule ON/OFF")
    plt.xlabel("day index")
    plt.ylabel("close")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
