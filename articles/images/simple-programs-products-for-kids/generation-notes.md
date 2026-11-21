# 挿絵の生成記録

- 日付：2026年11月2日
- 方法：組み込み image_gen（CLI/APIフォールバックは不使用）
- 日英で同じ5枚を使い、本文のaltは各言語に翻訳。
- 以下は実際に送信したプロンプトです。

## 01-pencil-case.png

```text
Use case: illustration-story. Asset type: chapter illustration for a Japanese/English beginner blog about simple software. Primary request: An open pencil case with only two pencils, one eraser and a short ruler, neatly arranged. Beside it a second overfilled pencil case spilling many unnecessary trinkets; a child's hands calmly pick a pencil from the organized case. Convey keeping everything needed while removing unrelated clutter. Style: warm editorial picture-book illustration, hand-painted gouache and subtle pencil texture, uncluttered warm ivory background, muted teal and golden-yellow accents, respectful school-age characters. Composition: wide landscape 3:2 with clear central objects. No text, letters, numerals, logos or watermark. The visual must be understandable in either language.
```

## 02-clear-instructions.png

```text
Use case: illustration-story. Asset type: chapter illustration for a Japanese/English beginner blog about simple software. Primary request: A friendly small toy robot and a child at a school desk, arranging three separate picture cards in a clear left-to-right row: a borrowed book, a calendar, then a bell. Each card has a single clear symbol and arrows connect them. A few tangled ribbon loops at the far edge contrast with the organized cards. Convey instructions whose roles and order are clear. Style: warm editorial picture-book illustration, hand-painted gouache and subtle pencil texture, uncluttered warm ivory background, muted teal and golden-yellow accents, respectful school-age characters. Composition: wide landscape 3:2 with clear central objects. No text, letters, numerals, logos or watermark. The visual must be understandable in either language.
```

## 03-easy-to-use.png

```text
Use case: illustration-story. Asset type: chapter illustration for a Japanese/English beginner blog about simple software. Primary request: A child at a desk with a borrowed library book and a large paper prototype of a phone app: a book icon, a calendar icon and one large save button represented by a check symbol. Next to it is a much busier prototype full of tiny empty form boxes. Convey a calm path for recording a borrowed book and its return date. Style: warm editorial picture-book illustration, hand-painted gouache and subtle pencil texture, uncluttered warm ivory background, muted teal and golden-yellow accents, respectful school-age characters. Composition: wide landscape 3:2 with clear central objects. No text, letters, numerals, logos or watermark. The visual must be understandable in either language.
```

## 04-keep-safety.png

```text
Use case: illustration-story. Asset type: chapter illustration for a Japanese/English beginner blog about simple software. Primary request: A friendly school locker with a clear easy-to-turn handle, its door open enough to reveal an orderly detailed lock mechanism inside. A child places a notebook safely in the locker while an adult maker checks the mechanism. Convey that a simple outside still needs careful safety inside. The lock stays installed; no crime or danger. Style: warm editorial picture-book illustration, hand-painted gouache and subtle pencil texture, uncluttered warm ivory background, muted teal and golden-yellow accents, respectful school-age characters. Composition: wide landscape 3:2 with clear central objects. No text, letters, numerals, logos or watermark. The visual must be understandable in either language.
```

## 05-paper-test.png

```text
Use case: illustration-story. Asset type: chapter illustration for a Japanese/English beginner blog about simple software. Primary request: Two children sitting side by side at a desk testing paper phone screens for a book-return reminder. One follows the screens without guidance while the other notes observations with a pencil. On the desk: one library book, a calendar with abstract marks, three simple paper cards, a pencil. Convey observing a real person to improve a small prototype. Style: warm editorial picture-book illustration, hand-painted gouache and subtle pencil texture, uncluttered warm ivory background, muted teal and golden-yellow accents, respectful school-age characters. Composition: wide landscape 3:2 with clear central objects. No text, letters, numerals, logos or watermark. The visual must be understandable in either language.
```


## Phase 1–2 差し替え記録（一般向け・社会人例への刷新）

- 対象記事：`articles/published/simple-programs-products-for-kids.md`（WordPress投稿ID: 100）
- 小学生・筆箱の例から、デスク引き出し・貸出書籍メモ・ロッカー施錠・成人2人でのペーパーテスト等の一般向け `v2` イラストへ順次差し替え中。

### Phase 1 アップロード済み
- `01-desk-bag-v2.jpg`（Media ID: 134）：`sips` 変換 PNG のアップロード時に SiteGuard Lite WAF が HTTP 403 を返したため、元の `.jpg` をそのままアップロードして採用。
- `02-clear-steps-v2.png`（Media ID: 135）：Phase 1 で生成・PNG変換・アップロード済み。
- `03-simple-screen-v2.png`（Media ID: 136）：Phase 1 で生成・PNG変換・アップロード済み。

### Phase 2a 完了（全5枚差し替え完了）
- `04-locker-safety-v2.jpg`（Media ID: 150）：`sips` 変換 PNG が SiteGuard Lite WAF 403 を返したため、元の `.jpg` を採用してアップロード済み。
- `05-paper-test-v2.png`（Media ID: 151）：生成・PNG変換・アップロード済み。
