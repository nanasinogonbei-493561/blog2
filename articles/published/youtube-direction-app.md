---
categories:
- Build in Public
- 課題と解決
excerpt: 大きな市場で稼げそうという軽い気持ちで参加したYouTubeオフ会で、多くの人が「運営の方向性」に迷っていると知りました。自分の姿勢を反省し、悩みに優劣はないと学んだ経緯と、方向性を整理する自作アプリの構想、既存ツール3種の比較、今日試せる3行メモをまとめました。
featured_image: articles/images/youtube-direction-app/01-light-start.jpg
featured_image_alt: 大きな円グラフから切り出した小さな欠片とお金の丸を前に、動画アイコン付きのパソコンのそばで楽観的に考える大人のイラスト
slug: youtube-direction-app
status: publish
tags:
- YouTube運営
- 個人開発
- アプリ開発
- 運営方針
title: YouTubeの悩みを聞いてる内に、真剣に運営の方向性を定まるアプリを作りたくなった
wordpress_featured_media_id: 182
wordpress_inline_media:
  01-light-start.jpg:
    alt: 大きな円グラフから切り出した小さな欠片とお金の丸を前に、動画アイコン付きのパソコンのそばで楽観的に考える大人のイラスト
    id: 182
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-light-start.jpg
  02-meetup-direction.jpg:
    alt: 木のテーブルを囲んで真剣に話し合う4人の大人と、頭上に浮かぶ羅針盤や分かれ道の道標のイラスト
    id: 183
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-meetup-direction.jpg
  03-reflection.jpg:
    alt: 午後の窓辺で、羅針盤の線画が入った開いたノートを見つめながら静かに振り返る大人のイラスト
    id: 184
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-reflection.jpg
  04-existing-tools.jpg:
    alt: 動画分析画面、表計算シート、メモとタグの画面という3つの既存道具を同じ大きさで並べて比べるイラスト
    id: 185
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-existing-tools.jpg
  05-app-vision.jpg:
    alt: 羅針盤のカード、棒グラフとメモのカード、道標と進む道のカードの3枚が矢印でつながる構想イラスト
    id: 186
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-app-vision.jpg
  06-next-step.jpg:
    alt: 朝の机の上で3つの枠に分かれた白いノートを両手で開き、そばにマグカップとペンと羅針盤が置かれたイラスト
    id: 187
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-next-step.jpg
wordpress_post_id: 188
wordpress_url: https://www.nanasinogonbei.com/blog/2026/11/24/youtube-direction-app/
---

