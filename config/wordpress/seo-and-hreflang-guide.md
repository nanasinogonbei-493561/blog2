# WordPress SEO設定・トップページ反映・日英URL分離（hreflang）ガイド

このガイドは、`codex/seo-fixes` ブランチで追加したテンプレート・設定・PHPスニペット・投稿スクリプト連携を WordPress 側へ反映するための手順書です。

> [!NOTE]
> 2026年11月27日時点の実サイト確認では、有効テーマは **Cocoon（`cocoon-master`）** です。Cocoon 有効時はすでに記事一覧10件表示・個別投稿の `<meta name="description">`・`og:description`・JSON-LD 構造化データが標準出力されるため、追加のSEOプラグインやブロックテンプレート反映は原則不要です。まずは下の「0. Cocoon 環境での推奨設定」を確認してください。

---

## 0. Cocoon 環境での推奨設定（現在の実サイト向け）

1. WordPress管理画面 → **「Cocoon設定」→「SEO」** を開く。
2. **フロントページ（トップページ）のメタディスクリプション** を入力して保存する（個別投稿には抜粋が自動出力されていますが、トップページ側は未設定だと空になります）。
3. **「タグページをnoindexにする」** にチェックを入れて保存する（1記事のみのタグアーカイブが低品質ページとしてインデックスされるのを防ぐため）。
4. 追加のSEOプラグイン（`SEO SIMPLE PACK` 等）を入れると Cocoon 標準のSEOタグと重複するため、Cocoon 利用中はプラグインを追加せず Cocoon 設定側で管理するのが安全です。[`seo-jsonld-and-hreflang.php`](./snippets/seo-jsonld-and-hreflang.php) は Cocoon 有効時に `meta description` と JSON-LD の出力を自動スキップし、将来の `hreflang` 出力のみ有効になります。

---

## 1. トップページテンプレート（`<h1>` と10件一覧）の反映（Twenty Twenty-Five 利用時のみ）

対象ファイル: [`config/wordpress/templates/twentytwentyfive-home.html`](./templates/twentytwentyfive-home.html)

1. WordPress管理画面 → **「設定」→「表示設定」** を開き、**「1ページに表示する最大投稿数」を `10` 件** に変更して保存する（テンプレート側の `inherit: true` と一致させるため）。
2. WordPress管理画面 → **「外観」→「エディター」→「テンプレート」** から、ブログのホーム／インデックステンプレートを開く。
3. 右上のオプション（⋮）から **「コードエディター」** に切り替え、`twentytwentyfive-home.html` の内容を貼り付けて保存する。
4. 公開後のトップページで以下を確認する:
   - `<h1>` が「個人開発と日常の困り事解決ブログ」になっていること
   - 直下にブログの概要文があること
   - 記事タイトル・公開日・カテゴリ・抜粋が最大10件表示され、リンクが青色（`#0000ff`）で下線付きであること

---

## 2. SEOプラグインでの `meta description`・構造化データ・タグアーカイブ制御

WordPress 側の出力方法は **A（SEOプラグイン導入・推奨）** と **B（軽量PHPスニペットのみ）** のどちらか一方を選びます。

### 方法A：SEOプラグインを使う（推奨：`SEO SIMPLE PACK` または `Yoast SEO`）

日本語テーマ（Twenty Twenty-Five）と相性が良く軽量な **`SEO SIMPLE PACK`** を例にした手順です（`Yoast SEO` でも同様に設定できます）。

1. **「プラグイン」→「新規プラグインを追加」** から `SEO SIMPLE PACK` をインストール・有効化。
2. **「SEO PACK」→「一般設定」**:
   - **基本設定**: トップページのタイトル・ディスクリプションを設定。
   - **投稿ページ**: 投稿のディスクリプション自動生成をオン（抜粋 `excerpt` を優先）。
   - **アーカイブ設定**: タグアーカイブページ（`タグ別一覧`）に **`noindex`** を設定（1記事のみの低品質タグページが検索インデックスに増えるのを防ぐため）。
