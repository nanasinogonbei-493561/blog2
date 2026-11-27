---
categories:
- 開発の裏側
excerpt: 借りた物を返す日に、持っていく物が分からず手が止まった。そんな体験をGoogleフォームで集めるところから、自作アプリの題材は探せます。頻度と体験を分けて聞く質問例、回答を数えるときの注意点、今の道具を試してから試作品を作る流れをまとめました。
featured_image: articles/images/survey-driven-app-ideas/optimized/01-questions.jpg
featured_image_alt: 選択式と自由記述の質問を組み合わせ、困り事を調べるアンケートを考える人のイラスト
slug: survey-driven-app-ideas
status: publish
tags:
- 個人開発
- アプリ開発
- アイデア検証
title: アンケートでアプリのアイデアを検証する方法｜Googleフォーム質問例
wordpress_featured_media_id: 266
wordpress_inline_media:
  01-questions.jpg:
    alt: 選択式と自由記述の質問を組み合わせ、困り事を調べるアンケートを考える人のイラスト
    id: 266
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-questions.jpg
  02-form-settings.jpg:
    alt: パソコンとスマートフォンでアンケートを確認し、回答の共有範囲を見直す人のイラスト
    id: 267
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-form-settings.jpg
  03-sort-ideas.jpg:
    alt: アンケートの件数と体験談を並べ、似た困り事ごとにまとめて1つの案を選ぶ人のイラスト
    id: 268
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-sort-ideas.jpg
  04-existing-tools.jpg:
    alt: 借りた本を前に、紙のメモ、カレンダー、スマートフォンのToDoリストを比べる人のイラスト
    id: 269
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-existing-tools-1.jpg
  05-small-app.jpg:
    alt: 返す物、返却先、日付、完了の操作に絞った小さなアプリを紙とスマートフォンで考える人のイラスト
    id: 270
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-small-app.jpg
  06-try-improve.jpg:
    alt: 借りた物の一覧をスマートフォンで試す人と、迷った操作をメモして改善につなげる人のイラスト
    id: 271
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-try-improve.jpg
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

<!-- wp:tabs {"activeTabIndex":0,"metadata":{"name":"日本語・English 切り替え"}} -->
<div class="wp-block-tabs"><!-- wp:tab-list -->
<div role="tablist" class="wp-block-tab-list"><button type="button" role="tab">日本語</button><button type="button" role="tab">English</button></div>
<!-- /wp:tab-list -->

