# 第12週 グループ課題：株価ダミーデータで「買いタイミング」を計算し、グラフ表示

## ねらい
- CSV読み込み（date, close）
- 基本統計（min/max）
- 移動平均（MA）
- 簡単な買いシグナル（ルールA）
- matplotlibで可視化

## 実行方法
```bash
pip install -r requirements.txt
python main.py

## 入力データ

data/stock_dummy.csv

date, close

## 出力

コンソール：件数、最小/最大、買いシグナル一覧（上位）

グラフ：終値、移動平均、買いシグナル点

ルールA（買いシグナル）

close[i] < ma5[i]

かつ close[i-1] > close[i] < close[i+1]（V字の底）

ma5[i] が None の日は判定しない

## 提出物

main.py / stock_utils.py（穴埋めを完成）

report.md（担当分担・ロジック説明・スクショ）

## 提出ルール（必ず守ってください）
🚫 **このリポジトリは必ず「Private」で作成してください。**
他の学生に見える状態（Public）にすると不正行為とみなされることがあります。

👩‍🏫 提出方法：
1. このテンプレートから「Use this template」で自分のリポジトリを作成  
2. リポジトリ名：`week12_学籍番号_名前（フルネーム）
   例：week12_20251234_山形太郎`  
3. 教員を「sichiura-yamagata-u」に追加  
4. コードを編集・コミット・プッシュして提出  

🧩 注意：
- Publicリポジトリは禁止です  
- 他人のコードをコピーしない  
- READMEを必ず残して提出  

---

## 提出期限
2026年1月16日 16:20

## 質問方法
Issueタブを開き、タイトルに「Q: ○○について」と書いて投稿してください。
