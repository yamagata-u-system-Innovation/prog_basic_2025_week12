from __future__ import annotations
import csv
from typing import List, Tuple, Optional

def read_stock_csv(path: str) -> Tuple[List[str], List[float]]:
    """
    CSV(date, close) を読み込み、dateのリストとcloseのリストを返す。
    例:
      dates = ["2025-01-01", ...]
      closes = [100.0, ...]
    """
    dates: List[str] = []
    closes: List[float] = []

    # TODO: csv.DictReader を使って読み込む
    # TODO: date を dates に追加
    # TODO: close を float にして closes に追加
    # ヒント: with open(path, newline="", encoding="utf-8") as f:

    return dates, closes


def moving_average(values: List[float], window: int) -> List[Optional[float]]:
    """
    移動平均を計算する。window未満の位置は None を入れる。
    例: window=3 の場合
      [1,2,3,4] -> [None, None, 2.0, 3.0]
    """
    ma: List[Optional[float]] = [None] * len(values)

    # TODO: window <= 0 のときは ValueError
    # TODO: i >= window-1 のとき、直近window個の平均を入れる

    return ma


def calc_buy_signals(
    dates: List[str],
    closes: List[float],
    ma: List[Optional[float]],
) -> List[int]:
    """
    買いシグナルのインデックス一覧を返す。
    ルールA:
      close[i] < ma[i]
      かつ close[i-1] > close[i] < close[i+1]
    注意:
      i-1 や i+1 を使うので、i は 1..len-2 の範囲のみ判定
      ma[i] が None の日は判定しない
    """
    signals: List[int] = []

    # TODO: for i in range(1, len(closes)-1):
    # TODO: ma[i] が None なら continue
    # TODO: ルールA を満たしたら signals.append(i)

    return signals


def summarize(closes: List[float]) -> Tuple[float, float]:
    """最小値と最大値を返す"""
    # TODO: min と max を使う
    return 0.0, 0.0
