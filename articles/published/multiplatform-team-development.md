---
categories:
- 開発の裏側
excerpt: 家のパソコンで保存した記録を、外出先のスマホでも見るにはどう作ればよいのか。図書館の窓口と裏方のたとえで、バックエンド・Web・スマホアプリの役割分担やAPIの約束、段階的な更新方法まで初心者向けに分かりやすく整理しました。
featured_image: articles/images/multiplatform-team-development/01-three-roles-v2.png
featured_image_alt: 1つの台帳を管理する図書館の司書と、パソコン・スマートフォンで同じ本の記録を見る2人の大人のイラスト
slug: multiplatform-team-development
status: publish
tags:
- マルチプラットフォーム開発
- アプリ設計
- チーム開発
title: Webとスマホアプリはどうつながる？バックエンド・画面の役割分担を図解
wordpress_featured_media_id: 137
wordpress_inline_media:
  01-three-roles-v2.png:
    alt: 1つの台帳を管理する図書館の司書と、パソコン・スマートフォンで同じ本の記録を見る2人の大人のイラスト
    id: 137
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-three-roles-v2.png
  02-message-cards-v2.png:
    alt: スマートフォンを持つ大人が窓口越しに司書へ本とカレンダーのカードを渡し、別の大人がパソコンで同じ記録を見るイラスト
    id: 138
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-message-cards-v2.png
  03-team-workbench.png:
    alt: 台帳・パソコン・スマホを担当する3人が、共通の絵カードを囲んで作業を進めるイラスト
    id: 105
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/multiplatform-team-development-03-team-workbench.png
  04-test-and-update.png:
    alt: パソコン・古いスマホ・新しいスマホの表示を、台帳とチェック用の紙で確かめるイラスト
    id: 106
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/multiplatform-team-development-04-test-and-update.png
  05-choose-small-v2.png:
    alt: Webだけの小さな構成と、裏方・Web・モバイルが連携する構成を見比べる大人開発者のイラスト
    id: 152
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-choose-small-v2.png
  06-paper-first-step-v2.png:
    alt: パソコン・台帳・スマホを描いた3枚の紙を机に並べてカードを渡す2人の大人のイラスト
    id: 153
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-paper-first-step-v2.png
wordpress_post_id: 109
wordpress_url: https://www.nanasinogonbei.com/blog/2026/11/11/multiplatform-team-development/
---

