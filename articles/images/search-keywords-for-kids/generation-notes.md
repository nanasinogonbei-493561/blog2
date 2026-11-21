# 画像生成メモ

Codex の ImageGen（内蔵ツール）で生成した画像を WebP に変換しました。本文の日英両版で同じ画像を使っています。

## 共通プロンプト

Wide landscape (3:2) editorial illustration for an elementary-school guide to better web searches. Warm ivory paper, textured cut-paper and colored-pencil style, indigo blue with moss green and coral accents, generously spaced large shapes, legible at mobile width, full-bleed composition. Recurring subject: an elementary-school child with dark bobbed hair and a mustard sweater, researching dandelion seeds for a school project. Use stylized, clearly recognizable fluffy white dandelion seedheads. No words, letters, numbers, pseudo-text, logos, borders, or watermarks.

## 章ごとのプロンプト

- `01-question.webp` — At a desk the child looks closely at a dandelion seedhead in a small vase. A single floating white seed drifting on air is framed in a simple thought bubble. A closed laptop and open blank notebook support the story. Emphasize deciding on one question before looking it up.
- `02-keywords.webp` — Overhead view of the child's hands arranging a small row of three large paper cards by a simple laptop. Cards contain only icons: a dandelion puff, one airborne seed, and curling wind lines with a question mark. Emphasize picking a few clues from a question.
- `03-adjust.webp` — The child compares two paths of imaginary search-result picture cards extending from a laptop. In one path a broad mix of flower bouquets, daisy and sunflower pictures becomes focused on dandelion seeds as the child adds a small seed icon card. In the other path a clutter of small filter symbol cards is simplified by sliding one away. Keep the composition uncluttered, with distinct paths and a few objects.
- `04-check.webp` — At the desk the child compares an open illustrated nature book with a botanical garden information page shown on a laptop. Both depict the same recognizable dandelion seed drifting on air. A magnifying glass over the open book emphasizes checking evidence. The book and laptop contain illustrations and blank space only.
- `05-practice.webp` — The child traces a dandelion seed blowing past an open notebook with four visual doodles along the page: a question bubble, three clue cards, a curved retry arrow and an open book with a check mark. Comfortable desk scene, pencil in hand, cheerful but calm. Clear learning sequence.

## Phase 1–2 差し替え記録（一般向け・家電リサイクル法例への刷新）

- 対象記事：`articles/published/search-keywords-for-kids.md`（WordPress投稿ID: 116）
- タンポポ調べ学習の例から、壊れた冷蔵庫の処分（家電リサイクル法）を調べる一般・大人向けの `v2` イラストへ順次差し替え中。既存の `.webp` は Phase 2 での投稿更新まで保持。

### Phase 1 アップロード済み
- `01-question-v2.png`（Media ID: 139）：Phase 1 で生成・PNG変換・アップロード済み。
- `02-keywords-v2.png`（Media ID: 140）：Phase 1 で生成・PNG変換・アップロード済み。

### 視覚検査で除外（不採用）
- `03_adjust_v2_1795136911201.jpg`（Phase 1）：人物の腕が3本ある描画破綻のため不採用。
- `03_adjust_v2_1795155541325.jpg`（Phase 2a）：再び右下に切り離された3本目の手が出現したため不採用。次回再生成時は「手元のみの俯瞰（両手のみ）」または「下段の絞り込み列は手ではなく矢印で整理を示す構図」に変更する。

### Phase 2b 完了（ChatGPT による生成・アップロード済み — 全5枚差し替え完了）
ユーザー指示に基づき、ChatGPT（`https://chatgpt.com/`）上で 1536×1024（3:2 横長）PNG として1枚ずつ生成・ダウンロードし、視覚検査を通過した3枚を WordPress へアップロードして記事本文へ反映済み。
- `03-adjust-v2.png`（Media ID: 158）：過去2回の3本腕破綻を解消するため「手元のみの俯瞰（両手のみ）」構図で生成し合格
- `04-check-v2.png`（Media ID: 159）：パソコンとタブレットの家電リサイクル3段階図を比較する大人イラスト
- `05-practice-v2.png`（Media ID: 160）：ノート左ページに4手順アイコン・右ページにチェックと要点を描く大人イラスト
