# 画像生成メモ（YouTask 構想記事）

- 対象記事：`articles/published/youtask-youtube-task-management.md`（旧保存先：`articles/drafts/youtask-youtube-task-management.md`、WordPress投稿ID: 173、`status: publish`、公開URL: https://www.nanasinogonbei.com/blog/2026/11/22/youtask-youtube-task-management/）
- 方針：各 H2 章（全6章）に1枚ずつ一般向けイラストを配置し、`01-problem-handwritten.jpg` をアイキャッチ画像としても設定する。
- 日英両版で同じ画像を使用し、`alt` 属性は日本語・英語それぞれに合わせて記述している。

## Codex での再生成・JPEG変換・アップロード記録（2026年11月21日）

- 生成方法：Codex CLI `0.169.1`（`/Applications/ChatGPT.app/Contents/Resources/codex-cli/CodexCLI.app/Contents/MacOS/codex exec`、`gpt-6.2-sol`、組み込み `image_gen.imagegen` ツール使用、Python描画・外部CLIフォールバック不使用）。
- 出力サイズ：6枚すべて `1536 × 1024`（3:2 横長）PNG として生成され、視覚検査を通過。
- WordPress 送信時の対応：`1536 × 1024` PNG のアップロード時にサーバー側 SiteGuard Lite WAF が HTTP 403 を返したため、`/usr/bin/sips` で同解像度の JPEG へ変換した（既存記事の運用と同様）。`02-three-phases.jpg` のみ品質 88 でも HTTP 403 が出たため、品質 85 へ再エンコードしてアップロードを通過させた（`01`/`03`/`04`/`05`/`06` は品質 88）。古い試作 PNG（Media ID: 167〜172）から記事内参照をすべて差し替え済み。

## 共通プロンプト

Wide landscape (3:2) editorial illustration for a general-audience guide. Warm ivory paper background, textured colored-pencil / gouache & cut-paper editorial style, calm indigo/teal blue with warm amber/coral and sage green accents, generously spaced uncluttered shapes, legible at mobile width, full-bleed composition. Strictly no words, letters, numbers, Japanese characters, pseudo-text, logos, YouTube brand logo marks (use a generic play-triangle frame), borders, or watermarks. Clean natural two-arm/two-hand anatomy.

## 章ごとの画像・生成元・WordPress登録結果

- `01-problem-handwritten.jpg`（WordPress Media ID: 175、アイキャッチ兼 第1章、品質88 JPEG、生成元 `exec-6b4485a9-e82d-4009-878f-3a845863166d.png`）: 木の机で開いたノート・無地付箋・汎用再生アイコン付きノートPCを見る大人。文字・ロゴ・手の破綻なし（合格）。
- `02-three-phases.jpg`（WordPress Media ID: 176、第2章、品質85 JPEG、生成元 `exec-fe186605-4261-4669-bbef-00246533a7a5.png`）: 公開前（電球と視聴者アイコン）→ 公開中（3本棒グラフと汎用再生アイコン）→ 公開後（2方向道標と閉じる扉）の3枚カード構成。文字・記号破綻なし（合格）。
- `03-input-and-tags.jpg`（WordPress Media ID: 177、第3章、品質88 JPEG、生成元 `exec-13ced081-0b53-40fc-bc4a-d0b9b89e7894.png`）: 汎用再生アイコン付きノートPCの横で棒グラフカード・短い横線カード・穴あき無地タグを並べる両手俯瞰。左右2本の手・指の本数・文字なしともに問題なし（合格）。
- `04-compare-tools.jpg`（WordPress Media ID: 178、第4章、品質88 JPEG、生成元 `exec-9f2f000e-5b5c-4ec5-8de5-efb068ad3af1.png`）: 表計算グリッド＋右上折れ線、横長メモ＋無地タグピル、3列カンバンボードの3画面を同じ大きさ・重みで並べた比較図。順位や文字なし（合格）。
- `05-who-it-fits.jpg`（WordPress Media ID: 179、第5章、品質88 JPEG、生成元 `exec-079ebd6c-18e2-4dfa-a8de-7a1074596ba9.png`）: 左側の落ち着いた1人用画面と、右側の3人チーム共有ボード・カレンダーの対比イラスト。人物の腕・指・表情・文字なしともに問題なし（合格）。
- `06-next-steps.jpg`（WordPress Media ID: 180、第6章、品質88 JPEG、生成元 `exec-7677158f-8e34-4e67-a7e8-0d887d4f2ef3.png`）: 朝の机で電球・棒グラフ・道標の3段構成ノートを開く手元とマグカップ・ノートPC。手の描写・文字なしともに問題なし（合格）。
