---
categories:
- 開発の裏側
excerpt: アプリの題材を探している個人開発者向けに、クラウドソーシングの依頼やアプリレビューから困り事を安全に収集・集計し、対象者への確認を経て小さなアプリで検証する手順を、架空の記入例と7日間の進め方で紹介します。
featured_image: articles/images/crowdsourcing-problems-to-app-ideas/01-overview.png
featured_image_alt: 複数の困り事を集めて整理し、小さなアプリの形にする流れを表したイラスト
slug: crowdsourcing-problems-to-app-ideas
status: publish
tags:
- 個人開発
- アプリ開発
- アイデア検証
- クラウドソーシング
- MVP
title: クラウドソーシングからアプリのアイデアを見つける方法｜困り事の収集・集計・検証
wordpress_featured_media_id: 43
wordpress_inline_media:
  01-overview.png:
    id: 43
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/01-overview.png
  02-collect-safely.png:
    id: 44
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/02-collect-safely.png
  03-cluster-score.png:
    id: 45
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/03-cluster-score.png
  04-validate.png:
    id: 46
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/04-validate.png
  05-mvp-measure.png:
    id: 47
    url: https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/05-mvp-measure.png
wordpress_post_id: 48
wordpress_url: https://www.nanasinogonbei.com/blog/2026/09/28/crowdsourcing-problems-to-app-ideas/
---

