---
categories:
- 課題と解決
excerpt: WordPressへの転記作業を減らしたい方へ。Pythonで公開記事を読み取り、テスト用の下書きを1件作る手順を紹介します。必要な準備、連携用パスワードの扱い、接続できないときの確認点、手作業のほうが向いている場合も説明します。
featured_image: ''
featured_image_alt: ''
slug: wordpress-rest-api-python
status: publish
tags:
- WordPress
- Python
- REST API
title: WordPress REST APIをPythonから使う方法｜記事の取得と下書き作成
wordpress_post_id: 10
wordpress_url: https://www.nanasinogonbei.com/blog/2026/09/07/wordpress-rest-api-python/
---

WordPress REST APIとPythonを使うと、公開記事を読み取ったり、管理画面を開かずに下書きを作ったりできます。毎回同じ形式の文章を貼り付けている人は、その転記作業を減らせます。

使うのは、外部のプログラムからWordPressと情報をやり取りする窓口「WordPress REST API」です。画面上で一つずつ操作する代わりに、プログラムから記事を読んだり送ったりできます。

Pythonは、こうした処理を書くためのプログラミング言語です。この記事では、公開記事の取得からテスト用の下書き1件の作成までを説明します。下書き作成の例に公開処理は含めません。

## 毎回の転記が多い人ほど、自動化を検討しやすい

たとえば、毎週のお知らせを別の場所で作り、WordPressにタイトルと本文を貼り直しているとします。同じ入力の繰り返しが多ければ、文章を送る部分をプログラムに任せる余地があります。

ただし、今回のサンプルがするのは、用意した短い文章を下書きとして送るところまでです。原稿ファイルの読み込み、画像の登録、定期実行は別途準備が必要です。内容の正しさや読みやすさも、自動では確認できません。

| 方法 | 向いている作業 | 始める手間と続ける負担 |
| --- | --- | --- |
| WordPressの編集画面で書く・貼り付ける | 投稿数が少ない、見た目を調整しながら書く | 追加の連携設定が不要です。投稿ごとの入力は残ります。 |
| Pythonから記事を送る | 同じ形式の文章を繰り返し登録する | 最初に設定とコードの準備が必要です。エラー時の確認も自分で行います。 |

投稿数が少なく、毎回見た目を調整するなら、編集画面だけで十分な場合があります。

今回の構成では、パソコンから自分のWordPressへ直接通信します。別の自動化サービスに原稿を預ける構成ではありませんが、パソコンとWordPress両方の管理は必要です。

## 用意するのはWordPressとPythonが動くパソコン

この記事は、自分で管理するサーバーに設置したWordPressを対象にします。WordPress.comの連携手順は対象外です。

- `https://` でアクセスできるWordPressサイト
- 下書きを作成できるWordPressユーザー
- Python 3と、追加の道具を入れる機能「pip」が使えるパソコン
- テキストを編集して `.py` 形式で保存できるエディター

