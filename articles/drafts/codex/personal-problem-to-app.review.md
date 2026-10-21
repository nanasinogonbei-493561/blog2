# 自分の悩み・困り事を自作アプリにする方法：レビュー記録

- 確認日：2026年10月21日（日本時間）
- 最新状態：ユーザーの確認と公開指示を受け、投稿ID 85を`publish`へ変更済み。以下の未送信・未公開という記述は、執筆・レビュー・下書き送信時点の履歴です。
- 対象：`articles/drafts/personal-problem-to-app.md`
- ブランチ：`codex/personal-problem-to-app`
- 参照：`AGENTS.md`、`CONTENT_STRATEGY.md`、`config/blog.yaml`、`prompts/article.md`、`prompts/review.md`

## 内容と構成

- 一般ユーザー向けに、困った場面の観察から、記録、既存手段の確認、機能の絞り込み、試作、生活の中での検証までを説明しました。
- 悩み・現在の対処法・残る不便・自作で試す解決・解決できない範囲を分けています。
- 主な記録例とアプリ案は架空であり、実体験・完成したアプリ・実測結果として扱っていません。
- 既存のメモ、ブックマーク、表による管理を公平に紹介しています。製品の料金や特定サービスの現行機能を未確認のまま断定していません。
- コピーできる整理用の記入例と、AIや作成を手伝う人への依頼文を掲載しました。
- 日英の章構成、表、記入例、画像、代替テキスト、関連リンクを揃えました。自作に向く人と既存の道具が合う人も明記しました。
- H1はありません。日英それぞれH2が6個、H3が6個です。導入と各見出しを独立したグループに分け、合計26グループにしました。
- 既存記事で使われているWordPressのTabsブロックを踏襲し、`activeTabIndex: 0`で日本語を初期タブに指定しました。

## リンク

次の関連する既存記事を読み、Front Matterに保存された公開URLを採用しました。公開URLへのHEADリクエストで、どちらもHTTP 200を確認しました。

- https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/
- https://www.nanasinogonbei.com/blog/2026/10/12/survey-driven-app-ideas/

日英すべての本文リンクに`color: #0000ff; text-decoration: underline;`を指定しています。関連記事、設定、公開済み記事に自作アプリのサブドメインURLを確認できなかったため、推測のURLや仮リンクは掲載していません。

## 画像

- 組み込みimage_genで6枚生成し、各H2に1枚ずつ配置しました。日本語・英語で共有しています。
- 保存先：`articles/images/personal-problem-to-app/`
- 最終プロンプト：同ディレクトリの`generation-notes.md`
- 各1536×1024ピクセル。生成結果の目視、ローカル参照先、altの有無、PNGの署名・チャンクのCRCを確認しました。
- WordPress用の画像ブロックには幅100％・高さ自動を指定しています。

## 実行した確認と未確認事項

- `prompts/review.md`に沿って自己レビューし、自作に向く人・向かない人の説明を日英に追記しました。
- ローカルでFront Matter、HTMLタグの入れ子、WordPressブロックコメントの入れ子とJSON属性、日英の章数・表数・記入例数、全画像の参照先、リンク色、初期タブ属性を確認しました。
- `python scripts/wp_publish.py articles/drafts/personal-problem-to-app.md --dry-run`は成功しました。ネットワーク接続や認証情報を使わない経路です。
- `status: draft`です。WordPressへの記事送信、画像アップロード、公開は一切行っていません。
- WordPress上でのタブ切り替え操作と、保存後のリンク色は未確認です。投稿しないという今回の指示に従い、投稿時の確認事項として残しています。
- `.gitignore`の`articles/`により、今回の新規記事・画像・記録はGitの除外対象です。ローカル保存のみ行い、除外設定変更、強制追加、コミットは行っていません。


## 追加レビュー：技術・冗長さ・SEO・AIO

ユーザーの追加依頼に従い、`prompts/review.md`の項目で再点検し、次を日英両方に反映しました。

### 技術と説明の整合性

