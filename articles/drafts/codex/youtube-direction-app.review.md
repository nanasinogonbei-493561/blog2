# 記事レビュー記録

- 確認日：2026年11月24日（日本時間）
- 対象原稿：`articles/published/youtube-direction-app.md`（旧保存先：`articles/drafts/codex/youtube-direction-app.md`）
- ブランチ：`codex/youtube-direction-app`
- 現在の状態：WordPress 公開済み（投稿ID **188**、`status: "publish"`、公開URL: https://www.nanasinogonbei.com/blog/2026/11/24/youtube-direction-app/）。2026年11月24日にユーザーの明示的な公開指示に従って公開へ切り替えました。以下の下書き時点の記録は履歴として保持しています。
- 参照：`AGENTS.md`、`CONTENT_STRATEGY.md`、`config/blog.yaml`、`prompts/article.md`、`prompts/review.md`

## レビューで確認・修正した点

### 1. 技術的・事実関係の修正（日英共通）

- **Google スプレッドシートの無料保存容量（15GB）に関する誤りを修正。** 2021年6月1日以降の仕様変更（Google公式ヘルプ確認）を踏まえ、「作成・編集したシートは基本的に無料容量の消費対象外」としていた記述を、「新規作成・編集したシートは Google アカウントの無料保存容量（Googleドライブ・Gmail・Googleフォト共有の15GB）の対象になる」へ修正しました。
- **YouTube Studio の用語補足を補強。** 第4章の比較表で「視聴者維持率」に「（動画がどれくらい見続けられたかの割合）」という平易な言い換えを添え、一般読者が表だけで意味を把握できるようにしました。
- **比較表の確認時点を明記。** 第4章の表キャプションを「記事作成時点」から「2026年11月時点の公式情報にもとづく整理（English: based on official info checked in November 2026）」へ具体化しました。

### 2. 冗長な表現・重複・文体の修正（日英共通）

- **構想段階・公開URL未定の説明重複を整理。** 導入と第6章の両方に書いていた括弧書き `（サブドメイン付きの専用ページ）` の重複を省き、導入では簡潔に1回示し、第6章では「公開URLやリリース時期は未定」と短くまとめました。
- **「開発のネタ」の表現反復を軽減。** 第1章と第3章で4回連続していた「ネタ」の言い回しを「材料」「題材」と自然な日本語に整理しつつ、ユーザーの指示内容（軽い気持ち・オフ会参加・悩み自体に優劣はない・卑しく見えて反省した）はすべて保持しました。
- **長い一文の分割と重複語の整理。** 第2章第3節・第4章第3節の長い文を55〜65文字前後で切り、第5章の重複表現「自分の自作アプリ」を「自作アプリ」へ直しました。また、第4章比較表1列目の3行連続だった「〜やすいです」の文末を「〜やすいツールです」「〜続けられます」「〜向いています」へ散らしました。

### 3. SEO・AIO の調整（日英共通）

- **タイトル・slug・statusの維持。** ユーザー指定のタイトル「YouTubeの悩みを聞いてる内に、真剣に運営の方向性を定まるアプリを作りたくなった」と `slug: "youtube-direction-app"`、`status: "draft"`、`excerpt`（132文字）を維持しました。
- **第4章 H2 直下に結論を先出し。** 「既存の道具でどこまで整理できるか」の冒頭で「結論から言うと、数字の確認や振り返りの記録だけなら既存の定番ツール3つでも十分に対応できます」と明示しました。
- **第4章 H3 見出しの対比を明確化。** 「既存ツールで十分な人と、それでも残るモヤモヤ」から「既存ツールで十分な人と、専用アプリが合いそうな人」へ改め、見出しだけで読者の判断軸が分かるようにしました。
- **第6章の「3行メモ」例を箇条書きリスト化。** 文中にスラッシュ区切りで埋もれていた例を `wp:list`（説明用の記入例と明記）へ整理し、一目で読み取れるようにしました。

## 確認した公式情報・内部リンク（日英共通6件）

- 内部リンク：`https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/`
- 内部リンク：`https://www.nanasinogonbei.com/blog/2026/11/22/youtask-youtube-task-management/`
- 内部リンク：`https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/`
- YouTube 公式ヘルプ：`https://support.google.com/youtube/answer/9002587?hl=ja`（英語版は `?hl=en`）
- Google スプレッドシート公式：`https://workspace.google.com/products/sheets/`
- Notion 公式料金ページ：`https://www.notion.com/pricing`
- すべてのリンクに青色（`#0000ff`）と下線を指定しています。なお、自作アプリの公開済みサブドメインURLはリポジトリ内に存在しないため、仮のURLは作成していません。

## レビュー時点の検証結果と未確認事項（下書き送信前）

