# Codex × WordPress ブログ自動投稿

CodexでMarkdown記事を作成し、WordPress REST APIへ下書き投稿・更新するための最小構成です。

## できること

- Codexにブログの執筆ルールを常時参照させる
- Markdown + Front Matterで記事を管理する
- WordPressへ下書き投稿する
- 投稿後のWordPress投稿IDをMarkdownへ自動保存する
- 2回目以降は新規投稿ではなく既存記事を更新する
- カテゴリ・タグを名前から取得し、なければ自動作成する
- ローカル画像をWordPressメディアへアップロードしてアイキャッチ設定する
- `--dry-run` で投稿前確認する
- `--publish` を付けた場合だけ明示的に公開する

## 1. WordPress側の準備

WordPress管理画面で、投稿権限を持つユーザーの「Application Password」を作成してください。

通常のログインパスワードではなく、Application Passwordを使います。
本番サイトではHTTPSを使用してください。

必要な値:

- WordPressサイトURL
- WordPressユーザー名
- Application Password

## 2. Python環境

Python 3.10以上を推奨します。

```bash
python -m venv .venv
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

依存関係をインストール:

```bash
python -m pip install -r requirements.txt
```

## 3. `.env` を設定

`.env` を編集します。

```env
WP_URL=https://example.com
WP_USERNAME=your-user-name
WP_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx"
```

`.env` は `.gitignore` に入っています。
GitHub等へコミットしないでください。

接続確認:

```bash
python scripts/wp_publish.py --check
```

## 4. Codexで記事を作る

Codexには例えば次のように依頼します。

> prompts/article.md と config/blog.yaml に従って、
> 「WordPress REST APIの使い方」という初心者向け記事を作成してください。
> articles/drafts/wordpress-rest-api.md に保存してください。
> WordPressへの投稿はまだしないでください。

記事は次の形式です。

```markdown
---
title: "WordPress REST APIの使い方"
slug: "wordpress-rest-api"
excerpt: "WordPress REST APIの基本を初心者向けに解説します。"
status: "draft"
categories:
  - "WordPress"
tags:
  - "REST API"
  - "Python"
featured_image: ""
featured_image_alt: ""
---

導入文。

## REST APIとは

本文...
```

## 5. レビュー

Codexへ:

> prompts/review.md に従って articles/drafts/wordpress-rest-api.md をレビューし、
> 問題があれば本文を修正してください。
> WordPressへの投稿はまだしないでください。

## 6. WordPressへ下書き投稿

まずdry-run（この段階ではWordPressへ接続せず、認証情報も不要です）:

```bash
python scripts/wp_publish.py articles/drafts/wordpress-rest-api.md --dry-run
```

問題なければ下書き送信:

```bash
python scripts/wp_publish.py articles/drafts/wordpress-rest-api.md
```

成功するとFront Matterへ以下が追加されます。

```yaml
wordpress_post_id: 123
wordpress_url: "https://example.com/?p=123"
```

次回同じファイルを送ると、投稿ID 123を更新します。
これにより二重投稿を防ぎます。

## 7. 公開

公開は明示的に行います。

```bash
python scripts/wp_publish.py articles/drafts/wordpress-rest-api.md --publish
```

公開成功後、設定が有効なら記事ファイルを `articles/published/` へ移動します。

## アイキャッチ画像

Front Matterの `featured_image` にローカル画像のパスを書きます。

```yaml
featured_image: "images/wordpress-rest-api.png"
featured_image_alt: "WordPress REST APIの構成図"
```

記事Markdownからの相対パス、またはプロジェクトルートからの相対パスを解決します。

一度アップロードしたアイキャッチは `wordpress_featured_media_id` をFront Matterへ保存し、更新時の重複アップロードを避けます。画像を差し替えたい場合は、このIDを削除してから再投稿してください。

画像アップロードだけ試したい場合:

```bash
python scripts/wp_media.py path/to/image.png --alt "画像の説明"
```

## カテゴリ・タグ

一覧確認:

```bash
python scripts/wp_categories.py list categories
python scripts/wp_categories.py list tags
```

単独作成:

```bash
python scripts/wp_categories.py create category "WordPress"
python scripts/wp_categories.py create tag "Python"
```

通常は `wp_publish.py` がFront Matterの名前を見て自動解決します。

## blog.yaml

`config/blog.yaml` で以下を調整できます。

- デフォルト投稿ステータス
- Markdown拡張
- カテゴリ/タグの自動作成
- 公開後のMarkdown移動
- コメント・ピンバック
- User-Agent

## Codexへのおすすめ指示

### 記事作成だけ

> AGENTS.md を最優先で読み、ブログ記事を1本作成してください。
> テーマは「○○」です。
> prompts/article.md と config/blog.yaml に従い、
> articles/drafts/ に保存してください。
> WordPressには投稿しないでください。

### 記事作成→レビュー→下書き投稿

> AGENTS.md に従って「○○」の記事を作成してください。
> prompts/article.md で執筆し、prompts/review.md で自己レビューしてください。
> --dry-run で投稿内容を確認してからWordPressへdraftで送信してください。
> publishは絶対にしないでください。

### 既存記事を修正して更新

> articles/drafts/xxx.md を改善してください。
> wordpress_post_id は変更しないでください。
> レビュー後、WordPressの既存下書きを更新してください。

## セキュリティ

- `.env` をGitへ入れない
- Application PasswordをチャットやAGENTS.mdへ貼らない
- WordPressサイトはHTTPSを使う
- 専用WordPressユーザーを作り、必要最小限の権限にするのも有効
- 最初は必ず `draft` 運用にする

## トラブルシューティング

### 401 / 403

- ユーザー名が正しいか確認
- Application Passwordを使っているか確認
- WordPressユーザーに投稿権限があるか確認
- セキュリティプラグインやWAFがREST APIを遮断していないか確認

### REST API URLが404

ブラウザで次を確認してください。

```text
https://あなたのサイト/wp-json/wp/v2/posts
```

### 画像アップロードが失敗

- WordPressで許可された画像形式か
- ファイルサイズ制限を超えていないか
- ユーザーにメディアアップロード権限があるか

## 公式仕様

WordPress REST APIではPosts、Media、Categories、Tagsなどの標準エンドポイントが利用できます。
このプロジェクトは標準の `/wp-json/wp/v2/...` を使用しています。