3. **「SEO PACK」→「OGP設定」**: Facebook / X (Twitter) 用のOGPタグとデフォルト画像を設定。
4. **`config/blog.yaml` と投稿スクリプトの連携**:
   - `SEO SIMPLE PACK` を使う場合、`config/blog.yaml` の `seo.plugin` を `"seo_simple_pack"` に変更すると、`scripts/wp_publish.py` 実行時に Front Matter の `meta_description`（未指定時は `excerpt`）が `ssp_meta_description` へ送信されます。
   - 対応値: `seo_simple_pack` / `yoast` / `aioseo` / `rank_math` / `custom`。
   - **注意**: WordPress REST API はデフォルトではプラグインのカスタムフィールド書き込みを拒否する場合があります。`wp_publish.py` 送信時に `meta` でエラーが出た場合は、プラグイン側のREST API対応有無を確認するか `seo.plugin: "none"` のままにして抜粋（`excerpt`）自動反映を使ってください。

### 方法B：プラグインを増やさず PHP スニペットで出力する

[`config/wordpress/snippets/seo-jsonld-and-hreflang.php`](./snippets/seo-jsonld-and-hreflang.php) を `wp-content/mu-plugins/seo-jsonld-and-hreflang.php` へ配置（または `Code Snippets` プラグインに登録）します。

このスニペットは次の3つを自動処理します（主要SEOプラグインが有効な場合は重複出力を避けるため自動でスキップします）:
1. `excerpt`（未設定時は本文先頭160文字）を使った `<meta name="description">` 出力
2. 個別投稿ページへの `BlogPosting` および `BreadcrumbList` JSON-LD 構造化データ出力
3. 日英URL分離用のカスタムフィールド `_blog_hreflang_ja_url` / `_blog_hreflang_en_url` の REST API 登録と `<link rel="alternate" hreflang="...">` 出力

### 反映後の確認

- ブラウザで記事ページを開き、「ページのソースを表示」で `<meta name="description">` と `<script type="application/ld+json">` が1組ずつ出力されていることを確認する。
- [Google リッチリザルトテスト](https://search.google.com/test/rich-results) に記事URLを入力し、`Article`（`BlogPosting`）と `パンくずリスト`（`BreadcrumbList`）がエラーなしで認識されることを確認する。

---

## 3. 将来的な日英URL分離（`hreflang`）の移行計画

現在は1つのURL内に `wp:tabs` で日英両方の本文を同居させています（`config/blog.yaml` の `bilingual.mode: "tabs"`）。英語検索からの流入を本格的に狙う段階になったら、次の手順で言語別URLへ分離できます。

### 方式の比較

| 方式 | メリット | デメリット | 向いている段階 |
| --- | --- | --- | --- |
| **方式1: 個別投稿＋`hreflang`メタ連携**（リポジトリ同梱スニペット使用） | 既存の `wp_publish.py` 運用・ディレクトリ構成と親和性が高い | URLルーティング（`/blog/en/...`）や英語側一覧ページを別管理する必要がある | まず主要記事から英語版ページを分けたい場合 |
| **方式2: 多言語プラグイン（Polylang 等）** | 言語スイッチャー・カテゴリ/タグ翻訳・`hreflang`・英語サイトマップを一括管理 | プラグイン依存が増え、`wp_publish.py` 側に言語パラメータ対応が必要 | ブログ全体を本格的に日英2サイト運用する場合 |

### 方式1で進める場合の手順

1. WordPress 側に `seo-jsonld-and-hreflang.php` を配置し、`_blog_hreflang_ja_url` と `_blog_hreflang_en_url` が REST API 経由で保存できるようにする。
2. `config/blog.yaml` の `seo.enable_hreflang_meta` を `true`、`bilingual.mode` を `"separate_urls"` へ変更する。
3. 英語版記事のMarkdown（例: `articles/published/en/<slug>.md`）を作成し、日英双方の Front Matter に以下を記載する:
   ```yaml
   hreflang_ja_url: "https://www.nanasinogonbei.com/blog/YYYY/MM/DD/slug/"
   hreflang_en_url: "https://www.nanasinogonbei.com/blog/en/YYYY/MM/DD/slug/"
   ```
4. 既存の日本語記事の `wp:tabs` から英語タブを外し、日本語記事の上部に「English version」リンク（青色）、英語記事の上部に「日本語版」リンク（青色）を配置する。
5. 公開後、日英両方のページソースに以下の3行が出力され、相互に参照できていることを確認する:
   ```html
   <link rel="alternate" hreflang="ja" href="https://www.nanasinogonbei.com/blog/.../" />
   <link rel="alternate" hreflang="en" href="https://www.nanasinogonbei.com/blog/en/.../" />
   <link rel="alternate" hreflang="x-default" href="https://www.nanasinogonbei.com/blog/.../" />
   ```