Pythonが未導入なら、[Python公式サイト](https://www.python.org/downloads/)から利用環境に合うものを入れてください。サーバーにPythonを入れる必要はありません。この記事では手元のパソコンで実行します。

パソコンのコマンド入力画面を開きます。macOSは「ターミナル」、Windowsは「PowerShell」を使います。以下のコマンドは、その画面に1行ずつ入力してEnterで実行してください。

### macOS・Linuxで作業場所を用意する

```bash
mkdir wp-api-practice
cd wp-api-practice
python3 -m venv .venv
.venv/bin/python -m pip install requests
```

### WindowsのPowerShellで作業場所を用意する

```powershell
mkdir wp-api-practice
cd wp-api-practice
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install requests
```

`.venv` は、この練習用に追加の道具を入れる場所です。他の作業と分けるために作ります。このような専用の実行場所は「仮想環境」と呼ばれます。[Python公式の仮想環境の説明](https://docs.python.org/3/library/venv.html)

`requests` は、Pythonからサイトへ情報を送ったり受け取ったりするための追加の道具です。

## Pythonで公開記事を最大3件取得する

公開記事の取得は、標準のWordPressでは通常、パスワードなしで試せます。アクセス制限のあるサイトでは、管理者への確認が必要です。

作成した `wp-api-practice` フォルダーに、次の内容を `read_posts.py` という名前で保存します。文字コードはUTF-8にしてください。

変更するのは `https://example.com` の部分です。通常は、読者がアクセスするサイトのURLに置き換えます。公開サイトが `/blog` にある場合は、`https://example.com/blog` のように、その部分も含めます。WordPress本体の設置場所と公開サイトのURLが異なる環境では、後述の404エラーの説明を参照してください。

```python
import html
import requests

site_url = "https://example.com"
response = requests.get(
    f"{site_url.rstrip('/')}/wp-json/wp/v2/posts",
    params={"per_page": 3, "status": "publish"},
    timeout=30,
)
response.raise_for_status()

posts = response.json()
if not posts:
    print("公開記事はありません。")
for post in posts:
    print(post["id"], html.unescape(post["title"]["rendered"]))
```

macOS・Linuxでは、次を実行します。

```bash
.venv/bin/python read_posts.py
```

Windowsでは、次を実行します。

```powershell
.\.venv\Scripts\python.exe read_posts.py
```

成功すると、記事の番号とタイトルが最大3件表示されます。次は架空の表示例です。実際の番号とタイトルはサイトによって変わります。

```text
123 今週のお知らせ
120 ブログを始めました
```

この番号は、記事を区別するための「投稿ID」です。あとで既存の記事を更新するときにも使います。この取得処理では、記事を書き換えません。

末尾の `/wp-json/wp/v2/posts` は、通常の記事を扱う窓口の場所です。固定ページは別の窓口になります。取得件数や送信先の仕様は、[WordPress公式の投稿API資料](https://developer.wordpress.org/rest-api/reference/posts/)で確認できます。

## 下書きを作る場合だけ、連携用パスワードを発行する

記事を送るときには、「このユーザーが操作してよい」とWordPressに確認してもらう必要があります。そのために、通常のログイン用とは別の「アプリケーションパスワード」を使います。

WordPress 5.6以降には、この機能が標準で用意されています。通信にはHTTPSを使います。[WordPress公式の認証方法](https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/)

1. WordPressの管理画面にログインします。
2. 自分のプロフィール、または対象ユーザーの編集画面を開きます。
3. 「アプリケーションパスワード」の欄で、用途の名前を `python-practice` などにします。
4. 新しいアプリケーションパスワードを追加し、表示された値をパスワード管理ツールなどに保管します。

画面の表記や利用可否は環境によって異なります。欄がない場合は、HTTPSで開いているか、管理者が機能を制限していないかを確認してください。

このパスワードは、発行したユーザーの権限に基づいて使われます。「下書き専用の鍵」ではありません。必要以上に強い権限のユーザーで発行せず、コードや公開リポジトリ、問い合わせのスクリーンショットに載せないでください。不要になったら、同じ管理画面で失効させます。

## テスト用の下書きを1件作り、管理画面で確認する

ここからのコードを実行すると、実際にWordPressへ下書きが1件送られます。読み取りだけ試したい場合は、ここで終了して構いません。

同じフォルダーに、次の内容を `create_draft.py` として保存します。`https://example.com` を先ほどと同じURLに置き換えてください。

```python
from getpass import getpass
import requests

site_url = "https://example.com"
if not site_url.startswith("https://"):
    raise SystemExit("サイトのURLは https:// で指定してください。")

username = input("WordPressのユーザー名: ").strip()
app_password = getpass("アプリケーションパスワード: ")

response = requests.post(
    f"{site_url.rstrip('/')}/wp-json/wp/v2/posts",
    auth=(username, app_password),
    json={
        "title": "Pythonから作ったテスト下書き",
        "content": "<p>これは送信確認用の文章です。</p>",
        "status": "draft",
    },
    timeout=30,
    allow_redirects=False,
)
if 300 <= response.status_code < 400:
    raise SystemExit("転送が発生しました。サイトの正式なHTTPS URLを確認してください。")
response.raise_for_status()

post = response.json()
print(f"投稿ID: {post['id']}")
print(f"保存状態: {post['status']}")
```

macOS・Linuxでは、次を実行します。

```bash
.venv/bin/python create_draft.py
```

Windowsでは、次を実行します。

```powershell
.\.venv\Scripts\python.exe create_draft.py
```

入力を求められたら、WordPressのユーザー名と、発行したアプリケーションパスワードを入力します。普段のログインパスワードは使いません。パスワードは入力しても画面に表示されないのが通常です。

`title` はタイトル、`content` は本文です。本文の `<p>` と `</p>` は、段落を表すHTMLという記法です。この例では段落を一つだけ送ります。Markdownの見出しなどをそのまま送っても、自動でHTMLに変換されるわけではありません。

`status` の `draft` は下書きという意味です。成功時の表示は、たとえば次のようになります。

```text
投稿ID: 124
保存状態: draft
```

WordPressの管理画面で「投稿」の一覧を開き、同じタイトルが下書きとして保存されているか確認してください。続けて本文のプレビューも確認します。

**このサンプルは実行するたびに、新しい下書きを作ります。** 同じ記事を修正したいときは、管理画面で編集してください。プログラムから更新する場合は、新規作成用の送信先ではなく、投稿IDを付けた更新用の送信先を使います。[WordPress公式の投稿作成・更新仕様](https://developer.wordpress.org/rest-api/reference/posts/)

## 接続できないときは、エラーの種類から確認する

コードにある `raise_for_status()` は、通信先が400番台・500番台のエラーを返したときに処理を止めます。`timeout=30` は接続待ちとデータを受け取れない待ち時間に上限を設ける指定です。処理全体の制限時間ではありません。[Requests公式のエラー処理とタイムアウト](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions)

### 401・403なら、ユーザー情報と利用制限を確認する

`401` は本人確認が通っていない場合、`403` は操作が許可されていない場合などに出ます。ただし、サーバー側の防御機能が返すこともあるため、番号だけで原因を断定できません。

- ユーザー名とアプリケーションパスワードの組み合わせは合っていますか。
- 通常のログインパスワードを入力していませんか。
- そのユーザーは、管理画面から下書きを作れますか。
- サーバーやセキュリティ対策が、外部からの記事送信を制限していませんか。

入力情報と権限が正しければ、サーバー管理者に「WordPress REST APIへの認証情報が届いているか」「アクセスが遮断されていないか」を確認してもらいます。問い合わせにパスワードを添付する必要はありません。

### 404・JSONDecodeErrorなら、送信先を確認する

`404` は送信先が見つからない場合に出ます。`JSONDecodeError` は、プログラムが期待するデータ形式ではない返事を受け取った場合などに出ます。ログイン画面やサーバーのエラーページが返っている可能性もあります。

まず、`site_url` に管理画面の `/wp-admin` を入れていないか、必要な `/blog` などが抜けていないか確認してください。`www` の有無も含め、転送後の正式なURLに合わせます。

記事のURLの付け方を決める「パーマリンク設定」によっては、`/wp-json/` 形式が使えません。その場合は、両方のコードにある送信先の行を、次の行に置き換える方法があります。記事の既存URLを変える必要はありません。

```python
    f"{site_url.rstrip('/')}/?rest_route=/wp/v2/posts",
```

特殊な設置構成では、URLを推測せず管理者にAPIの場所を確認してください。サイトのページソースにある `rel="https://api.w.org/"` のリンクも手がかりになります。[WordPress公式のAPIの場所を確認する方法](https://developer.wordpress.org/rest-api/using-the-rest-api/discovery/)

### タイムアウトしたら、再送前に投稿一覧を見る

`Timeout` や `ConnectionError` が出た場合は、通信状況とサイトが開けるかを確認します。

下書き送信では、返事を受け取れなくても、WordPress側では保存済みの場合があります。すぐに再実行すると重複する可能性があるため、先に管理画面の投稿一覧を確認してください。

`SSLError` が出る場合は、サイトのHTTPS証明書やパソコンの日時などを確認します。証明書の確認を無効にして回避すると、接続先の安全確認ができなくなるため、このコードでは無効化しません。

### requestsが見つからない場合は、実行コマンドをそろえる

`ModuleNotFoundError: No module named 'requests'` は、道具を入れた場所と、プログラムを動かした場所が違う場合などに出ます。

作業フォルダーに移動し、この記事にある `.venv` を含むコマンドでインストールと実行を行ってください。`read_posts.py.txt` のように、保存したファイル名に余分な拡張子が付いていないかも確認します。

## 最初の目標は、下書き1件を確認できること

まず公開記事を読めることを確かめ、必要なら下書きを1件だけ送ってみてください。管理画面でタイトルと本文を確認できたら、次は自分が繰り返し入力している文章に置き換える段階です。

文章の確認や見た目の調整は、引き続き編集画面で行えます。

本記事は2026年9月7日に公式資料を確認して作成しました。表示結果は説明用の例です。実サイトへの送信テストは行っていません。