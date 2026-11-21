# 記事レビュー記録

- 日付：2026年11月21日
- 対象原稿：`articles/published/youtask-youtube-task-management.md`（旧保存先：`articles/drafts/youtask-youtube-task-management.md`）
- ブランチ：`codex/youtube-task-management`
- 現在の状態：WordPress 公開済み（投稿ID **173**、`status: publish`、URL: https://www.nanasinogonbei.com/blog/2026/11/22/youtask-youtube-task-management/）。2026年11月22日にユーザーの明示的な公開指示に従って公開へ切り替えました。以下の下書き検証履歴は作業記録として保持しています。

## 執筆・レビュー方針

- `AGENTS.md`、`CONTENT_STRATEGY.md`、`config/blog.yaml`、`prompts/article.md`、`prompts/review.md` を確認して執筆・レビューを行いました。
- カテゴリは `Build in Public` と `開発の裏側` の2件、タグは `YouTube運営`・`タスク管理`・`YouTask`・`個人開発` の4件、抜粋は129文字です。
- YouTask はユーザーから共有された情報どおり **構想中（公開URL未定）** として扱い、リリース時期・料金・実装済み画面や実測成果の創作は行っていません。表のサンプル数値には架空の例であることを明記しました。
- 一般ユーザー向けに専門用語（「ペルソナ」「視聴継続率」）を日常の言葉で言い換え、「視聴継続率」については YouTube Studio の公式表示名である「視聴者維持率」（英語：Audience retention）を補足しました。
- 第4章では既存ツール3つ（Google スプレッドシート・Notion・Trello）を公式情報にもとづいて比較し、「既存ツールでも十分解決できること」「無料枠やデータ・プライバシーの扱い」「YouTask を無理に1位にしないこと」を明記しました。

## レビュー時に行った主な修正

- 日本語版第2章第1節で「〜なります。」が2文連続していた箇所を「〜整います。」へ修正し、文末の単調さを解消しました。
- 第2章第2節（日英双方）で「登録者数」が時点値か増減値か迷わないよう補足を入れ、YouTube Studio の視聴者維持率レポートの反映目安（1〜2日）について注意点として整理しました。
- 第4章の比較表（日英双方）に「続けやすさ」と「データ・プライバシーの扱い（保存容量・非公開設定・共有管理）」を明示的に追加し、`config/blog.yaml` の比較軸6項目をすべて満たすようにしました。
- 第5章の日本語表タイトルを「YouTaskが向いている人と既存ツールが向いている人の整理」に整え、英語版と意味をそろえました。

## 確認した公式情報・内部関連記事（日英共通7件）

- 関連記事：`https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/`
- YouTube 公式ヘルプ：`https://support.google.com/youtube/answer/9002587?hl=ja`（英語版は `?hl=en`）
- 関連記事：`https://www.nanasinogonbei.com/blog/2026/11/02/simple-programs-products-for-kids/`
- Google スプレッドシート公式：`https://workspace.google.com/products/sheets/`
- Notion 公式料金ページ：`https://www.notion.com/pricing`
- Trello 公式料金ページ：`https://trello.com/pricing`
- 関連記事：`https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/`

## 本文・ブロック・Codex画像差し替え

- 本文に H1 はなく、日英各6個の H2（合計12個）と各4個の H3（合計8個）をそれぞれ `wp:group` ブロック（合計22個）に分けています。
- 冒頭に `wp:tabs`（`activeTabIndex: 0`）を配置し、初期表示を日本語、切り替え先を英語としています。
- 全14リンクに青色（`#0000ff`）と下線を指定しています。
- 要点の青マーカー（各4か所）、注意点の黄マーカー（各2か所）、避けたい例・行動の赤マーカー（各2か所）を日英の対応箇所で一致させました。
- ユーザー指示に基づき、2026年11月21日に Codex CLI `0.169.1`（組み込み `image_gen.imagegen` ツール）で全6枚（1536×1024 PNG）を再生成し、すべて視覚検査を通過しました。
- WordPress 送信時は SiteGuard Lite WAF の HTTP 403 回避のため `/usr/bin/sips` で同解像度の JPEG（品質 88、`02-three-phases.jpg` のみ品質 85）へ変換し、WordPress メディアライブラリへ新規アップロード（Media ID: 175〜180、アイキャッチ ID: 175）したうえで、日英各6か所（計12か所）の `wp:image` ブロックと `featured_image` をすべて差し替えました。旧画像（ID: 167〜172）の参照は残っていません。

## WordPress 送信・API・公開確認

- 2026年11月21日：`--dry-run`（`UPDATE` 対象 ID `173`・`status: draft`）通過後、既存下書き（投稿ID `173`）を `--draft` で更新しました。
- 2026年11月22日：ユーザーの公開指示を受け、`--dry-run --publish` で `UPDATE`（ID `173`）・`status: publish` を確認したうえで `wp_publish.py articles/drafts/youtask-youtube-task-management.md --publish` を実行しました。公開完了に伴い、原稿ファイルは `articles/published/youtask-youtube-task-management.md` へ移動済みです。
- `GET /wp-json/wp/v2/posts/173?context=edit` および公開 URL（`https://www.nanasinogonbei.com/blog/2026/11/22/youtask-youtube-task-management/`）への HTTP GET で以下を確認済みです。
  - 投稿ID `173` のステータスが `publish` であること（公開URLが HTTP `200` を返すこと）
  - `featured_media` が `175` であること
  - `content.raw`・`title.raw`・`slug` が送信データと一致すること
  - 公開HTMLおよび `content.rendered` に `core/tabs` の切り替え属性、`日本語` / `English` タブ、Codex 画像（ID `175`〜`180` の `.jpg`）全6枚（日英計12か所）、青色下線リンク（`#0000ff`）、3色マーカー装飾（青8・黄4・赤4）が含まれていること