<!-- wp:html {"metadata":{"name":"画像・表・青色リンクの表示スタイル"}} -->
<style>
.mpt-panel,.mpt-subsection {box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere;}
.mpt-panel a {color:#0000ff;text-decoration:underline;}
.mpt-panel figure {max-width:100%;margin:1em 0;}
.mpt-panel img {display:block;max-width:100%!important;height:auto!important;}
.mpt-table-scroll {max-width:100%;overflow-x:auto;}
.mpt-panel table {width:100%;border-collapse:collapse;}
.mpt-panel caption {text-align:left;font-weight:bold;padding:0.5em 0;}
.mpt-panel th,.mpt-panel td {border:1px solid #cbd5e1;padding:0.6em;text-align:left;vertical-align:top;}
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
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel" lang="ja">
<!-- wp:group {"metadata":{"name":"ja: 導入"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:paragraph -->
<p>家のパソコンで借りた本の返却日を登録し、外出先でスマホから確認する。<strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">画面は端末に合わせ、記録を管理する仕組みは共通にする</mark></strong>と、こうした使い方ができます。Web版やスマホアプリなど、複数の環境に対応するサービスを作るのが、マルチプラットフォーム開発です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>図書館なら、窓口と裏方にどんな仕事を任せるでしょうか。役割の決め方から、チームでつないで試すところまで、「本の返却メモ」を架空の例にして紙でもたどれる形で整理します。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: バックエンド・Webフロントエンド・モバイルの役割を図書館で考える"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">バックエンド・Webフロントエンド・モバイルの役割を図書館で考える</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":137,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-three-roles-v2.png" alt="1つの台帳を管理する図書館の司書と、パソコン・スマートフォンで同じ本の記録を見る2人の大人のイラスト" class="wp-image-137" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>対応する環境には、ブラウザで使うWeb版、iPhone向けアプリ、Android向けアプリなどがあります。使う場所が違っても、同じ本の記録を見られる仕組みを考えます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>図書館で、カウンターに聞いたときと検索端末で調べたときとで、借りている本が違っていたら困りますよね。アプリでも、入口は使う場所に合わせつつ、借りた本の記録や貸し出しの決まりはそろえておきたいところです。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>3つの役割を、図書館の仕事に置き換える</caption><thead><tr><th scope="col">役割</th><th scope="col">身近なたとえ</th><th scope="col">本の返却メモで担当すること</th></tr></thead><tbody>
<tr><td>バックエンド</td><td>記録を管理する裏方</td><td>本の名前や返す日を保存し、誰の記録か確かめる。</td></tr>
<tr><td>Webフロントエンド</td><td>ブラウザで使う窓口</td><td>入力欄や一覧を表示する。広い画面にも狭い画面にも合わせる。</td></tr>
<tr><td>モバイル</td><td>スマホに入れて使う窓口</td><td>指で押しやすい画面を作り、必要ならカメラなど端末の機能とつなぐ。</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>モバイルの画面も、使う人が触る部分という意味ではフロントエンドの仲間です。この記事では、担当を比べやすくするため「Webの画面」と「スマホに入れるアプリ」を分けて呼びます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>「スマホで見たい」なら、ブラウザでWeb版を開く方法もあります。専用アプリを作る場合も、iPhone版とAndroid版でプログラムの一部は共用できます。<mark style="background-color:#fef08a;color:#422006" class="has-inline-color">役割を分けることと、プログラムを全部別々に作ることは別の判断です。</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>利用者にとってのよさは、家ではパソコン、外ではスマホという使い分けができることです。ただし、同じ記録を見るには、同じ利用者として入り、共通の保存先を使う仕組みが必要です。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: Webとモバイルは、APIという共通の窓口で裏方とつながる"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Webとモバイルは、APIという共通の窓口で裏方とつながる</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":138,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-message-cards-v2.png" alt="スマートフォンを持つ大人が窓口越しに司書へ本とカレンダーのカードを渡し、別の大人がパソコンで同じ記録を見るイラスト" class="wp-image-138" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>パソコンで「旅行ガイドを11月20日までに返す」と登録すると、あとでスマホを開いたときにもさっきの記録が見えます。この間に、画面と裏方では次のやり取りが起きています。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>パソコンの画面で、本の名前と返す日を入力します。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>画面から裏方へ「この内容を保存して」と頼みます。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>裏方が利用者と入力内容を確かめ、その人の記録として保存します。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>保存が終わったという返事を受けて、画面に「保存しました」と出します。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>同じ利用者がスマホで一覧を読み込むと、裏方から受け取った記録を表示します。</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>図書館で本の名前を伝えると、返す日を教えてもらえます。プログラム同士にも、そんな決まったやり方でお願いと返事を交わす窓口があり、それが<strong>API</strong>です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ブラウザがお願いを送り、サーバーが返事をする基本的な流れは、<a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview" style="color:#0000ff;text-decoration:underline;">MDNのクライアントとサーバーの解説</a>でも確認できます。サーバーは、ここでは裏方のプログラムを動かすコンピュータです。</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"ja: 「何を渡すと、何が返るか」を先にそろえる"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">「何を渡すと、何が返るか」を先にそろえる</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>本の返却メモで決める、やり取りの約束の例</caption><thead><tr><th scope="col">場面</th><th scope="col">先に決めておくこと</th></tr></thead><tbody>
<tr><td>保存をお願いする</td><td>本の名前と返す日を渡す。利用者を確かめる方法もそろえる。</td></tr>
<tr><td>保存できた</td><td>どの記録を保存したか分かる印と、その内容を返す。</td></tr>
<tr><td>入力が足りない</td><td>何を直せばよいかを返し、未完成の記録は保存しない。</td></tr>
<tr><td>通信が途切れた</td><td>保存できたか不明だと伝え、通信が戻ったら一覧を読み直せるようにする。保存し直すときの重複対策も決める。</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>受け取った「11/20」と「20/11」が同じ日かどうか、書き方が混ざると判断しづらくなります。この例でやり取りする日付は「2026-11-20」のような年-月-日にそろえます。画面には「11月20日」と読みやすく表示すれば十分です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Webで使うAPIの説明を、同じ形式で残す方法の1つが「OpenAPI」です。<a href="https://spec.openapis.org/oas/v3.2.1.html" style="color:#0000ff;text-decoration:underline;">OpenAPIの公式仕様</a>に沿って書き残せるのは、何を渡し、何が返るかという約束です。保存などの処理は、その約束に合わせて実装します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>返事が届かなくても、裏方では保存が済んでいるかもしれません。</strong> 通信が戻ったときに、まず記録があるかを確認する必要があります。もう一度頼む場合に備え、同じお願いなら二重に作らない仕組みも欠かせません。詳しくは<a href="https://developer.mozilla.org/en-US/docs/Glossary/Idempotent" style="color:#0000ff;text-decoration:underline;">MDNの、同じ要求を繰り返したときの動作の解説</a>が参考になります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>同じ保存先を使うだけで、すべての画面がすぐに書き換わるとは限りません。</strong>この例は、一覧を読み直したときに最新の記録を取ってくる作りです。開いたままの画面も自動で変えたいなら、その仕組みを別に用意します。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: チーム開発では、役割とやり取りの約束を先に決める"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">チーム開発では、役割とやり取りの約束を先に決める</h2>
<!-- /wp:heading -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none","id":105} -->
<figure class="wp-block-image size-full"><img class="wp-image-105" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/multiplatform-team-development-03-team-workbench.png" alt="台帳・パソコン・スマホを担当する3人が、共通の絵カードを囲んで作業を進めるイラスト"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>3人がそれぞれ違う貸し出しルールで図書館の仕組みを作ったら、最後につないだときに食い違います。分担の前にすり合わせたいのは、<mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">誰が何をできればよいかと、画面と裏方が何をやり取りするか</mark>です。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>目的を1つ決める。例は「外出先で、借りた本の返す日を確認できること」です。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>保存する情報と、APIでやり取りする内容を決める。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>裏方・Web・モバイルの担当を決める。1人で複数を受け持っても構いません。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>画面の担当は仮の返事で進め、裏方の担当は実際に保存する処理を作る。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>早めにつないで、「保存して別の端末で見る」ところまで試す。</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>裏方がまだできていないなら、決めておいた返事を返す代役があると画面を先に作れます。この代役が「モック」です。仮の返事で動いたあとには、実物同士をつなぐ番になります。</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"ja: ファイルの置き場所は、役割の分け方と別に選べる"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">ファイルの置き場所は、役割の分け方と別に選べる</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>プログラムなどのファイルと、変更の履歴をまとめて管理する場所を「リポジトリ」と呼びます。仕事道具を入れる箱だと考えると分かりやすいです。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>ファイルをまとめる方法と、分ける方法</caption><thead><tr><th scope="col">方法</th><th scope="col">イメージ</th><th scope="col">判断するポイント</th></tr></thead><tbody>
<tr><td>1つにまとめる（モノレポ）</td><td>1つの箱の中を、裏方・Web・モバイルの棚に分ける。</td><td>一度の変更をまとめて確認しやすい。同じ箱でも担当は分けられる。</td></tr>
<tr><td>別々に置く（マルチレポ）</td><td>役割ごとに別の箱を使う。</td><td>見られる人を箱ごとに分けやすい。共通の約束を変えるときは、複数の箱で調整が要る。</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>ファイルを同じ箱に置くか迷ったら、普段どれくらい一緒に直すか、管理を分ける事情があるかを手がかりに決めます。1つの箱に置いても、Web版だけ先に公開する運用はできます。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 作業用の枝は、直す内容ごとに作る"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">作業用の枝は、直す内容ごとに作る</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>変更履歴の本流から作業を分ける仕組みを「ブランチ」と呼びます。「本の名前を検索できるようにする」など、1つの目的ごとに枝を作り、動きを確かめてから本流へ戻す進め方ができます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>担当ごとの枝を長く離したままにすると、合わせたときの食い違いが増えがちです。小さく作って確認し、こまめに本流へ戻します。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 「保存して別の端末で見る」まで試し、更新で壊れないようにする"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">「保存して別の端末で見る」まで試し、更新で壊れないようにする</h2>
<!-- /wp:heading -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none","id":106} -->
<figure class="wp-block-image size-full"><img class="wp-image-106" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/multiplatform-team-development-04-test-and-update.png" alt="パソコン・古いスマホ・新しいスマホの表示を、台帳とチェック用の紙で確かめるイラスト"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>パソコンで保存ボタンを押したら、確認はもう一歩先まで見ます。<mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">同じ人がスマホで一覧を開いて、同じ本と返す日を見られるところまで</mark>が、この例で試したい流れです。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>架空の返却メモで、確かめたい場面</caption><thead><tr><th scope="col">試すこと</th><th scope="col">期待する結果</th></tr></thead><tbody>
<tr><td>パソコンで保存し、スマホで一覧を読み直す</td><td>同じ利用者の本の名前と返す日が見える。</td></tr>
<tr><td>返す日が空欄、または「2月30日」の状態で保存する</td><td>修正を求め、そのまま保存しない。画面だけでなく、裏方でも確かめる。</td></tr>
<tr><td>保存の途中で通信が切れ、その後に同じ保存をやり直す</td><td>成功を断定せず、通信が戻ったら確認できる。やり直しても同じ記録が二重にできない。</td></tr>
<tr><td>別の利用者として入る</td><td>ほかの人だけに許された記録を見たり変えたりできない。</td></tr>
<tr><td>以前のアプリから、新しくした裏方へつなぐ</td><td>対応を続けると決めた範囲の操作ができる。</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>それぞれの担当部分を調べる確認と、つないで一通り使う確認は、両方必要です。自動で繰り返せる確認もあります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>たとえば、<a href="https://docs.github.com/en/actions/get-started/understand-github-actions" style="color:#0000ff;text-decoration:underline;">GitHub Actionsの公式ガイド</a>では、変更を確認するときのテストなどを自動で実行できる仕組みが説明されています。自動の確認を用意しても、文字が読めるか、指で押しやすいかといった使い心地は別に確かめます。</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"ja: 新しい裏方は、古いアプリからも使える期間を考える"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">新しい裏方は、古いアプリからも使える期間を考える</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Web版の画面を更新する時期と、スマホに入れたアプリを利用者が更新する時期は、そろうとは限りません。App Storeにも更新を段階的に届ける仕組みがあります。詳しくは、Appleの<a href="https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/" style="color:#0000ff;text-decoration:underline;">段階的なバージョン更新の案内</a>で確認できます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>裏方が返す「本の名前」を「タイトル」に変えるところを考えてみます。<mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">古い項目をすぐ消すと、まだ「本の名前」を探すアプリは本を表示できなくなることがあります。</mark></p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>裏方が、しばらく「本の名前」と「タイトル」の両方を返すようにします。2つの項目には同じ値を入れます。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Web版とモバイル版を、「タイトル」の項目を読むように更新します。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>古いアプリの利用状況と対応期限を確認し、利用者へ案内してから「本の名前」の項目を返すのをやめます。</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>公開前には、試すための場所で古いアプリと新しいアプリの両方を確認します。問題が出たときに更新を戻せるか、保存済みの記録が失われないかも確かめます。</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 最初から3つに分けるかは、使う場面と増える手間で決める"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">最初から3つに分けるかは、使う場面と増える手間で決める</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":152,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-choose-small-v2.png" alt="Webだけの小さな構成と、裏方・Web・モバイルが連携する構成を見比べる大人開発者のイラスト" class="wp-image-152" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>画面だけ変えたいときに直す場所を見つけやすく、複数の窓口で同じ決まりを使いやすいのが、役割を分ける利点です。作るものが増えれば、組み合わせて試す手間も増えます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>「スマホでも見たい」だけなら、まずスマホで使いやすいWeb版を考えられます。</strong>専用アプリが本当に必要かは、使う場面を見て判断します。通知やカメラはWebでも使える場合があり、対応する端末やブラウザの確認が必要です。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>どこまで作るかを決める目安</caption><thead><tr><th scope="col">使う場面</th><th scope="col">考えられる始め方</th><th scope="col">注意すること</th></tr></thead><tbody>
<tr><td>自分が数冊の返す日を覚えたい</td><td>紙のメモや、今使っている予定表で試す。</td><td>既存の方法で足りるなら、自作しなくてもよい。</td></tr>
<tr><td>パソコンとスマホのブラウザで確認したい</td><td>画面の大きさに合わせて使えるWeb版から試す。</td><td>同じ利用者として入る方法と、情報の共有が必要。</td></tr>
<tr><td>スマホならではの操作を、繰り返し快適に使いたい</td><td>必要な操作を試し、専用アプリも検討する。</td><td>Webで足りない理由、配布・更新・保守の手間を確かめる。</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>複数の窓口を作る場合は、公開する場所の費用、使う道具や配布方法の費用、問い合わせへの対応も考えます。具体的な料金は選ぶサービスで違うため、契約前に公式情報を確かめます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>どこまで減らしてよいか迷うときは、<a href="https://www.nanasinogonbei.com/blog/2026/11/02/simple-programs-products/" style="color:#0000ff;text-decoration:underline;">アプリ設計はシンプルが正解？使いやすさと安全を両立する機能の絞り方</a>でも、必要な働きと安全を残して整理する考え方を説明しています。</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"ja: 裏方を共通にしても、安全や通信の問題は残る"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">裏方を共通にしても、安全や通信の問題は残る</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>裏方は、記録を読んだり変えたりするたびに、その利用者に許された操作かを確かめます。画面のボタンを隠すだけでは守れません。この考え方は、<a href="https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" style="color:#0000ff;text-decoration:underline;">OWASPのアクセス権限に関するガイド</a>でも示されています。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>また、端末が増えるほど、保存した情報やログイン状態をどこに残すかも重要になります。共用端末では使い終わったあとにログアウトし、どの情報を端末に残すかを決めておきます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>この例は通信できることが前提です。電波がないときにも使いたいなら、端末に一時保存する仕組みと、つながったときの合わせ方が必要です。パソコンとスマホで同じ記録を別々に直したら、どちらを残すかも決めます。<strong>共通の裏方を作るだけで、こうした問題がすべて解決するわけではありません。</strong></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: まず紙に3つの役割を描き、1つの操作を通してみる"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">まず紙に3つの役割を描き、1つの操作を通してみる</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":153,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-paper-first-step-v2.png" alt="パソコン・台帳・スマホを描いた3枚の紙を机に並べてカードを渡す2人の大人のイラスト" class="wp-image-153" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>保存する情報と扱い方の決まりは共通にし、使う人が触る画面はWebやスマホそれぞれに合わせます。いきなり全部を作る前に、まずは1つの操作を通すところから始めます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>最初はプログラムを書かず、紙とペンで次を試せます。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>「パソコンの画面」「裏方の台帳」「スマホの画面」の3枚を描きます。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>「旅行ガイド・11月20日まで」というカードを、パソコン側から裏方へ渡します。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>裏方役は、利用者と内容を確かめたつもりで台帳へ書き、保存できたと返事をします。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>スマホ側から同じ利用者の一覧を頼み、裏方が台帳を見て返事をします。</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>返す日が空欄のときや、途中で返事が届かないとき、画面で何を伝えるかも書きます。</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>紙でたどると、担当が決まっていない作業や、返事の決め忘れに気づけます。<mark style="background-color:#fef08a;color:#422006" class="has-inline-color">保存・通信・安全が本当に機能するかは、組み上がった実物で確認が必要です。</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>題材がまだ決まっていなければ、<a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">自分の悩み・困り事を自作アプリにする方法｜題材の見つけ方から小さな試作まで</a>から、日常の1つの不便を選んでみてください。<strong>まずは「誰が、どの窓口で、何を1つできればよいか」を書くことが、次の一歩です。</strong></p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"ja: 出典と、もう少し詳しく知るための資料"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">出典と、もう少し詳しく知るための資料</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>仕様に関する資料は2026年11月11日時点の公式情報をもとにしています。この記事の構成例や進め方は、資料を踏まえた説明用の提案です。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><a href="https://zenn.dev/nanashinogonbei/articles/multiplatform-team-development" style="color:#0000ff;text-decoration:underline;">元記事：バックエンド・フロントエンド・モバイルを分けるマルチプラットフォーム開発</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview" style="color:#0000ff;text-decoration:underline;">MDN：クライアントとサーバーのやり取り</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://spec.openapis.org/oas/v3.2.1.html" style="color:#0000ff;text-decoration:underline;">OpenAPI公式仕様：やり取りの窓口を記述する形式</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Idempotent" style="color:#0000ff;text-decoration:underline;">MDN：同じ要求を繰り返したときの動作</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://docs.github.com/en/actions/get-started/understand-github-actions" style="color:#0000ff;text-decoration:underline;">GitHub公式：GitHub Actionsと自動の確認</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/" style="color:#0000ff;text-decoration:underline;">Apple公式：アプリの更新を段階的に届ける</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" style="color:#0000ff;text-decoration:underline;">OWASP：利用者のアクセス権限を毎回確認する</a></li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 関連記事"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">関連記事</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/11/02/simple-programs-products/" style="color:#0000ff;text-decoration:underline;">アプリ設計はシンプルが正解？使いやすさと安全を両立する機能の絞り方</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">自分の悩み・困り事を自作アプリにする方法｜題材の見つけ方から小さな試作まで</a></li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->
</section>
<!-- /wp:tab-panel -->

<!-- wp:tab-panel {"label":"English","metadata":{"name":"English article"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel" lang="en">
<!-- wp:group {"metadata":{"name":"en: Introduction"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:paragraph -->
<p><strong>How Web and Mobile Apps Work Together: Separating Backend and Frontend Roles</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You save a book’s due date on your computer at home and check it on your phone later. <strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">The screens can suit each device while one backend keeps track of the records.</mark></strong> Building a service for several environments, such as the web and phone apps, is called multiplatform development.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What would you put at the counter of a public library, and what would you leave to the staff behind it? Using a fictional book-return memo, this guide walks through how to divide roles, coordinate as a team, and trace the flow on paper.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Backend, web frontend, and mobile: three roles in a library example"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Backend, web frontend, and mobile: three roles in a library example</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":137,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-three-roles-v2.png" alt="An adult librarian maintains one ledger while two adults view matching book and calendar information on a computer and a smartphone" class="wp-image-137" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Supported environments can include a web version in a browser, an iPhone app, and an Android app. The example explores how people can see the same book records through these different entrances.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Imagine getting two different lists of borrowed books depending on whether you ask at the library counter or look them up on a catalog terminal. The two entrances can work differently, but they need the same records and lending rules.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>Three software roles compared with library work</caption><thead><tr><th scope="col">Role</th><th scope="col">Everyday comparison</th><th scope="col">Job in the book-return memo</th></tr></thead><tbody>
<tr><td>Backend</td><td>The staff managing records behind the scenes</td><td>Save book titles and due dates, and check whose records they are.</td></tr>
<tr><td>Web frontend</td><td>A counter you use through a browser</td><td>Show input fields and lists. Adapt them to wide and narrow screens.</td></tr>
<tr><td>Mobile</td><td>A counter installed on a phone</td><td>Make controls comfortable to tap and connect to device features, such as the camera, when needed.</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>A mobile screen is also a frontend in the broader sense: it is something people interact with. This article distinguishes web screens from installed phone apps to make their responsibilities easier to compare.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you want to use a service on a phone, you can open its web version in a browser. If you do build apps, the iPhone and Android versions can share some code. <mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Separating responsibilities and writing every part independently are two different decisions.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The benefit for users is being able to use a computer at home and a phone outside. To see the same records, however, both need a way to recognize the same user and use a shared place to store information.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Web and mobile communicate with the backend through an API"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Web and mobile communicate with the backend through an API</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":138,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-message-cards-v2.png" alt="An adult holding a smartphone passes a book-and-calendar card through a library window to a librarian while another adult checks the same record on a laptop" class="wp-image-138" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>You save “Return the travel guide by November 20” on your computer. Later, the same record shows up on your phone. Here’s what happens between the screens and the backend.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>Enter the book title and due date on the computer screen.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>The screen asks the backend to save those details.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>The backend checks the user and the input, then saves it as that person’s record.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>The screen says “Saved” after receiving confirmation that saving has finished.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>When the same user loads the list on a phone, the phone displays records received from the backend.</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Tell a librarian the name of a book and they can tell you when it’s due. Programs have agreed ways to make requests and receive replies, too. One such interface is an <strong>API</strong>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The basic flow of a browser sending a request and a server responding is described in <a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview" style="color:#0000ff;text-decoration:underline;">MDN’s client–server overview</a>. Here, a server is a computer running the behind-the-scenes program.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"en: Agree on what to send and what comes back"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Agree on what to send and what comes back</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>Example communication agreements for the book-return memo</caption><thead><tr><th scope="col">Situation</th><th scope="col">What to agree on first</th></tr></thead><tbody>
<tr><td>Requesting a save</td><td>Send the book title and due date. Also agree on how to identify the user.</td></tr>
<tr><td>Saving succeeds</td><td>Return an identifier for the saved record and its contents.</td></tr>
<tr><td>Required input is missing</td><td>Explain what to correct and do not save the incomplete record.</td></tr>
<tr><td>The connection breaks</td><td>Explain that the result is uncertain and allow reloading after the connection returns. Also agree on how to prevent duplicates when saving again.</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Mix “11/20” with “20/11” and you have to work out whether they mean the same day. Here the programs exchange dates as year-month-day, like “2026-11-20.” The screen can still display “November 20.”</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>OpenAPI provides a standard format for describing APIs that use web communication. The <a href="https://spec.openapis.org/oas/v3.2.1.html" style="color:#0000ff;text-decoration:underline;">official OpenAPI specification</a> defines how to describe inputs and responses. Writing a description does not create saving behavior by itself: the actual program must follow the agreement, too.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>A missing response does not mean saving failed: the backend may already have saved the record.</strong> Check the state when the connection returns. If the save is retried, the system needs a way to recognize the same request and avoid creating a duplicate. See <a href="https://developer.mozilla.org/en-US/docs/Glossary/Idempotent" style="color:#0000ff;text-decoration:underline;">MDN’s explanation of the effect of repeated requests</a> for technical detail.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Using shared storage does not automatically update every open screen immediately.</strong> In this example, reloading the list retrieves the latest records. Automatically changing screens that are already open requires additional behavior.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: In team development, agree on responsibilities and communication first"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">In team development, agree on responsibilities and communication first</h2>
<!-- /wp:heading -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none","id":105} -->
<figure class="wp-block-image size-full"><img class="wp-image-105" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/multiplatform-team-development-03-team-workbench.png" alt="Three makers responsible for a ledger, a computer, and a phone coordinate around one shared reference card"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>If three people build parts of a library around different lending rules, the pieces won’t fit. Before splitting up the work, agree on <mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">who needs to do what and how the screens and backend will talk to one another</mark>.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>Choose one goal: for example, checking a borrowed book’s due date while away from home.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Agree on the information to store and exchange through the API.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Assign backend, web, and mobile responsibilities. One person can take more than one role.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Build screens using sample responses while the backend developer builds real saving behavior.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Connect the parts early and try saving on one device and reading on another.</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>If the backend isn’t ready, a substitute that gives the replies you’ve agreed on can let you build the screens. That substitute is called a mock. Once the real parts are ready, connect and test them together.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"en: Choose where files live separately from how responsibilities are divided"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Choose where files live separately from how responsibilities are divided</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A repository stores project files and their change history. Think of it as a box holding the work tools.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>Keeping files together or in separate places</caption><thead><tr><th scope="col">Approach</th><th scope="col">Everyday comparison</th><th scope="col">What to consider</th></tr></thead><tbody>
<tr><td>One repository: a monorepo</td><td>One box with separate shelves for backend, web, and mobile.</td><td>Related changes can be reviewed together. Responsibilities can still be distinct inside one box.</td></tr>
<tr><td>Multiple repositories: a multirepo</td><td>A separate box for each role.</td><td>Access can be controlled separately for each box. Shared agreements may require changes across several boxes.</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>To decide where to keep the files, ask how often you’ll change them together and whether you need to manage them separately. One repository can still let you release the web version first.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Create a working branch for a particular change"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Create a working branch for a particular change</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>A branch lets work diverge from the main line of change history. You can create a branch for one goal, such as adding book-title search, check the result, and merge it back.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Keeping separate working branches apart for too long can increase mismatches when they reconnect. Make small changes, check them, and merge them back frequently.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Test saving on one device and reading on another, then protect that flow during updates"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Test saving on one device and reading on another, then protect that flow during updates</h2>
<!-- /wp:heading -->

<!-- wp:image {"sizeSlug":"full","linkDestination":"none","id":106} -->
<figure class="wp-block-image size-full"><img class="wp-image-106" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/multiplatform-team-development-04-test-and-update.png" alt="Makers check a computer, an older phone, and a newer phone against a ledger and a paper checklist"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Once the save button works on the computer, go one step further. <mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">Open the list on a phone as the same user and check that the book and due date match.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>Situations to check in the fictional book-return memo</caption><thead><tr><th scope="col">What to try</th><th scope="col">Expected result</th></tr></thead><tbody>
<tr><td>Save on a computer, then reload the list on a phone.</td><td>The same user sees the book title and due date.</td></tr>
<tr><td>Try saving with an empty due date or an impossible date such as February 30.</td><td>The app asks for a correction and does not save it. The backend checks this as well as the screen.</td></tr>
<tr><td>Lose the connection during saving, then retry the same save.</td><td>The app does not claim success and allows checking when connectivity returns. Retrying does not create a duplicate record.</td></tr>
<tr><td>Sign in as a different user.</td><td>Records restricted to somebody else cannot be viewed or changed.</td></tr>
<tr><td>Connect an older app to the updated backend.</td><td>Operations still work within the support you have agreed to maintain.</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>Check individual parts and the complete connected journey. Some checks can also run automatically whenever relevant work changes.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For example, the <a href="https://docs.github.com/en/actions/get-started/understand-github-actions" style="color:#0000ff;text-decoration:underline;">official GitHub Actions guide</a> describes running automated tests as part of reviewing changes. Automated checks still leave usability questions to examine, such as readable text and comfortable tap targets.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"en: Allow time for older apps to work with the new backend"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Allow time for older apps to work with the new backend</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Updating a web screen and users updating their installed phone apps do not necessarily happen together. The App Store also supports phased updates; see <a href="https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/" style="color:#0000ff;text-decoration:underline;">Apple’s guide to phased version releases</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Suppose the backend changes “book name” to “title.” <mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">Remove the old field right away and apps that still look for “book name” may stop displaying it.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>Let the backend return both “book name” and “title” for a transition period, with the same value in both fields.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Update the web and mobile versions to read the “title” field.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Check usage of older apps and the support deadline, inform users, and only then stop returning the “book name” field.</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Before release, use a testing environment to check both old and new apps. Also check whether a problematic update can be rolled back without losing saved records.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Decide how far to separate things by the use case and the extra work"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Decide how far to separate things by the use case and the extra work</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":152,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-choose-small-v2.png" alt="An adult developer compares a small web-only setup with a coordinated backend, web, and mobile setup" class="wp-image-152" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>When roles are separate, it’s easier to see where a screen-only change belongs and keep the same rules across interfaces. More pieces also mean more combinations to test.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>If the need is simply “I want to see it on my phone,” consider a phone-friendly web version first.</strong> Decide whether a dedicated app is needed by looking at real use. Notifications and camera access can also be available on the web; check the devices and browsers you intend to support.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="mpt-table-scroll"><table><caption>A starting point for deciding what to build</caption><thead><tr><th scope="col">Use case</th><th scope="col">Possible starting point</th><th scope="col">What to check</th></tr></thead><tbody>
<tr><td>Remember due dates for a few books yourself.</td><td>Try paper notes or a calendar you already use.</td><td>If that works, you may not need a custom app.</td></tr>
<tr><td>Check records in computer and phone browsers.</td><td>Start with a web version that adapts to different screen sizes.</td><td>It still needs a way to recognize the same user and share information.</td></tr>
<tr><td>Repeatedly use a phone-specific interaction comfortably.</td><td>Try the interaction and consider a dedicated app.</td><td>Check what the web version cannot meet and the work of distribution, updates, and maintenance.</td></tr>
</tbody></table></div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p>When providing several interfaces, consider hosting, tools or distribution costs, and answering user questions. Prices depend on the services chosen, so check official information before committing.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For another perspective on keeping necessary behavior and safety while reducing complexity, see <a href="https://www.nanasinogonbei.com/blog/2026/11/02/simple-programs-products/" style="color:#0000ff;text-decoration:underline;">Should App Design Always Be Simple? Balancing Usability, Safety, and Feature Scope</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"en: A shared backend still needs access controls and a plan for lost connections"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">A shared backend still needs access controls and a plan for lost connections</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Whenever a record is read or changed, the backend must check that the user is allowed to perform that action. Hiding a button is not enough. This principle is also explained in the <a href="https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" style="color:#0000ff;text-decoration:underline;">OWASP authorization guide</a>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>More devices also mean thinking about where information and sign-in state remain. Sign out after using a shared device and decide what information the device should keep.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>This example assumes a working connection. Offline use needs temporary local storage and a plan for reconciling changes later. If a computer and a phone edit the same record independently, decide which change to keep. <strong>A shared backend alone does not solve all these problems.</strong></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Start with three paper roles and walk one action through them"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading -->
<h2 class="wp-block-heading">Start with three paper roles and walk one action through them</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":153,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-paper-first-step-v2.png" alt="Two adults pass a book-and-calendar card across three paper sheets for computer, ledger, and phone roles" class="wp-image-153" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Keep the stored information and its rules in common, and tailor the web and phone screens to how people use each device. Before building everything, walk one action through all three roles.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>You can start with paper and a pen before writing any code:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list">
<!-- wp:list-item -->
<li>Draw three sheets: a computer screen, the backend ledger, and a phone screen.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Pass a card saying “Travel guide — due November 20” from the computer role to the backend role.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>The backend role pretends to check the user and input, records it in the ledger, and confirms that it was saved.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>The phone role asks for the same user’s list, and the backend responds using the ledger.</li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li>Write what the screens should say if the due date is missing or a response never arrives.</li>
<!-- /wp:list-item -->
</ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Paper can show where no one owns a task or where you never agreed what reply should come back. <mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Test storage, networking, and security on the working system.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If you have not chosen a problem yet, <a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">How to Turn a Personal Problem into a Homemade App: From Finding an Idea to a Small Prototype</a> can help you choose one inconvenience. <strong>Your next step is to write who needs to do one thing, through which interface.</strong></p>
<!-- /wp:paragraph -->

<!-- wp:group {"metadata":{"name":"en: Sources and further reading"},"className":"mpt-subsection","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-subsection">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Sources and further reading</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Specification-related sources reflect official documentation checked on November 11, 2026. The architecture examples and workflow in this article are explanatory suggestions informed by those sources.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><a href="https://zenn.dev/nanashinogonbei/articles/multiplatform-team-development" style="color:#0000ff;text-decoration:underline;">Original article: Separating Backend, Frontend, and Mobile in Multiplatform Development (in Japanese)</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview" style="color:#0000ff;text-decoration:underline;">MDN: Client–server interactions</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://spec.openapis.org/oas/v3.2.1.html" style="color:#0000ff;text-decoration:underline;">Official OpenAPI specification: Describing interfaces</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Idempotent" style="color:#0000ff;text-decoration:underline;">MDN: The effect of repeated requests</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://docs.github.com/en/actions/get-started/understand-github-actions" style="color:#0000ff;text-decoration:underline;">GitHub: GitHub Actions and automated checks</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/" style="color:#0000ff;text-decoration:underline;">Apple: Releasing app updates in phases</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" style="color:#0000ff;text-decoration:underline;">OWASP: Checking access permissions on every request</a></li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Related articles"},"className":"mpt-panel","layout":{"type":"default"}} -->
<div class="wp-block-group mpt-panel">
<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Related articles</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list">
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/11/02/simple-programs-products/" style="color:#0000ff;text-decoration:underline;">Should App Design Always Be Simple? Balancing Usability, Safety, and Feature Scope</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">How to Turn a Personal Problem into a Homemade App: From Finding an Idea to a Small Prototype</a></li>
<!-- /wp:list-item -->
</ul>
<!-- /wp:list -->
</div>
<!-- /wp:group -->
</section>
<!-- /wp:tab-panel -->
</div>
<!-- /wp:tab-panels -->
</div>
<!-- /wp:tabs -->