- 修正後のローカル Python 検証で、Front Matter（`status: "draft"`、抜粋132文字、投稿ID未設定）、本文内 H1=0、日英各 H2=6・H3=4・`wp:group`=11（計22）・`wp:image`=6（計12、全画像ファイル実在）・青色下線リンク=6（計12）・3色マーカー（青4・黄2・赤2）・WordPress ブロック開閉一致（164組）、Google スプレッドシート容量記述の修正反映と重複表現の解消を確認しました。
- WordPress 下書き送信前のローカル確認履歴として残しています。実際の送信結果は下の記録を参照してください。

## WordPress下書き送信：2026年11月24日

ユーザーの「`--dry-run` で投稿内容を確認してください。問題なければWordPressへ `draft` で送信してください。`publish` はしないでください」という指示に従って実施しました。

- `.venv/bin/python scripts/wp_publish.py articles/drafts/codex/youtube-direction-app.md --dry-run --draft` で `CREATE` / `status: "draft"` / `slug: "youtube-direction-app"` / カテゴリ・タグ・本文ブロック構造を確認しました。
- `.venv/bin/python scripts/wp_publish.py --check` で認証成功を確認し、`GET /posts?slug=youtube-direction-app&status=any` で同スラグの既存投稿がないこと（`0` 件）を確認しました。
- `wp_media.upload_media` で6枚の画像（`01-light-start.jpg`〜`06-next-step.jpg`）をアップロードし、Media ID `182`〜`187` と公開URLを取得しました（アイキャッチ画像 ID：`182`）。Front Matter の `wordpress_featured_media_id`・`wordpress_inline_media` および日英計12か所の `wp:image` ブロックをアップロード先URLへ差し替えました。
- 差し替え後に再度 `--dry-run --draft` を実行して `../../images/` が残っていないこととペイロードの整合性を確認したうえで、`.venv/bin/python scripts/wp_publish.py articles/drafts/codex/youtube-direction-app.md --draft` を実行しました（`--publish` は使用していません）。
- 作成された下書き投稿 ID：**188**（`status: "draft"`）。Front Matter へ `wordpress_post_id: 188`、`wordpress_url: https://www.nanasinogonbei.com/blog/?p=188`、`wordpress_featured_media_id: 182` が保存されました。
- 編集URL：https://www.nanasinogonbei.com/blog/wp-admin/post.php?post=188&action=edit
- プレビューURL：https://www.nanasinogonbei.com/blog/?p=188&preview=true （WordPress へのログインが必要です）
- `GET /posts/188?context=edit` で以下を確認しました：
  - `status` が `"draft"`、`slug` が `"youtube-direction-app"`、`title.raw` が期待どおり、`featured_media` が `182`、`categories: [9, 6]`、`tags: [33, 12, 19, 36]` であること
  - `content.raw` および `content.rendered` の双方で H1=0、H2=12、H3=8、画像12か所（相対パス残存0・アップロード済み6URL各2回以上）、リンク12か所すべてに `#0000ff` と `underline`、3色マーカー（青8・黄4・赤4）、`wp-block-tabs`（`tablist`・`日本語`・`English`）が保持されていること
- ブラウザ実機での目視表示および日英タブのクリック切り替え動作は未実行・未確認です（`publish` への変更は行っていません）。

## WordPress公開：2026年11月24日

ユーザーの「確認して、良かったので、公開してください。draftからpublishに変更してください。」という明示的な指示に従って実施しました。

- `.venv/bin/python scripts/wp_publish.py articles/drafts/codex/youtube-direction-app.md --dry-run --publish` で `操作: UPDATE`・`投稿ID: 188`・`status: "publish"`・`slug: "youtube-direction-app"` を確認しました。
- `.venv/bin/python scripts/wp_publish.py articles/drafts/codex/youtube-direction-app.md --publish` を実行し、既存投稿 ID **188** のステータスを `publish` へ更新しました。公開完了に伴い、原稿ファイルは `articles/published/youtube-direction-app.md` へ自動移動され、`status: publish`、`wordpress_post_id: 188`、`wordpress_url: https://www.nanasinogonbei.com/blog/2026/11/24/youtube-direction-app/`、`wordpress_featured_media_id: 182` および `wordpress_inline_media` がすべて保持されていることを確認しました。
- `GET /posts/188?context=edit` および公開URL（`https://www.nanasinogonbei.com/blog/2026/11/24/youtube-direction-app/`）への無認証 HTTP GET で以下を確認しました：
  - API 上の `status` が `"publish"`、`slug` が `"youtube-direction-app"`、`featured_media` が `182`、公開URLが HTTP `200` を返すこと
  - `content.raw`・`content.rendered`・公開HTMLにタイトル、`wp-block-tabs`（`日本語` / `English`）、アップロード済み画像6URL（`content.raw` / `content.rendered` 内画像12か所）、青色下線リンク12か所（`#0000ff`）、3色マーカー（青8・黄4・赤4）、本文内 H1=0 がすべて含まれていること
- なお、ブラウザ画面でのクリックによるタブ切り替え操作は未実行です。
