---
categories:
- 課題と解決
excerpt: 自分の悩み・困り事から自作アプリを考える手順を紹介します。困った場面の記録、既存の道具との比較、最初に作る機能の決め方、AIへの依頼文、試作品の確かめ方を具体例で整理。プログラミング未経験でも、何を作り、何から試すかを決められます。
featured_image: articles/images/personal-problem-to-app/01-notice.png
featured_image_alt: 日常の困り事を振り返り、自作アプリの題材をノートへ書き留める人のイラスト
slug: personal-problem-to-app
status: publish
tags:
- 個人開発
- アプリ開発
- アイデア検証
title: 自分の悩み・困り事を自作アプリにする方法｜題材の見つけ方から小さな試作まで
wordpress_featured_media_id: 79
wordpress_inline_media:
  01-notice.png:
    id: 79
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/01-notice.png
  02-choose.png:
    id: 80
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/02-choose.png
  03-define.png:
    id: 81
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/03-define.png
  04-build.png:
    id: 82
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/04-build.png
  05-test.png:
    id: 83
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/05-test.png
  06-next.png:
    id: 84
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/06-next.png
wordpress_post_id: 85
wordpress_url: https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/
---

<!-- wp:html {"metadata":{"name":"本文・画像の表示スタイル"}} -->
<style>
.personal-app-panel {box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere;}
.personal-app-panel a {color:#0000ff;text-decoration:underline;}
.personal-app-panel figure {box-sizing:border-box;width:100%;max-width:100%;margin:1em 0;}
.personal-app-panel img {display:block;max-width:100%!important;height:auto!important;}
.personal-app-panel .table-scroll {max-width:100%;overflow-x:auto;}
.personal-app-panel table {width:100%;border-collapse:collapse;}
.personal-app-panel caption {text-align:left;font-weight:bold;padding:0.5em 0;}
.personal-app-panel th,.personal-app-panel td {padding:0.6em;border:1px solid #cbd5e1;text-align:left;vertical-align:top;}
.personal-app-panel pre {box-sizing:border-box;max-width:100%;white-space:pre-wrap;overflow-wrap:anywhere;padding:1em;background:#f3f6f8;}
</style>
<!-- /wp:html -->
<!-- wp:tabs {"activeTabIndex":0,"metadata":{"name":"日本語・English 切り替え"}} -->
<div class="wp-block-tabs">
<!-- wp:tab-list -->
<div role="tablist" class="wp-block-tab-list"><button type="button" role="tab">日本語</button><button type="button" role="tab">English</button></div>
<!-- /wp:tab-list -->
<!-- wp:tab-panels -->
<div class="wp-block-tab-panels">
<!-- wp:tab-panel {"label":"日本語","metadata":{"name":"日本語本文"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel">
<!-- wp:group {"metadata":{"name":"ja: 導入"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:paragraph -->
<p>自分の悩み・困り事を自作アプリにするには、<strong>困った場面を記録し、今の方法で残る手間を一つ選び、その手間を減らす試作品を作ります。</strong>まずは「誰にでも便利」より、自分の一つの作業が楽になることを目指します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>「何を作ればよいか分からない」「不便はあるけれど、アプリの形が浮かばない」という人向けに、題材の見つけ方から、自分で使って確かめるまでを紹介します。プログラミングの知識は前提にしません。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>日常の「探す・繰り返す・忘れる」をメモする。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>今の対処法を試し、それでも残る不便を選ぶ。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>何を入力し、何が分かればよいかを決める。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>小さく作り、実際に困る場面で使ってみる。</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>以下の記録・アプリ案・試す期間は、説明用の架空の例です。筆者が完成させたアプリや、実測した成果を示すものではありません。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 自分の困り事は「面倒だった瞬間」から見つける"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">自分の困り事は「面倒だった瞬間」から見つける</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":79} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-79" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/01-notice.png" alt="日常で探し直すことや忘れたことを振り返り、ノートへ困り事を書き留める人のイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>「自分には特別な悩みがない」と感じたら、少し面倒だった瞬間をメモしてみてください。記録する期間は、たとえば3日間です。週に一度の家事なら、その作業をする日も含めます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>見るのは、生活の中で手が止まった場面です。「買い物が面倒」より、「店に着いてから在庫が分からず、同じ物を買った」と書くと、変えたい部分が見えてきます。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><strong>探す：</strong>保存した記事や写真、連絡を毎回探し直している。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>繰り返す：</strong>同じ内容を何度も入力したり、別の場所へ書き写したりする。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>忘れる：</strong>締切や持ち物に、必要な場面で気づけない。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>迷う：</strong>候補はあるのに、比べる情報が散らばって決められない。</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 気持ちだけでなく、場面・対処法・残る不便を書く"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">気持ちだけでなく、場面・対処法・残る不便を書く</h3>
<!-- /wp:heading -->
<!-- wp:html -->
<div class="table-scroll"><table><caption>困り事メモの架空の記入例</caption><thead><tr><th scope="col">場面</th><th scope="col">困ったこと</th><th scope="col">今の対処法</th><th scope="col">残っている不便</th></tr></thead><tbody>
<tr><td>休憩中に記事を読みたい</td><td>未読の記事を見つけにくく、検索からやり直す</td><td>ブラウザのブックマークへ保存する</td><td>読み終えた記事と未読の記事が混ざる</td></tr>
<tr><td>買い物中に洗剤を買うか迷う</td><td>家に残っているか思い出せない</td><td>冷蔵庫に買い物メモを貼る</td><td>外出先ではメモを確認できない</td></tr>
<tr><td>外出直前に持ち物を確認する</td><td>前回も忘れた物をまた忘れる</td><td>出かけるたびに思い出す</td><td>行き先ごとの持ち物が決まっていない</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>便利な機能を思いついても、この段階では脇へメモするだけにします。「通知が欲しい」は解決案です。その前に、「何を、いつ思い出せなくて困るのか」を残してください。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>自分の記録は題材を選ぶ材料です。同じ悩みを多くの人が持つ証拠にはなりません。まずは自分が使う道具として考えます。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 題材は「負担・頻度・試しやすさ」で一つ選ぶ"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">題材は「負担・頻度・試しやすさ」で一つ選ぶ</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":80} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-80" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/02-choose.png" alt="紙のノート、スマートフォン、表形式の道具を比べ、取り組む困り事を一つ選ぶ人のイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>候補は、<strong>負担の大きさ・困る頻度・自分で試せるか</strong>の3点で比べます。頻繁に起きる小さな手間も、回数は少なくても負担の大きい作業も候補です。次に使う場面を思い浮かべられるものから選びます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>「休憩中に読みたい記事をすぐ開く」のように場面を限定すると、作る範囲と確かめ方を決めやすくなります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ここからは、<strong>保存した記事から、まだ読んでいないものを探しにくい</strong>という例を使います。ただし、読む時間がないこと自体が原因なら、整理用のアプリを作っても読書時間は増えません。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 自作する前に、今ある3つの方法を試す"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">自作する前に、今ある3つの方法を試す</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>保存記事を探す例では、次の3つが候補です。すでに使っている方法から試してください。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>既存の方法で試せることと確認する点</caption><thead><tr><th scope="col">方法</th><th scope="col">まず試すこと</th><th scope="col">合う場面・確かめたい点</th></tr></thead><tbody>
<tr><td>今使っているメモ</td><td>記事名とURLを一か所へまとめ、読んだら印を付ける</td><td>件数が少なく、手作業で整理できる人向け。増えたときも探せるかを見る</td></tr>
<tr><td>ブラウザのブックマーク</td><td>未読用のフォルダーを作り、読んだら移動する</td><td>普段のブラウザで完結したい人向け。移動する手間が気にならないかを見る</td></tr>
<tr><td>表に記録する方法</td><td>記事名・URL・読んだかどうかを列に分ける</td><td>一覧で管理したい人向け。利用する道具で絞り込みができるか、入力を続けられるかを見る</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>同じ記事を数件入れ、「保存する→未読を探す→開く→読んだ印を付ける」を試します。悩みへの合い方、始めやすさ、操作、続けやすさを比べてください。必要な機能の料金と、保存先・同期先・共有範囲も、使う道具の設定や公式案内で確認します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>既存の道具で解決するなら、自作する必要はありません。作る練習が目的なら、「悩みを減らせたか」と「作り方を学べたか」を分けて振り返ります。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 悩みを「入力・操作・結果」に置き換える"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">悩みを「入力・操作・結果」に置き換える</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":81} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-81" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/03-define.png" alt="保存する記事の入力、一覧で確認する操作、読んだ印を付ける結果を紙に整理するイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>自作する理由が残ったら、「どんなアプリか」よりも先に、「何を入れて、何をすると、何が分かるか」を決めます。記事の例なら、目標は<strong>休憩中に、まだ読んでいない記事を一つ開けること</strong>です。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>困り事から小さなアプリへ落とし込む架空の設計例</caption><thead><tr><th scope="col">項目</th><th scope="col">決める内容</th></tr></thead><tbody>
<tr><td>悩みそのもの</td><td>未読の記事が埋もれ、読みたいときに探し直してしまう</td></tr>
<tr><td>現在の対処法</td><td>ブックマークへ保存し、フォルダーで分ける</td></tr>
<tr><td>試しても残った不便という想定</td><td>自分には、読んだ記事を別のフォルダーへ動かす操作が続かなかった</td></tr>
<tr><td>入力</td><td>記事の名前とURL</td></tr>
<tr><td>操作</td><td>追加する、未読だけを見る、記事を開く、読んだ印を付ける</td></tr>
<tr><td>得られる結果</td><td>次に読む記事を同じ画面で選べる</td></tr>
<tr><td>作らないこと</td><td>自動で記事を集める、本文を保存する、要約する、他人と共有する</td></tr>
<tr><td>解決できない範囲</td><td>読む時間の確保、保存し忘れた記事の発見、リンク先の削除や変更</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>「残った不便」は、既存の道具を使った後に自分の経験で書き換えてください。上の例は、ブックマークが誰にとっても使いにくいという評価ではありません。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 最初は一つの作業が終わる範囲に絞る"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">最初は一つの作業が終わる範囲に絞る</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>「便利そうだから」と、通知・検索・共有を一度に足すと、どこを確かめたいのかがぼやけます。最初は「未読の記事を選んで開く」という一つの作業が最後までできれば十分です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ただし、入力間違いを直す、不要な記録を消すといった日常の操作も考えておきます。機能を減らした結果、困っていた作業が終わらないなら削りすぎです。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<pre><code class="language-text">私が困るのは、［いつ・どこで］です。
今は［対処法］を使っています。
それでも［具体的な手間］が残っています。
最初は［一つの作業］ができるアプリにします。
［入力する内容］を入れて、［操作］すると、［望む結果］が得られます。
今回は［作らない機能］を作りません。
［実際の場面］で使い、［変化を確かめる項目］を記録します。</code></pre>
<!-- /wp:html -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 紙の画面を描いてから、動く試作品を作る"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">紙の画面を描いてから、動く試作品を作る</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":82} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-82" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/04-build.png" alt="紙に描いた画面を見ながら、パソコンで小さな記事整理アプリを試作する人のイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>まず紙に、記事名とURLの入力欄、未読の記事一覧、「読んだ」ボタンを描きます。架空の3件を使い、指でたどって「追加から読了まで進めるか」を確かめます。この段階では、デザインを整える必要はありません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>画面の並びが決まったら、作成機能のあるAIや、開発を手伝ってくれる人へ依頼します。最初は自分の端末で試す方法を選び、公開や会員登録は後に回すと、確認する範囲を絞れます。作成サービスの料金や保存場所は、利用前に公式案内で確認してください。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: プログラミング未経験なら、AIに何を伝えればよい？"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">プログラミング未経験なら、AIに何を伝えればよい？</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p><strong>使う場面・今の対処法・残る不便・完成の条件</strong>を伝えます。次の依頼文を自分の状況に合わせて書き換えてください。会社資料や個人情報を含むURLは渡さず、架空の内容で作り始めます。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<pre><code class="language-text">自分だけで試す、小さな記事整理アプリを作りたいです。
プログラミングは未経験です。

困る場面：休憩中、保存した記事から未読のものを探し直してしまう。
今の方法：ブックマークのフォルダーで分けている。
残る不便：読んだ記事を移す操作が続かなかった、という想定です。
目的：未読の記事を選び、そのページを開けるようにする。
使う端末：［普段使う端末とブラウザを書く］
作成費用・毎月の費用の上限：［自分の予算を書く］

入力：記事名、URL。
必要な操作：追加、未読だけの表示、記事を開く、読了・未読の切り替え、修正、削除。
作らない機能：会員登録、共有、自動収集、本文保存、要約、通知。

まず不足している情報を質問し、回答を待ってください。
その後、画面の案と、動く試作品の作り方を提案してください。
可能なら、ブラウザで開ける1つのHTMLファイル
（画面の見た目と動きをまとめたファイル）にしてください。
保存して開く手順も、初めての人向けに説明してください。
その方式が使う端末で画面表示と記録の保存に対応できるかを分けて説明してください。
適さない場合は、理由と別の方法を提案してください。

完成の条件：
・架空の記事3件を追加し、未読だけを表示して、元のページを開ける。
・読了にした記事を、未読へ戻せる。
・修正と削除ができ、画面を閉じて開き直しても記録を確認できる。
・記録を予備のファイルへ書き出し、読み戻せる。
・保存先、消える条件、外部へ送る情報の有無を説明できる。
・記事名などの入力は文字として表示し、プログラムとして実行しない。
・URLとして正しく読み取れ、通信方式がhttp:またはhttps:のものだけを受け付ける。
  文字列の先頭だけで判定しない。
・これらの条件で、リンク先の安全性まで保証できるとは説明しない。
未確認の動作を「確認済み」とは書かないでください。</code></pre>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>試作品を受け取ったら、開く手順に沿って、一つずつ操作します。動かなければ、「どの端末で、何を押し、どうなったか」を伝えます。「うまくいかない」より、「追加した3件が、開き直したら消えた」のように書くと、直す場所を絞れます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>画面が動くことと、安全に使えることは別に確認します。判断できない部分は、詳しい人に見てもらってから大切な情報を入れてください。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 保存した記録が消えるのはなぜ？"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">保存した記録が消えるのはなぜ？</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p><strong>保存方法とブラウザの設定によっては、記録が残らないためです。</strong>ブラウザ内に記録を残す仕組み（localStorage）では、プライベートブラウズの終了やサイトデータの削除で記録が失われます。HTMLファイルを直接開く場合の保存動作も、ブラウザ間で保証されません。出典：<a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage" style="color: #0000ff; text-decoration: underline;">MDNのlocalStorage解説</a>（2026年10月21日確認）。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>試作時は、普段使う端末と通常のブラウザ画面で、閉じて開き直す操作を試します。予備のファイルへ書き出して読み戻せるかも確認してください。保存が安定しなければ、作る人に別の保存方法を相談します。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 実際に困る場面で使い、手間が減ったか確かめる"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">実際に困る場面で使い、手間が減ったか確かめる</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":83} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-83" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/05-test.png" alt="普段の休憩中にスマートフォンで保存記事を開き、使った時間や不便をノートに記録するイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>動いたら、普段の休憩で使ってみます。たとえば一週間を試用の区切りにし、期間中に何回その場面があったかも記録します。一週間たっても使う機会がなければ、良し悪しを急いで決める必要はありません。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>試用前後に残す記録の例（測定結果ではありません）</caption><thead><tr><th scope="col">見ること</th><th scope="col">記録する内容</th></tr></thead><tbody>
<tr><td>探す手間</td><td>未読の記事を開くまでの時間、迷った操作</td></tr>
<tr><td>入力の負担</td><td>保存するときの操作、途中でやめた理由</td></tr>
<tr><td>続けやすさ</td><td>使う機会があった回数、そのうち使った回数</td></tr>
<tr><td>記録の扱い</td><td>開き直した後の保存、書き出しと読み戻しの成否</td></tr>
<tr><td>解決できなかったこと</td><td>未読は見つかったが、読む時間がなかったなど</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>できるだけ似た条件で今の方法と比べます。速くなっても、保存の手間が増えて使わなくなれば、全体として楽になったとは言えません。数回の試用では、他の人にも同じ効果があるとは判断できない点も覚えておきます。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 使わなかった理由を見て、一か所ずつ直す"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">使わなかった理由を見て、一か所ずつ直す</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><strong>入力が面倒：</strong>記入項目を減らせるか、今の保存方法のほうが合うかを考えます。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>開くことを忘れる：</strong>使う場面で目に入る場所へ入口を置きます。それでも開かなければ、別の方法も試します。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>未読を見ても選べない：</strong>困り事が「探すこと」ではなく「優先順位を決めること」だった可能性があります。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>今の方法で十分だった：</strong>試作を止める判断もできます。残った不便を確かめられたことは、次の題材選びに使えます。</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>直したら、同じ場面でもう一度試します。一度にたくさん変えるより、何が役立ったかを確かめやすくなります。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 今日困ったことを一つ書き、小さく試す"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">今日困ったことを一つ書き、小さく試す</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":84} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-84" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/06-next.png" alt="困り事を一つ選び、観察する、形にする、試すという次の行動を決める人のイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>まずは、<strong>「今日困った場面／今の対処法／残った手間」</strong>を一行で書いてみてください。たとえば「休憩中、未読の記事が見つからない／ブックマークへ保存している／読んだ記事と混ざる」です。次の休憩では、未読用のフォルダーで解決するか試してみます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>自分の道具として続けられそうなら、同じ悩みを持つ人にも、最近困った場面を聞いてみます。聞き取りの進め方は、<a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">1人の困り事を自作アプリで解決する方法</a>にまとめています。複数の人へ質問を広げるなら、<a href="https://www.nanasinogonbei.com/blog/2026/10/12/survey-driven-app-ideas/" style="color: #0000ff; text-decoration: underline;">Googleフォームで自作アプリを考える方法</a>も参考になります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>他の人へ提供する前には、記録の閲覧範囲、削除や問い合わせへの対応、費用と保守を確認します。自分用の試作に加えて必要になる確認です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>自作が向くのは、今の道具で残る不便が具体的にあり、使いながら直す時間を取れる人です。すぐに解決したい人や、管理の手間を増やしたくない人は、既存の道具を使うほうが合う場合があります。</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->
</section>
<!-- /wp:tab-panel -->
<!-- wp:tab-panel {"label":"English","metadata":{"name":"English本文"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel">
<!-- wp:group {"metadata":{"name":"en: Introduction"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:paragraph -->
<p>To turn a personal frustration into an app, <strong>record a difficult moment, choose one task that remains awkward with your current tools, and build a small prototype to reduce that effort.</strong> Start with making one task easier for yourself rather than aiming for something useful to everyone.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This article is for people who cannot decide what to build, or who notice an inconvenience but cannot picture an app for it. It covers finding a problem, shaping a small solution, and trying it yourself. No programming knowledge is assumed.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>Note everyday moments of searching, repeating work, or forgetting.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Try your current tools and choose one inconvenience that remains.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Decide what to enter and what result you need.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Build something small and use it when the problem actually occurs.</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>The records, app idea, and trial periods below are fictional examples for explanation. They do not describe an app the author has completed or measured results.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Find personal problems in moments that felt inconvenient"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Find personal problems in moments that felt inconvenient</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":79} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-79" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/01-notice.png" alt="A person reviewing everyday moments of searching or forgetting and noting the difficulties in a notebook" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>If you feel you have no particular problem to solve, note moments of inconvenience. Three days is one possible recording period; for a weekly chore, include a day when you actually do it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Look for moments when your activity stalls. Instead of “shopping is annoying,” write “At the store, I could not remember what was left at home and bought a duplicate.” A specific moment makes the part you want to change clearer.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><strong>Searching:</strong> You keep looking again for saved articles, photos, or messages.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>Repeating:</strong> You enter the same information repeatedly or copy it between places.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>Forgetting:</strong> You do not notice a deadline or something to bring when it matters.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>Deciding:</strong> You have options, but the information needed to compare them is scattered.</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Record the situation, current workaround, and remaining difficulty"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Record the situation, current workaround, and remaining difficulty</h3>
<!-- /wp:heading -->
<!-- wp:html -->
<div class="table-scroll"><table><caption>Fictional entries in a personal problem log</caption><thead><tr><th scope="col">Situation</th><th scope="col">Difficulty</th><th scope="col">Current workaround</th><th scope="col">What remains awkward</th></tr></thead><tbody>
<tr><td>Reading an article during a break</td><td>I cannot easily find unread articles and search again</td><td>Save it in browser bookmarks</td><td>Read and unread articles get mixed together</td></tr>
<tr><td>Deciding whether to buy detergent</td><td>I cannot remember whether any is left at home</td><td>Put a shopping note on the refrigerator</td><td>I cannot check the note while away</td></tr>
<tr><td>Checking what to bring before leaving</td><td>I forget the same item again</td><td>Try to recall everything each time</td><td>I have no packing list for each destination</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>If a feature comes to mind, keep it as a separate note for now. “I want notifications” is a proposed solution. First record what you fail to remember and when that becomes a problem.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Your own records help you choose a topic. They do not prove that many other people have the same need. Start by considering a tool for yourself.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Choose one problem by burden, frequency, and ease of testing"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Choose one problem by burden, frequency, and ease of testing</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":80} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-80" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/02-choose.png" alt="A person comparing a notebook, a smartphone, and a table-based tool before choosing one problem to address" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>Compare ideas by <strong>the burden involved, how often the problem occurs, and whether you can try a solution yourself</strong>. Frequent small hassles and less frequent but burdensome tasks can both be candidates. Start with one whose next use you can picture.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A situation such as “open an article I want to read during a break” makes the scope and evaluation easier to define.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The running example is <strong>difficulty finding unread articles among saved links</strong>. If the underlying problem is having no time to read, however, an organizing app will not create reading time.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Try three existing approaches before building"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Try three existing approaches before building</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>For saved articles, consider these three approaches, starting with one you already use.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>Existing approaches to try and questions to check</caption><thead><tr><th scope="col">Approach</th><th scope="col">First experiment</th><th scope="col">When it may fit and what to check</th></tr></thead><tbody>
<tr><td>Your current notes tool</td><td>Keep article names and URLs together; mark each one after reading</td><td>Useful for a small collection you can organize manually. Check whether finding items remains manageable as it grows</td></tr>
<tr><td>Browser bookmarks</td><td>Create an unread folder and move articles after reading</td><td>Useful if you want to stay in your usual browser. Check whether moving items feels burdensome</td></tr>
<tr><td>A table-based record</td><td>Use columns for the article name, URL, and reading status</td><td>Useful if you prefer a list. Check whether your chosen tool can filter it and whether you keep entering items</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Enter a few of the same articles and try the sequence: save, find an unread item, open it, and mark it read. Compare fit, setup, operation, and ease of continued use. Also check the chosen tool’s settings and official guidance for the cost of needed features, storage, synchronization, and sharing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If an existing tool solves the problem, you do not need to build one. If your goal is practice, evaluate “Did I reduce the problem?” separately from “Did I learn how to build it?”</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Translate the problem into input, actions, and a result"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Translate the problem into input, actions, and a result</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":81} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-81" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/03-define.png" alt="A person planning the input, list actions, and read status of a small saved-article app on paper" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>If a reason to build remains, decide what you enter, what you do, and what result you get before choosing an app concept. In this example, the goal is <strong>to open one unread article during a break</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>A fictional plan for turning a problem into a small app</caption><thead><tr><th scope="col">Item</th><th scope="col">Decision</th></tr></thead><tbody>
<tr><td>The problem</td><td>Unread articles get buried, so I search again when I want to read</td></tr>
<tr><td>Current workaround</td><td>Save links in bookmarks and organize them into folders</td></tr>
<tr><td>Assumed difficulty after trying it</td><td>Moving read articles into another folder was not a habit I maintained</td></tr>
<tr><td>Input</td><td>Article name and URL</td></tr>
<tr><td>Actions</td><td>Add a link, show unread items, open an article, and mark it read</td></tr>
<tr><td>Useful result</td><td>Choose the next article to read on one screen</td></tr>
<tr><td>Leave out for now</td><td>Automatic collection, saving article text, summaries, and sharing</td></tr>
<tr><td>Outside its scope</td><td>Creating time to read, finding articles never saved, and preventing linked pages from changing or disappearing</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Replace the assumed remaining difficulty with your own experience after trying existing tools. This example does not claim bookmarks are inconvenient for everyone.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Keep enough functionality to finish one task"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Keep enough functionality to finish one task</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Adding notifications, search, and sharing just because they sound useful makes it harder to tell what you are testing. Start with a complete path for one task: choosing and opening an unread article.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Include everyday needs such as correcting a mistaken entry or removing an unwanted one. If cutting features prevents the original task from being completed, the scope is too small.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<pre><code class="language-text">I run into difficulty when [time and situation].
I currently use [workaround].
The remaining effort is [specific difficulty].
The first version will help me complete [one task].
I enter [input], do [action], and get [desired result].
I will leave out [features] for now.
I will use it during [real situation] and record [what to check].</code></pre>
<!-- /wp:html -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Sketch the screen before making a working prototype"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Sketch the screen before making a working prototype</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":82} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-82" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/04-build.png" alt="A person using a paper sketch to build a small saved-article app prototype on a laptop" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>Draw fields for the article name and URL, an unread list, and a “Read” button on paper. Use three fictional entries and trace the flow with your finger from adding an item to finishing it. There is no need to polish the design yet.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once the layout makes sense, ask an AI tool with app-building capabilities or someone who can help develop it. Starting with a method you can try on your own device, while leaving publishing and account registration for later, keeps the scope of checking smaller. Consult official guidance about service fees and storage before choosing a building service.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: What should a beginner tell AI or a developer?"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What should a beginner tell AI or a developer?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Describe <strong>the situation, current workaround, remaining difficulty, and acceptance conditions</strong>. Adapt the example below to your circumstances, starting with fictional information rather than company documents or URLs containing personal information.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<pre><code class="language-text">I want a small article organizer to try on my own.
I have no programming experience.

Situation: During breaks, I search again for unread articles I saved.
Current method: Bookmark folders.
Remaining difficulty: Assume I did not keep moving read articles between folders.
Goal: Choose an unread article and open its page.
Device: [My usual device and browser]
Budget for creation and monthly operation: [My limits]

Input: Article name and URL.
Actions: Add, show unread items, open, switch between read and unread, edit, delete.
Leave out: Accounts, sharing, automatic collection, article text storage, summaries, notifications.

First ask for missing information and wait for my answers.
Then propose a screen layout and a way to build a working prototype.
If suitable, provide one HTML file
(a file containing the screen layout and its behavior) that opens in a browser.
Explain how to save and open it for a first-time user.
Explain separately whether that method supports displaying the app
and saving records on my device. If unsuitable, explain why and suggest another method.

Acceptance conditions:
- Add three fictional entries, show unread items, and open the original pages.
- Mark a read article as unread again.
- Edit and delete entries, then close and reopen the screen to check saved records.
- Export records to a backup file and import them again.
- Explain the storage location, when records can disappear,
  and whether any information is sent externally.
- Display article names and other entered text without executing them as code.
- Parse the URL and accept it only if its protocol is http: or https:.
  Do not check only the beginning of the input string.
- Do not claim that these checks guarantee a safe destination.
Do not describe untested behavior as verified.</code></pre>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>When you receive a prototype, follow the opening instructions and check each action. If something fails, describe the device, what you pressed, and what happened. “The three entries disappeared after reopening” narrows the issue more clearly than “it does not work.”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Check safe operation separately from whether the screen works. Have someone knowledgeable review anything you cannot assess before entering important information.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Why might saved records disappear?"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Why might saved records disappear?</h3>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p><strong>Persistence depends on the storage method and browser settings.</strong> With localStorage, a mechanism that keeps records in the browser, closing private browsing or deleting site data removes records. Storage behavior when opening an HTML file directly is also not guaranteed across browsers. Source: <a href="https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage" style="color: #0000ff; text-decoration: underline;">MDN’s localStorage documentation</a> (checked October 21, 2026).</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>On your usual device in a normal browser window, close and reopen the prototype. Check that you can also export a backup and import it again. If storage is unreliable, ask your helper about another storage method.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Use it when the problem occurs and check whether effort falls"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Use it when the problem occurs and check whether effort falls</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":83} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-83" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/05-test.png" alt="A person opening saved articles during an ordinary break and recording time and difficulties in a notebook" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>Once it works, try it during your usual breaks. You might use a week as an initial trial period and note how often the relevant situation occurs. If there is no opportunity to use it that week, there is no need to rush a judgment.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>Example trial records to keep, not measured results</caption><thead><tr><th scope="col">What to check</th><th scope="col">What to record</th></tr></thead><tbody>
<tr><td>Searching effort</td><td>Time to open an unread article and actions that caused confusion</td></tr>
<tr><td>Entry burden</td><td>Steps needed to save an article and reasons for giving up midway</td></tr>
<tr><td>Continued use</td><td>Number of opportunities and how often you actually used the app</td></tr>
<tr><td>Record handling</td><td>Saving after reopening, and whether export and import succeeded</td></tr>
<tr><td>What remains unsolved</td><td>For example, finding an unread article but still having no time to read</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Compare with your previous method under similar conditions where possible. Faster searching does not make the whole process easier if saving becomes so tedious that you stop using it. A few personal trials also cannot show that other people will get the same benefit.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Look at why you skipped it and change one thing at a time"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Look at why you skipped it and change one thing at a time</h3>
<!-- /wp:heading -->
<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><strong>Entry is tedious:</strong> Consider reducing fields or returning to your existing saving method.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>You forget to open it:</strong> Put an entry point where you will see it during the relevant situation. Try another approach if you still do not open it.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>You cannot choose from the unread list:</strong> The real problem may be prioritizing rather than finding items.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><strong>Your previous method was sufficient:</strong> You can stop the prototype. Learning what inconvenience remains can help you choose your next topic.</li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>After a change, try the same situation again. Changing one thing at a time makes it easier to see what helped.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Write down one problem from today and try a small solution"},"className":"personal-app-panel","layout":{"type":"default"}} -->
<div class="wp-block-group personal-app-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Write down one problem from today and try a small solution</h2>
<!-- /wp:heading -->
<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":84} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-84" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/10/06-next.png" alt="A person choosing one difficulty and deciding the next steps of observing, shaping a solution, and trying it" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->
<!-- wp:paragraph -->
<p>Write one line using <strong>“today’s difficult moment / current workaround / remaining effort.”</strong> For example: “Cannot find an unread article during a break / save links in bookmarks / read and unread articles get mixed together.” At your next break, try an unread folder and see whether it solves the problem.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If the tool seems worth continuing for yourself, ask someone with a similar problem about a recent difficult moment. See <a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">How to Solve One Person’s Problem With a Homemade App</a> for an interview-based approach. To ask a wider group, <a href="https://www.nanasinogonbei.com/blog/2026/10/12/survey-driven-app-ideas/" style="color: #0000ff; text-decoration: underline;">How to Develop App Ideas With Google Forms</a> covers the next step.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Before providing the app to others, check access to records, handling of deletion and inquiries, costs, and maintenance. These are additional checks beyond a personal prototype.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Building your own tool may fit if a specific inconvenience remains and you have time to improve it as you use it. Existing tools may be a better fit if you need a solution immediately or do not want more maintenance work.</p>
<!-- /wp:paragraph -->

</div>
<!-- /wp:group -->
</section>
<!-- /wp:tab-panel -->
</div>
<!-- /wp:tab-panels -->
</div>
<!-- /wp:tabs -->