---
name: deep-audit
description: システム整合性の完全監査 — 全データファイルの一貫性チェック、壊れた参照の検出、古いデータの特定、スキル間の矛盾を発見。スクリプトベースの自動チェック。
---

# Deep Audit — システム完全監査

全データファイル・スキル間の整合性を自動チェックする。

## 起動条件

- `/deep-audit` — 完全監査
- `/deep-audit fix` — 検出された問題を自動修正

## 監査フロー

### Step 1: データファイル検証

以下のファイルを順番にチェックする:

```bash
# 各ファイルの存在・構造・鮮度を確認
DATA_DIR=~/.content-autopilot

files=(
  "profile.json"
  "content-history.json"
  "content-dna.json"
  "active-series.json"
  "algorithm-guide.json"
  "best-times.json"
  "brand-voice.json"
  "monetize-data.json"
  "hook-library.json"
  "ab-tests.json"
  "hashtag-sets.json"
  "content-bank.json"
  "content-genome.json"
  "pipeline-state.json"
)
```

各ファイルについて:
- **存在チェック**: ファイルがあるか
- **JSON妥当性**: パース可能か
- **必須フィールド**: version, 主要フィールドが存在するか
- **鮮度チェック**: 最終更新が30日以上前 → STALE警告

### Step 2: クロスリファレンスチェック

```
content-history ↔ vault      — 履歴で参照されたファイルがvaultに存在するか
content-history ↔ performance — パフォーマンスデータが欠落しているエントリ
active-series ↔ content-history — シリーズエントリの整合性
hook-library ↔ content-dna   — スコアリングされていないフック
ab-tests ↔ content-history   — 結果が未反映のABテスト
```

### Step 3: フィードバックループ検証

```
perf-log → content-dna      — パフォーマンスがDNAに反映されているか
ab-test → content-dna       — ABテスト結果がDNAに反映されているか
post-mortem → hook-library   — 振り返りがフックに反映されているか
confidence calibration       — 最後のキャリブレーションからの日数
```

### Step 4: スクリプト動作チェック

```bash
# 各スクリプトの基本動作を確認
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/autopilot.py --mode execute 2>&1
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/grader.py --help 2>&1
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/pre_publish.py --help 2>&1
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/record_history.py --help 2>&1
```

各スクリプトがエラーなく実行可能かチェック。

## レポート形式

```
============================================
  System Deep Audit — システム監査レポート
============================================

データファイル:
  [OK] profile.json — 有効、完全
  [OK] content-history.json — {N}エントリ、孤立なし
  [古] content-dna.json — {N}日前に更新（{N}件の新エントリが未反映）
  [OK] algorithm-guide.json — {N}日前に更新
  [無] best-times.json — 未作成（/best-time で作成）
  [OK] monetize-data.json — {N}エントリ

クロスリファレンス:
  [OK] content-history ↔ vault — 参照ファイル全て存在
  [NG] content-history ↔ performance — {N}エントリのパフォーマンスデータ欠落
  [OK] active-series ↔ content-history — シリーズ整合
  [NG] hook-library ↔ content-dna — {N}フック未スコアリング

フィードバックループ:
  [OK] perf-log → content-dna: 接続済み
  [NG] ab-test → content-dna: {N}件の結果未反映
  [OK] post-mortem → hook-library: 接続済み
  [NG] confidence calibration: 最終キャリブレーションから{N}日経過

スクリプト動作:
  [OK] autopilot.py — 正常（実行マニフェスト出力確認）
  [OK] grader.py — 正常
  [OK] pre_publish.py — 正常
  [OK] record_history.py — 正常

問題: {count} | 警告: {count} | 正常: {count}

自動修正可能: {N}件。/deep-audit fix で修正
============================================
```

## 自動修正（`/deep-audit fix`）

以下の問題は自動修正可能:

| 問題 | 修正アクション |
|------|--------------|
| 欠落ファイル | デフォルト構造で新規作成 |
| 不正JSON | バックアップ作成 → 修復試行 |
| STALEデータ | 関連スキルの再実行を推奨（自動実行はしない） |
| 未スコアリングフック | content-dnaの再計算をトリガー |
| 未反映ABテスト | content-dnaへの結果反映を実行 |
| パフォーマンスデータ欠落 | 空のperformanceエントリを追加（手動入力待ち） |

自動修正できない問題はリストアップして報告。

## 連携スキル

- confidence-score — キャリブレーション再実行のトリガー
- feedback-loop-status — フィードバックループ状態の詳細
- content-dna — DNA再計算
- performance-log — パフォーマンスデータ入力
