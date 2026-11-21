# 章の挿絵の生成記録

- 対象記事：`articles/published/self-introduction-learning-roadmap.md`（WordPress投稿ID: 15）
- 方針：各H2章（全8章）に1枚ずつ一般向けイラストを配置し、`01` をアイキャッチ画像としても設定する。
- 日英両版で同じ画像を使用し、本文の `alt` 属性は日本語・英語それぞれに合わせて記述する。

## Phase 1 完了分（生成・WordPressアップロード済み）

`image-generator` サブエージェントで生成し、`sips` で PNG 変換後に WordPress メディアライブラリへアップロード済み。

- `01-ai-ambition.png`（Media ID: 129、アイキャッチ兼 第1章）: AI活用や個人開発に向けた前向きな学習イメージ
- `02-learning-roadmap.png`（Media ID: 130、第2章）: 学習ロードマップ全体のイメージ
- `03-typing-and-java.png`（Media ID: 131、第3章）: タイピング練習と Java 基礎学習のイメージ

## Phase 2a 完了分（生成・WordPressアップロード済み）

- `04-read-vs-write.png`（Media ID: 154、第4章）: コードを読む力と書く力の違い（記事本文へ反映済み）

## Phase 2b 完了分（ChatGPT による生成・WordPressアップロード済み — 全8枚完了）

ユーザー指示に基づき、ChatGPT（`https://chatgpt.com/`）のブラウザ画面上で 1536×1024（3:2 横長）の PNG 画像として1枚ずつ生成・ダウンロードし、視覚検査を通過した4枚を WordPress メディアライブラリへアップロード済み。

- `05-different-approaches.png`（Media ID: 161、第5章）：同じ結果でもアプローチが異なる例（記事本文へ反映済み）
- `06-ai-and-work.png`（Media ID: 162、第6章）：AIと仕事・学習の進め方（記事本文へ反映済み）
- `07-step-by-step-logic.png`（Media ID: 163、第7章）：順序立てて論理的に考える手順（手元俯瞰・両手のみ、記事本文へ反映済み）
- `08-build-in-public.png`（Media ID: 164、第8章）：今後の個人開発と Build in Public（記事本文へ反映済み）
