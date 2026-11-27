---
categories:
- 開発の裏側
excerpt: アプリやプログラムは機能が少ないほどよいのでしょうか。机の引き出し整理や本の返却メモを例に、使う人の迷いを減らしつつ安全や取り消し機能を守る設計の基準を整理しました。削ってよい項目と残すべき仕組みを、紙の画面と確認表で見分けられます。
featured_image: articles/images/simple-programs-products-for-kids/optimized/01-desk-bag-v2.jpg
featured_image_alt: 必要な道具が取り出しやすい整理された引き出しと、物が詰め込まれた引き出しを比べるイラスト
slug: simple-programs-products
status: publish
tags:
- 個人開発
- アプリ設計
- 初心者向け
title: アプリ設計はシンプルが正解？使いやすさと安全を両立する機能の絞り方
wordpress_featured_media_id: 253
wordpress_inline_media:
  01-desk-bag-v2.jpg:
    alt: 必要な道具が取り出しやすい整理された引き出しと、物が詰め込まれた引き出しを比べるイラスト
    id: 253
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-desk-bag-v2-1.jpg
  02-clear-steps-v2.jpg:
    alt: 返却確認・日付比較・通知を表す3枚のカードを矢印で順番に並べる大人のイラスト
    id: 254
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-clear-steps-v2.jpg
  03-simple-screen-v2.jpg:
    alt: 必要な情報だけのシンプルな画面案と、入力項目が多すぎる画面案を見比べる大人のイラスト
    id: 255
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-simple-screen-v2.jpg
  04-locker-safety-v2.jpg:
    alt: 使いやすい取っ手のあるロッカーと、内側で安全を守る鍵の仕組みを描いたイラスト
    id: 256
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-locker-safety-v2-1.jpg
  05-paper-test-v2.jpg:
    alt: 2人の大人が本の返却メモの紙画面モックを試し、操作と反応を確認するイラスト
    id: 257
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-paper-test-v2.jpg
wordpress_post_id: 100
wordpress_url: https://www.nanasinogonbei.com/blog/2026/11/02/simple-programs-products/
---

