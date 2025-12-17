from __future__ import annotations
import csv
from typing import List, Tuple, Optional

# -------------------------
# Step1/2で使う：CSV読み込み
# -------------------------
def load_csv(path: str) -> Tuple[List[str], List[float]]:
    """
    CSV(date, close) を読み込み、dates と closes を返す。
    """
    dates: List[str] = []
    closes: List[float] = []

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row["date"])
            closes.append(float(row["close"]))

    return dates, closes

# -------------------------
# Step2で使う：移動平均
# -------------------------
def moving_average(values: List[float], window: int) -> List[Optional[float]]:
    """
    移動平均を計算する。window未満の位置は None。
    例: window=3
      [1,2,3,4] -> [None, None, 2.0, 3.0]
    """
    if window <= 0:
        raise ValueError("window must be >= 1")

    ma: List[Optional[float]] = [None] * len(values)

    # i日目の移動平均 = (i-window+1 〜 i の合計) ÷ window
    for i in range(window - 1, len(values)):
        total = 0.0
        for j in range(i - window + 1, i + 1):
            total += values[j]
        ma[i] = total / window

    return ma


# -------------------------
# （オプション）Step3：買いシグナル
# 今回の90分では未使用。時間がある人向け。
# -------------------------
def calc_buy_signals(
    dates: List[str],
    closes: List[float],
    ma: List[Optional[float]],
) -> List[int]:
    """
    買いシグナルのインデックス一覧を返す（オプション）。
    ルールA:
      close[i] < ma[i]
      かつ close[i-1] > close[i] < close[i+1]
    """
    signals: List[int] = []

    for i in range(1, len(closes) - 1):
        if ma[i] is None:
            continue
        if closes[i] < ma[i] and closes[i - 1] > closes[i] and closes[i] < closes[i + 1]:
            signals.append(i)

    return signals


# -------------------------
# Step0：データの概要確認（完成固定）
# ・CSVが正しく読めているか確認するために使う
# ・学生は中身を変更しない
# -------------------------
def summarize(closes: List[float]) -> Tuple[float, float]:
    """最小値と最大値を返す"""
    return min(closes), max(closes)
