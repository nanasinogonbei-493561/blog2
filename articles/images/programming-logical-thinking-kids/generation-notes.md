# Chapter illustration generation notes

- Generated with the built-in image_gen tool (imagegen skill), 2026-10-27.
- Five chapter illustrations; reused in the matching Japanese and English chapters with translated alt text.
- Outputs were inspected visually in the generation results, then copied into this directory.
- The five images were later uploaded to WordPress (media IDs 88–92) and included in the article published on 2026-10-27. Featured media ID: 88.

## 01-reasons.png

Use case: illustration-story. Asset type: chapter illustration for a Japanese and English blog explaining programming and reasoning to elementary-school readers. Primary request: A child looks out a window at rain, then chooses an umbrella beside the door, visually connecting observed rain with the decision to keep dry. Style: clear friendly editorial storybook illustration, soft navy outlines, warm cream paper background, muted teal and yellow accents. Wide landscape composition, uncluttered, suitable for all ages. No written text, no letters, no logos, no watermark. This is one coherent scene, not a poster or a collage.

Original generated filename: `exec-92d23c90-467c-4b5f-a333-d26dad0b6cda.png`.

## 02-backpack.png

Use case: illustration-story. Asset type: chapter illustration about precise instructions. Primary request: A child and a small friendly toy-like robot check a school backpack on a table; one notebook is already inside the open backpack and another school item is on the table. The child points to a simple picture checklist, showing checking what is already packed before adding a missing item. Clear friendly editorial storybook illustration, soft navy outlines, warm cream background, muted teal and yellow accents. Wide landscape composition, uncluttered. No written text, no letters, no logos, no watermark. A single coherent scene.

Original generated filename: `exec-30d2efc9-4c4d-438d-8bc9-9e172ea89c38.png`.

## 03-practice.png

Use case: illustration-story. Asset type: chapter illustration about practicing reasoning through programming. Primary request: A child arranges three pictorial instruction cards beside a laptop, predicts what a small robot will do, then compares the robot's movement on a simple tabletop path with the cards. Emphasize thoughtful checking, not instant success or magic. Clear friendly editorial storybook illustration, soft navy outlines, warm cream background, muted teal and yellow accents. Wide landscape composition, uncluttered. No written text, no letters, no logos, no watermark. A single coherent scene.

Original generated filename: `exec-80edf0d3-9fbe-4139-94b2-144a731f9519.png`.

## 04-test.png

Use case: illustration-story. Asset type: chapter illustration about finding errors by trying different cases. Primary request: A child with a notebook carefully checks three small school pencil cases on a desk: one empty case, one holding a single pencil, one with several pencils. A laptop alongside has abstract simple blocks without text. Show observation and comparing the cases, calm curiosity. Clear friendly editorial storybook illustration, soft navy outlines, warm cream background, muted teal and yellow accents. Wide landscape composition, uncluttered. No written text, no letters, no logos, no watermark. A single coherent scene.

Original generated filename: `exec-2dc4a123-7a81-4fca-ad73-cb2c9c9fd972.png`.

## 05-first-step.png

Use case: illustration-story. Asset type: closing chapter illustration about a first reasoning exercise. Primary request: A child uses a pencil to draw a few picture-only steps in an open notebook for checking tomorrow's school supplies; a school backpack and a few books are nearby. Calm encouraging mood, focused on starting small on paper. Clear friendly editorial storybook illustration, soft navy outlines, warm cream background, muted teal and yellow accents. Wide landscape composition, uncluttered. No written text, no letters, no logos, no watermark. A single coherent scene.

Original generated filename: `exec-f342f5bd-fe19-4505-8d09-431221deecb4.png`.


## Phase 1–2 差し替え記録（一般向け・社会人例への刷新）

- 対象記事：`articles/published/programming-logical-thinking-kids.md`（WordPress投稿ID: 93）
- 子ども向けイラストを一般・社会人向け（外出時の傘判断、通勤バッグの準備、コーヒー在庫、0〜3の境界チェック等）の `v2` イラストへ順次差し替え中。既存の Phase 0 画像は Phase 2 での記事本体更新完了まで保持。

### Phase 1 アップロード済み
- `01-umbrella-decision-v2.png`（Media ID: 132）：傘を持っていくかの判断シーン
- `03-predict-check-v2.png`（Media ID: 133）：条件分岐・在庫チェック等の一般向けイラスト

### 視覚検査で除外（不採用）
- `02_packing_steps_v2_1795136897846.jpg`：人物の頭部が切れていたため不採用。

### Phase 2a 完了（全5枚差し替え完了）
- `02-packing-steps-v2.png`（Media ID: 147）：余裕ある構図で再生成・PNG変換・アップロード済み。
- `04-debug-cases-v2.jpg`（Media ID: 148）：`sips` 変換 PNG が SiteGuard Lite WAF 403 を返したため、元の `.jpg` を採用してアップロード済み。
- `05-paper-rule-v2.png`（Media ID: 149）：生成・PNG変換・アップロード済み。