<!-- wp:html {"metadata":{"name":"本文・画像・表・青色リンクの表示スタイル"}} -->
<style>
.ytdir-panel {box-sizing:border-box;min-width:0;max-width:100%;overflow-wrap:anywhere;}
.ytdir-panel a {color:#0000ff;text-decoration:underline;}
.ytdir-panel .wp-block-image {box-sizing:border-box;width:100%;max-width:100%;margin:1em 0;}
.ytdir-panel .wp-block-image img {display:block;max-width:100%!important;height:auto!important;}
.ytdir-panel .table-scroll {max-width:100%;overflow-x:auto;}
.ytdir-panel table {width:100%;border-collapse:collapse;}
.ytdir-panel caption {text-align:left;font-weight:bold;padding:0.5em 0;}
.ytdir-panel th,.ytdir-panel td {padding:0.6em;border:1px solid #cbd5e1;text-align:left;vertical-align:top;}
</style>
<!-- /wp:html -->

<!-- wp:tabs {"activeTabIndex":0,"metadata":{"name":"日本語・English 切り替え"}} -->
<div class="wp-block-tabs"><!-- wp:tab-list -->
<div role="tablist" class="wp-block-tab-list"><button type="button" role="tab">日本語</button><button type="button" role="tab">English</button></div>
<!-- /wp:tab-list -->

<!-- wp:tab-panels -->
<div class="wp-block-tab-panels"><!-- wp:tab-panel {"label":"日本語","metadata":{"name":"日本語本文"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel"><!-- wp:group {"metadata":{"name":"ja: 導入"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:paragraph -->
<p>最初は「YouTubeは大きな市場だから、小さな隙間に絞ってアプリを作れば儲かりそう」という軽い気持ちで、所属しているオンラインコミュニティのYouTubeオフ会に参加しました。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>ところが、そこで色々な人の話を聞くうちに考えが変わります。<strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">多くの人に共通していたのは「運営の方向性」についての迷いであり、その悩みに上も下もないと気づいたことが、真剣に方向性を定める自作アプリを作ろうと決めたきっかけです。</mark></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>現時点でアプリはまだ構想段階のため、試用できる公開URL（サブドメイン付きページ）はありません。この記事では、軽い気持ちから反省を経て本気で開発に向き合うまでの経緯と、既存の道具3つでどこまで整理できるのか、今日から手元で試せる工夫をまとめました。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 1. 「大きな市場でニッチを狙えば儲かる」という軽い気持ちで始めた最初の一歩"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">1. 「大きな市場でニッチを狙えば儲かる」という軽い気持ちで始めた最初の一歩</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":182} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-182" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-light-start.jpg" alt="大きな円グラフから切り出した小さな欠片とお金の丸を前に、動画アイコン付きのパソコンのそばで楽観的に考える大人のイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>アプリ作りの題材を探していたとき、最初に目をつけたのがYouTubeの世界でした。見ている人も動画を出している人も非常に多く、大きな市場であることは明らかです。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>そこで頭によぎったのが、大きな市場の中でまだ大手があまり手をつけていない小さな困り事に絞って狙う考え方、いわゆる「ニッチ戦略」です。市場全体が大きければ、そのほんの一部の悩みを解決するアプリでも十分に儲かるはず。そんな打算から、「まずはYouTubeのことを知って、そのままアプリ開発に反映しよう」と考えました。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>現場の様子を知るため、自分が所属しているオンラインコミュニティのYouTubeオフ会に参加しました。当時の本音は、「ついでにみんなの悩みを聞いて、次のアプリ開発のネタにしよう」という気楽な気持ちでした。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">「大きな市場で隙間を狙えば儲かりそう」という計算だけで作り始めると、目の前で困っている人の実感から離れてしまい、本当に使われる形になりにくいと後から分かります。</mark> このときはまだ、その危うさに気づいていませんでした。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 2. オフ会で色々な人に聞いて分かった共通の悩みは「運営の方向性」"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">2. オフ会で色々な人に聞いて分かった共通の悩みは「運営の方向性」</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":183} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-183" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-meetup-direction.jpg" alt="木のテーブルを囲んで真剣に話し合う4人の大人と、頭上に浮かぶ羅針盤や分かれ道の道標のイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>オフ会で色々な参加者と話をしてみると、出している動画のジャンルも、チャンネルを続けている年数もさまざまでした。てっきり「編集ソフトの使い方」や「撮影機材の選び方」といった作業の質問が多いのだろうと予想していたのですが、実際に聞いてみると様子がまったく違いました。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">色々な人の話を聞いていくうちに浮かび上がった共通点は、運営の方向性について迷っている人が大半だったことです。</mark></strong></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 再生回数や編集の悩みも、たどると「方向性の迷い」につながっていた"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">再生回数や編集の悩みも、たどると「方向性の迷い」につながっていた</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>会話の入り口は人によって違っても、少し深掘りして話を聞いていくと、どれも同じ根っこに行き着きました。たとえば次のような迷いです。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>誰に届けたいのかがぶれてくる：</strong>最初は好きなテーマで始めたものの、途中で別の企画が伸びたため、「このまま同じ路線を続けるべきか、伸ばしやすい企画へ寄せるべきか」が決められない。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>数字を見ても次の行動が決まらない：</strong>再生回数や登録者の増減を眺めて一喜一憂はするけれど、「では次の1本は何を変えればいいのか」という判断に結びつかない。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>続けるか切り替えるかの目安がない：</strong>時間と気力をかけて動画を出しているのに手応えが薄いとき、「まだ我慢して続ける時期なのか、やり方を変えるタイミングなのか」を判断する材料がない。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>つまり、困り事の表面は「再生が伸びない」「企画が思いつかない」に見えても、その奥にはいつも「このチャンネルをどこへ向かわせるか」という運営の軸への迷いがありました。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: ひとりで考え続けるほど、判断基準が見えにくくなる"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">ひとりで考え続けるほど、判断基準が見えにくくなる</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>もう一つ印象的だったのは、皆さん真剣にチャンネルと向き合っているのに、判断材料が散らばりやすい点です。企画の意図を書いたメモと、公開後の数字、今の迷いが別々の場所に置かれています。これらが一つの画面でつながらないと、「なんとなく不安」という感覚だけが残りやすくなります。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fef08a;color:#422006" class="has-inline-color">ただし、ここで触れているのは私が参加した一つのオフ会で聞いた範囲の話であり、すべてのYouTube発信者に当てはまるとは限りません。</mark> それでも、目の前で語られた悩みはどれも切実で、片手間に聞ける軽い話ではありませんでした。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 3. 悩みを「開発のネタ」として聞いていた自分が卑しく見えて反省した話"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">3. 悩みを「開発のネタ」として聞いていた自分が卑しく見えて反省した話</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":184} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-184" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-reflection.jpg" alt="午後の窓辺で、羅針盤の線画が入った開いたノートを見つめながら静かに振り返る大人のイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>オフ会で色々な人の話を聞いているうちに、私の中で大きな変化が起きました。最初は開発の材料を探すつもりで聞いていたのに、耳を傾けるほど、話し手の真剣さが伝わってきたからです。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>チャンネル登録者がまだ少ない人の悩みも、すでに何本も動画を出して伸び方に迷っている人の悩みも、そこにある本気度は変わりませんでした。<strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">真剣に取り組んでいるからこそ悩みが出てくるのであり、悩みそのものに優劣は関係ないのだと知りました。</mark></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>そのことに気づいた瞬間、今までの自分が卑しく見えて、強く反省しました。目の前の人が時間と気力を注いで向き合う問題を、自分は「儲かりそうな市場」や「アプリ作りの都合のよい材料」として品定めしていたからです。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">誰かの切実な悩みを「自分の開発に使える材料」としか見ない姿勢は、打ち明けてくれた相手の真剣さを軽く扱うことになり、ものづくりをする側として避けたい態度だと痛感しました。</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>一人の困り事を起点にアプリを考える手順そのものは、<a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">1人の困り事を自作アプリで解決する方法｜アイデア出しから提供まで</a>でも整理しています。けれど今回の体験で学んだのは、作り方以上に「相手の悩みにどう向き合うか」が大切だという点でした。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 4. 既存の道具で「運営の方向性」はどこまで整理できるか"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">4. 既存の道具で「運営の方向性」はどこまで整理できるか</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":185} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-185" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-existing-tools.jpg" alt="動画分析画面、表計算シート、メモとタグの画面という3つの既存道具を同じ大きさで並べて比べるイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>結論から言うと、数字の確認や振り返りの記録だけなら既存の定番ツール3つでも十分に対応できます。悩みを真剣に解決したいからこそ、まずは既存の道具でどこまで整理できるのかを正直に比べました。</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>YouTube運営の方向性を整理するときに使える既存ツール3つの比較（2026年11月時点の公式情報にもとづく整理）</caption><thead><tr><th scope="col">ツール名</th><th scope="col">悩みへの合い方・続けやすさ</th><th scope="col">導入しやすさ・使いやすさ</th><th scope="col">料金・無料枠とデータ・プライバシー</th></tr></thead><tbody><tr><td>YouTube Studio（アナリティクス）</td><td>再生回数、視聴時間、登録者の増減、視聴者維持率（動画がどれくらい見続けられたかの割合）など公式の正確な数字で反応を確かめられます。投稿を続ける人ほど見直す習慣がつきやすいツールです</td><td>チャンネルを持っていれば追加登録なしですぐ開けます。項目が多いぶん最初はどこを見るか迷うことがあります</td><td>チャンネル運営者なら無料で利用可能。データは自分のGoogleアカウント内に保たれ、権限管理で共有範囲を決められます</td></tr><tr><td>Google スプレッドシート</td><td>動画ごとの狙い・公開日・数字を1行ずつ並べて比べられます。普段から表計算に慣れている人なら無理なく続けられます</td><td>Googleアカウントがあればすぐ使えます。どんな列を作ってどう比べるかは自分で設計する必要があります</td><td>個人向けの基本機能は無料。新規作成・編集したシートはGoogleアカウントの無料保存容量（Googleドライブ・Gmail・Googleフォト共有の15GB）の対象になります。共有範囲はファイルごとに調整できます</td></tr><tr><td>Notion</td><td>企画の背景、狙う視聴者像、公開後の気づきを自由な文章とタグで1か所にまとめられます。日常のメモ帳にしている人に向いています</td><td>テンプレートを組むのが好きな人には快適。自由度が高いぶん、最初の型づくりや見た目調整に時間がかかる場合があります</td><td>個人のソロ利用向けFreeプランはページ・ブロック数無制限。クラウド保存（1ファイル5MB、変更履歴7日間などの制限あり）で、非公開ページとして個人管理できます</td></tr></tbody></table></div>
<!-- /wp:html -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>YouTube Studio（アナリティクス）：</strong>「どの動画が見られ、どこで離脱されたか」という事実を正確に見るなら一番確実です。ただし「なぜその企画を撮ったのか」「次に方向をどう変えるか」といった自分の考えを並べて残す場所ではありません。基本の見方は<a href="https://support.google.com/youtube/answer/9002587?hl=ja" style="color: #0000ff; text-decoration: underline;">YouTube ヘルプ「YouTube アナリティクスの基礎」</a>で確認できます。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Google スプレッドシート：</strong>過去の動画と今の動画を横に並べて比較するには非常に便利です。表を自分で作るのが苦にならないなら、これだけで十分回る人も少なくありません。詳しくは<a href="https://workspace.google.com/products/sheets/" style="color: #0000ff; text-decoration: underline;">Google スプレッドシート公式ページ</a>で機能を見られます。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Notion：</strong>「このチャンネルは誰を助けたいのか」という文章のメモと、動画ごとの振り返りを一か所にまとめたい場合に役立ちます。個人利用の条件は<a href="https://www.notion.com/pricing" style="color: #0000ff; text-decoration: underline;">Notion 公式料金ページ</a>に掲載されています。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fef08a;color:#422006" class="has-inline-color">無料プランの上限や有料プランの条件、データの保管や共有の仕様は変わることがあるため、使い始める前に各サービスの公式案内で最新の内容を確かめておくと安心です。</mark></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 既存ツールで十分な人と、専用アプリが合いそうな人"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">既存ツールで十分な人と、専用アプリが合いそうな人</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>正直なところ、すでにスプレッドシートやNotionで自分の振り返り用の型を作れていて、「これを見れば次の動画が決まる」と感じている人なら、既存のツールで十分です。わざわざ新しいアプリを待つ必要はありません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>一方で、オフ会で聞いたような迷いが残りやすいのは、そもそも「表やノートに何を書けば方向性が定まるのか分からない」と感じているときです。YouTubeの数字画面と自分のメモが別の場所にあり、見比べる前に手が止まってしまう場合も同様です。真っ白な表を前に迷ってしまう人には、最初から「方向性を確かめる問い」が並んだ専用アプリが合いやすくなります。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 5. これから真剣に作りたい「運営の方向性を定めるアプリ」の構想"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">5. これから真剣に作りたい「運営の方向性を定めるアプリ」の構想</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":186} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-186" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-app-vision.jpg" alt="羅針盤のカード、棒グラフとメモのカード、道標と進む道のカードの3枚が矢印でつながる構想イラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>反省したからには、これからは「YouTube運営の悩み」に対して真剣に取り組み、出来たらで良いので、自作アプリでその迷いを少しでも減らせるように真剣に開発していきたいと考えています。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>現時点で描いている理想の状態は、派手な分析機能がたくさん並んだ道具ではありません。目指しているのは次の3点を1つの流れでつなぐシンプルな仕組みです。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>チャンネルの軸を先に言葉にする：</strong>「誰の、どんな困り事を減らしたくてこのチャンネルをやっているのか」を短い言葉で固定し、迷ったらいつでも見返せるようにする。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>1本ごとの狙いと結果を同じ型で残す：</strong>動画を作る前に考えた狙いと、公開後の反応（再生数や最後まで見られた割合、視聴者の声）を同じ画面に並べる。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>続ける・少し変える・手放すの判断材料を揃える：</strong>「なんとなく不安だから止める」のではなく、「最初の軸と照らし合わせると、次はここを直してみよう」と落ち着いて決められるようにする。</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>実は、以前に書いた<a href="https://www.nanasinogonbei.com/blog/2026/11/22/youtask-youtube-task-management/" style="color: #0000ff; text-decoration: underline;">YouTube動画制作のタスク管理を見える化するアプリ「YouTask」の構想｜公開前から継続判断まで</a>でも、公開前・公開中・公開後の3段階で作業と継続判断を残す案を整理しました。今回のオフ会での気づきを経て、単なる作業チェックだけでなく「運営の方向性を迷わず見直せること」に重心を置いて、あらためて形を練り直したいと思っています。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: アプリだけでは解決できない範囲も正直に見ておく"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">アプリだけでは解決できない範囲も正直に見ておく</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>どれほど丁寧に作ったとしても、アプリだけで解決できないことははっきり残ります。たとえば、動画の撮影や編集にかかる時間を増やしたり、話し方や企画そのものを自動で面白くしたり、YouTube側のおすすめ表示を思い通りに動かしたりはできません。</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>さらに言えば、最終的に「このテーマで続けるか、別の道へ進むか」を決めるのは、アプリではなく発信する本人です。自作アプリが引き受けられるのは、頭の中のモヤモヤを紙に書き出す手間を減らし、判断に必要な材料を静かに目の前へ並べてあげることまでだと考えています。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"ja: 6. 今後の進め方と、運営の方向性に迷ったとき今日から試せる一歩"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">6. 今後の進め方と、運営の方向性に迷ったとき今日から試せる一歩</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":187} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-187" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-next-step.jpg" alt="朝の机の上で3つの枠に分かれた白いノートを両手で開き、そばにマグカップとペンと羅針盤が置かれたイラスト" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>アプリはまだ構想段階のため、公開URLやリリース時期は未定です。焦って立派な画面を作るより、悩みの当事者に本当に役立つかを確かめながら、次の順で一歩ずつ進めるつもりです。</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li><strong>実際の迷いの整理：</strong>オフ会で聞いた「方向性に迷う場面」を思い返し、何を書き出せれば判断が楽になるのかを紙で確かめる。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>ごく小さな試作づくり：</strong>機能を増やしすぎず、まず自分や身近な人が「1本の動画の狙いと結果、次の方針」を書ける最小限の試作品を作る。</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>使ってもらいながら直す：</strong>机の上の想像で終わらせず、実際に運営に悩んでいる人に触ってもらい、迷いが減らなかった点は作り直す。</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>そして、もし今まさにYouTubeの方向性に迷っているなら、新しいアプリを待たずに今日からできる小さな方法があります。<strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">まずは手元のメモ帳や表計算に「今回の狙い／見ておきたい変化／次の判断」の3行だけを書いて、次の動画1本を試してみてください。</mark></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>たとえば、次のように短い1文ずつ書いてみるだけでも、数字だけを眺めて落ち込む時間を減らせます（以下は説明用の記入例です）。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>今回の狙い：</strong>初心者向けに、道具の選び方を1つだけ分かりやすく伝える</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>見ておきたい変化：</strong>最後まで見てくれた人の割合（視聴者維持率）が上がるか</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>次の判断：</strong>反応が良ければ同じ相手向けに続きを出し、合わなければ切り口を変える</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>身近な困り事を言語化して小さな試作につなげる進め方は、<a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color: #0000ff; text-decoration: underline;">自分の悩み・困り事を自作アプリにする方法｜題材の見つけ方から小さな試作まで</a>にもまとめています。これから先、試作できる形ができたら公開URLとあわせて、うまくいった点もつまずいた点もこのブログで正直に共有していきます。</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel -->

<!-- wp:tab-panel {"label":"English","metadata":{"name":"English article"}} -->
<section role="tabpanel" tabindex="0" class="wp-block-tab-panel"><!-- wp:group {"metadata":{"name":"en: Introduction"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:paragraph -->
<p>At first, I joined an online community’s YouTube meetup with a fairly casual thought: YouTube is a huge market, so picking a small corner and building an app for it looked like an easy way to earn money.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Talking with people there completely changed how I saw things. <strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">What most creators shared was uncertainty about their channel’s direction, and realizing there is no hierarchy in people’s struggles made me want to build a dedicated app seriously.</mark></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>At the time of writing, this app is still in the concept stage, so there is no public URL or subdomain site yet. Below, I share how a lighthearted profit mindset turned into honest self-reflection, how well three existing tools cover this problem, and a simple three-line note you can try today.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: 1. Starting Lightly with the Idea of Targeting a Niche in a Huge Market"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">1. Starting Lightly with the Idea of Targeting a Niche in a Huge Market</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":182} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-182" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/01-light-start.jpg" alt="An adult sitting casually beside a laptop with a generic play icon while looking at a large pie chart with one small separated slice and plain coin circles" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>When I was looking for my next app topic, the YouTube space caught my eye right away. With so many viewers and creators around the world, it is clearly a massive market.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>That led me to what people often call a “niche strategy”—focusing on one narrow pain point inside a huge market that big tools overlook. I figured that in a market that large, solving even a tiny fraction of people’s trouble could still be profitable. So I decided to learn more about YouTube and turn what I heard into an app.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>To see what real creators were experiencing, I attended a YouTube meetup inside the online community I belong to. Looking back honestly, my mindset before going was pretty shallow: I figured I could pick up people’s worries on the side and turn them into material for my next app.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">Building purely around the calculation that “targeting a niche in a giant market looks profitable” pulls you away from how real people actually struggle, making it hard to create anything they will keep using.</mark> Back then, I had not yet noticed that trap.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: 2. What Listening at the Meetup Revealed: Most Creators Struggle with Channel Direction"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">2. What Listening at the Meetup Revealed: Most Creators Struggle with Channel Direction</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":183} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-183" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/02-meetup-direction.jpg" alt="Four adults talking earnestly around a wooden café table with a floating compass and branching signpost icons above them" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>As I spoke with different people at the meetup, their video topics and years of experience varied widely. I had assumed most questions would be about editing software or camera gear, yet the actual conversations pointed somewhere else entirely.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">The common thread across nearly everyone I listened to was feeling unsure about the direction of their channel.</mark></strong></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Even View-Count and Editing Worries Traced Back to Unclear Direction"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Even View-Count and Editing Worries Traced Back to Unclear Direction</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Even when someone started with a different symptom, listening a bit deeper kept leading back to the same core uncertainties:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>Drifting away from who the channel is for:</strong> You start with topics you love, another style happens to get views, and suddenly you cannot decide whether to stay the course or pivot toward what gets clicks.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Numbers do not translate into next steps:</strong> Checking view counts or subscriber gains brings highs and lows, yet leaves you guessing what to change in your next upload.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>No clear signal for continuing or shifting:</strong> When effort stays high and traction feels thin, there is little evidence showing whether to keep pushing patiently or rethink the theme.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>On the surface, the trouble sounded like “views are flat” or “ideas ran dry,” but underneath lay the same persistent question of where the channel should go next.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Thinking Alone Makes Decision Criteria Harder to See"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Thinking Alone Makes Decision Criteria Harder to See</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Another thing stood out: everyone cared deeply about their channel, yet the clues needed for a calm decision were scattered. When your original goal sits in one notebook while performance numbers live on another screen, those pieces never connect—and vague anxiety lingers.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Keep in mind that these impressions come only from people I spoke with at one meetup and do not automatically apply to every YouTube creator.</mark> Even so, the worries shared across that table were genuine and far heavier than casual small talk.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: 3. Why Treating Real Worries as “Dev Material” Made Me Ashamed and Reflect"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">3. Why Treating Real Worries as “Dev Material” Made Me Ashamed and Reflect</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":184} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-184" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/03-reflection.jpg" alt="An adult sitting quietly beside a sunlit window looking down thoughtfully at an open notebook containing a hand-drawn compass sketch" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>While listening around the room, something inside me shifted. I had shown up looking for app-building leads, yet the more honestly people spoke, the more I felt how seriously they were trying.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Whether someone was starting with a handful of subscribers or already uploading dozens of videos and questioning their next move, the weight behind their words felt equally real. <strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">Worries appear precisely because people take their work seriously, and no worry is higher or lower than another.</mark></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Once that clicked, my earlier attitude looked genuinely mean and small. People were opening up about challenges they poured real hours into, while I had been sizing up their struggles as a profitable niche and convenient fuel for my own project.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fee2e2;color:#991b1b" class="has-inline-color">Viewing someone’s sincere struggle merely as handy fuel for your next build treats their effort lightly and is an attitude worth avoiding as a maker.</mark></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Starting from one person’s real problem is still a sound way to design software, as I wrote in <a href="https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/" style="color: #0000ff; text-decoration: underline;">How to Solve One Person’s Problem With a Homemade App: From Idea to Sharing</a>. What this meetup taught me, however, is that how you face someone’s struggle matters far more than any method.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: 4. How Far Existing Tools Can Clarify Channel Direction"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">4. How Far Existing Tools Can Clarify Channel Direction</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":185} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-185" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/04-existing-tools.jpg" alt="Three equal-sized cards arranged side by side showing a video analytics chart, a spreadsheet grid, and a notes-and-tags layout" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>The short answer is yes: for checking numbers and logging reflections, three established tools already cover most of the job. Because I want to approach this problem honestly, I compared those three everyday options fairly.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div class="table-scroll"><table><caption>Comparison of three existing tools for clarifying YouTube direction (based on official info checked in November 2026)</caption><thead><tr><th scope="col">Tool</th><th scope="col">Fit &amp; Continuity</th><th scope="col">Ease of Setup &amp; Use</th><th scope="col">Free Tier &amp; Data / Privacy</th></tr></thead><tbody><tr><td>YouTube Studio (Analytics)</td><td>Lets you verify real performance via views, watch time, subscriber gains, and audience retention; natural to check regularly once you publish</td><td>Ready immediately with any YouTube channel; the number of tabs and metrics can feel overwhelming at first</td><td>Free for channel owners; data stays inside your Google account with channel-permission controls for sharing</td></tr><tr><td>Google Sheets</td><td>Good for lining up each video’s goal, upload date, and results row by row; easy to keep up if you already like spreadsheets</td><td>Starts right away with a Google account; you must design your own columns and review layout</td><td>Core features are free for personal accounts; newly created or edited Sheets files count toward the shared 15 GB Google Account storage (shared across Drive, Gmail, and Photos), with per-file sharing controls</td></tr><tr><td>Notion</td><td>Great for keeping channel purpose, target viewer notes, and post-upload lessons together with tags; easy to maintain if you already take daily notes there</td><td>Comfortable for people who enjoy building templates; high flexibility can consume time on layout tweaks</td><td>Solo Free plan includes unlimited pages and blocks; cloud-stored (5 MB file upload cap and 7-day history on Free) and private by default</td></tr></tbody></table></div>
<!-- /wp:html -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>YouTube Studio (Analytics):</strong> Nothing beats it for checking accurate numbers on which videos held attention and where viewers left. Still, it is a reporting screen rather than a workspace for recording why you chose a topic or how your direction should shift. You can check the basics in <a href="https://support.google.com/youtube/answer/9002587?hl=en" style="color: #0000ff; text-decoration: underline;">YouTube Help: YouTube Analytics basics</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Google Sheets:</strong> Very practical for comparing past uploads side by side in a table. If setting up columns feels effortless to you, a sheet may already cover everything you need. Details are available on the <a href="https://workspace.google.com/products/sheets/" style="color: #0000ff; text-decoration: underline;">official Google Sheets page</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Notion:</strong> Useful when you want written thoughts about who your channel serves alongside video-by-video reflection logs. Check solo plan details on the <a href="https://www.notion.com/pricing" style="color: #0000ff; text-decoration: underline;">official Notion pricing page</a>.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p><mark style="background-color:#fef08a;color:#422006" class="has-inline-color">Free-tier limits, paid plan rules, and storage or sharing policies can change over time, so always verify current terms on each service’s official site before moving your records there.</mark></p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Who Existing Tools Already Serve—and Who Might Benefit from a Dedicated App"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Who Existing Tools Already Serve—and Who Might Benefit from a Dedicated App</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Honestly, if you already have a spreadsheet or Notion page that clearly tells you what to shoot next, existing tools are more than enough—there is no need to wait for a new app.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Where hesitation lingers is when you stare at a blank sheet unsure which questions actually help settle your direction. The same friction appears when your original intent and your YouTube numbers live in separate places, tiring you out before you review. For creators who stall at a blank page, a dedicated app built around direction-setting prompts can fit better.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: 5. The Concept for an App That Helps Set Channel Direction Seriously"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">5. The Concept for an App That Helps Set Channel Direction Seriously</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":186} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-186" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/05-app-vision.jpg" alt="Three rounded interface cards connected left to right on a wooden desk, depicting a compass, a bar chart with memo lines, and a signpost pointing along a path" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>After stepping back and reflecting, I want to engage earnestly with YouTube creators’ struggles and—if I can manage it—build a homemade app that genuinely helps people clarify and settle their channel direction.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Rather than cramming in flashy charts, the ideal tool I picture connects three simple pieces in one calm flow:</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>Put the channel’s core axis into words first:</strong> Pin down who the channel helps and what problem it addresses in a short statement you can revisit whenever doubt creeps in.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Keep each video’s intent beside its outcome:</strong> Display why you made a video right next to what happened after publishing—views, how long viewers stayed, and viewer comments.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Line up clues for continuing, adjusting, or letting go:</strong> Replace vague discouragement with calm comparisons against your stated axis so you can decide what to tweak next.</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>In an earlier post, <a href="https://www.nanasinogonbei.com/blog/2026/11/22/youtask-youtube-task-management/" style="color: #0000ff; text-decoration: underline;">Concept for “YouTask,” an App Visualizing YouTube Production Tasks</a>, I outlined a three-stage workflow covering before, during, and after publishing. Carrying forward what I learned at the meetup, I want to reshape that direction around helping creators step back and decide where their channel should head—not just checking off tasks.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: Being Honest About What No App Can Solve Alone"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading {"level":3} -->
<h3 class="wp-block-heading">Being Honest About What No App Can Solve Alone</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Even with sincere effort behind it, an app has clear boundaries. No planning tool can add extra filming hours to your week, automatically make scripts more engaging, or steer YouTube’s recommendation system.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>More importantly, choosing whether to stick with a theme or take a new turn always rests with the creator. All a good app can do is take away messy paperwork and lay out the facts calmly so you can think clearly for yourself.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:group {"metadata":{"name":"en: 6. Next Steps for Development and One Practical Step to Try Today"},"className":"ytdir-panel","layout":{"type":"default"}} -->
<div class="wp-block-group ytdir-panel"><!-- wp:heading -->
<h2 class="wp-block-heading">6. Next Steps for Development and One Practical Step to Try Today</h2>
<!-- /wp:heading -->

