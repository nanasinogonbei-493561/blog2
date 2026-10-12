---
categories:
- 開発の裏側
excerpt: 作りたいアプリが決まらないときは、身近な人の困り事をアンケートで調べてみましょう。Googleフォームで頻度と具体的な体験を聞く質問例、回答の整理、既存の道具との比較、小さな試作品への落とし込みまで紹介します。回答数だけで需要を決めない考え方もまとめます。
featured_image: articles/images/survey-driven-app-ideas/01-questions.png
featured_image_alt: 選択式と自由記述の質問を組み合わせ、困り事を調べるアンケートを考える人のイラスト
slug: survey-driven-app-ideas
status: publish
tags:
- Googleフォーム
- 個人開発
- アイデア検証
title: Googleフォームで自作アプリを考える方法｜アンケートの質問例から試作まで
wordpress_featured_media_id: 70
wordpress_inline_media:
  01-questions.png:
    id: 70
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/01-questions.png
  02-form-settings.png:
    id: 71
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/02-form-settings.png
  03-sort-ideas.png:
    id: 72
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/03-sort-ideas.png
  04-existing-tools.png:
    id: 73
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/04-existing-tools.png
  05-small-app.png:
    id: 74
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/05-small-app.png
  06-try-improve.png:
    id: 75
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/06-try-improve.png
wordpress_post_id: 76
wordpress_url: https://www.nanasinogonbei.com/blog/2026/10/12/survey-driven-app-ideas/
---