<!-- wp:html {"metadata":{"name":"画像・表・青色リンクの表示スタイル"}} -->
<style>
.simple-product-panel {box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere;}
.simple-product-panel a {color:#0000ff;text-decoration:underline;}
.simple-product-panel figure {max-width:100%;margin:1em 0;}
.simple-product-panel img {display:block;max-width:100%!important;height:auto!important;}
.simple-product-panel .wp-block-table {max-width:100%;overflow-x:auto;}
.simple-product-panel table {width:100%;border-collapse:collapse;}
.simple-product-panel th,.simple-product-panel td {border:1px solid #cbd5e1;padding:0.6em;text-align:left;vertical-align:top;}
</style>
<!-- /wp:html -->

<!-- wp:tabs {"activeTabIndex":0,"metadata":{"name":"日本語・English 切り替え"}} -->
<div class="wp-block-tabs"><!-- wp:tab-list -->
<div role="tablist" class="wp-block-tab-list"><button type="button" role="tab">日本語</button><button type="button" role="tab">English</button></div>
<!-- /wp:tab-list -->

<!-- wp:tab-panels -->
<div class="wp-block-tab-panels"><!-- wp:tab-panel {"label":"日本語","metadata":{"name":"日本語本文"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel" lang="ja"><!-- wp:group {"metadata":{"name":"ja: 導入"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:paragraph -->
<p>引き出しを軽くしたくて、仕事で使うノートやペンまで出してしまったら作業が進みません。プログラムやアプリも同じです。<strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">必要な働きや安全を残し、迷うところや余計な手間を減らす。</mark></strong> そのほうが、使う人にも作る人にも扱いやすくなります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>「プログラム」はコンピュータを動かす指示、「プロダクト」は人が使うために作ったものです。この記事では、普段使うアプリを題材に「削ってよい項目」と「残すべき安全の仕組み」の境目を整理します。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: プログラムやアプリのシンプルさは、数だけでは決まりません"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">プログラムやアプリのシンプルさは、数だけでは決まりません</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":253,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-desk-bag-v2-1.jpg" alt="必要な道具が取り出しやすい整理された引き出しと、物が詰め込まれた引き出しを比べるイラスト" class="wp-image-253" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>ノートやペンの間に、古いレシートや使わない鍵、絡まったケーブルが詰まっている机の引き出しを想像してみてください。いざメモを取りたいとき、欲しい物がすぐに出てきません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>不要な物を出し、よく使うノートとペンと充電ケーブルだけを取り出しやすく並べる。これなら仕事が進めやすい引き出しになります。でも、中身をすべて出して空っぽにしたら、メモも書けません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>引き出しを整えるときに見たいのは、何個減らせたかより、必要な道具を迷わず手に取れるかです。アプリでも、画面から減らした項目の数だけでは使いやすさは分かりません。</p>
<!-- /wp:paragraph -->

<!-- wp:table {"hasFixedLayout":false} -->
<figure class="wp-block-table"><table><thead><tr><th scope="col">どちらを見る？</th><th scope="col">分かりやすさの例</th></tr></thead><tbody><tr><td>作る人が読むプログラム</td><td>どの指示が何をしていて、どこを直せばよいか分かる。</td></tr><tr><td>使う人が触るアプリ</td><td>何を入力し、どこを押せば用事が済むか分かる。</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>使う人の操作が少なくても、裏側の処理まで少ないとは限りません。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: プログラムは「何をする手順か」が分かるようにします"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">プログラムは「何をする手順か」が分かるようにします</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":254,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-clear-steps-v2.jpg" alt="返却確認・日付比較・通知を表す3枚のカードを矢印で順番に並べる大人のイラスト" class="wp-image-254" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>プログラムに「本の返却を、いい感じにお知らせして」と曖昧に頼むことはできません。何を見て、どの条件のときに知らせるのかを、順番が追える形にする必要があります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>知らせてほしいのは、<strong>まだ返していない本のうち、返す日が今日か、それより前の本</strong>です。手元に残すのは、本の名前・返す日・返したかどうかの3項目です。日付が正しく入っていれば、1冊ずつ次の順で確かめられます。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>もう返した本なら、その本については知らせずに終わる。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>まだ返していない本なら、返す日と今日の日付を比べる。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>返す日が今日か、それより前なら「返す日を確認してください」と知らせる。未来の日なら、まだ知らせない。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>「返したか調べる」「日付を比べる」「知らせる」の3つが分かれていれば、動きを追いやすく、お知らせの文だけ変えたいときも、どこを直せばよいかすぐに分かります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">「返したか調べる」を省くと、返却済みの本までお知らせが来ます。</mark> <strong>短く書くことより、必要な条件が読み取れることが大事です。</strong> この例で決めたのは1回の確認で知らせるかどうかであり、通知する時刻や回数は別に考えます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>手順を順番に考える練習は、<a href="https://www.nanasinogonbei.com/blog/2026/10/27/programming-logical-thinking/" style="color:#0000ff;text-decoration:underline;">プログラミングに論理的思考力は必要？日常の例と紙でできる練習法を解説</a>でも、日常の例を使って説明しています。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: アプリは「用事が済むまでの迷い」を減らします"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">アプリは「用事が済むまでの迷い」を減らします</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":255,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-simple-screen-v2.jpg" alt="必要な情報だけのシンプルな画面案と、入力項目が多すぎる画面案を見比べる大人のイラスト" class="wp-image-255" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>使う人は、借りた本と返す日をあとで見られればひとまず困りません。そのために、どこまで入力してもらう必要があるでしょうか。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>記録するたびに、本の名前、返す日、出版社、ISBNコード、表紙の写真、星評価、読書メモまで毎回必須で入力するとしたらどうでしょう。返却日を控えたいだけなのに、書評を書き始めるような手間がかかります。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">最初に必須にする項目と後回しにする項目</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>本の名前と返す日を保存して、一覧で見られれば目的は果たせます。お知らせを出すなら「返却済み」の印も用意します。読書メモは書きたい人があとから足せる形にすれば、毎回入力せずに済みます。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>反対に、返す日を削ったら「いつ返せばいい？」に答えられません。何でも1画面に詰め込めば見やすくなるとも限らないので、<mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">使う人が用事を終えられるか</mark>を手がかりに判断します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>必要な情報は、使う人によって変わります。自分が借りた本だけを管理するなら借りた人の名前は省けても、図書館全体や家族で共有するなら「誰が借りたか」も必要です。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>そもそも、紙のメモや普段のカレンダーで忘れず返せているなら、それで十分です。家族と同じ一覧を見たいなど、今の方法で困ることが残ったらアプリを考えます。題材の絞り方は、<a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">自分の悩みから自作アプリを作る方法｜題材選びから小さな試作まで</a>につながります。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: アプリの安全を守る仕組みや、間違いを取り消す方法は残します"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">アプリの安全を守る仕組みや、間違いを取り消す方法は残します</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":256,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-locker-safety-v2-1.jpg" alt="使いやすい取っ手のあるロッカーと、内側で安全を守る鍵の仕組みを描いたイラスト" class="wp-image-256" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>ロッカーの扉は、取っ手を引くだけで開くと使いやすいですね。でも、「部品を減らそう」と鍵まで外したら、大事な荷物を守れなくなります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>アプリにも、画面には見えない鍵があります。他の人の記録を勝手に見られないようにする仕組みがその1つです。<mark style="background-color:#fef08a;color:#422006" class="has-inline-color">画面をすっきりさせても、記録を守る仕組みは必要です。</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>本の返却メモなら、次も確かめます。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>本の名前や返す日が空なら、保存する前に入力を求めるか。「2月30日」のような存在しない日付も見つけられるか。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>保存に失敗したら、「保存できた」と思い込ませない表示になるか。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>間違って消したとき、取り消せるか。取り消せないなら、消す前に確かめられるか。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>毎回の確認画面を減らして、消した直後に「元に戻す」を出す方法もあります。どちらが合うかは、消すデータの大切さと、本当に元に戻せるかで変わります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>使う人の操作を分かりやすくするために、作る側の仕事が増えることはあります。</strong>その場合も、裏側を何でも複雑にしてよいわけではありません。何のための仕組みかを説明でき、直す場所を追えるように整理します。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>シンプルにすれば、間違いが絶対になくなるわけでもありません。必要な働きが残っているか、実際に動かして確かめることが必要です。</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">削ってよい工夫と、残すべき安全の仕組み</h3>
<!-- /wp:heading -->

<!-- wp:table {"hasFixedLayout":false} -->
<figure class="wp-block-table"><table><thead><tr><th scope="col">見直す場所</th><th scope="col">最初に削ってよい例</th><th scope="col">残すべき働き・安全の仕組み</th></tr></thead><tbody><tr><td>入力項目</td><td>出版社や星評価など、なくても目的を果たせる項目</td><td>本の名前・返す日と、空欄や「2月30日」を防ぐ入力チェック</td></tr><tr><td>画面の見た目</td><td>飾りや細かい色分け設定、凝ったグラフ</td><td>保存失敗を伝える表示と、誤削除のやり直し・確認</td></tr><tr><td>裏側の処理</td><td>最初から大量の連携や複雑な自動化</td><td>他の人に記録を見られないようにするアクセス制御</td></tr></tbody></table></figure>
<!-- /wp:table --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: シンプルにできたかは、紙の画面と実際の動きで確かめます"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">シンプルにできたかは、紙の画面と実際の動きで確かめます</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":257,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-paper-test-v2.jpg" alt="2人の大人が本の返却メモの紙画面モックを試し、操作と反応を確認するイラスト" class="wp-image-257" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>「機能はいくつまで？」と数え始める前に、誰がどんな用事で画面を開くかを紙に書きます。本を1冊記録して、返す日を見つける流れだけを描けば始められます。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li><strong>誰の、どんな用事かを書く。</strong>例は「自分が、借りた本の返す日を確かめたい」です。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>必要な情報と画面を描く。</strong>本の名前、返す日、保存するボタン、保存した本の一覧を用意します。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>使う人に試してもらう。</strong>「本を1冊記録して、返す日を見つけてください」と頼み、どこで止まるかを見ます。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>止まった理由を1つずつ直す。</strong>ボタンの意味が不明なら名前を変えます。必要な情報がないなら足します。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>紙の画面で分かるのは、言葉や操作の分かりやすさです。<mark style="background-color:#fef08a;color:#422006" class="has-inline-color">保存やお知らせが本当に動くかは、アプリを作ってから確かめます。</mark> 入力の確認と、保存した本について知らせるかどうかは分けて試せます。</p>
<!-- /wp:paragraph -->

<!-- wp:table {"hasFixedLayout":false} -->
<figure class="wp-block-table"><table><thead><tr><th scope="col">確かめる場面</th><th scope="col">入力や本の状態</th><th scope="col">予想する結果</th></tr></thead><tbody><tr><td>保存する前</td><td>本の名前や返す日が空、または日付が存在しない</td><td>入力を直すよう伝え、そのまま保存しない。</td></tr><tr><td>保存した本を確認する</td><td>まだ返していない・返す日は今日</td><td>返す日を確認するよう知らせる。</td></tr><tr><td>保存した本を確認する</td><td>まだ返していない・返す日は昨日</td><td>返す日を確認するよう知らせる。</td></tr><tr><td>保存した本を確認する</td><td>まだ返していない・返す日は明日</td><td>まだ知らせない。</td></tr><tr><td>保存した本を確認する</td><td>もう返した・返す日は今日</td><td>知らせない。</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>試す相手がいなければ、時間を空けて自分で紙の画面をたどってみてください。他の人に使ってもらう代わりにはなりませんが、言葉や情報の抜けに気づく手がかりになります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>普段使っている道具を1つ思い浮かべて、「どこで迷ったか」「なくなると何が困るか」を書き出すところから始めてみてください。<strong>用事が済むこと、安全が守られること、あとから仕組みを追えること</strong>が、整理できたかを判断する基準になります。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 参考・出典"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">参考・出典</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="https://zenn.dev/nanashinogonbei/articles/should-programs-and-products-be-simple" style="color:#0000ff;text-decoration:underline;">もとになった記事「プログラム・プロダクトは、出来ればシンプルであるべきか？」（Zenn）</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.mozilla.org/ja/docs/Learn_web_development/Extensions/Forms/Form_validation" style="color:#0000ff;text-decoration:underline;">MDN：クライアント側フォーム検証（入力内容の確認）</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" style="color:#0000ff;text-decoration:underline;">OWASP：利用者のアクセス権限を確認するガイド</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 関連記事"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">関連記事</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/27/programming-logical-thinking/" style="color:#0000ff;text-decoration:underline;">プログラミングに論理的思考力は必要？日常の例と紙でできる練習法を解説</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/11/11/multiplatform-team-development/" style="color:#0000ff;text-decoration:underline;">Webとスマホアプリはどうつながる？バックエンド・画面の役割分担を図解</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">自分の悩みから自作アプリを作る方法｜題材選びから小さな試作まで</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel -->

<!-- wp:tab-panel {"label":"English","metadata":{"name":"English body"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel" lang="en"><!-- wp:group {"metadata":{"name":"en: Introduction"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:paragraph -->
<p><strong>Should App Design Always Be Simple? Balancing Usability, Safety, and Feature Scope</strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Empty your desk drawer of the notebook and pen you actually work with, and you won’t be able to get anything done. The same goes for programs and apps. <strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">Keep the features and protections people need, and remove the places they get stuck or waste time.</mark></strong> That makes things easier for both the people who use them and the people who build them.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>A “program” is a set of instructions for a computer. A “product” is something made for people to use. Using everyday apps as examples, this guide draws the line between items you can cut and safeguards you need to keep.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Simplicity in programs and apps is not just about quantity"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">Simplicity in programs and apps is not just about quantity</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":253,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-desk-bag-v2-1.jpg" alt="A neatly organized desk drawer holding a notebook, pen, and coiled cable beside an overstuffed drawer tangled with cords, keys, and old receipts" class="wp-image-253" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Picture a desk drawer crammed with old receipts, spare keys, and tangled cables wedged around your notebook and pen. When you need to jot something down, finding what you need takes effort.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Taking out unused clutter and arranging just your notebook, pen, and charger makes the drawer practical for work. Emptying it completely, however, leaves you without tools.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>When tidying a drawer, what matters is whether you can reach the tools you need without hesitation. Counting how many items you removed from an app tells you little about how easy it is to use, either.</p>
<!-- /wp:paragraph -->

<!-- wp:table {"hasFixedLayout":false} -->
<figure class="wp-block-table"><table><thead><tr><th scope="col">What are we looking at?</th><th scope="col">What clarity looks like</th></tr></thead><tbody><tr><td>The program a maker reads</td><td>It is clear what each instruction does and where a change belongs.</td></tr><tr><td>The app a person uses</td><td>It is clear what to enter and what to press to finish the task.</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>Fewer steps for the user do not necessarily mean less work behind the scenes.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Make it clear what each step in a program does"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">Make it clear what each step in a program does</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":254,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-clear-steps-v2.jpg" alt="An adult arranging three workflow cards connected by arrows for return check, calendar comparison, and reminder" class="wp-image-254" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>You cannot tell a program, “Please handle book returns nicely.” You need clear steps that specify what to check and when to send a reminder.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Instead, we decide to <strong>send a reminder for books that have not been returned and whose return date is today or earlier.</strong> We store three items for each book: its title, return date, and whether it has been returned. Assuming valid dates are saved, check each book in order.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>If the book has already been returned, finish checking that book without sending a reminder.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>If it has not been returned, compare its return date with today’s date.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>If the return date is today or earlier, say “Please check the return date.” If the date is in the future, do not send a reminder yet.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Check whether the book was returned, compare dates, then send the reminder. Separating those three roles makes the flow easy to trace and the reminder wording easy to update.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">Skip the returned-book check and the system will send reminders about books you already returned.</mark> <strong>The rules need to be clear enough to read again later.</strong> This example decides whether to send a reminder during one check; when and how often checks run are separate decisions.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For more practice planning steps, <a href="https://www.nanasinogonbei.com/blog/2026/10/27/programming-logical-thinking/" style="color:#0000ff;text-decoration:underline;">Why Logical Thinking Matters in Programming: Everyday Examples and Paper Practice</a> uses everyday examples too.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Help people finish their task with less confusion"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">Help people finish their task with less confusion</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":255,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-simple-screen-v2.jpg" alt="An adult comparing a clean phone mockup showing book, date, and save icons against an overloaded form screen" class="wp-image-255" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Someone using the app just wants to check a borrowed book and see when it’s due. How much do they really need to fill in for that?</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>What if every entry required the title, return date, publisher, ISBN, cover photo, star rating, and reading notes? You only wanted to track the due date, yet adding a book would feel like writing a full review.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What to require first vs. what to make optional</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Save the title and return date and show them in a list. If reminders exist, let people mark a book as returned. Anyone who wants to jot down reading notes can add them optionally later, without making it a required step every time.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Remove the due date and people can’t tell when the book must go back. Cramming everything onto one screen can make things harder to read, too. Look at <mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">whether the person can finish the task</mark>.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>The information needed depends on who uses the app. A personal list may not need a borrower’s name, whereas a shared household or library list needs to track who borrowed each book.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>If a paper note or calendar already helps you return books on time, that is enough. Consider an app when a gap remains, such as sharing the same list with family. For narrowing down a problem to solve, see <a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">How to Turn a Personal Problem into a Homemade App: From Finding an Idea to a Small Prototype</a>.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Keep app protections and ways to undo mistakes"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">Keep app protections and ways to undo mistakes</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":256,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-locker-safety-v2-1.jpg" alt="A storage locker with a simple handle and an internal lock mechanism inspected by a maker" class="wp-image-256" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>A locker is easy to use when you can open the door by pulling a single handle. Yet removing its lock just to reduce the number of parts would leave your belongings unprotected.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Apps have locks you don’t see on the screen, such as protections that stop someone else from viewing your records. <mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Keep those protections even as you make the screen less crowded.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>For our book-return list, we should also check these points.</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li>Does the app ask for a missing book title or return date before saving? Does it also catch dates that do not exist, such as February 30?</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>If saving fails, does the screen avoid making the user think it succeeded?</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Can an accidental deletion be undone? If it cannot, can the user confirm before deleting?</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>One alternative to asking for confirmation every time is offering “Undo” right after deletion. Which fits better depends on what you’re deleting and whether you can reliably restore it.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Making an app easier to use can mean more work for its maker.</strong> That does not mean anything goes behind the scenes. Each part should have an explainable purpose, and makers should be able to trace where a change belongs.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Simplicity does not guarantee zero mistakes. You still need to run the app and verify that its required protections and features work.</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">What you can simplify vs. protections you should keep</h3>
<!-- /wp:heading -->

<!-- wp:table {"hasFixedLayout":false} -->
<figure class="wp-block-table"><table><thead><tr><th scope="col">Area to review</th><th scope="col">Safe to leave out at first</th><th scope="col">Behaviors and protections to keep</th></tr></thead><tbody><tr><td>Input fields</td><td>Publisher, star ratings, or fields unnecessary for the task</td><td>Title, return date, and checks blocking blank entries or “February 30”</td></tr><tr><td>Screen layout</td><td>Decorative styling, custom color themes, or extra charts</td><td>Clear save-failure errors and confirmation or Undo before deletion</td></tr><tr><td>Behind the scenes</td><td>Large integrations or complex automation on day one</td><td>Access checks preventing other users from viewing your records</td></tr></tbody></table></figure>
<!-- /wp:table --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Check simplicity with paper screens and the working app"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">Check simplicity with paper screens and the working app</h2>
<!-- /wp:heading -->

<!-- wp:image {"id":257,"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none"} -->
<figure class="wp-block-image size-full is-resized"><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-paper-test-v2.jpg" alt="Two adults testing paper smartphone mockups for a book-return list and recording notes" class="wp-image-257" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Before counting features, write down who opens the app and what they came to do. Recording one book and finding its due date is enough to start sketching on paper.</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li><strong>Write who needs to do what.</strong> For example: “I want to check when I must return a borrowed book.”</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Draw the information and screens needed.</strong> Include the book’s title, return date, a save button, and a list of saved books.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Ask someone to try it.</strong> Say “Please record one book and find its return date,” then watch where they get stuck.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Address one cause at a time.</strong> Rename a button if its meaning is unclear. Add information if something needed is missing.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Paper is good for spotting unclear words or controls. <mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Try saving and reminders in the working app before you count on them.</mark> You can test input validation separately from the rule that sends reminders for saved books.</p>
<!-- /wp:paragraph -->

<!-- wp:table {"hasFixedLayout":false} -->
<figure class="wp-block-table"><table><thead><tr><th scope="col">Stage being checked</th><th scope="col">Input or book’s state</th><th scope="col">Expected result</th></tr></thead><tbody><tr><td>Before saving</td><td>The book’s title or return date is missing, or the date does not exist</td><td>Ask for corrected input and do not save it as is.</td></tr><tr><td>Checking a saved book</td><td>Not returned; return date is today</td><td>Ask the user to check the return date.</td></tr><tr><td>Checking a saved book</td><td>Not returned; return date was yesterday</td><td>Ask the user to check the return date.</td></tr><tr><td>Checking a saved book</td><td>Not returned; return date is tomorrow</td><td>Do not send a reminder yet.</td></tr><tr><td>Checking a saved book</td><td>Already returned; return date is today</td><td>Do not send a reminder.</td></tr></tbody></table></figure>
<!-- /wp:table -->

<!-- wp:paragraph -->
<p>If nobody is available to try it, step away for a bit and walk through the paper screens yourself. It won’t replace watching another person try it, yet it helps catch unclear wording or missing fields.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Pick a tool you use regularly and write down where you hesitate and what you’d miss if it disappeared. <strong>Can you finish the task? Are you protected? Could the person maintaining it follow what happens?</strong> Those questions help you judge whether you’ve simplified well.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Sources and references"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Sources and references</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="https://zenn.dev/nanashinogonbei/articles/should-programs-and-products-be-simple" style="color:#0000ff;text-decoration:underline;">Original Zenn article: “Should Programs and Products Be Simple When Possible?” (in Japanese)</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation" style="color:#0000ff;text-decoration:underline;">MDN: Client-side form validation</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html" style="color:#0000ff;text-decoration:underline;">OWASP Authorization Cheat Sheet</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Related articles"},"className":"simple-product-panel","layout":{"type":"default"}} -->
<div class="wp-block-group simple-product-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Related articles</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/27/programming-logical-thinking/" style="color:#0000ff;text-decoration:underline;">Why Logical Thinking Matters in Programming: Everyday Examples and Paper Practice</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/11/11/multiplatform-team-development/" style="color:#0000ff;text-decoration:underline;">How Web and Mobile Apps Work Together: Separating Backend and Frontend Roles</a></li>
<!-- /wp:list-item -->
<!-- wp:list-item -->
<li><a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color:#0000ff;text-decoration:underline;">How to Turn a Personal Problem into a Homemade App: From Finding an Idea to a Small Prototype</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel --></div>
<!-- /wp:tab-panels --></div>
<!-- /wp:tabs -->