<!-- wp:group {"anchor":"problem-app-language-switch","metadata":{"name":"困り事からアプリを考える（日英切り替え）"},"layout":{"type":"default"}} -->
<div id="problem-app-language-switch" class="wp-block-group">
<!-- wp:html {"metadata":{"name":"言語切り替え・共通スタイル"}} -->
<style>
#problem-app-language-switch label {display:inline-block;padding:0.5em 1em;border:2px solid #174e67;border-radius:6px;cursor:pointer;}
#problem-app-language-switch input:focus-visible + label {outline:3px solid #174e67;outline-offset:3px;}
#problem-app-language-switch input:checked + label {background:#174e67;color:#fff;}
#problem-app-language-switch .language-panel {display:none;}
#problem-app-ja:checked ~ .panel-ja,#problem-app-en:checked ~ .panel-en {display:block;}
#problem-app-language-switch a {color:#0000ff;text-decoration:underline;}
#problem-app-language-switch img {max-width:100%;height:auto;}
#problem-app-language-switch .language-panel {overflow-wrap:anywhere;}
#problem-app-language-switch .table-scroll {overflow-x:auto;}
#problem-app-language-switch table {width:100%;border-collapse:collapse;}
#problem-app-language-switch th,#problem-app-language-switch td {padding:0.5em;border:1px solid #cbd5e1;text-align:left;vertical-align:top;}
</style>
<input type="radio" name="problem-app-language" id="problem-app-ja" checked><label for="problem-app-ja" lang="ja">日本語</label>
<input type="radio" name="problem-app-language" id="problem-app-en"><label for="problem-app-en" lang="en">English</label>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：導入・全体の流れ"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="導入・全体の流れ">
<p>クラウドソーシングからアプリのアイデアを見つけるなら、依頼された機能ではなく、<strong>お金や時間をかけてでも解決したい困り事</strong>を読み取ります。公開依頼は、その手がかりの一つです。</p>
<p>ただし、依頼を一件見つけただけでは需要があるとは言えません。依頼文をそのまま製品仕様にしたり、投稿者の情報を別の目的で利用したりするのも避ける必要があります。</p>
<p><strong>結論は、次の5段階で進めることです。</strong></p>
<ol>
<li>利用条件を確認できた公開情報から、困り事を30件程度記録する。</li>
<li>「誰が・いつ・何に困るか」で分類し、重複を除いた事例数を集計する。</li>
<li>5項目で比べ、確認する候補を3案までに絞る。</li>
<li>同じ悩みを持つ対象者5人を目安に、直近の行動を聞く。</li>
<li>最も根拠が集まった一案を、一つの作業だけできる最小版で試す。</li>
</ol>
<p>30件や5人は需要を証明する数字ではなく、思い込みを減らすための初回調査の目安です。</p>
<p>本記事は調査手順の提案です。以下の依頼例・集計値・点数はすべて架空で、実際に案件収集や利用者テストを行った結果ではありません。調査に使える範囲はサービスごとに異なるため、収集前に利用目的を含めて規約を確認してください。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：依頼を「作る機能」ではなく「困っている状況」として読む"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="依頼を「作る機能」ではなく「困っている状況」として読む">
<h2>依頼を「作る機能」ではなく「困っている状況」として読む</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/01-overview.png" alt="困っている人の声を集め、分類してアプリ候補へ絞る流れを表したイラスト"></p>
<p>クラウドソーシングには、「表計算へ転記してほしい」「毎週の報告をまとめてほしい」といった依頼があります。ここから読むべきなのは、指定された納品物だけではありません。</p>
<p>架空の例として「請求書の内容を表へ転記してほしい」という依頼を考えます。背景を確認できた場合は、次のように整理できます。依頼文にない項目は、推測で埋めず「未確認」にします。</p>
<ul>
<li>誰が困るのか：少人数の会社で事務を担当する人</li>
<li>いつ困るのか：月末に請求書がまとまって届くとき</li>
<li>今の対処法：一枚ずつ開き、表へ手入力する</li>
<li>何が失われるのか：時間がかかり、入力間違いの確認も必要になる</li>
<li>望む結果：確認しながら短時間で一覧にしたい</li>
</ul>
<p>この形に直すと、「転記代行を受注する」という発想から、「確認しやすい下書きを作る道具」など、別の解決方法も考えられます。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：一つの場所だけで需要を決めない"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="一つの場所だけで需要を決めない">
<h3>一つの場所だけで需要を決めない</h3>
<div class="table-scroll">
<table>
<thead><tr><th>見る場所</th><th>分かること</th><th>読み違えやすい点</th></tr></thead>
<tbody>
<tr><td>クラウドソーシングの公開依頼</td><td>外注したい作業、予算を付けるほどの手間</td><td>一社だけの特殊な事情や、発注者が考えた解決方法かもしれない</td></tr>
<tr><td>既存アプリのレビュー</td><td>現在の道具で足りない点、利用中に起きる不満</td><td>古い版の問題や、一部の強い不満に偏ることがある</td></tr>
<tr><td>質問サイトや公開コミュニティ</td><td>利用者自身の言葉、困る場面や背景</td><td>困っている人の数や、支払う意思までは分からない</td></tr>
<tr><td>自分の仕事と知人への聞き取り</td><td>作業の順番、例外、感情まで詳しく確認できる</td><td>自分の周囲だけの問題を一般化しやすい</td></tr>
</tbody>
</table>
</div>
<p>Appleは、レビューをアプリの利用体験に関するフィードバックと説明しています。調査では星の数だけでなく、投稿日・対象バージョン・具体的な作業を読みましょう。古い不満が現在も残っているかは、現行版で確認します。<a href="https://developer.apple.com/app-store/ratings-and-reviews/" style="color: #0000ff; text-decoration: underline;">Appleの評価・レビューの案内</a></p>
<p>まずは「経理」「SNS運用」「予約管理」のように対象を一つ決めます。そのうえで二種類以上の場所を見て、同じ状況が別の人からも出てくるかを確かめます。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：利用条件を確認し、30件を目安に困り事を記録する"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="利用条件を確認し、30件を目安に困り事を記録する">
<h2>利用条件を確認し、30件を目安に困り事を記録する</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/02-collect-safely.png" alt="公開依頼やレビューなどから個人情報を除いて困り事を記録する人のイラスト"></p>
<p>必要なのは、記録用の表と調査範囲のメモです。「直近3か月・小規模事業者の経理」のように対象と期間を決め、使った検索語も残します。該当する例が少なければ、30件に届かせるために無関係な内容を足す必要はありません。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：検索するときは、作業と負担を表す言葉を見る"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="検索するときは、作業と負担を表す言葉を見る">
<h3>検索するときは、作業と負担を表す言葉を見る</h3>
<p>クラウドソーシング内では、対象分野に「転記」「集計」「毎日」「大量」「確認」「管理」「リマインド」「自動化」などを組み合わせます。「アプリを作ってほしい」という依頼だけでなく、人が繰り返している作業も探してください。</p>
<p>見つけた内容は、次の列を持つ表へ一件一行で記録します。</p>
<div class="table-scroll">
<table>
<thead><tr><th>列</th><th>記録する内容</th></tr></thead>
<tbody>
<tr><td>記録ID・分類・重複先</td><td>調査用の連番、困り事の分類名、同じ依頼の再投稿なら元の記録ID</td></tr>
<tr><td>確認日・投稿日・情報源</td><td>いつ確認し、いつ投稿された情報か。検索語や対象バージョンも記録する</td></tr>
<tr><td>参照URL</td><td>必要な範囲で原文確認用に保存する。リンク先から個人を識別できる場合は、共有用の表やAIへの入力に含めない</td></tr>
<tr><td>困る人・場面</td><td>誰が、いつ、どの作業で困るか</td></tr>
<tr><td>困り事の要約</td><td>固有名詞を外し、自分の言葉で一文にする</td></tr>
<tr><td>現在の対処法</td><td>手入力、表計算、外注、確認の二重化など</td></tr>
<tr><td>負担の証拠</td><td>頻度、作業量、締切、予算など、明記された事実</td></tr>
<tr><td>不明点</td><td>人数、発生頻度、例外など、まだ確かめていないこと</td></tr>
</tbody>
</table>
</div>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：依頼文は転載せず、自動収集は規約と許可を確認する"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="依頼文は転載せず、自動収集は規約と許可を確認する">
<h3>依頼文は転載せず、自動収集は規約と許可を確認する</h3>
<p>公開ページでも、文章を自由にコピーして再配布できるとは限りません。文化庁は、出所を示すだけですべての利用が認められるわけではなく、引用には公表済みであることや、目的上正当な範囲などの条件があると説明しています。<a href="https://www.bunka.go.jp/seisaku/bunka_gyosei/kibankyoka/faq/index.html" style="color: #0000ff; text-decoration: underline;">文化庁「文化芸術活動に関する法的問題についてよくあるご質問」</a></p>
<p>個人情報保護委員会も、インターネットなどですでに公表されている個人情報を保護の対象としています。名前を外しても、参照URLや具体的な事情から本人が分かる場合は、匿名になったとは言えません。<a href="https://www.ppc.go.jp/all_faq_index/faq1-q1-5/" style="color: #0000ff; text-decoration: underline;">個人情報保護委員会「公開済みの個人情報も保護されるか」</a></p>
<p>そのため、調査表には氏名、会社名、ユーザー名、連絡先、依頼文の長いコピーを保存せず、困り事の要点だけを自分の言葉で残します。非公開の依頼、提案、メッセージ、秘密保持の対象も使いません。</p>
<p>クラウドワークスの利用規約第23条(15)は、事前の書面承認がある場合を除き、同サービスの業務委託以外の営利活動やその準備を目的とする利用を禁じています。本記事の調査が認められると決めつけず、利用目的を運営へ確認してください。<a href="https://crowdworks.jp/pages/agreement" style="color: #0000ff; text-decoration: underline;">クラウドワークス利用規約</a></p>
<p>ランサーズには依頼の非公開設定があり、プロジェクト方式の提案は非公開です。閲覧できる範囲と二次利用の条件は別に確認します。<a href="https://www.lancers.jp/faq/C1006/189" style="color: #0000ff; text-decoration: underline;">ランサーズの公開・非公開に関する案内</a></p>
<p>公開ページを閲覧できることと、その内容を製品調査に使ってよいことは同じではありません。利用目的が規約上明確でなければ、運営へ確認するか、そのサービスを調査元から外します。</p>
<p><strong>調査元としての利用が認められている場合も、公開情報の閲覧と匿名化したメモにとどめます。</strong>大量の自動取得、ログイン制限の回避、投稿者への営業連絡は行いません。自動収集を検討する場合は、各サービスの最新規約、技術的なアクセス条件、必要な許可を個別に確認してください。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：記入例は、原文を残さず具体性を保つ"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="記入例は、原文を残さず具体性を保つ">
<h3>記入例は、原文を残さず具体性を保つ</h3>
<div class="table-scroll">
<table>
<thead><tr><th>困る人・場面</th><th>困り事の要約</th><th>現在の対処</th><th>確認が必要なこと</th></tr></thead>
<tbody>
<tr><td>小規模事業者が月末に請求書を処理する</td><td>書式の異なるPDFから必要項目を表へ移すのに時間がかかる</td><td>一枚ずつ開いて手入力し、あとで見直す</td><td>月の枚数、許容できる誤り、機密情報の扱い</td></tr>
<tr><td>店舗担当者が複数のSNSへ告知する</td><td>媒体ごとに文章と画像サイズを直す作業が繰り返される</td><td>過去の投稿を複製して手直しする</td><td>利用媒体、承認の流れ、予約投稿の必要性</td></tr>
</tbody>
</table>
</div>
<p><em>上の二例は手順を説明するために作った架空の内容で、特定の依頼を転載したものではありません。</em></p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：重複を除いて困り事を集計し、候補を採点する"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="重複を除いて困り事を集計し、候補を採点する">
<h2>重複を除いて困り事を集計し、候補を採点する</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/03-cluster-score.png" alt="集めた困り事を似た内容ごとにまとめ、点数で候補を比較するイラスト"></p>
<p>集めた困り事は「同じ立場の人が、同じ場面で、同じ結果を得たいか」で分類します。「PDF」という単語が共通していても、経理担当者の請求書処理と学生の資料整理は、別の候補として扱います。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：投稿件数と、重複を除いた事例数を分ける"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="投稿件数と、重複を除いた事例数を分ける">
<h3>投稿件数と、重複を除いた事例数を分ける</h3>
<ol>
<li>同じ依頼の再投稿や他サイトへの転載と分かるものに、重複先の記録IDを付ける。</li>
<li>一つの記録に主な困り事を一つ付け、分類名で表を並べ替える。</li>
<li>分類ごとに「収集件数」「確認済みの重複件数」「残った事例数」を数える。重複か判断できない記録は残った事例数に含め、その内数を「重複未確認」として併記する。</li>
<li>情報源の種類と、作業の発生頻度も確認する。投稿の多さと、その人が困る頻度は別に扱う。</li>
</ol>
<div class="table-scroll">
<table>
<caption>架空の集計例：収集30件から確認済みの重複6件を除く（重複未確認は0件）</caption>
<thead><tr><th>困り事</th><th>収集件数</th><th>重複件数</th><th>重複を除いた事例数</th></tr></thead>
<tbody>
<tr><td>請求書の転記</td><td>12</td><td>3</td><td>9</td></tr>
<tr><td>SNS投稿の調整</td><td>10</td><td>2</td><td>8</td></tr>
<tr><td>共有画像の仕分け</td><td>8</td><td>1</td><td>7</td></tr>
<tr><td>合計</td><td>30</td><td>6</td><td>24</td></tr>
</tbody>
</table>
</div>
<p>この24件は調べた範囲の事例数で、24人の利用者や市場全体の需要を意味しません。投稿していない人や、そのサービスを使わない人の困り事は含まれないためです。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：まとめた候補ごとに、1から5で採点する"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="まとめた候補ごとに、1から5で採点する">
<h3>まとめた候補ごとに、1から5で採点する</h3>
<div class="table-scroll">
<table>
<thead><tr><th>項目</th><th>1点</th><th>5点</th></tr></thead>
<tbody>
<tr><td>繰り返し</td><td>一度しか見ていない</td><td>複数の情報源で繰り返し見つかる</td></tr>
<tr><td>負担の強さ</td><td>少し面倒</td><td>仕事が止まる、締切や損失に関わる</td></tr>
<tr><td>現在の支出</td><td>現状は費用をかけていないと確認できた</td><td>継続して外注費や既存ツール代を払っていると確認できた</td></tr>
<tr><td>対象者への届きやすさ</td><td>話を聞ける相手がいない</td><td>自分の経験やつながりから話を聞ける</td></tr>
<tr><td>小さく試せるか</td><td>最初から大規模な連携や許認可が必要</td><td>一つの作業だけを手動補助でも試せる</td></tr>
</tbody>
</table>
</div>
<p>2〜4点は両端の基準の中間として、理由を一行添えます。根拠のない項目は1点ではなく「未確認」とし、合計を出さず追加調査へ回します。全項目を確認できた候補の満点は25点ですが、これは本記事で提案する比較用の目安です。</p>
<p><strong>依頼に書かれた予算は希望額であり、実際の支出とは限りません。</strong>実際に外注費を払っていても、アプリへ払う意思とは別です。募集予算・支払実績・有料試用への反応を分けて記録します。</p>
<p>個人情報や専門判断を扱うリスクは点数と分けて確認します。安全な試用ができる体制を用意できなければ、高得点でも開発候補から外します。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：架空の3案を比べる"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="架空の3案を比べる">
<h3>架空の3案を比べる</h3>
<div class="table-scroll">
<table>
<thead><tr><th>候補</th><th>繰り返し</th><th>負担</th><th>現在の支出</th><th>届きやすさ</th><th>小さく試せる</th><th>合計</th></tr></thead>
<tbody>
<tr><td>請求書から確認用の一覧を作る</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>21</td></tr>
<tr><td>SNS投稿を媒体ごとに整える</td><td>4</td><td>3</td><td>3</td><td>4</td><td>3</td><td>17</td></tr>
<tr><td>共有画像を用途別に仕分ける</td><td>3</td><td>3</td><td>2</td><td>3</td><td>4</td><td>15</td></tr>
</tbody>
</table>
</div>
<p><em>点数も含めて架空の例です。21点だから成功する、という意味ではありません。</em></p>
<p>候補への検索上の関心は、Google Trendsでも補助的に確認できます。「検索語」は入力語を含む検索などを対象とし、「トピック」は言語をまたぐ関連語をまとめます。比較時は地域・期間・検索の種類をそろえます。<a href="https://support.google.com/trends/answer/4359550?hl=ja" style="color: #0000ff; text-decoration: underline;">Google Trendsの検索キーワード比較ガイド</a></p>
<p>ただし、Google Trendsの数値は検索回数そのものではなく、期間と地域に合わせて0から100へ調整された相対値です。検索量が少ない語は0になることもあります。順位を決める証拠ではなく、言い換えや季節変動を探す材料として使います。<a href="https://support.google.com/trends/answer/4365533" style="color: #0000ff; text-decoration: underline;">Google Trendsデータに関するFAQ</a></p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：作る前に5人へ話を聞き、試用への協力を確かめる"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="作る前に5人へ話を聞き、試用への協力を確かめる">
<h2>作る前に5人へ話を聞き、試用への協力を確かめる</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/04-validate.png" alt="困り事を持つ人と作り手が簡単な試作品を見ながら話すイラスト"></p>
<p>候補が決まったら、作り込む前に対象者へ話を聞きます。知人や調査への協力者を募れるコミュニティなどで、参加に同意した人を探してください。クラウドソーシングの依頼主へ規約外の営業連絡をする方法は使いません。</p>
<p>最初の5人では、依頼文から読み取った困り事が実際の作業と合っているかを確かめます。</p>
<p>聞き取りの目的と記録の扱いを先に伝え、録音や資料の保存は本人の同意を得ます。会社の資料は、その人が共有してよいものかも確認してください。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：「欲しいですか」ではなく、直近の行動を聞く"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="「欲しいですか」ではなく、直近の行動を聞く">
<h3>「欲しいですか」ではなく、直近の行動を聞く</h3>
<ol>
<li>最後にその作業をしたのはいつですか。</li>
<li>最初から最後まで、どの順番で進めましたか。</li>
<li>一番時間がかかった場所と、間違いやすい場所はどこですか。</li>
<li>今は何を使って対処していますか。</li>
<li>その方法に払っている時間や費用はどのくらいですか。</li>
<li>可能なら、個人情報を隠した状態で実際の作業を見せてもらえますか。</li>
</ol>
<p>「こんなアプリがあれば使いますか」は、相手が好意で「使う」と答えやすい質問です。未来の希望より、直近に実際に起きた行動を確認します。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：合格条件を先に決める"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="合格条件を先に決める">
<h3>合格条件を先に決める</h3>
<p>たとえば初回は、次のような条件を決めます。</p>
<ul>
<li>5人に話を聞く</li>
<li>3人以上が過去1か月以内に同じ問題を経験している</li>
<li>2人以上が現在の作業や資料を見せることに同意する</li>
<li>1人以上が、有料の試用または具体的な試験導入に同意する</li>
</ul>
<p>これは月次作業を想定した例です。対象や作業周期に合わせて条件を先に決めます。無料の試験導入への同意は支払い意思の証明にならないため、有料試用とは分けて記録します。</p>
<p>既存の表計算テンプレートや自動化サービスで十分なら、それも結果です。まず手作業で一回だけ代行する、画面をクリックできる見本を見せる、利用希望者を募るなど、完成品より小さい方法で確かめます。申込者数を装ったり、完成していない機能を完成済みと見せたりしてはいけません。</p>
<p>既存の解決策は有力なものを最大3つ選び、同じ架空データ・同じ作業で比べます。目的を達成できるか、導入の手間、料金、操作のしやすさ、データの扱い、続けやすさを記録し、それでも残った不便をアプリ候補にします。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：一つの作業だけを最小版にし、続けるかを数字で決める"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="一つの作業だけを最小版にし、続けるかを数字で決める">
<h2>一つの作業だけを最小版にし、続けるかを数字で決める</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/05-mvp-measure.png" alt="小さなアプリを利用者に試してもらい、続行・修正・中止を判断するイラスト"></p>
<p>検証で根拠が集まった一つの流れを、価値を確かめる最小版（MVP）にします。請求書の例なら「PDFを入れる → 項目の下書きが出る → 人が確認する → 表へ出す」までです。会計ソフト連携や専用のスマートフォンアプリは後回しにできます。</p>
<p>最初は架空の請求書で試します。実際の資料を預かる段階では、本人以外にデータを見せない仕組みや保存・削除のルールも必要です。個別の書式に対応できるか、訂正の手間を含めて時間を減らせるかを検証します。この最小版は会計上の判断や内容の正しさを保証するものではありません。</p>
<p>最小版では、次の数字を見ます。</p>
<ul>
<li>初回に目的の作業を完了できた人数と割合</li>
<li>その作業が次に発生する周期内に、もう一度使った人数と割合（月次作業なら翌月まで）</li>
<li>同程度の量・難しさの作業で、確認と修正を含めて減った時間</li>
<li>処理した全項目数に対する、修正が必要だった項目数と割合</li>
<li>提示した価格で継続を希望した人数と、実際に支払った人数</li>
</ul>
<p>利用者が戻ってこない場合は、画面の使いにくさだけでなく、問題の頻度が低い、既存手段で十分、対象者が違う、といった可能性も見ます。数字が弱ければ機能を増やす前に、対象と問題の選び方へ戻ります。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：この方法が向いている人・向いていない人"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="この方法が向いている人・向いていない人">
<h3>この方法が向いている人・向いていない人</h3>
<p>この方法は、繰り返される事務作業や業務上の不便を題材にしたい人、対象者へ話を聞ける人、小さな範囲から検証できる人に向いています。</p>
<p>一方、話を聞かずに流行の機能をすぐ作りたい人や、必要な知識・安全対策がないまま医療・金融・法務などの判断を自動化したい人には向きません。規制や安全性が関わる分野では、専門家への確認と適切な体制が先です。</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：最初の7日間は、調査だけでもよい"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="最初の7日間は、調査だけでもよい">
<h3>最初の7日間は、調査だけでもよい</h3>
<ol>
<li><strong>1日目：</strong>対象を一つ選び、使うサービスの規約と公開範囲を確認する。</li>
<li><strong>2〜3日目：</strong>二種類以上の情報源から、個人を特定する情報を除いた困り事を30件程度集める。</li>
<li><strong>4日目：</strong>「誰が・いつ・何に困るか」で分類し、重複を除いた事例数を集計する。</li>
<li><strong>5日目：</strong>5項目の根拠を整理し、確認する候補を最大3案に絞る。未確認の項目は聞き取りの質問にする。</li>
<li><strong>6日目：</strong>対象者2人へ予備的に話を聞き、質問と候補のずれを確認する。</li>
<li><strong>7日目：</strong>残す案を一つ決め、初回5人のうち残り3人へ確認する計画を立てる。対象者を変えた場合は、その対象で聞き直す。</li>
</ol>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"日本語：よくある失敗を先に避ける"}} -->
<section class="language-panel panel-ja" lang="ja" aria-label="よくある失敗を先に避ける">
<h3>よくある失敗を先に避ける</h3>
<ul>
<li><strong>一件の依頼を市場だと思う：</strong>別の情報源と別の人でも同じ問題があるか確認します。</li>
<li><strong>依頼された機能をそのまま作る：</strong>機能ではなく、困る場面と望む結果へ言い換えます。</li>
<li><strong>原文と個人情報をため込む：</strong>要約と確認日を中心に記録し、本人へたどれる情報は共有用の表から外します。</li>
<li><strong>AIへ機密情報を貼る：</strong>外部のAIを使う場合も、投稿者や顧客を特定できる情報、契約上の秘密を入力しません。</li>
<li><strong>聞く前に数週間作る：</strong>会話、紙の見本、手作業の試験提供を先に行います。</li>
<li><strong>既存アプリを無視する：</strong>すでに安く解決できるなら、自作しない判断も残します。</li>
</ul>
<p>まずは対象と調査範囲を決め、利用条件を確認できた情報源から10件を記録してみてください。重複を除いて集計し、既存手段で残る不便を対象者へ確かめる。それが、小さなアプリを作り始める判断材料になります。</p>
<p><em>サービスの規約・公式資料は2026年9月28日に確認しました。この記事は法的助言ではありません。利用するサービスと情報の扱いに応じて、最新の規約や法令、必要な許可を確認してください。挿絵はAIで生成したイメージで、実在のサービス画面や人物を表すものではありません。</em></p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Introduction and overview"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Introduction and overview">
<p><strong>How to Find App Ideas on Crowdsourcing Sites: Collect, Group, and Validate Real Problems</strong></p>
<p>To find an app idea on crowdsourcing sites, read the underlying <strong>problem that someone wants to solve enough to commit time or money</strong>, rather than copying the requested feature. Public requests are one possible source of evidence.</p>
<p>One request does not prove demand. You should also avoid treating a request as a ready-made product specification or using a poster's information for another purpose.</p>
<p><strong>Use this five-step process:</strong></p>
<ol>
<li>Record about 30 problems from public information whose conditions of use you have checked.</li>
<li>Group entries by who struggles, when, and with what, then count cases after removing duplicates.</li>
<li>Compare the groups on five factors and keep no more than three candidates.</li>
<li>Ask about recent behavior with about five people who experience the problem.</li>
<li>Test the best-supported candidate with a minimum version that completes one task.</li>
</ol>
<p>Thirty examples and five interviews do not prove demand. They are starting points for reducing assumptions.</p>
<p>This article proposes a research process. All request examples, counts, and scores below are fictional, not results from collecting real listings or running user tests. Before collecting information, check whether each service permits your intended research use.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Read a request as a difficult situation, not a feature list"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Read a request as a difficult situation, not a feature list">
<h2>Read a request as a difficult situation, not a feature list</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/01-overview.png" alt="A flow from collecting people's difficulties to grouping them and selecting an app opportunity"></p>
<p>Crowdsourcing sites contain requests such as entering data into a spreadsheet or compiling a weekly report. The requested deliverable is not the only useful signal.</p>
<p>Consider a fictional request to enter invoice data into a spreadsheet. Once the background is confirmed, you could organize it as follows. Mark details absent from the request as unconfirmed instead of filling them in by assumption.</p>
<ul>
<li>Who struggles: a person handling administration at a small company</li>
<li>When it happens: many invoices arrive at the end of the month</li>
<li>Current workaround: open each file and enter the data manually</li>
<li>What it costs: time, plus another pass to find typing errors</li>
<li>Desired outcome: create a reviewable list in less time</li>
</ul>
<p>This framing moves you beyond “offer a data-entry service” and opens other possibilities, such as a tool that prepares a draft for human review.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Do not judge demand from one source"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Do not judge demand from one source">
<h3>Do not judge demand from one source</h3>
<div class="table-scroll">
<table>
<thead><tr><th>Source</th><th>What it can reveal</th><th>What you may misread</th></tr></thead>
<tbody>
<tr><td>Public crowdsourcing requests</td><td>Work people want to outsource and effort worth assigning a budget to</td><td>The situation may be unique to one company, or the request may already assume a particular solution</td></tr>
<tr><td>Reviews of existing apps</td><td>Gaps and frustrations in tools people already use</td><td>Reviews may concern an old version or overrepresent a vocal minority</td></tr>
<tr><td>Question sites and public communities</td><td>Users' own words, context, and moments of difficulty</td><td>They do not reveal how many people share the problem or whether anyone will pay</td></tr>
<tr><td>Your work and interviews with people you know</td><td>The full workflow, exceptions, and emotional impact</td><td>It is easy to generalize from your immediate circle</td></tr>
</tbody>
</table>
</div>
<p>Apple describes reviews as feedback about users' experience with an app. For research, read the date, app version, and specific task as well as the rating. Check the current version before assuming an old complaint remains unresolved. See <a href="https://developer.apple.com/app-store/ratings-and-reviews/" style="color: #0000ff; text-decoration: underline;">Apple's guidance on ratings and reviews</a>.</p>
<p>Start with one area, such as bookkeeping, social media operations, or appointment management. Then use at least two kinds of sources and check whether different people describe the same situation.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Check conditions of use and aim to record thirty problems"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Check conditions of use and aim to record thirty problems">
<h2>Check conditions of use and aim to record thirty problems</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/02-collect-safely.png" alt="A researcher recording anonymized problems from public requests, reviews, and discussions"></p>
<p>Prepare a table and a note defining your research scope, such as small-business bookkeeping over the last three months. Record your search terms too. If few examples qualify, do not add unrelated entries just to reach thirty.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Search for words that describe work and burden"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Search for words that describe work and burden">
<h3>Search for words that describe work and burden</h3>
<p>Within a crowdsourcing service, combine your chosen field with words meaning data entry, aggregation, daily, high volume, review, management, reminder, or automation. Do not look only for requests to build an app. Repeated human work can be an equally valuable signal.</p>
<p>Record one problem per row with these columns:</p>
<div class="table-scroll">
<table>
<thead><tr><th>Column</th><th>What to record</th></tr></thead>
<tbody>
<tr><td>Record ID, category, and duplicate reference</td><td>A research-only sequence number, problem category, and the original record ID for a repost</td></tr>
<tr><td>Review date, posting date, and source</td><td>When you checked it and how old it is; include the search term and relevant app version</td></tr>
<tr><td>Reference URL</td><td>Keep only as needed to verify the original. Exclude links that can identify a person from shared tables and AI inputs</td></tr>
<tr><td>Person and situation</td><td>Who struggles, when, and during which task</td></tr>
<tr><td>Problem summary</td><td>One sentence in your own words, with names removed</td></tr>
<tr><td>Current workaround</td><td>Manual entry, spreadsheets, outsourcing, double-checking, and so on</td></tr>
<tr><td>Evidence of burden</td><td>Stated frequency, volume, deadline, or budget</td></tr>
<tr><td>Unknowns</td><td>People affected, frequency, exceptions, and other facts still to validate</td></tr>
</tbody>
</table>
</div>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Do not republish request text, and check rules and permission before automating collection"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Do not republish request text, and check rules and permission before automating collection">
<h3>Do not republish request text, and check rules and permission before automating collection</h3>
<p>Public text is not automatically free to copy and redistribute. Japan's Agency for Cultural Affairs explains that attribution alone does not make every use permissible and that quotation has conditions, including prior publication and a scope justified by the purpose. See the <a href="https://www.bunka.go.jp/seisaku/bunka_gyosei/kibankyoka/faq/index.html" style="color: #0000ff; text-decoration: underline;">Agency for Cultural Affairs' FAQ on legal issues in cultural and artistic activity</a>.</p>
<p>Japan's Personal Information Protection Commission explains that personal information already published online remains protected. Removing a name does not make a record anonymous if a reference URL or specific circumstances still identify the person. See the <a href="https://www.ppc.go.jp/all_faq_index/faq1-q1-5/" style="color: #0000ff; text-decoration: underline;">PPC's FAQ on protection of published personal information</a>.</p>
<p>Do not save names, company names, usernames, contact details, or long copies of request text in your research table. Write only the core problem in your own words. Do not use private requests, proposals, messages, or information covered by confidentiality obligations.</p>
<p>Article 23(15) of CrowdWorks' terms restricts use for commercial activities, or preparation for them, outside work contracted through the service unless approved in writing beforehand. Do not assume this research is permitted; confirm your intended use with the operator. See the <a href="https://crowdworks.jp/pages/agreement" style="color: #0000ff; text-decoration: underline;">CrowdWorks Terms of Use</a>.</p>
<p>Lancers offers non-public requests and keeps project-format proposals private. Check visibility and reuse conditions separately. See <a href="https://www.lancers.jp/faq/C1006/189" style="color: #0000ff; text-decoration: underline;">Lancers' guidance on public and private content</a>.</p>
<p>Being able to view a public page does not automatically mean its content may be used for product research. If that purpose is not clearly permitted, ask the operator or exclude the service from your research sources.</p>
<p><strong>Even where research use is permitted, limit collection to ordinary viewing and anonymized notes.</strong> Do not perform large-scale automated collection, bypass login restrictions, or send sales messages to posters. If you later consider automation, review the service's current terms, technical access rules, and required permissions.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Preserve specificity without preserving the original wording"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Preserve specificity without preserving the original wording">
<h3>Preserve specificity without preserving the original wording</h3>
<div class="table-scroll">
<table>
<thead><tr><th>Person and situation</th><th>Problem summary</th><th>Current workaround</th><th>What still needs validation</th></tr></thead>
<tbody>
<tr><td>A small business processes invoices at month-end</td><td>Moving required fields from differently formatted PDFs into a table takes too long</td><td>Open each file, type the data, and review it later</td><td>Monthly volume, acceptable error rate, and handling of confidential data</td></tr>
<tr><td>A store operator posts announcements to several social networks</td><td>Rewriting copy and resizing images for each channel is repetitive</td><td>Duplicate and edit previous posts</td><td>Channels used, approval flow, and need for scheduled posts</td></tr>
</tbody>
</table>
</div>
<p><em>These are fictional examples created to explain the method. They are not copied from particular requests.</em></p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Remove duplicates, count problems, and score candidates"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Remove duplicates, count problems, and score candidates">
<h2>Remove duplicates, count problems, and score candidates</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/03-cluster-score.png" alt="People grouping similar problem notes and comparing candidate opportunities with scores"></p>
<p>Group problems by whether the same type of person wants the same outcome in the same situation. Even if both involve PDFs, an administrator processing invoices and a student organizing study materials should remain separate candidates.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Separate post counts from cases after deduplication"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Separate post counts from cases after deduplication">
<h3>Separate post counts from cases after deduplication</h3>
<ol>
<li>Mark confirmed reposts or copies on other websites with the original record ID.</li>
<li>Assign one primary problem to each record and sort the table by category.</li>
<li>Count collected entries, confirmed duplicates, and remaining cases in each category. Keep uncertain duplicates in the remaining count and report how many of those cases still need a duplicate check.</li>
<li>Check source types and how often the task occurs. The number of posts and a person's task frequency are different measures.</li>
</ol>
<div class="table-scroll">
<table>
<caption>Fictional example: removing six confirmed duplicates from thirty entries, with no duplicate checks pending</caption>
<thead><tr><th>Problem</th><th>Collected entries</th><th>Duplicates</th><th>Remaining cases</th></tr></thead>
<tbody>
<tr><td>Invoice data entry</td><td>12</td><td>3</td><td>9</td></tr>
<tr><td>Adapting social posts</td><td>10</td><td>2</td><td>8</td></tr>
<tr><td>Sorting shared images</td><td>8</td><td>1</td><td>7</td></tr>
<tr><td>Total</td><td>30</td><td>6</td><td>24</td></tr>
</tbody>
</table>
</div>
<p>These twenty-four cases describe only the material examined. They do not establish twenty-four distinct users or market-wide demand. People who do not post or use these services are missing from the sample.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Score each group from one to five"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Score each group from one to five">
<h3>Score each group from one to five</h3>
<div class="table-scroll">
<table>
<thead><tr><th>Factor</th><th>1 point</th><th>5 points</th></tr></thead>
<tbody>
<tr><td>Repetition</td><td>You saw it once</td><td>It recurs across multiple sources</td></tr>
<tr><td>Severity</td><td>It is mildly annoying</td><td>It blocks work or affects deadlines or losses</td></tr>
<tr><td>Current spending</td><td>You confirmed that people currently spend no money on it</td><td>You confirmed recurring payments for outsourcing or another tool</td></tr>
<tr><td>Access to users</td><td>You cannot reach anyone affected</td><td>Your experience or network lets you interview them</td></tr>
<tr><td>Ability to test small</td><td>It immediately requires large integrations or licenses</td><td>You can test one task, even with manual assistance</td></tr>
</tbody>
</table>
</div>
<p>Use scores from two to four for intermediate cases, with a one-line reason. Mark unsupported factors as unconfirmed rather than giving them one point; investigate them before calculating a total. Fully assessed candidates can score up to twenty-five. This is a comparison method proposed in this article.</p>
<p><strong>A listed budget is a proposed amount, not proof of actual spending.</strong> Even a verified outsourcing payment does not prove willingness to pay for an app. Record proposed budgets, actual payments, and responses to paid trials separately.</p>
<p>Assess risks involving personal data or specialist decisions separately from scores. Exclude even high-scoring candidates if you cannot provide a safe trial.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Compare three fictional candidates"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Compare three fictional candidates">
<h3>Compare three fictional candidates</h3>
<div class="table-scroll">
<table>
<thead><tr><th>Candidate</th><th>Repetition</th><th>Severity</th><th>Current spending</th><th>Access</th><th>Small test</th><th>Total</th></tr></thead>
<tbody>
<tr><td>Create a reviewable list from invoices</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>21</td></tr>
<tr><td>Adapt social posts for each channel</td><td>4</td><td>3</td><td>3</td><td>4</td><td>3</td><td>17</td></tr>
<tr><td>Sort shared images by purpose</td><td>3</td><td>3</td><td>2</td><td>3</td><td>4</td><td>15</td></tr>
</tbody>
</table>
</div>
<p><em>The candidates and scores are fictional. A score of 21 does not predict success.</em></p>
<p>Google Trends can provide supporting evidence of search interest. Search terms cover searches containing the entered words, among other matching rules; topics group related terms across languages. Keep the region, period, and search type consistent when comparing. See <a href="https://support.google.com/trends/answer/4359550?hl=ja" style="color: #0000ff; text-decoration: underline;">Google Trends' guide to comparing search terms</a>.</p>
<p>Google Trends does not show raw search volume. Its values are normalized for time and location and scaled from 0 to 100, while low-volume queries may appear as zero. Use it to explore wording and seasonality, not to declare a winner. See the <a href="https://support.google.com/trends/answer/4365533" style="color: #0000ff; text-decoration: underline;">FAQ about Google Trends data</a>.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Interview five people and ask whether they will try a prototype"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Interview five people and ask whether they will try a prototype">
<h2>Interview five people and ask whether they will try a prototype</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/04-validate.png" alt="A maker and a potential user discussing a simple prototype and the user's real workflow"></p>
<p>Once you have a candidate, interview target users before investing in development. Recruit consenting participants through your network or communities that allow research invitations. Do not send sales messages to crowdsourcing clients outside the platform's rules.</p>
<p>Use the first five interviews to check whether the problem inferred from requests matches people's actual work.</p>
<p>Explain the research purpose and how notes will be used. Obtain consent before recording audio or retaining documents, and check that the person is authorized to share any company materials.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Ask about recent behavior, not whether someone likes your idea"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Ask about recent behavior, not whether someone likes your idea">
<h3>Ask about recent behavior, not whether someone likes your idea</h3>
<ol>
<li>When did you last do this task?</li>
<li>Can you walk me through it from beginning to end?</li>
<li>Which step took the most time, and which was most error-prone?</li>
<li>What do you use today?</li>
<li>How much time or money does the current approach cost?</li>
<li>If possible, can you show the real workflow with personal information hidden?</li>
</ol>
<p>“Would you use this app?” invites a polite yes. Evidence from a recent real event is more useful than a hopeful statement about the future.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Define a pass condition before the interviews"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Define a pass condition before the interviews">
<h3>Define a pass condition before the interviews</h3>
<p>For example, you might set these first-round conditions:</p>
<ul>
<li>Interview five people</li>
<li>At least three experienced the same problem within the last month</li>
<li>At least two agree to show their current workflow or sanitized materials</li>
<li>At least one agrees to a paid trial or a concrete pilot</li>
</ul>
<p>This example assumes a monthly task. Set criteria in advance for your audience and task frequency. Agreement to a free pilot does not prove willingness to pay, so record it separately from paid trials.</p>
<p>If a spreadsheet template or existing automation service already solves the problem well, that is a valid result. Test something smaller than a finished product: perform the service manually once, show a clickable mockup, or collect genuine trial sign-ups. Do not fabricate sign-ups or present unfinished capabilities as complete.</p>
<p>Select up to three credible existing solutions and compare them on the same task with the same fictional data. Record whether they achieve the outcome, setup effort, price, ease of use, data handling, and suitability for continued use. Consider building around the gaps that remain.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Build one end-to-end task, then use evidence to continue, revise, or stop"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Build one end-to-end task, then use evidence to continue, revise, or stop">
<h2>Build one end-to-end task, then use evidence to continue, revise, or stop</h2>
<p><img src="https://www.nanasinogonbei.com/blog/wp-content/uploads/2026/09/05-mvp-measure.png" alt="People testing a small app while the maker decides whether to continue, revise, or stop"></p>
<p>Turn the best-supported workflow into a minimum viable product (MVP): the smallest version that tests its value. In the invoice example, that might be: upload a PDF → receive draft fields → review them → export a table. Accounting integrations and a dedicated mobile app can wait.</p>
<p>Start with fictional invoices. Before accepting real documents, provide access controls that keep each person's data private and define storage and deletion rules. Test support for individual formats and whether the workflow saves time after corrections. This minimum version does not guarantee accounting judgments or the correctness of the content.</p>
<p>Measure:</p>
<ul>
<li>The number and share of first-time users who complete the intended task</li>
<li>The number and share who return within the task's natural cycle—for a monthly task, measure through the following month</li>
<li>Time saved on tasks of comparable volume and difficulty, including review and corrections</li>
<li>The number and proportion of processed fields requiring correction</li>
<li>How many want to continue at the stated price, and how many actually pay</li>
</ul>
<p>If people do not return, the interface may not be the only problem. The task may happen too rarely, the current method may be good enough, or you may be targeting the wrong users. Return to your problem choice before adding features.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Who this method is and is not for"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Who this method is and is not for">
<h3>Who this method is and is not for</h3>
<p>This method suits people exploring repetitive administrative work or operational friction, who can interview affected users and test a narrow workflow.</p>
<p>It is not a good fit for someone who wants to build a fashionable feature immediately without interviews, or to automate medical, financial, or legal decisions without the necessary expertise and safeguards. In regulated or safety-critical fields, expert review and an appropriate operating structure come first.</p>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Your first seven days can be research only"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Your first seven days can be research only">
<h3>Your first seven days can be research only</h3>
<ol>
<li><strong>Day 1:</strong> Choose one field and review each service's terms and visibility rules.</li>
<li><strong>Days 2–3:</strong> Collect about thirty problems from at least two types of sources, excluding identifying information.</li>
<li><strong>Day 4:</strong> Group entries by who struggles, when, and with what, then count cases after removing duplicates.</li>
<li><strong>Day 5:</strong> Organize evidence for the five factors and select up to three candidates to investigate. Turn unconfirmed factors into interview questions.</li>
<li><strong>Day 6:</strong> Run two preliminary interviews and check whether your questions and candidate match the real workflow.</li>
<li><strong>Day 7:</strong> Select one candidate and plan interviews with the remaining three people in your first round of five. If the target audience changes, restart validation with that audience.</li>
</ol>
</section>
<!-- /wp:html -->

