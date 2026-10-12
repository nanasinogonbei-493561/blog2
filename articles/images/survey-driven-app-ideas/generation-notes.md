# 画像生成と確認メモ

- 作成日: 2026-10-12（Asia/Tokyo）
- 使用: imagegen スキル、組み込み image_gen ツール（CLI未使用）
- 保存先: articles/images/survey-driven-app-ideas/
- 6章それぞれに生成画像を1枚配置し、日英で同じ画像を使用。altは両言語で記載。
- 画像を目視確認済み。実在の画面・調査結果としては扱わない。

## 最終プロンプト

### 01-questions.png

```text
Use case: illustration-story. Asset type: landscape chapter illustration for a Japanese/English general-reader blog about using surveys to plan a homemade app. Primary request: An adult planning a short everyday survey at a wooden desk: a laptop with generic radio circles and blank paragraph fields, beside handwritten-looking blank note cards and an open calendar; two distinct visual types, choices and stories. Style: warm editorial illustration with soft paper texture, muted teal and ochre accents, off-white background, natural adult proportions, clear uncluttered composition, landscape 3:2. No readable text, numbers, logos, brand marks, watermarks, realistic product screenshots, or claims about survey results. Conceptual illustration, not an actual interface.
```

### 02-form-settings.png

```text
Use case: illustration-story. Asset type: landscape chapter illustration for a Japanese/English general-reader blog about using surveys to plan a homemade app. Primary request: An adult reviewing a generic online survey on a laptop and checking the same survey on a smartphone, with a small closed padlock and sealed envelope on the desk, evoking careful sharing and private responses. Style: warm editorial illustration with soft paper texture, muted teal and ochre accents, off-white background, natural adult proportions, clear uncluttered composition, landscape 3:2. No readable text, numbers, logos, brand marks, watermarks, realistic product screenshots, or claims about survey results. Conceptual illustration, not an actual interface.
```

### 03-sort-ideas.png

```text
Use case: illustration-story. Asset type: landscape chapter illustration for a Japanese/English general-reader blog about using surveys to plan a homemade app. Primary request: An adult sorting survey response cards into three clusters on a desk, with a small non-numeric bar chart beside a few speech-bubble cards, then selecting one cluster with a simple outline ring. Style: warm editorial illustration with soft paper texture, muted teal and ochre accents, off-white background, natural adult proportions, clear uncluttered composition, landscape 3:2. No readable text, numbers, logos, brand marks, watermarks, realistic product screenshots, or claims about survey results. Conceptual illustration, not an actual interface.
```

### 04-existing-tools.png

```text
Use case: illustration-story. Asset type: landscape chapter illustration for a Japanese/English general-reader blog about using surveys to plan a homemade app. Primary request: An adult comparing three everyday ways to remember borrowed items: a paper note with book icon, a calendar with a small book icon, and a generic smartphone task checklist; borrowed books sit alongside, thoughtful calm scene. Style: warm editorial illustration with soft paper texture, muted teal and ochre accents, off-white background, natural adult proportions, clear uncluttered composition, landscape 3:2. No readable text, numbers, logos, brand marks, watermarks, realistic product screenshots, or claims about survey results. Conceptual illustration, not an actual interface.
```

### 05-small-app.png

```text
Use case: illustration-story. Asset type: landscape chapter illustration for a Japanese/English general-reader blog about using surveys to plan a homemade app. Primary request: An adult sketching a tiny return-items app on paper and matching it to a generic smartphone prototype, showing only book item icon, location pin, calendar and a completion check, no other functions; cozy desk. Style: warm editorial illustration with soft paper texture, muted teal and ochre accents, off-white background, natural adult proportions, clear uncluttered composition, landscape 3:2. No readable text, numbers, logos, brand marks, watermarks, realistic product screenshots, or claims about survey results. Conceptual illustration, not an actual interface.
```

### 06-try-improve.png

```text
Use case: illustration-story. Asset type: landscape chapter illustration for a Japanese/English general-reader blog about using surveys to plan a homemade app. Primary request: Two adults seated together, one trying a small generic borrowed-item checklist on a smartphone while the other takes notes, a borrowed book on the desk, a simple loop arrow on a blank note suggesting try and improve. Style: warm editorial illustration with soft paper texture, muted teal and ochre accents, off-white background, natural adult proportions, clear uncluttered composition, landscape 3:2. No readable text, numbers, logos, brand marks, watermarks, realistic product screenshots, or claims about survey results. Conceptual illustration, not an actual interface.
```

## 初稿作成時の確認

- AGENTS.md、CONTENT_STRATEGY.md、prompts/article.md、config/blog.yaml、prompts/review.mdを確認。
- 前回記事: articles/published/solve-one-perrsons-problem-with-an-app.md（Front Matterに保存された公開URLを使用）。公開ページのブラウズ取得は失敗したため、オンライン疎通確認済みとは扱わない。
- サブドメイン付き自作アプリのURLはリポジトリのMarkdown・設定内で確認できず、掲載しなかった。
- Googleフォームの質問形式・公開共有・回答保存とGoogle ToDo リストの操作は公式ヘルプで確認。参照リンクは本文の該当箇所に配置。
- 本文にH1なし。各言語でH2を6章、章ごとに画像あり。
- 一般ユーザー向けに定量・定性を説明。質問ひな形、分母付き集計例、回答→案の対応表、既存の方法3候補、設計メモ、開発相談文、試用手順を掲載。
- 調査結果・数字・アプリ案は架空と明示。メール収集・結果概要共有・閲覧権限・回答重複・対象の偏りを説明。
- statusはdraft。WordPressへの投稿、画像アップロード、既存記事更新は行っていない。
- 投稿スクリプトのdry-run成功。日英各6章・6画像、全14リンクの青色と下線のインライン指定、日英の出典URL一致、画像ファイルの存在、HTMLのタグ対応、128文字のexcerptを確認。
- ローカルプレビューで初期表示が日本語であることと、English→日本語の往復切り替えを実操作で確認。画面上で前回記事リンクの青色・下線を確認。
- レビューで対象外の人が必須質問に阻まれないよう修正。ひな形は質問1のみ必須、質問2〜8は任意と日英両方に明記。
- 本文画像は記事ファイルからの相対パス。将来WordPressへ送信するときは画像をアップロードしてURLを置換し、言語切り替え・青色リンクが実サイトで保持されるか再確認する。

## レビュー・投稿後の状態

- レビュー修正、画像アップロード、draft送信を経て、ユーザーの公開指示により投稿ID 76をpublishへ変更。
- 公開記事: https://www.nanasinogonbei.com/blog/2026/10/12/survey-driven-app-ideas/
- 本文とメタデータの保存先: articles/published/survey-driven-app-ideas.md
- 画像ID 70〜75とURLは記事のFront Matterへ保存し、本文の日英各6か所に反映。アイキャッチは70を再利用。
- 言語切り替えをWordPress標準タブへ変更し、見出し・画像・章のブロックを整備。公開ページで日本語初期表示、日英の往復切り替え、青色・下線付きリンクを確認。
- 詳細な修正・検証の記録: articles/drafts/codex/survey-driven-app-ideas.review.md