<!-- wp:image {"width":"100%","height":"auto","sizeSlug":"full","linkDestination":"none","id":187} -->
<figure class="wp-block-image size-full is-resized"><img class="wp-image-187" src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/11/06-next-step.jpg" alt="Morning sunlight over a wooden desk as two hands hold open a blank notebook divided into three sections beside a mug, pen, and small compass" style="width:100%;height:auto"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>As noted earlier, this app is still in the concept stage, so its public URL and release timing remain undecided. Rather than rushing out a shiny screen, I plan to build slowly in three steps while checking whether it actually eases real worries:</p>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li><strong>Organize real moments of doubt:</strong> Revisit the direction struggles I heard at the meetup and test on paper which prompts actually make decisions easier.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Build a tiny prototype:</strong> Keep features minimal so one creator can record a single video’s goal, outcome, and next adjustment without clutter.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Refine through real use:</strong> Put it in front of creators facing genuine channel decisions and rewrite anything that fails to clear up their confusion.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Meanwhile, if you feel unsure about your YouTube direction right now, you do not have to wait for any app. <strong><mark style="background-color:#dbeafe;color:#1e3a8a" class="has-inline-color">Open your favorite notes app or spreadsheet and write just three short lines for your next video: “Aim / Change to Watch / Next Decision.”</mark></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Writing one brief sentence for each turns blank staring at analytics into one concrete experiment (sample entry for illustration):</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><strong>Aim:</strong> Explain one beginner tool choice clearly for newcomers</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Change to Watch:</strong> Whether the share of viewers staying to the end (audience retention) improves</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><strong>Next Decision:</strong> Keep this angle for the same viewer if response is strong, or shift topics if not</li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>For more on turning a concrete everyday struggle into a small working prototype, see <a href="https://www.nanasinogonbei.com/blog/2026/10/21/personal-problem-to-app/" style="color: #0000ff; text-decoration: underline;">How to Turn a Personal Problem into a Homemade App: From Finding an Idea to a Small Prototype</a>. Once a testable version is ready, I will share both its live link and honest lessons—successes and setbacks alike—here on the blog.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group --></section>
<!-- /wp:tab-panel --></div>
<!-- /wp:tab-panels --></div>
<!-- /wp:tabs -->