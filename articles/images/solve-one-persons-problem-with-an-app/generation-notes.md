# 章ごとの画像生成メモ

- 生成日：2026年10月4日
- 使用方法：imagegen スキルの組み込み image_gen ツール（CLI未使用）
- 用途：各H2に1枚を掲載。日本語版と英語版で同じ画像を使い、altを翻訳。
- 保存先：articles/images/solve-one-persons-problem-with-an-app/
- 各画像は説明用の挿絵です。実在のアプリ画面や実施済みのテストを表しません。
- 2026年10月4日、画像6枚をWordPressメディアへアップロードしました（ID 55〜60）。記事の本文画像参照を実際のメディアURLへ置き換え、アイキャッチにID 55を使用しています。
- 2026年10月4日、記事をWordPressへdraftとして送信しました（投稿ID 61）。当日は公開していません。
- 保存後にREST APIから下書きを読み取り、draft状態、日英各6章の画像、青色・下線リンク、言語切り替えのCSSと入力要素が保持されていることを確認しました。Chromeの操作が許可されなかったため、実画面での切り替え操作は未確認です。
- 2026年10月6日、日英の導入と各見出しを20個の独立したグループへ分割しました。画像12か所を標準の画像ブロックに変換し、幅100％・高さ自動に設定しました。APIで保存後の本文・画像幅・リンク色・言語切り替え用の構造を確認しました。ユーザーの希望により、この修正後の確認はAPIのみです。
- 同日、ユーザーによる確認と公開指示を受け、投稿ID 61をpublishへ変更しました。公開APIと記事URLが認証なしで取得できることを確認しました。
- 公開URL：https://www.nanasinogonbei.com/blog/2026/10/06/solve-one-persons-problem-with-an-app/
- 公開済みの記事ファイル：articles/published/solve-one-perrsons-problem-with-an-app.md

## 01-listen.png

保存先：`articles/images/solve-one-persons-problem-with-an-app/01-listen.png`

最終プロンプト：

```text
Use case: illustration-story
Asset type: chapter illustration for a Japanese/English everyday problem-solving blog article.
Primary request: Two adults at a kitchen table, one describing a frustrating everyday errand while the other listens and writes on a notebook. A smartphone, a few unlabelled sticky notes and a small calendar suggest trying to remember things to return. Emphasize listening to ONE person's real difficulty.
Style/medium: polished editorial illustration, gentle hand-drawn shapes, subtle paper texture, off-white background, muted teal and warm orange accents, natural human proportions, calm and relatable.
Composition/framing: single landscape 3:2 illustration, generous margins, clear central subjects, no collage.
Constraints: NO text, letters, numbers, branding, watermark, real product UI or identifiable real people. Icons only. This is an illustrative concept, not a screenshot.
```

## 02-ideas.png

保存先：`articles/images/solve-one-persons-problem-with-an-app/02-ideas.png`

最終プロンプト：

```text
Use case: illustration-story
Asset type: chapter illustration for a Japanese/English everyday problem-solving blog article.
Primary request: One adult at a desk consulting a laptop displaying an abstract friendly conversation with an AI. Three distinct illustrated sticky note ideas on desk: a reminder bell, an organized list, a returned package. Emphasize choosing a small idea grounded in daily inconvenience.
Style/medium: polished editorial illustration, gentle hand-drawn shapes, subtle paper texture, off-white background, muted teal and warm orange accents, natural human proportions, calm and relatable.
Composition/framing: single landscape 3:2 illustration, generous margins, clear central subjects, no collage.
Constraints: NO text, letters, numbers, branding, watermark, real product UI or identifiable real people. Icons only. This is an illustrative concept, not a screenshot.
```

## 03-alternatives.png

保存先：`articles/images/solve-one-persons-problem-with-an-app/03-alternatives.png`

最終プロンプト：

```text
Use case: illustration-story
Asset type: chapter illustration for a Japanese/English everyday problem-solving blog article.
Primary request: One adult calmly comparing three existing ways to remember errands on a desk: paper notebook, smartphone task checklist, simple laptop spreadsheet. Different tools have equal visual weight, no ranking or winning product. Emphasize considering existing options before making an app.
Style/medium: polished editorial illustration, gentle hand-drawn shapes, subtle paper texture, off-white background, muted teal and warm orange accents, natural human proportions, calm and relatable.
Composition/framing: single landscape 3:2 illustration, generous margins, clear central subjects, no collage.
Constraints: NO text, letters, numbers, branding, watermark, real product UI or identifiable real people. Icons only. This is an illustrative concept, not a screenshot.
```

## 04-prototype.png

保存先：`articles/images/solve-one-persons-problem-with-an-app/04-prototype.png`

最終プロンプト：

```text
Use case: illustration-story
Asset type: chapter illustration for a Japanese/English everyday problem-solving blog article.
Primary request: Two adults testing a tiny smartphone web app prototype together. The simple abstract screen has three fields represented by grey lines, a calendar icon and a completion checkmark, with a parcel beside it. One adult taps, the other observes and notes what happens. Emphasize one task solved by a small prototype.
Style/medium: polished editorial illustration, gentle hand-drawn shapes, subtle paper texture, off-white background, muted teal and warm orange accents, natural human proportions, calm and relatable.
Composition/framing: single landscape 3:2 illustration, generous margins, clear central subjects, no collage.
Constraints: NO text, letters, numbers, branding, watermark, real product UI or identifiable real people. Icons only. This is an illustrative concept, not a screenshot.
```

## 05-share.png

保存先：`articles/images/solve-one-persons-problem-with-an-app/05-share.png`

最終プロンプト：

```text
Use case: illustration-story
Asset type: chapter illustration for a Japanese/English everyday problem-solving blog article.
Primary request: A maker at a laptop offers their small web app to a few other adults on phones in separate locations, linked through an abstract central web cloud. A simple checklist and small lock by the cloud represent limited pilot use and care of data. Emphasize providing a small app through an external hosting service, no logos.
Style/medium: polished editorial illustration, gentle hand-drawn shapes, subtle paper texture, off-white background, muted teal and warm orange accents, natural human proportions, calm and relatable.
Composition/framing: single landscape 3:2 illustration, generous margins, clear central subjects, no collage.
Constraints: NO text, letters, numbers, branding, watermark, real product UI or identifiable real people. Icons only. This is an illustrative concept, not a screenshot.
```

## 06-next-step.png

保存先：`articles/images/solve-one-persons-problem-with-an-app/06-next-step.png`

最終プロンプト：

```text
Use case: illustration-story
Asset type: chapter illustration for a Japanese/English everyday problem-solving blog article.
Primary request: One adult writes one concrete next step on a notebook beside a phone, while a nearby second person offers feedback. Three small symbolic stepping stones with ear, simple phone app and sharing icons suggest listen, try, share. Calm practical ending, not triumphant or promotional.
Style/medium: polished editorial illustration, gentle hand-drawn shapes, subtle paper texture, off-white background, muted teal and warm orange accents, natural human proportions, calm and relatable.
Composition/framing: single landscape 3:2 illustration, generous margins, clear central subjects, no collage.
Constraints: NO text, letters, numbers, branding, watermark, real product UI or identifiable real people. Icons only. This is an illustrative concept, not a screenshot.
```