<!-- wp:tab-panels -->
<div class="wp-block-tab-panels"><!-- wp:tab-panel {"label":"日本語","metadata":{"name":"日本語本文"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel" lang="ja"><!-- wp:group {"metadata":{"name":"ja: 導入"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:paragraph -->
<p>「どんなアプリが欲しい？」と聞く前に、「最後に困ったとき、何があった？」と聞いてみる。Googleフォームでアイデアを探すなら、<strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">困った回数と、そのときの出来事を両方聞く</mark></strong>ところから始められます。借りた物の返却を例に、回答を読んで、残る不便を試作品で確かめるところまで扱います。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>前回の<a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">作りたいアプリがない人へ｜1人の困り事から自作アプリを作る方法</a>では、身近な人への聞き取りから始めました。今回は同じ「借りた物の返却」を題材に、アンケートへ広げるとどう見方が変わるかをたどります。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>誰の、どんな場面の困り事を調べるか決める。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>選択式と自由記述を組み合わせたGoogleフォームを作る。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>件数と体験を整理し、確かめたいアイデアを1つ選ぶ。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>既存の道具で解決できるか試す。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>不便が残る部分を小さなアプリにし、本人に使ってもらう。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>この記事の質問例・回答例・集計値・アプリ案は、流れを説明するために用意した架空の例です。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 誰の困り事を調べるか決め、数字と体験を分けて聞く"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">誰の困り事を調べるか決め、数字と体験を分けて聞く</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":266,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-questions.jpg" alt="選択式と自由記述の質問を組み合わせ、困り事を調べるアンケートを考える人のイラスト" class="wp-image-266" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>最初から欲しい機能を聞くと、出てくるのはその場で思いついた案ばかりかもしれません。今回、話を聞きたいのは最近本やレンタル品を借りた人。返すときのことなら、実際にあった場面を思い出して答えてもらえます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>「過去3か月に何回困った？」と、回数や選択肢で傾向を見るのが<strong>定量調査</strong>。「最後に困ったとき、何が起きた？」と尋ねて、体験や理由を本人の言葉で聞くのが<strong>定性調査</strong>です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>回数が分かっても、なぜ困ったかまでは見えてきません。体験談ばかりだと、同じところで困った人がどれくらいいたかを比べづらい。そこで、1つのフォームに両方の質問を入れます。気になる答えがあれば、あとで話を聞く余地もあります。</p>
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
<p>このひな形で必須にするのは質問1だけにします。質問2〜8は任意です。質問1で「いいえ」を選んだ人は、残りを空欄のまま送信できます。フォームにもそう書いておけば、困った経験がない人まで、無理に何かを書かずに済みます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>「便利な通知アプリがあれば使いますよね」のように、賛成へ誘導する質問は避けます。選択肢の内容や質問の順番でも回答は変わるため、配布前に読み方を確かめます。<a href="https://www.pewresearch.org/writing-survey-questions/" style="color: #0000ff; text-decoration: underline;">Pew Research Center：アンケートの質問設計</a></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: Googleフォームを作り、回答しやすい設定で配る"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">Googleフォームを作り、回答しやすい設定で配る</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":267,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-form-settings.jpg" alt="パソコンとスマートフォンでアンケートを確認し、回答の共有範囲を見直す人のイラスト" class="wp-image-267" style="width:100%;height:auto"/></figure>
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
<p>この設定だと、同じ人が二度答えても確実には見分けられません。<mark style="background-color:#fef08a;color:#422006" class="has-inline-color">集計に書くのは「答えた人数」ではなく「届いた回答の件数」です。</mark> ログインが必要かどうかはアクセス範囲にもよるので、配る相手と同じ条件で開けるかも確かめます。</p>
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
<p>最初の10〜20件は、聞き方を見直す目安にできます。話を聞きたい人に届いたか、困った場面まで書いてもらえたかを見ます。<mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">件数だけで「このアプリには需要がある」と決めるのは早計です。</mark></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 回答の件数と体験を整理し、アイデアを1つに絞る"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">回答の件数と体験を整理し、アイデアを1つに絞る</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":268,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-sort-ideas.jpg" alt="アンケートの件数と体験談を並べ、似た困り事ごとにまとめて1つの案を選ぶ人のイラスト" class="wp-image-268" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>回答の概要は、フォームの「回答」タブで確認できます。必要ならGoogleスプレッドシートへ保存できます。フォームとシートはそれぞれ誰が見られるか確認が必要です。保管期限が来たら、回答が残っている場所を両方確認して削除します。片方で消しただけでは、もう片方に残ります。<a href="https://support.google.com/docs/answer/2917686?hl=ja" style="color: #0000ff; text-decoration: underline;">Google公式：回答の保存先と削除</a></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>対象外の回答や空欄、矛盾する選択をどう扱うかは、先に決めておきます。「返却で困ったことがない」という答えも、どんな人なら今の方法で足りるかを考える材料。<mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">自分の案に都合のよい答えだけを残すと、傾向を読み違えます。</mark></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">割合には分母を添え、回答件数と人数を区別する</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>架空の集計例として、全20件のうち借りた経験がある回答が16件、その16件すべてで質問3に回答があり、「持ち忘れた」が7件なら、<strong>「対象条件を満たす質問3の回答16件中7件」</strong>と書きます。複数選択なので、各選択肢の件数を足すと16件を超える場合があります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>質問3が空欄なら、この質問の母数には入れず、空欄の件数を別に記録します。<mark style="background-color:#fef08a;color:#422006" class="has-inline-color">答えが書かれていないことと、「困っていない」と答えたことは区別します。</mark> 知人を中心に聞いた結果から言えるのは、その回答の範囲に限られます。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">自由記述を「誰が・いつ・何に困るか」でまとめる</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>自由記述は、似た体験をまとめて読みます。同じ回答に同じ困り事が何度出ても、そのグループでは1件。別々の困り事が書かれていれば、複数のグループに入れて、どこで件数が重なるかを記録します。文章が似ていても、それだけで同じ人の回答だとは判断できません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>本人が書いた出来事は、そのまま体験として残します。「なぜそうなったのか」は、聞き取りで確かめる前の見立て。下の表では「困り事の仮説」に入れています。</p>
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
<p>件数の多かったものから順に作る必要はありません。どのくらい困るか、今のやり方で何が残るか、小さく試せるかを見比べます。困った場面が具体的で、その本人に試してもらえる案なら、次に確かめたいことを決めやすくなります。</p>
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

<!-- wp:image {"id":269,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-existing-tools-1.jpg" alt="借りた本を前に、紙のメモ、カレンダー、スマートフォンのToDoリストを比べる人のイラスト" class="wp-image-269" style="width:100%;height:auto"/></figure>
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
<p>架空の返却予定を同じ条件で入れてみると、困り事に合うか、操作で迷わないかを比べられます。始めやすさや続けやすさのほか、必要な機能がどの契約に含まれ、いくらかかるかも確認してください。個人情報はどこに残り、誰が見られるでしょうか。紙でも、置き場所によっては他の人の目に触れます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>カレンダーなど、今ある道具で用が済んだら、そこで解決です。何度も別々の画面を開いて日付・持ち物・場所を確認するなど、残った手順が具体的に見えたら、そこを減らせるアプリを考えます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>この案は、返す物を記録でき、出発前に画面を確認する人に向いています。画面を見ること自体を忘れる人には、一覧を作るだけでは足りません。その場合は、確認のきっかけを先に考え直します。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 選んだアイデアを、1つの作業ができるアプリにする"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">選んだアイデアを、1つの作業ができるアプリにする</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":270,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-small-app.jpg" alt="返す物、返却先、日付、完了の操作に絞った小さなアプリを紙とスマートフォンで考える人のイラスト" class="wp-image-270" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>フォームに書かれた要望を全部入れると、何を試すアプリなのか見えづらくなります。作り始める前に、<strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">「誰が、いつ、何をできれば助かるか」を一文にする。</mark></strong> 機能に迷ったときは、この一文に戻れます。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<blockquote><p>返却日を把握している人が、外出前に、今日返す物と返却先を一画面で確認できる。</p></blockquote>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>その一文から考えると、初回に欲しいのは、物・返却先・日付を残す、今日の返却を一覧で見る、間違いを直すか不要な記録を消す、返却済みにする、という操作。通知、家族との共有、返却先の自動検索はあとに回せます。</p>
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
<tr><td>最初の保存範囲</td><td>試用端末のブラウザ内だけ。端末間の同期や共有はしない</td></tr>
<tr><td>解決できないこと</td><td>記入していない物の把握、返却の代行、画面を見ること自体の忘れ</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>まず紙に画面を描いて、「入力するならどこ？」「今日返す物はどう探す？」と聞いてみます。画面の並びが伝わったら、画面を組み合わせる道具やAIを使う、開発に慣れた人へ頼むなど、手が届く方法で動く試作品にします。</p>
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

初回の試用では架空のデータだけを使います。
データは試用端末のブラウザ内だけに保存してください。
保存場所と削除方法を画面に説明し、全件削除もできるようにしてください。
今回は通知・アカウント登録・共有・外部サービスとの自動連携は作りません。
予算：[作成費と月額費用の上限]
修正を担当する人：[担当者]

まず画面案と操作の流れを見せてください。
不明点や、この保存方法の制約を説明してください。</code></pre>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>この保存方法では、別の端末で同じ記録を使えず、ブラウザのデータを消すと記録も失う場合があります。初回の操作確認用として選ぶ案です。作った人と一緒に、保存・修正・削除が意図どおり動くかを確認します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>URLから試してもらうなら、アプリを置くサービスの費用と公開範囲を確認します。URLを知っているだけで入れる場所には、本番の個人情報を置きません。共有やアカウント登録が必要になったら、誰がどの記録を見られるか、削除や問い合わせを誰が担当するかを改めて決めます。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 試作品を使ってもらい、手間が減るかを確かめる"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading -->
<h2 class="wp-block-heading">試作品を使ってもらい、手間が減るかを確かめる</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":271,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-try-improve.jpg" alt="借りた物の一覧をスマートフォンで試す人と、迷った操作をメモして改善につなげる人のイラスト" class="wp-image-271" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>アンケートで聞けたのは、経験したことや欲しいものです。<mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">作業が楽になったかは、動く試作品を使うところを見て確かめます。</mark> 協力してくれる数人に、次の作業を頼み、操作は説明しすぎずに見守ります。</p>
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
<p>「便利でしたか？」と聞く前に、最後までできたか、どこで手が止まったか、助けが要ったか、何分かかったかをメモしておきます。時間を比べる条件はそろえます。初めて画面を触る人は、操作に不慣れな分も時間に出ます。</p>
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
<p>次に選ぶのは、操作を1つ直す、対象を絞り直す、既存の道具を使う、いったん作るのをやめる、といった行動です。好意的な感想だけでなく、実際の行動を根拠に決めます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>最初は困り事を1つ選んで、選択式と自由記述の質問をGoogleフォームに1つずつ入れるところから始めてみてください。集まった回数を手がかりに、どんな場面だったかを読み、今の道具で残る不便を試作で確かめます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><small>GoogleフォームとGoogle ToDo リストの仕様は2026年10月12日時点の公式ヘルプをもとにしています。最新の機能や仕様は各サービスの案内で確認してください。</small></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 関連記事"},"className":"survey-app-panel panel-ja","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-ja"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">関連記事</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">作りたいアプリがない人へ｜1人の困り事から自作アプリを作る方法</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color: #0000ff; text-decoration: underline;">自分の悩みから自作アプリを作る方法｜題材選びから小さな試作まで</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/09/28/crowdsourcing-problems-to-app-ideas/" style="color: #0000ff; text-decoration: underline;">クラウドソーシングでアプリのアイデアを探す方法｜収集から検証まで</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel -->

<!-- wp:tab-panel {"label":"English","metadata":{"name":"English body"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel" lang="en"><!-- wp:group {"metadata":{"name":"en: Introduction"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:paragraph -->
<p><strong>How to Validate App Ideas With Surveys: Google Forms Questions to a Prototype</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Before asking “What app would you like?”, try asking “What happened the last time you had trouble?” To look for an idea in Google Forms, <strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">ask both how often it happened and what happened on a particular occasion.</mark></strong> We’ll use the example of returning borrowed items, from reading the answers to testing what a prototype might fix.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The previous article, <a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">No App Idea Yet? How to Build a Homemade App From One Person’s Problem</a>, started with a conversation with someone you know. This article carries the same borrowed-item return example over to a survey so you can see how comparing wider responses changes what to build.</p>
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
<p>The questions, responses, counts, and app ideas below are fictional examples created to walk through the steps.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Choose whose problem to investigate, then ask about both counts and experiences"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Choose whose problem to investigate, then ask about both counts and experiences</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":266,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-questions.jpg" alt="A person planning a survey that combines multiple-choice questions and written accounts of everyday difficulties" class="wp-image-266" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Start by asking about features and you may get a list of ideas people just thought of. For this survey, look for people who recently borrowed a book or rented something. They have a real return to think back on.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Quantitative research</strong> compares patterns through counts and choices, such as how many times a problem occurred in the past three months. <strong>Qualitative research</strong> explores experiences and reasons in people’s own words, such as what happened the last time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A count won’t tell you why something happened. With stories alone, it’s hard to see how many people got stuck in the same place. Put both kinds of questions in one form and follow up when an answer makes you curious.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Questions you can adapt for a survey about returning items</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Google Forms offers multiple choice for one answer, checkboxes for several answers, and paragraph fields for written responses. Select the appropriate type and enter the questions and options below. See <a href="https://support.google.com/docs/answer/7322334?hl=en" style="color: #0000ff; text-decoration: underline;">Google’s official guide to question types</a>.</p>
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

<!-- wp:image {"id":267,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-form-settings.jpg" alt="A person reviewing a survey on a laptop and phone while checking who can access responses" class="wp-image-267" style="width:100%;height:auto"/></figure>
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
<p>For this example, turn off email collection and “Limit to 1 response.” Enabling the limit requires Google sign-in. Keep “View results summary” off because it exposes full written answers to people who can respond. See <a href="https://support.google.com/docs/answer/2839588?hl=en" style="color: #0000ff; text-decoration: underline;">Google’s official publishing and sharing guide</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>With these settings, you can’t reliably tell if someone answered twice. <mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Report the number of submissions you received.</mark> Whether a sign-in is required also depends on who has access, so try opening the form under the same conditions as your respondents.</p>
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
<p>The first 10–20 submissions can be a chance to revise your questions. Look for answers from the people you meant to reach and for details about what happened. <mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">Treating the response count alone as proof of demand is a mistake.</mark></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Organize counts and stories, then choose one app idea"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Organize counts and stories, then choose one app idea</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":268,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-sort-ideas.jpg" alt="A person grouping survey counts and experience cards by similar difficulties and choosing one idea" class="wp-image-268" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Review the summary under “Responses” and save answers to Google Sheets if useful. Check permissions separately for the form and sheet. At the end of the retention period, check and delete retained answers in both places: deleting one file does not delete the other. See <a href="https://support.google.com/docs/answer/2917686?hl=en" style="color: #0000ff; text-decoration: underline;">Google’s official guide to response storage and deletion</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Decide in advance what to do with ineligible responses, blanks, and conflicting choices. “I had no difficulty” tells you something about who can get by with their current tools. <mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">Keeping only answers that suit your idea will skew what you see.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">State the denominator and distinguish submissions from people</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>In a fictional example, suppose 16 of 20 submissions meet the borrowing criterion, all 16 answer question 3, and seven select “Forgot to bring the item.” Report <strong>“7 of 16 eligible submissions answering question 3.”</strong> Because multiple choices are allowed, totals across options may exceed 16.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If someone leaves question 3 blank, keep that submission out of the count for that question and record it separately. <mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Count “No difficulty” only when someone actually selects it.</mark> If you mainly asked people you know, the results describe the submissions you received.</p>
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
<p>The idea with the most responses doesn’t have to be the one you build. Compare the burden, frequency, what remains difficult, and what you could test on a small scale. A concrete situation and someone willing to try a fix give you a place to start.</p>
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

<!-- wp:image {"id":269,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-existing-tools-1.jpg" alt="A person comparing a paper note, calendar, and phone task list beside borrowed books" class="wp-image-269" style="width:100%;height:auto"/></figure>
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
<p>Google Tasks supports adding details and dates or times. See <a href="https://support.google.com/tasks/answer/7675838?hl=en" style="color: #0000ff; text-decoration: underline;">Google’s official guide to adding and editing tasks</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Use the same fictional return plans to compare fit, setup effort, ease of use, cost, data handling, and continued use. Check costs for the features and plan you need. Check where information is stored and who can see it; even paper notes may be visible to others depending on where you leave them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If a calendar already does the job, you have a solution. Consider building when there’s a step you can name and reduce, such as checking separate screens for the date, item, and place every time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This idea suits people who can record items and check a screen before leaving. A list alone will not help someone whose main difficulty is remembering to look at the screen. Reconsider the prompt to check before building.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Turn the selected idea into an app that supports one task"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading -->
<h2 class="wp-block-heading">Turn the selected idea into an app that supports one task</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":270,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-small-app.jpg" alt="A person sketching a small app limited to an item, return location, date, and completion action" class="wp-image-270" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Try to include every request and it gets hard to tell what the app is meant to test. <strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">Write down who should be able to do what, and when, in one sentence.</mark></strong> Return to it whenever you’re unsure about adding a feature.</p>
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
<p>Sketch a screen and ask where someone would enter an item or find today’s returns. Once the layout makes sense, make something that works using a visual builder, AI development assistance, or help from someone who builds apps.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">A request you can give to AI or someone helping you build</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<pre><code class="language-text">I want a small prototype for tracking borrowed items to return.
Users: People who know the return date but leave without the items.
Purpose: Show today’s items and return locations on one screen before leaving.

Required actions:
- Enter and save the item name, return location, and return date.
- View items due today.
- Edit entries and delete unwanted records.
- Mark an item returned and remove it from the outstanding list.

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

<!-- wp:image {"id":271,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-try-improve.jpg" alt="One person testing a borrowed-item list on a phone while another notes confusing steps for improvement" class="wp-image-271" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>A survey gives you people’s accounts and wishes. <mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">To see whether the app saves them work, watch someone try a working prototype.</mark> Ask a few willing participants to do the tasks below and let them find their way through.</p>
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
<p>Before asking “Was it convenient?”, note whether people finished, where they hesitated, whether they needed help, and how long it took. Compare similar tasks under similar conditions. Someone who has never seen the screen may need longer just to get their bearings.</p>
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
<p>Pick one problem and add a multiple-choice question and an open question to Google Forms. Use the answers to see how often it happens and understand why. Then test a small fix for the part people still struggle with.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><small>Google Forms and Google Tasks details reflect official help pages checked on October 12, 2026. Please check Google’s current documentation for the latest features.</small></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Related articles"},"className":"survey-app-panel panel-en","layout":{"type":"default"}} -->
<div class="wp-block-group survey-app-panel panel-en"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Related articles</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">No App Idea Yet? How to Build a Homemade App From One Person’s Problem</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color: #0000ff; text-decoration: underline;">How to Turn a Personal Problem into a Homemade App: From Finding an Idea to a Small Prototype</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/09/28/crowdsourcing-problems-to-app-ideas/" style="color: #0000ff; text-decoration: underline;">How to Find App Ideas on Crowdsourcing Sites: Collect, Group, and Validate Real Problems</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel --></div>
<!-- /wp:tab-panels --></div>
<!-- /wp:tabs -->