# 画像生成メモ（YouTube運営の方向性を定めるアプリ構想記事）

- 作成日：2026年11月24日（日本時間）
- 対象記事：`articles/published/youtube-direction-app.md`（旧保存先：`articles/drafts/codex/youtube-direction-app.md`、WordPress投稿ID: 188、`status: "publish"`、公開URL: https://www.nanasinogonbei.com/blog/2026/11/24/youtube-direction-app/）
- 方針：各 H2 章（全6章）に1枚ずつ一般向けイラストを配置し、`01-light-start.jpg` をアイキャッチ画像としても設定する。
- 日英両版で同じ画像を使用し、`alt` 属性は日本語・英語それぞれに合わせて記述する。
- 2026年11月24日、6枚すべてを WordPress メディアライブラリへアップロード済み（Media ID: `182`〜`187`、アイキャッチ ID: `182`）。WAF HTTP 403 による再圧縮は不要だった。同日、ユーザーの明示的な公開指示により記事を `publish` へ更新済み。

## 生成・検証記録

- 生成方法：`image-generator` サブエージェント（`generate_image` ツール、外部CLIやコード描画不使用）
- 出力形式：6枚すべて `1264 × 848`（約 3:2 横長）JPEG として生成し、全枚の視覚検査を実施した。

### 共通スタイル・制約

Warm ivory paper background, textured colored-pencil / gouache & cut-paper editorial style, calm indigo/teal blue with warm amber/coral and sage green accents, generously spaced uncluttered shapes, legible at mobile width, full-bleed composition. Strictly no words, letters, numbers, Japanese characters, pseudo-text, logos, YouTube brand logo marks (use a generic play-triangle frame only), borders, or watermarks. Clean natural two-arm/two-hand anatomy.

### 各章の画像と視覚検査結果

- `01-light-start.jpg`（Media ID: `182`、アイキャッチ兼 第1章、生成元 `01_light_start_v3_1795501405755.jpg`）: 汎用再生アイコン付きノートPCの横で、大きな円グラフから切り離された小さな黄色の欠片と無地のコイン形を見ながら楽観的に考える大人。3回目生成で指・手・文字なし・汎用再生アイコンすべて自然（合格）。
- `02-meetup-direction.jpg`（Media ID: `183`、第2章、生成元 `02_meetup_direction_1795501347442.jpg`）: 木のテーブルを囲んで真剣に語り合う4人の大人と、頭上に浮かぶ文字なしの羅針盤と分岐する道標。腕・指・カップ・文字なしともに破綻なし（合格）。
- `03-reflection.jpg`（Media ID: `184`、第3章、生成元 `03_reflection_1795501344076.jpg`）: 午後の窓辺で、羅針盤の線画だけが入ったノートを見つめながら静かに振り返る大人。左右の手と指5本・文字なし・表情ともに自然（合格）。
- `04-existing-tools.jpg`（Media ID: `185`、第4章、生成元 `04_existing_tools_1795501362186.jpg`）: 汎用再生アイコンと分析グラフのカード、表計算グリッドのカード、ノートとタグピルのカードを同じ大きさ・重みで並べた比較イラスト。優劣表現や文字・ロゴなし（合格）。
- `05-app-vision.jpg`（Media ID: `186`、第5章、生成元 `05_app_vision_1795501353472.jpg`）: 羅針盤カード → 棒グラフと横線メモのカード → 道標と進む道のカードの3枚を左から右へ矢印でつないだ構想図。文字・記号破綻なし（合格）。
- `06-next-step.jpg`（Media ID: `187`、第6章、生成元 `06_next_step_1795501356563.jpg`）: 朝の机の上で3つの枠に分かれた白いノートを両手で開き、そばにマグカップ・万年筆・文字なしの小さな羅針盤を置いたイラスト。両手・指・文字なしともに自然（合格）。