<!-- wp:html {"metadata":{"name":"本文・画像の表示スタイル"}} -->
<style>
.survey-app-panel {max-width:100%;overflow-wrap:anywhere;}
.survey-app-panel a {color:#0000ff;text-decoration:underline;}
.survey-app-panel img {display:block;max-width:100%;height:auto;}
.survey-app-panel figure {margin:1em 0;}
.survey-app-panel .table-scroll {max-width:100%;overflow-x:auto;}
.survey-app-panel table {width:100%;border-collapse:collapse;}
.survey-app-panel th,.survey-app-panel td {padding:0.6em;border:1px solid #cbd5e1;text-align:left;vertical-align:top;}
.survey-app-panel caption {text-align:left;font-weight:bold;padding:0.5em 0;}
.survey-app-panel pre {box-sizing:border-box;max-width:100%;white-space:pre-wrap;overflow-wrap:anywhere;padding:1em;background:#f3f6f8;}
</style>
<!-- /wp:html -->

<!-- wp:tabs {"metadata":{"name":"日本語・English 切り替え"}} -->
<div class="wp-block-tabs"><!-- wp:tab-list -->
<div role="tablist" class="wp-block-tab-list"><button type="button" role="tab">日本語</button><button type="button" role="tab">English</button></div>
<!-- /wp:tab-list -->

<!-- wp:tab-panels -->
<div class="wp-block-tab-panels"><!-- wp:tab-panel {"label":"日本語","metadata":{"name":"日本語本文"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel"><!-- wp:group {"metadata":{"name":"ja: 導入"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:paragraph -->
<p>自作アプリのアイデアを探すなら、<strong>Googleフォームで困る頻度と具体的な体験を聞き、既存の道具で残る不便を、小さな試作品で確かめる</strong>方法があります。この記事では、質問の作り方から、回答の整理、アプリにする機能の絞り込みまで紹介します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>前回の<a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">1人の困り事を自作アプリで解決する方法</a>では、身近な人への聞き取りから始めました。今回は、同じような悩みを持つ人へアンケートを広げ、答えを比べながら作るものを決めます。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>誰の、どんな場面の困り事を調べるか決める。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>選択式と自由記述を組み合わせたGoogleフォームを作る。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>件数と体験を整理し、確かめたいアイデアを一つ選ぶ。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>既存の道具で解決できるか試す。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>不便が残る部分を小さなアプリにし、本人に使ってもらう。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>この記事の質問例・回答例・集計値・アプリ案は、すべて説明用の架空の例です。アンケートを実施した成果や、完成したアプリの紹介ではありません。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 誰の困り事を調べるか決め、数字と体験を分けて聞く"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">誰の困り事を調べるか決め、数字と体験を分けて聞く</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":70,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/01-questions.png" alt="選択式と自由記述の質問を組み合わせ、困り事を調べるアンケートを考える人のイラスト" class="wp-image-70" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>最初から「どんなアプリが欲しいですか」と聞くと、思いついた機能の一覧になりがちです。まずは「最近、本やレンタル品などを借りた人」のように対象を決めます。今回は、借りた物を返すときの不便を調べる例で進めます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>定量調査</strong>は、回数や選択肢で傾向を比べる調査です。「過去3か月に何回困ったか」などを聞きます。<strong>定性調査</strong>は、体験や理由を本人の言葉で知る調査です。「最後に困ったとき、何が起きたか」を聞きます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>数字だけでは理由が分からず、体験談だけでは似た人がどれくらいいるかを比べにくくなります。最初は一つのフォームに両方を入れ、詳しく知りたいことが残ったら聞き取りを追加します。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">そのまま使える、返却の困り事を調べる質問例</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Googleフォームには、1つ選ぶ「ラジオボタン」、複数選ぶ「チェックボックス」、自由記述の「段落」などがあります。下の表の形式を選び、質問文と選択肢を入力します。<a href="https://support.google.com/docs/answer/7322334?hl=ja" style="color: #0000ff; text-decoration: underline;">Google公式：質問の形式</a></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>調査期間を「過去3か月」にそろえた質問のひな形</caption>
<thead><tr><th>質問</th><th>形式と回答例</th><th>何を知るか</th></tr></thead>
<tbody>
<tr><td>1. 過去3か月に、本や物を借りましたか。</td><td>ラジオボタン：はい／いいえ</td><td>対象に当てはまるか</td></tr>
<tr><td>2. 過去3か月に、返却のことで困ったのは何回ですか。</td><td>ラジオボタン：0回／1回／2〜3回／4回以上／覚えていない</td><td>困る頻度</td></tr>
<tr><td>3. 過去3か月に、返却についてどんなことで困りましたか。複数選べます。</td><td>チェックボックス：返却日を忘れた／返す物を持ち忘れた／返却先を探した／その他／困っていない／覚えていない</td><td>困り事の種類。「困っていない」「覚えていない」はそれぞれ単独で選ぶよう説明を添える</td></tr>
<tr><td>4. 今はどんな方法で管理していますか。複数選べます。</td><td>チェックボックス：紙／メモアプリ／カレンダー／ToDoアプリ／覚えているだけ／その他</td><td>現在の対処法</td></tr>
<tr><td>5. 過去3か月で最後に返却に困ったとき、負担はどの程度でしたか。</td><td>ラジオボタン：ほとんど負担なし／少し負担／かなり負担／とても負担／期間内に困っていない／覚えていない</td><td>本人が感じる負担</td></tr>
<tr><td>6. 過去3か月で最後に返却に困ったとき、何が起きたかを教えてください。</td><td>段落：そのときしようとしていたことや、作業の順番を記入。期間内に困っていなければ空欄</td><td>具体的な場面</td></tr>
<tr><td>7. 今の方法で、やりにくいところは何ですか。</td><td>段落：「日付と持ち物が別々」など。特になければ「なし」</td><td>残っている不便</td></tr>
<tr><td>8. その場面で、何が変われば助かりますか。</td><td>段落：「出発前に返す物をまとめて見たい」など</td><td>望む状態</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>このひな形では質問1だけを必須にし、質問2〜8は任意にします。質問1で「いいえ」なら、残りは空欄で送信してよいと説明します。困っていない人も、無理に体験を作らず答えられます。どこまでが必須かは、フォーム内でも明示してください。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>「便利な通知アプリがあれば使いますよね」のように、賛成へ誘導する質問は避けます。選択肢の内容や質問の順番でも回答は変わるため、配布前に読み方を確かめます。<a href="https://www.pewresearch.org/writing-survey-questions/" style="color: #0000ff; text-decoration: underline;">Pew Research Center：アンケートの質問設計</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: Googleフォームを作り、回答しやすい設定で配る"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">Googleフォームを作り、回答しやすい設定で配る</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":71,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/02-form-settings.png" alt="パソコンとスマートフォンでアンケートを確認し、回答の共有範囲を見直す人のイラスト" class="wp-image-71" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>フォームを作るためのGoogleアカウントと、質問の下書きを用意します。<a href="https://forms.google.com/" style="color: #0000ff; text-decoration: underline;">Googleフォーム</a>で新しいフォームを開き、題名を「借りた物の返却に関するアンケート」などにします。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>説明欄に、調査目的、対象者、回答の使い道、保管期間、問い合わせ先を書きます。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>前章の質問を追加し、このひな形では質問1だけを必須にします。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>下の設定を確認し、プレビューでスマートフォンの読みやすさを見ます。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>回答できる人の範囲を確認してフォームを公開し、回答者用リンクを取得します。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>対象者1〜2人に試してもらい、迷う質問や実際の所要時間を確かめてから配ります。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>説明欄の下書きには、次の文を使えます。角括弧を埋め、所要時間は試しに回答してもらった後で記入してください。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<pre><code class="language-text">目的：借りた物を返す際の不便を調べ、小さなアプリの案を考えます。
対象：過去3か月に本や物を借りた方。
回答は任意です。自由記述には氏名・連絡先・勤務先の情報を書かないでください。
利用範囲：アプリ案の検討に使います。回答原文は公開しません。
保管：回答は[閲覧する担当者]だけが確認し、[削除予定日]まで保管します。
問い合わせ先：[調査用の連絡先]
所要時間：[試しに回答してもらって確認した時間]</code></pre>
<!-- /wp:html -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">メール収集・ログイン・結果の共有を確認する</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>この例ではメールアドレス収集と「回答を1回に制限する」をオフにします。1回制限をオンにするとGoogleへのログインが必要です。「結果の概要を表示する」は、自由記述の全文も回答可能な人に見えるためオフにします。<a href="https://support.google.com/docs/answer/2839588?hl=ja" style="color: #0000ff; text-decoration: underline;">Google公式：公開と回答者への共有</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>この設定では、同じ人の複数回答を確実には見分けられません。集計は人数ではなく回答件数で示します。ログインの要否はアクセス範囲などにも左右されるため、想定する回答者の環境で確認してください。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>詳しい聞き取りに協力してもらいたい場合は、別の応募フォームを用意して、連絡先の使い道と保管期間を説明します。その応募だけでは元の回答との対応は分かりません。聞き取り時に、改めて体験を教えてもらう方法があります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>募集先は、対象に合う知人や、募集を許可しているコミュニティなどです。最近その作業をした人へ届けます。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">アンケートは何件集めればよい？</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>需要を証明できる一律の件数はありません。</strong>最初の10〜20件を質問の見直しの区切りにする方法はありますが、この記事での進め方の一例です。件数だけでなく、対象に合う回答か、具体的な体験が書かれているかを確認します。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 回答の件数と体験を整理し、アイデアを一つに絞る"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">回答の件数と体験を整理し、アイデアを一つに絞る</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":72,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/03-sort-ideas.png" alt="アンケートの件数と体験談を並べ、似た困り事ごとにまとめて一つの案を選ぶ人のイラスト" class="wp-image-72" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>フォームの「回答」で概要を確認し、必要ならGoogleスプレッドシートへ保存します。フォームとシートの閲覧権限はそれぞれ確認します。保管期限が来たら、フォーム内の回答とシートに残る回答の両方を確認して削除します。片方の削除では、もう片方のファイルは消えません。<a href="https://support.google.com/docs/answer/2917686?hl=ja" style="color: #0000ff; text-decoration: underline;">Google公式：回答の保存先と削除</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>最初に対象外の回答、未回答、矛盾する選択などの扱いを決めます。「返却で困った経験がない」という回答は失敗ではなく、アプリを必要としない人を知る材料です。都合のよい回答だけを残さないようにします。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">割合には分母を添え、回答件数と人数を区別する</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>架空の集計例として、全20件のうち借りた経験がある回答が16件、その16件すべてで質問3に回答があり、「持ち忘れた」が7件なら、<strong>「対象条件を満たす質問3の回答16件中7件」</strong>と書きます。複数選択なので、各選択肢の件数を足すと16件を超える場合があります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>質問3が空欄なら、その回答を質問3の分母から外し、空欄の件数を別に記録します。空欄を「困っていない」とは数えません。知人中心の募集結果はその回答群の傾向であり、市場全体の割合には広げません。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">自由記述を「誰が・いつ・何に困るか」でまとめる</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>自由記述は、意味が近い体験をまとめます。1件の回答内に同じ困り事が何度出ても、その分類では1件と数えます。別々の困り事は複数の分類に入れて構いませんが、分類間で回答が重なることを記録します。回答者が同一かどうかは、文章の似方だけで決めません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>本人が書いた体験と、作り手が考えた原因を分けます。下の表の「困り事の仮説」は、追加の聞き取りで確かめる解釈です。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>架空の回答をアプリ候補へ置き換える例</caption>
<thead><tr><th>体験の要約</th><th>困り事の仮説</th><th>アイデア候補</th><th>次に確かめること</th></tr></thead>
<tbody>
<tr><td>返す日は覚えていたが、本を持たずに外出した</td><td>出発前に、返す物を確認できていない</td><td>今日返す物をまとめて見る一覧</td><td>外出前に一覧を見る習慣を作れるか</td></tr>
<tr><td>返却日を書いたメモを見なかった</td><td>確認するきっかけがない</td><td>普段のカレンダーで返却を知らせる</td><td>今のカレンダー設定で足りるか</td></tr>
<tr><td>返却場所を調べ直すのが面倒だった</td><td>必要な情報が散らばっている</td><td>物・日付・返却先をまとめる記録</td><td>既存のメモでもまとめられるか</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>候補は「頻度」「負担の大きさ」「今の方法で残る不便」「小さく試せるか」で比べます。回答件数の最多だけで選ばず、具体的な体験があり、困った本人に試してもらえる案を優先します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>今回の例では、「返す日は分かっているが、持って出る物を確認しづらい人」に絞り、今日返す物の一覧を試す案を選びます。これは架空の判断例です。実際には、頻度や負担についての回答と照らし合わせて決めます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>AIに整理を手伝ってもらうなら、氏名などを取り除いた要約だけを渡します。「事実として書かれた体験と、推測した理由を分けて」と頼み、元の回答で確認してください。AIの分類や件数を、そのまま調査結果にしないようにします。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 既存の道具で足りるか試し、自作する理由を確かめる"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">既存の道具で足りるか試し、自作する理由を確かめる</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":73,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/04-existing-tools.png" alt="借りた本を前に、紙のメモ、カレンダー、スマートフォンのToDoリストを比べる人のイラスト" class="wp-image-73" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>アンケートから困り事が見つかっても、新しいアプリが必要とは限りません。返却の例では、まず次の3つを試す候補にします。順位や実測評価ではありません。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>「出発前に返す物を確認する」ための既存の方法</caption>
<thead><tr><th>候補</th><th>試す使い方</th><th>向いている人と、残りうる不便</th></tr></thead>
<tbody>
<tr><td>紙のメモ</td><td>返す物・返却日・返却先を書き、玄関など目に入る所へ置く</td><td>家で確認できれば十分な人。外出先での更新や持ち歩きは工夫が必要</td></tr>
<tr><td>今使っているカレンダー</td><td>予定名に返す物と場所を入れ、必要なら普段の通知を使う</td><td>予定を見る習慣がある人。返す物が増えたときの一覧性を確認する</td></tr>
<tr><td>Google ToDo リスト</td><td>物の名前をタスク名、返却先を詳細に入れ、日時を設定する</td><td>ToDoを使う人。入力と確認の操作が負担にならないか試す</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Google ToDo リストでは、タスクに詳細や日時を追加できます。具体的な操作は<a href="https://support.google.com/tasks/answer/7675838?hl=ja" style="color: #0000ff; text-decoration: underline;">Google公式：タスクの追加・編集</a>で確認できます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>同じ架空の返却予定を使い、困り事への合い方、始めやすさ、操作の分かりやすさ、費用、データの扱い、続けやすさを比べます。料金は必要な機能と契約内容で確認し、個人情報がどこに保存され、誰から見えるかも見ます。紙でも置き場所によってはほかの人に見える点に注意します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>既存の道具で十分なら、それを使うことが解決です。</strong>「日付・持ち物・場所を毎回別々に確認する手間が残る」など、自作で減らしたい手順が具体的になったときに、アプリ作りへ進みます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>この案は、返す物を記録でき、出発前に画面を確認する人に向いています。画面を見ること自体を忘れる人には、一覧を作るだけでは足りません。その場合は、確認のきっかけを先に考え直します。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 選んだアイデアを、一つの作業ができるアプリにする"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">選んだアイデアを、一つの作業ができるアプリにする</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":74,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/05-small-app.png" alt="返す物、返却先、日付、完了の操作に絞った小さなアプリを紙とスマートフォンで考える人のイラスト" class="wp-image-74" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>回答に出てきた要望を全部載せると、何を確かめるためのアプリかがぼやけます。まず、<strong>「誰が、いつ、何をできれば助かるか」</strong>を一文にします。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<blockquote><p>返却日を把握している人が、外出前に、今日返す物と返却先を一画面で確認できる。</p></blockquote>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>この一文から必要な操作を決めます。「物・返却先・日付を保存する」「今日の返却を一覧で見る」「間違いを直す・不要な記録を消す」「返却済みにする」が初回の範囲です。通知、家族共有、返却先の自動検索は、今回の検証から外します。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>作る前にまとめる、返却アプリの設計メモ</caption>
<thead><tr><th>項目</th><th>今回の案</th></tr></thead>
<tbody>
<tr><td>元の悩み</td><td>返却日は分かっているが、返す物を持たずに出かける</td></tr>
<tr><td>今の対処法と弱点</td><td>予定と物のメモを別々に開いている</td></tr>
<tr><td>アプリの役割</td><td>今日返す物・返却先・日付をまとめて確認する</td></tr>
<tr><td>画面</td><td>入力・編集の画面と、今日返す物の一覧</td></tr>
<tr><td>初回の試用</td><td>実名を使わない架空の記録を、本人のスマートフォンで操作してもらう</td></tr>
<tr><td>最初の保存範囲</td><td>試用端末のブラウザー内だけ。端末間の同期や共有はしない</td></tr>
<tr><td>解決できないこと</td><td>記入していない物の把握、返却の代行、画面を見ること自体の忘れ</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>まず紙に画面を描き、入力する場所と、今日返す物の見つけ方が伝わるか確かめます。その後、画面を組み合わせる道具、AIによる開発支援、開発が得意な人への相談など、経験に合う方法で動く試作品にします。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">AIや開発を手伝う人に渡せる依頼文</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<pre><code class="language-text">借りた物の返却を管理する、小さな試作品を作りたいです。
対象：返却日は分かっているが、返す物を持たずに外出してしまう人。
目的：出発前に、今日返す物と返却先を一画面で確認する。

必要な操作：
・物の名前、返却先、返却日を入力して保存する。
・今日返す物を一覧で見る。
・入力を修正し、不要な記録を削除する。
・返却済みにして、未返却の一覧から外す。

初回は架空のデータだけを使います。
データは試用端末のブラウザー内だけに保存してください。
保存場所と削除方法を画面に説明し、全件削除もできるようにしてください。
今回は通知・アカウント登録・共有・外部サービスとの自動連携は作りません。
予算：[作成費と月額費用の上限]
修正を担当する人：[担当者]

まず画面案と操作の流れを見せてください。
不明点や、この保存方法の制約を説明してください。</code></pre>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>この保存方法では、別の端末で同じ記録を使えず、ブラウザーのデータを消すと記録も失う場合があります。初回の操作確認用として選ぶ案です。作った人と一緒に、保存・修正・削除が意図どおり動くかを確認します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>URLから試してもらうなら、アプリを置くサービスの費用と公開範囲を確認します。URLを知っているだけで入れる場所には、本番の個人情報を置きません。共有やアカウント登録が必要になったら、誰がどの記録を見られるか、削除や問い合わせを誰が担当するかを改めて決めます。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 試作品を使ってもらい、手間が減るかを確かめる"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">試作品を使ってもらい、手間が減るかを確かめる</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":75,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/06-try-improve.png" alt="借りた物の一覧をスマートフォンで試す人と、迷った操作をメモして改善につなげる人のイラスト" class="wp-image-75" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>アンケートで分かるのは、本人が報告した体験や希望です。アプリで手間が減るかは、動く試作品で確かめます。協力に同意してくれた少人数に、次の作業を説明しすぎず試してもらいます。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>架空の本を、返却先と今日の日付で登録してもらう。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>いったん画面を閉じ、もう一度開いて、今日返す物を探してもらう。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>返却先を修正し、返却済みにしてもらう。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>今の方法と比べ、手間が減った所と、増えた所を聞く。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>記録するのは、作業を終えられたか、どこで迷ったか、助けが必要だったか、確認にかかった時間です。時間を比べるなら同じ作業条件にそろえ、初回は操作への慣れも影響することを残します。「便利でしたか」だけで終わらせません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>架空の試用記録なら、「3人中2人が説明なしで今日の一覧を見つけ、1人は入口で迷った」のように残せます。この確認で分かるのは初回の操作のしやすさです。継続利用は、実際に返却する機会があった後で、再び使ったか、使わなかった理由は何かを聞きます。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">反応が弱いときは、機能を増やす前に困り事へ戻る</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>回答が集まらない：</strong>募集先が対象に合うか、リンクを開けるか、質問が長すぎないかを確認します。需要がないと即断しません。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>「特に困っていない」が多い：</strong>無理に賛成を集めず、誰には必要ないのかを整理します。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>「通知が欲しい」ばかり出る：</strong>一覧を見ないことが主な問題なら、今回の案がずれている可能性があります。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>入力が続かない：</strong>必要な入力が多いのか、今の方法で十分なのか、作業の流れに合わないのかを聞き直します。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>次に選ぶのは、操作を一つ直す、対象を絞り直す、既存の道具を使う、いったん作るのをやめる、といった行動です。好意的な感想だけでなく、実際の行動を根拠に決めます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>まずは、調べたい困り事を一つ書き、Googleフォームに選択式と自由記述の質問を入れてみてください。大切なのは回答数を増やすことだけでなく、<strong>数字で傾向を見て、体験で理由を確かめ、小さな試作品で役立つかを試すこと</strong>です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><small>Googleの機能・操作の記述は、2026年10月12日に公式ヘルプで確認しました。実際のフォーム作成・配布・試用は実施していません。画像はAIで生成した概念イラストで、実在するサービスの画面ではありません。</small></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel -->

<!-- wp:tab-panel {"label":"English","metadata":{"name":"English body"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel"><!-- wp:group {"metadata":{"name":"en: Introduction"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:paragraph -->
<p><strong>Plan Your Own App With Google Forms: From Survey Questions to a Prototype</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To find an idea for an app you make yourself, <strong>ask about frequency and concrete experiences in Google Forms, then use a small prototype to test a difficulty that existing tools leave unresolved.</strong> This article covers writing questions, organizing answers, and deciding which app functions to build first.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The previous article, <a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">How to Solve One Person’s Problem With an App You Make Yourself</a>, started with a conversation with someone you know. This article extends that approach to a survey of people with similar experiences, so you can compare their answers.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>Decide whose problem to investigate and in what situation.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Create a Google Form combining choices and open questions.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Organize counts and experiences, then choose one idea to investigate.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Try existing tools first.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Build a small app for the remaining difficulty and let the intended users try it.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>All questions, responses, counts, and app ideas below are fictional examples. This is not a report of a completed survey or a finished app.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Choose whose problem to investigate, then ask about both counts and experiences"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Choose whose problem to investigate, then ask about both counts and experiences</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":70,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/01-questions.png" alt="A person planning a survey that combines multiple-choice questions and written accounts of everyday difficulties" class="wp-image-70" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Asking “What app would you like?” can produce a list of imagined features. Start with a defined group, such as people who recently borrowed books or other items. We will investigate difficulties with returning borrowed items.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Quantitative research</strong> compares patterns through counts and choices, such as how many times a problem occurred in the past three months. <strong>Qualitative research</strong> explores experiences and reasons in people’s own words, such as what happened the last time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Counts alone do not explain why something happened. Individual stories alone make it harder to compare how many respondents had similar experiences. Combine both in one form, then follow up with conversations when you need more detail.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Questions you can adapt for a survey about returning items</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Google Forms offers multiple choice for one answer, checkboxes for several answers, and paragraph fields for written responses. Select the appropriate type and enter the questions and options below. See <a href="https://support.google.com/docs/answer/7322334?hl=ja" style="color: #0000ff; text-decoration: underline;">Google’s official guide to question types</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>A question template using the same three-month reference period</caption>
<thead><tr><th>Question</th><th>Type and sample options</th><th>What it tells you</th></tr></thead>
<tbody>
<tr><td>1. Have you borrowed books or other items in the past three months?</td><td>Multiple choice: Yes / No</td><td>Whether the person fits the intended group</td></tr>
<tr><td>2. How many times have you had difficulty returning items in the past three months?</td><td>Multiple choice: 0 / 1 / 2–3 / 4 or more / Cannot remember</td><td>Frequency</td></tr>
<tr><td>3. What difficulties did you have returning items in the past three months? Select all that apply.</td><td>Checkboxes: Forgot the date / Forgot to bring the item / Had to find the return location / Other / No difficulty / Cannot remember</td><td>Problem types. Explain that “No difficulty” and “Cannot remember” should each be selected alone</td></tr>
<tr><td>4. How do you currently keep track? Select all that apply.</td><td>Checkboxes: Paper / Notes app / Calendar / Task app / Memory only / Other</td><td>Current methods</td></tr>
<tr><td>5. How much of a burden was the most recent difficulty returning items within the past three months?</td><td>Multiple choice: Almost none / A little / Quite a lot / A great deal / No difficulty during this period / Cannot remember</td><td>Perceived burden</td></tr>
<tr><td>6. Describe what happened the last time you had difficulty returning items within the past three months.</td><td>Paragraph: Describe what you were trying to do and the sequence of actions. Leave blank if you had no difficulty during this period</td><td>A concrete situation</td></tr>
<tr><td>7. What is awkward about your current method?</td><td>Paragraph: For example, “The date and the items are in different places.” Write “None” if appropriate</td><td>Remaining difficulty</td></tr>
<tr><td>8. What change would help in that situation?</td><td>Paragraph: For example, “See everything I need to return before leaving”</td><td>The desired outcome</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>For this template, require only question 1 and make questions 2–8 optional. Explain that people who answer “No” to question 1 can submit with the rest blank. People without difficulties will not feel pressured to invent an experience. State which questions are required within the form as well.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Avoid leading wording such as “You would use a convenient reminder app, wouldn’t you?” Choices and question order can also affect answers, so check how people interpret the form before distributing it. See <a href="https://www.pewresearch.org/writing-survey-questions/" style="color: #0000ff; text-decoration: underline;">Pew Research Center’s guide to writing survey questions</a>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Create the Google Form and share it with settings that suit respondents"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Create the Google Form and share it with settings that suit respondents</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":71,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/02-form-settings.png" alt="A person reviewing a survey on a laptop and phone while checking who can access responses" class="wp-image-71" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Prepare a Google account for creating the form and a draft of your questions. Open a new form in <a href="https://forms.google.com/" style="color: #0000ff; text-decoration: underline;">Google Forms</a> and give it a descriptive title, such as “Survey About Returning Borrowed Items.”</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>Explain the purpose, intended respondents, use of answers, retention period, and contact details.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Add the questions; for this template, require only question 1.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Review the settings below and use the preview to check readability on a phone.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Check who can respond, publish the form, and obtain the responder link.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Ask one or two intended respondents to try it. Check confusing questions and actual completion time before wider distribution.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Adapt this description by filling in the brackets. Add the estimated time after someone has tried answering.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<pre><code class="language-text">Purpose: Investigate difficulties with returning borrowed items and explore a small app idea.
Who should respond: People who borrowed books or other items in the past three months.
Participation is voluntary. Do not include names, contact details, or workplace information in written responses.
Use: Answers will inform app planning. Original written responses will not be published.
Storage: Only [people who will review answers] will have access. Answers will be kept until [deletion date].
Contact: [survey contact details]
Estimated time: [time confirmed through a trial response]</code></pre>
<!-- /wp:html -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Check email collection, sign-in, and result sharing</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>For this example, turn off email collection and “Limit to 1 response.” Enabling the limit requires Google sign-in. Keep “View results summary” off because it exposes full written answers to people who can respond. See <a href="https://support.google.com/docs/answer/2839588?hl=ja" style="color: #0000ff; text-decoration: underline;">Google’s official publishing and sharing guide</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With these settings, you cannot reliably identify repeat submissions from the same person. Report submission counts rather than people. Sign-in also depends on access settings, so test with the intended audience.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For follow-up interviews, you can use a separate volunteer form explaining how contact details will be used and retained. That application alone will not identify the person’s original answers; you can ask them to describe their experience again during the interview.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Recruit through relevant acquaintances or communities that allow survey requests. Reach people who recently performed the task.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">How many survey responses do you need?</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p><strong>No universal response count proves demand.</strong> Reviewing the first 10–20 submissions is one possible checkpoint for revising questions, suggested here as an example workflow. Check whether answers fit your intended group and describe concrete experiences, as well as how many you collect.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Organize counts and stories, then choose one app idea"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Organize counts and stories, then choose one app idea</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":72,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/03-sort-ideas.png" alt="A person grouping survey counts and experience cards by similar difficulties and choosing one idea" class="wp-image-72" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Review the summary under “Responses” and save answers to Google Sheets if useful. Check permissions separately for the form and sheet. At the end of the retention period, check and delete retained answers in both places: deleting one file does not delete the other. See <a href="https://support.google.com/docs/answer/2917686?hl=ja" style="color: #0000ff; text-decoration: underline;">Google’s official guide to response storage and deletion</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Decide how to handle ineligible responses, missing answers, and contradictory choices. “I had no difficulty” helps you understand who may not need an app. Do not keep only the answers that support your idea.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">State the denominator and distinguish submissions from people</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In a fictional example, suppose 16 of 20 submissions meet the borrowing criterion, all 16 answer question 3, and seven select “Forgot to bring the item.” Report <strong>“7 of 16 eligible submissions answering question 3.”</strong> Because multiple choices are allowed, totals across options may exceed 16.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If question 3 is blank, exclude that submission from this question’s denominator and record the missing-answer count separately. A blank does not mean “No difficulty.” Results collected mainly through acquaintances describe those submissions, not the entire market.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Group written answers by who struggled, when, and with what</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Group similar experiences. Count the same problem once per submission even if it appears several times in that submission. An answer can belong to several groups if it describes different problems; record the overlap. Similar wording alone does not establish that submissions came from the same person.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Separate the reported experience from your explanation of its cause. The “Problem hypothesis” column below contains interpretations to check in follow-up conversations.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>Turning fictional responses into candidate ideas</caption>
<thead><tr><th>Experience summary</th><th>Problem hypothesis</th><th>Possible idea</th><th>Next question to investigate</th></tr></thead>
<tbody>
<tr><td>Remembered the return date but left without the book</td><td>Did not check which items to bring</td><td>A list of items due today</td><td>Will the person check a list before leaving?</td></tr>
<tr><td>Did not look at the note containing the return date</td><td>No prompt to check</td><td>A return reminder in the person’s usual calendar</td><td>Are existing calendar settings sufficient?</td></tr>
<tr><td>Had to look up the return location again</td><td>Information is scattered</td><td>Keep item, date, and return location together</td><td>Can an existing notes app do this?</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Compare frequency, burden, the difficulty remaining with current methods, and how easily you can test a small solution. Do not choose solely by submission count; favor a concrete experience and a person willing to try a solution.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For this example, we choose a list of items due today for people who know the date but struggle to check what to bring. This is a fictional decision, which in real research should be checked against frequency and burden responses.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If AI helps organize answers, provide summaries with identifying information removed. Ask it to distinguish reported experiences from inferred reasons, then verify against the originals. Do not present AI-generated groupings or counts as research findings without checking them.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Try existing tools and establish a reason to build your own"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Try existing tools and establish a reason to build your own</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":73,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/04-existing-tools.png" alt="A person comparing a paper note, calendar, and phone task list beside borrowed books" class="wp-image-73" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Finding a problem does not necessarily mean you need a new app. For returning items, try these three existing approaches first. They are candidates, not rankings or measured evaluations.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>Existing ways to check what to return before leaving</caption>
<thead><tr><th>Candidate</th><th>What to try</th><th>Who it suits and possible limitations</th></tr></thead>
<tbody>
<tr><td>Paper note</td><td>Write the item, date, and location, then place it somewhere visible, such as by the door</td><td>People who only need to check at home. Updating it away from home or carrying it requires extra thought</td></tr>
<tr><td>Current calendar</td><td>Include the item and location in the event title and use usual reminders if needed</td><td>People who already check their calendar. Check how readable it remains with many items</td></tr>
<tr><td>Google Tasks</td><td>Use the item as the task title, add the location in details, and set a date and time</td><td>People who use task lists. Test whether entering and checking tasks becomes a burden</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Google Tasks supports adding details and dates or times. See <a href="https://support.google.com/tasks/answer/7675838?hl=ja" style="color: #0000ff; text-decoration: underline;">Google’s official guide to adding and editing tasks</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Use the same fictional return plans to compare fit, setup effort, ease of use, cost, data handling, and continued use. Check costs for the features and plan you need. Check where information is stored and who can see it; even paper notes may be visible to others depending on where you leave them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>If an existing tool is sufficient, using it is a valid solution.</strong> Build an app when you can identify a specific step to reduce, such as repeatedly opening separate places to check dates, items, and locations.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This idea suits people who can record items and check a screen before leaving. A list alone will not help someone whose main difficulty is remembering to look at the screen. Reconsider the prompt to check before building.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Turn the selected idea into an app that supports one task"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Turn the selected idea into an app that supports one task</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":74,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/05-small-app.png" alt="A person sketching a small app limited to an item, return location, date, and completion action" class="wp-image-74" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Including every requested feature makes the purpose of a test unclear. Write one sentence explaining <strong>who should be able to do what, and when.</strong></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<blockquote><p>A person who knows the return date can check today’s items and return locations on one screen before leaving home.</p></blockquote>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Derive the necessary actions from that sentence: save an item, location, and date; view items due today; edit or delete records; and mark an item returned. Leave notifications, family sharing, and automatic location searches out of this initial test.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table>
<caption>A planning note for the proposed return-items app</caption>
<thead><tr><th>Item</th><th>Proposal</th></tr></thead>
<tbody>
<tr><td>Original problem</td><td>Knows the return date but leaves without the item</td></tr>
<tr><td>Current approach and weakness</td><td>Opens the schedule and item notes separately</td></tr>
<tr><td>App purpose</td><td>Show today’s items, return locations, and dates together</td></tr>
<tr><td>Screens</td><td>An entry/edit screen and a list of items due today</td></tr>
<tr><td>Initial trial</td><td>Let the person use fictional records without real names on their own phone</td></tr>
<tr><td>Initial storage</td><td>Only in the trial device’s browser, without syncing or sharing</td></tr>
<tr><td>Outside its scope</td><td>Discovering unrecorded items, returning them for the user, or ensuring the person checks the screen</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Draw the screens on paper first. Check whether people understand where to enter data and how to find today’s items. Then make a working prototype using a visual app builder, AI development assistance, or help from someone with development experience.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">A request you can give to AI or someone helping you build</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<pre><code class="language-text">I want a small prototype for tracking borrowed items to return.
Users: People who know the return date but leave without the items.
Purpose: Show today’s items and return locations on one screen before leaving.

Required actions:
・Enter and save the item name, return location, and return date.
・View items due today.
・Edit entries and delete unwanted records.
・Mark an item returned and remove it from the outstanding list.

Use fictional data only for the initial trial.
Store data only in the trial device’s browser.
Explain storage and deletion on screen and provide a way to delete all records.
Do not build notifications, accounts, sharing, or automatic integrations yet.
Budget: [creation and monthly cost limits]
Person responsible for fixes: [name or role]

Show the proposed screens and workflow first.
Explain unknowns and the limitations of this storage approach.</code></pre>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>With this approach, the same records are not available on another device, and clearing browser data may erase them. It is an option for initial usability checks. Confirm with the maker that saving, editing, and deletion work as intended.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If people will try it through a URL, check hosting costs and access settings. Do not put real personal information somewhere anyone with the URL can enter. Before adding sharing or accounts, decide who can see which records and who will handle deletion and questions.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Let people try the prototype and check whether it reduces effort"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Let people try the prototype and check whether it reduces effort</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":75,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/06-try-improve.png" alt="One person testing a borrowed-item list on a phone while another notes confusing steps for improvement" class="wp-image-75" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>A survey tells you about reported experiences and wishes. Use a working prototype to check whether the app reduces effort. Ask a few consenting participants to try the following tasks without explaining every step.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>Register a fictional book with a return location and today’s date.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Close and reopen the screen, then find the items due today.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Edit the return location and mark the item returned.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Compare it with the current method and describe where effort decreased or increased.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Record whether people finish, where they hesitate, whether they need help, and how long checking takes. Compare times under the same task conditions and note that familiarity affects a first trial. Do not stop at “Was it convenient?”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A fictional trial record might read, “Of three participants, two found today’s list without explanation; one struggled to find the entry point.” This checks initial ease of use. To investigate continued use, follow up after participants have an actual opportunity to return something: did they use it again, and if not, why?</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Return to the problem before adding features when the response is weak</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>Few survey responses:</strong> Check whether recruitment reaches the intended group, whether the link opens, and whether the form is too long. Do not immediately conclude there is no demand.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Many people report no difficulty:</strong> Identify who does not need the solution rather than pushing for agreement.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Most requests are for reminders:</strong> If people do not check lists, this proposal may address the wrong problem.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>People stop entering items:</strong> Ask whether entry takes too much effort, existing methods are sufficient, or the app does not fit their routine.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Possible next steps include fixing one interaction, narrowing the intended group, using an existing tool, or stopping development for now. Base the decision on behavior as well as favorable comments.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Start by writing down one difficulty and adding choice-based and open questions to Google Forms. The aim is more than collecting responses: <strong>use counts to identify patterns, experiences to understand reasons, and a small prototype to test usefulness.</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><small>Google feature and workflow descriptions were checked against official help pages on October 12, 2026. No form was created or distributed, and no user trial was conducted. Images are AI-generated conceptual illustrations, not actual service interfaces.</small></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel --></div>
<!-- /wp:tab-panels --></div>
<!-- /wp:tabs -->