- **直接開くHTMLファイルの保存に関する説明不足を修正。** 画面を表示できることと記録を保持できることを分けました。localStorageのプライベートブラウズ終了時の消失、サイトデータ削除、`file:`で直接開く場合の動作が保証されない点を説明し、通常の利用環境での再起動確認と書き出し・読み戻しを案内しています。日英の該当箇所に出典を掲載しました。
- **URLの受け付け条件を明確化。** 「httpまたはhttpsで始まる」という依頼を、URLの解析と`http:`/`https:`の通信方式の確認へ変更しました。文字列の先頭だけで判定せず、リンク先の安全性を保証するものではないことも依頼文に追加しました。実装コードを掲載している記事ではないため、アプリの動作・安全性を実証したとは扱っていません。
- 記録表の「保存先を忘れる」という例を、後続の説明と同じ「未読の記事を見つけにくい」に揃えました。
- 技術確認資料：
  - [MDN：Window.localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
  - [MDN：URL.protocol](https://developer.mozilla.org/en-US/docs/Web/API/URL/protocol)

### 冗長さと読者の行動

- 記録期間の説明、題材の選び方、既存の方法を紹介する前置き、他の人への提供時の説明を短くしました。
- まとめで導入の手順を繰り返すリストを削除し、「困った場面／今の対処法／残る手間」の一行メモと、次の休憩に試せる行動へ置き換えました。
- 一方で、保存に関する不足説明は追加しています。本文全体の短縮を成果とは扱っていません。

### SEO・AIOの確認

- タイトルとslugは検索意図と一致しているため維持しました。excerptは116文字で、題材の発見から試作・検証までの範囲と、読者が決められることを明示しました。
- 「何度も困る」だけを基準と誤解しないよう、見出しを「負担・頻度・試しやすさ」での選択に変更しました。
- 「プログラミング未経験なら、AIに何を伝えればよい？」と「保存した記録が消えるのはなぜ？」を独立した見出しにし、直後の文章で答えています。
- 重要な説明、記入例、比較基準は画像内だけに置かず、HTMLの本文として保持しました。架空の例と確認できた技術仕様を区別し、既存記事への内部リンクも維持しています。
- AIOは、質問に答えること、正確さ、出典、読み取れる本文の整備として扱いました。GoogleのAI Overviews/AI Modeについては[Google Search Centralの公式案内](https://developers.google.com/search/docs/appearance/ai-features)を確認しました。通常のSEOの基本が適用され、専用のマークアップは必要ないと案内されています。そのため、AI向けという理由だけで追加の構造化データやファイルは作っていません。
- 検索順位やAI回答への引用が改善したとは主張しません。ローカル下書きのため、インデックス状況、公開ページの描画、検索流入の測定は対象外です。

### 修正後の確認

- Front Matterの`draft`、タイトル・slugの維持、画像の参照先、日英の各H2が6個・H3が6個、合計26グループ、4表・2記入例／言語、全6リンクの青色・下線指定、HTMLとWordPressブロックの入れ子を確認しました。
- 既存の6枚の画像と、翻訳されたaltを保持しました。H2ごとの画像配置も確認しました。
- 修正後に`python scripts/wp_publish.py articles/drafts/personal-problem-to-app.md --dry-run`を実行し、成功しました。
- WordPressへの送信・画像アップロード・公開は行っていません。WordPress上の切り替え操作と保存後の見え方は未確認です。


## WordPress下書き送信：2026年10月21日

ユーザーの「dry-runで確認し、問題なければdraftで送信。publishはしない」という指示に従って実施しました。

- 送信前に`--dry-run --draft`を実行し、status、本文構造、日英各6章の画像、全リンクの青色・下線指定を確認しました。
- 同じslugの投稿がないことを認証付きAPIで確認しました。
- 既存の`wp_media.upload_media`を使って6枚をアップロードし、画像ID 79〜84とURLをFront Matterへ保存しました。本文の日英12か所の画像をアップロード先URLへ変更し、アイキャッチを画像ID 79へ設定しました。
- 画像の置き換え後もdry-runを実行し、既存の`wp_publish.publish_article`へ`force_status="draft"`を明示して送信しました。投稿スクリプト自体は変更していません。
- 投稿ID：85。`wordpress_post_id`、`wordpress_url`、`wordpress_featured_media_id`をMarkdownへ保存しました。今後はこの投稿IDを使って更新します。
- 編集URL：https://www.nanasinogonbei.com/blog/wp-admin/post.php?post=85&action=edit
- プレビューURL：https://www.nanasinogonbei.com/blog/?p=85&preview=true （WordPressへのログインが必要です）
- APIで読み戻し、statusが`draft`、保存本文が送信本文と一致、26グループ、日英それぞれH2が6個・H3が6個、画像12か所、アイキャッチ、画像alt、全6リンクの青色・下線指定を確認しました。
- WordPress側で生成したHTMLでも、画像・見出し・リンク色が保持され、日英タブにクリック処理と初期タブの設定があることを確認しました。
- ブラウザによる確認は`Computer Use permissions are not granted`で実行できませんでした。実画面での日英切り替え操作と見た目は未確認です。APIの確認を、ブラウザで操作した結果とは扱っていません。
- `publish`は使用しておらず、記事は公開していません。


## 公開：2026年10月21日

- ユーザーが下書きを確認し、「公開してください。draftからpublishに変更してください」と明示したため、既存投稿ID 85へ`{"status":"publish"}`だけを送信しました。
- 公開直前のWordPress本文・タイトル・抜粋・slug・アイキャッチ・カテゴリ・タグと、公開後の値が同じであることを確認しました。
- 認証付きAPIの`publish`状態、認証なしAPIでの取得、公開URLのHTTP 200を確認しました。
- 公開URL：https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/
- 公開済みファイル：`articles/published/personal-problem-to-app.md`
- WordPressで保存されている本文と公開後の投稿情報をローカルへ反映し、既存の投稿ID・URL・アイキャッチID・本文画像IDを保持しました。設定に従い、記事をdraftsからpublishedへ移動しました。