<!-- wp:html {"metadata":{"name":"English：Avoid the common failures early"}} -->
<section class="language-panel panel-en" lang="en" aria-label="Avoid the common failures early">
<h3>Avoid the common failures early</h3>
<ul>
<li><strong>Treating one request as a market:</strong> Look for the same problem in another source and from another person.</li>
<li><strong>Building the requested feature literally:</strong> Rewrite it as a situation and a desired outcome.</li>
<li><strong>Stockpiling original text and personal data:</strong> Focus on summaries and dates, and remove information that can identify a person from shared tables.</li>
<li><strong>Pasting confidential material into AI:</strong> Do not enter information that identifies posters or customers, or anything covered by a confidentiality obligation.</li>
<li><strong>Building for weeks before talking:</strong> Start with conversations, a paper mockup, or a manually delivered trial.</li>
<li><strong>Ignoring existing apps:</strong> If an affordable product already solves the problem, deciding not to build is useful progress.</li>
</ul>
<p>Start by defining an audience and research scope, then record ten examples from sources whose conditions of use you have checked. Remove duplicates, count the cases, and ask target users about difficulties left unresolved by existing tools. Use that evidence to decide whether to build a small app.</p>
<p><em>The service terms and official materials were checked on September 28, 2026. This article is not legal advice. Check the latest terms, laws, and permissions for the services and information you use. The illustrations were generated with AI and do not depict real service interfaces or people.</em></p>
</section>
<!-- /wp:html -->
</div>
<!-- /wp:group -->