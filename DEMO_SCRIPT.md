# Content Autopilot - 3分デモ動画台本

> **ハッカソンテーマ**: 「一度命じたら、あとは任せろ」
> **審査配点**: Autonomy (40%) + Quality (35%) + Impact (25%)
> **動画尺**: 3:00 厳守

---

## 収録前の準備

### 環境設定

```bash
# iTerm2の設定
# - テーマ: ダークテーマ（Solarized Dark または Minimal）
# - フォントサイズ: 18pt以上（審査員がスマホで見る可能性あり）
# - ウィンドウサイズ: 1280x720 以上
# - Preferences > Profiles > Text > Font size: 18

# 不要な通知をオフにする
# macOS: システム設定 > 通知 > 「おやすみモード」ON
# Slack/Discord等を終了

# ターミナルをクリーンにする
clear
```

### データリセット（クリーンデモ用）

```bash
# 既存データをバックアップして削除（初回実行を見せるため）
mv ~/.content-autopilot ~/.content-autopilot.bak 2>/dev/null
rm -rf ~/Desktop/content-autopilot-output 2>/dev/null

# ※収録後に戻す場合:
# mv ~/.content-autopilot.bak ~/.content-autopilot
```

### 画面収録ツール

- **推奨**: OBS Studio（無料）または macOS標準の画面収録（Cmd+Shift+5）
- **解像度**: 1920x1080 or 1280x720
- **FPS**: 30fps
- **音声**: マイク入力でナレーション同時録音（後付けでもOK）
- **Tips**: 収録中はマウスカーソルを大きくする（システム設定 > アクセシビリティ > ディスプレイ > カーソルサイズ）

---

## シーン1: オープニング（0:00 - 0:15）

### 画面に映すもの

ターミナル全画面。事前に以下を表示しておく:

```bash
# ターミナルに以下をタイプして表示（echoで事前表示してもOK）
echo ""
echo "  Content Autopilot"
echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  129 skills | 12 Python scripts | 3 platforms | Zero intervention"
echo ""
```

### ナレーション（日本語）

> Content Autopilot。
> 「一度命じたら、あとは任せろ」を文字通り実現する、完全自律型コンテンツ生成プラグインです。
> 129のスキル、12本のPythonスクリプト。人間が介入するのは、最初の1コマンドだけ。

### タイミング

| 時刻 | 動作 |
|------|------|
| 0:00 | 画面表示、ナレーション開始 |
| 0:05 | 「129 skills...」の行を指さす（カーソルで強調） |
| 0:13 | 一拍置いて次のシーンへ |

---

## シーン2: 課題提起（0:15 - 0:30）

### 画面に映すもの

ターミナルに以下をタイプ（またはスライド画像を表示）:

```bash
echo ""
echo "  [問題] コンテンツ継続の壁"
echo ""
echo "    毎日のネタ探し .............. 30-60分"
echo "    3プラットフォーム別の書き分け .. 2-3時間"
echo "    品質チェック ................ 手動・属人的"
echo "    ファネル設計 ................ 概念は知ってるが実行できない"
echo ""
echo "  → 合計: 1日3-4時間。しかも品質にムラがある。"
echo ""
```

### ナレーション（日本語）

> コンテンツマーケティングの現実。
> 毎日のネタ探しに30分、3つのプラットフォームへの書き分けに2〜3時間、品質チェックは手動で属人的。
> これを、1コマンドでゼロにします。

### タイミング

| 時刻 | 動作 |
|------|------|
| 0:15 | 課題の行が順番に表示される演出（echoを1行ずつ実行するか、事前表示） |
| 0:28 | 「これを、1コマンドでゼロにします」と言いながら次のシーンへ |

---

## シーン3: ワンコマンドデモ（0:30 - 2:00）

**ここがデモの核心。90秒で全パイプラインを見せる。**

### 画面に映すもの

Claude Codeのターミナル画面。

### 手順とナレーション

#### Step 3-1: コマンド入力（0:30 - 0:40）

```
# Claude Codeのプロンプトで以下を入力:
/daily-autopilot
```

**ナレーション**:

> 実行するのは、この1コマンドだけです。
> `/daily-autopilot`。ここから先、人間は何もしません。見ているだけです。

**Tips**: タイプする瞬間を見せる。ゆっくり打つ。Enterを押す瞬間に一拍置く。

---

#### Step 3-2: プロフィール自動生成（0:40 - 0:50）

画面に表示されるもの（パイプラインの出力）:

```
━━━━ Content Autopilot ━━━━━━━━━━━━━━━━━━
[1/8] Profile loaded (auto-created: default)
      Theme: "AI x ビジネス" | Stage: TOFU
```

**ナレーション**:

> まずプロフィール。初回なので存在しませんが、システムが自動生成しました。
> セットアップは不要。ゼロコンフィグです。これが最初の自律判断ポイントです。

**強調ポイント**: 「auto-created」の文字をカーソルで指す。

---

#### Step 3-3: ファネル分析 + トレンド検索（0:50 - 1:10）

画面に表示されるもの:

```
[2/8] Funnel analysis: TOFU 0% → target 50% ↑adjust
      Decision: TOFU trending selected
[3/8] WebSearch: 3 candidates found
      → "AIで月10時間の作業削減" (score: 0.92) ← selected
      → "ChatGPT新機能まとめ" (score: 0.71)
      → "AI導入の失敗例" (score: 0.65)
```

**ナレーション**:

> 次にファネル分析。過去の履歴からTOFU・MOFU・BOFUのバランスを計算し、
> 今日はTOFUが不足しているから、TOFUコンテンツを作ると自動判断しました。
>
> そしてWebSearchでトレンドを調査。3つの候補から、最もエンゲージメントが期待できるトピックを
> スコアリングして自動選択しています。
> 注目してください。人間はトピックを選んでいません。システムが選んでいます。

**強調ポイント**:
- 「Decision: TOFU trending selected」 → ファネル判断の自律性
- 「← selected」 → トピック選択の自律性
- 「score: 0.92」 → スコアリングによる定量的判断

---

#### Step 3-4: コンテンツ同時生成（1:10 - 1:20）

画面に表示されるもの:

```
[4/8] Generating: note(3,200字) + X(6tweets) + IG
```

**ナレーション**:

> 3プラットフォーム同時生成。note、X、Instagram。
> それぞれのプラットフォームに最適化されたコンテンツが一度に作られます。

---

#### Step 3-5: 品質ゲート + 自動改善（1:20 - 1:40）

画面に表示されるもの:

```
[5/8] Quality gate:
      note: 64/100 → auto-improving hook...
      note: 82/100 ✓ (improved +18)
      X: 78/100 ✓
      IG: 75/100 ✓
```

**ナレーション**:

> ここが最大の差別化ポイントです。6軸の品質採点が自動で走ります。
> Hook、Readability、Structure、Platform Fit、CTA、AI Smell。
>
> 注目してください。noteのスコアが64点で閾値の70点を下回りました。
> 普通のツールならここでユーザーに修正を求めます。
> しかしContent Autopilotは違います。何が悪いかを自分で特定し、自動で改善しました。
> 64点から82点へ、プラス18点の改善。人間は何もしていません。

**強調ポイント**: ここが最重要。「auto-improving」と「improved +18」を強調。
**カーソル動作**: 64→82の変化を指し示す。

---

#### Step 3-6: プレパブリッシュ + 記録 + ダッシュボード（1:40 - 2:00）

画面に表示されるもの:

```
[6/8] Pre-publish: 5/5 checks passed ✓
[7/8] History recorded: entry 2026-03-21
[7.5] Dashboard generated → opening in browser...
[8/8] Pipeline complete ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

--- Intelligence Report ---
Total runs: 1 | Avg quality: 78 → Today: 78 (—)
Best title logic: N/A (need 3 more runs)
Quality trend: N/A (need 2 more runs)
Funnel health: TOFU 100% / MOFU 0% / BOFU 0% (initial run)
```

**ナレーション**:

> 8項目のプレパブリッシュチェックを全パス。
> 履歴を自動記録し、HTMLダッシュボードが自動生成されてブラウザで開きました。
>
> そしてIntelligence Report。実行を重ねるほどデータが蓄積され、
> どのタイトルパターンが効果的か、品質トレンドは上昇しているか、
> ファネルのバランスは取れているか、すべて可視化されます。

**ブラウザ切り替え**: ダッシュボードのHTMLがブラウザで開いている画面を2〜3秒見せる。
ダッシュボードの以下を指す:
- Intelligence Reportのカード群（Total Runs, Quality, Trend, Streak）
- Quality Scoresのバーチャート
- Funnel Balanceの横棒グラフ（Actual vs Target）

---

## シーン4: アーキテクチャ（2:00 - 2:30）

### 画面に映すもの

ターミナルに戻り、プロジェクト構造を表示:

```bash
# プロジェクトルートで実行
echo ""
echo "  Architecture"
echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  plugins/content-autopilot/"
echo "  ├── skills/     ← 129 skills (SKILL.md x 129)"
echo "  │   ├── daily-autopilot/    State machine orchestrator"
echo "  │   ├── content-writer/     Multi-platform generator"
echo "  │   ├── trend-scout/        WebSearch + scoring"
echo "  │   ├── content-grader/     6-axis quality gate"
echo "  │   └── ... 125 more skills"
echo "  └── scripts/    ← 12 Python scripts"
echo "      ├── autopilot.py        Pipeline control + manifest"
echo "      ├── grader.py           6-axis scoring engine"
echo "      ├── dashboard.py        HTML dashboard generator"
echo "      ├── pre_publish.py      8-item validation"
echo "      ├── funnel_balance.py   TOFU/MOFU/BOFU calculator"
echo "      └── ... 5 more scripts"
echo ""
```

次にスキル数を実証:

```bash
ls plugins/content-autopilot/skills/ | wc -l
# → 129
```

### ナレーション（日本語）

> アーキテクチャを簡単に。
> 129のスキルと12本のPythonスクリプトで構成されています。
>
> 核になるのはdaily-autopilotスキル。これが状態機械として全体を制御します。
> 各ステップの判断ロジックはPythonスクリプトが担い、
> grader.pyが6軸の品質採点、funnel_balance.pyがファネル計算、
> dashboard.pyがHTML可視化を行います。
>
> 実際にスキル数を数えてみましょう。129。嘘偽りなしです。

---

## シーン5: なぜこれが勝つのか（2:30 - 2:50）

### 画面に映すもの

```bash
echo ""
echo "  Why Content Autopilot Wins"
echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  Autonomy (40%)"
echo "    7つの自律判断ポイント、ゼロのユーザー入力"
echo "    ・プロフィール自動生成"
echo "    ・ファネルステージ自動選択"
echo "    ・トピック自動選択（スコアリング）"
echo "    ・品質不合格時の自動改善"
echo "    ・重複時のサフィックス自動付与"
echo "    ・WebSearch失敗時のフォールバック"
echo "    ・note有料/無料の自動判定"
echo ""
echo "  Quality (35%)"
echo "    6軸採点 + 自動改善ループ + 日本語ネイティブチェック"
echo ""
echo "  Impact (25%)"
echo "    コンテンツクリエイター誰でも、1コマンドで使える"
echo ""
```

### ナレーション（日本語）

> なぜContent Autopilotが勝つのか。
>
> Autonomy。7つの判断ポイントすべてがシステムによる自律的決定です。
> ユーザー入力はゼロ。文字通り「一度命じたら、あとは任せろ」。
>
> Quality。6軸の採点と自動改善ループ。スコアが低ければ自分で直す。
> しかも日本語に特化したチェック。漢字率、です/ます体の一貫性、AI臭の検出。
>
> Impact。Claude Codeさえあれば、どんなコンテンツクリエイターでも今すぐ使えます。

---

## シーン6: クロージング（2:50 - 3:00）

### 画面に映すもの

```bash
echo ""
echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  Content Autopilot"
echo "  一度命じたら、コンテンツは自律的に生まれ続ける。"
echo ""
echo "  github.com/FP-sudo/content-autopilot"
echo ""
echo "  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
```

### ナレーション（日本語）

> Content Autopilot。
> 一度命じたら、コンテンツは自律的に生まれ続ける。
> ありがとうございました。

### タイミング

| 時刻 | 動作 |
|------|------|
| 2:50 | クロージング画面表示 |
| 2:53 | ナレーション |
| 2:58 | 余韻を持たせて終了 |
| 3:00 | 動画終了 |

---

## 全体タイムライン（サマリー）

| 時刻 | シーン | 内容 | 秒数 |
|------|--------|------|------|
| 0:00-0:15 | Opening | プロジェクト名、ワンライナー、バッジ | 15s |
| 0:15-0:30 | Problem | コンテンツ継続の壁 | 15s |
| 0:30-0:40 | Demo: Command | `/daily-autopilot` 入力 | 10s |
| 0:40-0:50 | Demo: Profile | プロフィール自動生成（自律判断#1） | 10s |
| 0:50-1:10 | Demo: Analysis | ファネル分析 + WebSearch + トピック選択（自律判断#2-4） | 20s |
| 1:10-1:20 | Demo: Generate | 3プラットフォーム同時生成 | 10s |
| 1:20-1:40 | Demo: Quality | 品質ゲート + 自動改善（自律判断#5、最重要シーン） | 20s |
| 1:40-2:00 | Demo: Dashboard | プレパブリッシュ + ダッシュボード + Intelligence Report | 20s |
| 2:00-2:30 | Architecture | 129 skills, 12 scripts, 状態機械 | 30s |
| 2:30-2:50 | Why This Wins | Autonomy/Quality/Impact のまとめ | 20s |
| 2:50-3:00 | Closing | コールトゥアクション、リポURL | 10s |

---

## 収録のコツ

### 全般

1. **ナレーションはゆっくり、はっきり** -- 3分は短いが早口は逆効果。審査員は初見。
2. **キーワードを強調** -- 「自律的に」「自動で」「人間は何もしていません」を繰り返す。
3. **カーソルで指す** -- 重要な出力行はマウスカーソルで強調。
4. **無音の間を恐れない** -- パイプラインが動いている間の1-2秒の沈黙はむしろ説得力がある。

### デモの実行について

- **リアル実行が理想** だが、WebSearchのレスポンス時間やClaude Codeの生成速度により3分を超える可能性が高い。
- **推奨方法**: 事前にフル実行して出力をキャプチャしておき、ナレーション録音時にはターミナルの録画を早送りで組み合わせる。
- **代替方法**: 事前に実行済みの出力をテキストファイルに保存し、`cat` で表示しながらナレーションをかぶせる。
- ダッシュボードのブラウザ画面はスクリーンショットでもよいが、実際にブラウザが開く瞬間を見せるとインパクトがある。

### 動画編集（最小限でOK）

- **カット編集**: パイプライン実行中の長い待ち時間をカット
- **テロップ（任意）**: 各シーンの見出しをテロップで入れると分かりやすい
- **BGM（任意）**: 控えめなBGMがあるとプロフェッショナルな印象

### もしデモが途中で失敗したら

Content Autopilotにはフォールバック機構が組み込まれている:
- WebSearch失敗 → フォールバックトピックライブラリから自動選択
- プロフィール未作成 → init_data.py で自動生成

万が一完全に止まった場合は、事前収録のバックアップ映像に切り替える。

---

## ナレーション全文（通し読み用）

以下をそのまま読めば3分のナレーションになる。

---

**[0:00]**
Content Autopilot。「一度命じたら、あとは任せろ」を文字通り実現する、完全自律型コンテンツ生成プラグインです。129のスキル、12本のPythonスクリプト。人間が介入するのは、最初の1コマンドだけ。

**[0:15]**
コンテンツマーケティングの現実。毎日のネタ探しに30分、3つのプラットフォームへの書き分けに2〜3時間、品質チェックは手動で属人的。これを、1コマンドでゼロにします。

**[0:30]**
実行するのは、この1コマンドだけです。`/daily-autopilot`。ここから先、人間は何もしません。見ているだけです。

**[0:40]**
まずプロフィール。初回なので存在しませんが、システムが自動生成しました。セットアップは不要。ゼロコンフィグです。

**[0:50]**
次にファネル分析。過去の履歴からTOFU・MOFU・BOFUのバランスを計算し、今日はTOFUが不足しているからTOFUコンテンツを作ると自動判断。そしてWebSearchでトレンドを調査。3つの候補からスコアリングして自動選択。注目してください。人間はトピックを選んでいません。システムが選んでいます。

**[1:10]**
3プラットフォーム同時生成。note、X、Instagram。それぞれに最適化されたコンテンツが一度に作られます。

**[1:20]**
ここが最大の差別化ポイントです。6軸の品質採点。Hook、Readability、Structure、Platform Fit、CTA、AI Smell。noteのスコアが64点で閾値を下回りました。普通のツールならここでユーザーに修正を求めます。しかしContent Autopilotは、何が悪いかを自分で特定し、自動で改善。64点から82点へ、プラス18点。人間は何もしていません。

**[1:40]**
8項目のプレパブリッシュチェックを全パス。HTMLダッシュボードが自動生成されてブラウザで表示。Intelligence Reportで、品質トレンドやファネルバランスも可視化されます。

**[2:00]**
アーキテクチャ。129のスキルと12本のPythonスクリプト。daily-autopilotが状態機械として全体を制御。grader.pyが6軸採点、funnel_balance.pyがファネル計算、dashboard.pyがHTML可視化。スキル数129、嘘偽りなしです。

**[2:30]**
なぜContent Autopilotが勝つのか。Autonomy。7つの判断ポイントすべてが自律的決定。ユーザー入力ゼロ。Quality。6軸採点と自動改善ループ。日本語ネイティブチェック。漢字率、文体一貫性、AI臭検出。Impact。Claude Codeさえあれば、どんなクリエイターでも今すぐ使えます。

**[2:50]**
Content Autopilot。一度命じたら、コンテンツは自律的に生まれ続ける。ありがとうございました。

---

## チェックリスト（収録前に確認）

- [ ] iTerm2のフォントサイズ 18pt 以上
- [ ] ダークテーマ設定済み
- [ ] 通知オフ（おやすみモード）
- [ ] `~/.content-autopilot` を削除（初回デモ用）
- [ ] `~/Desktop/content-autopilot-output` を削除
- [ ] Claude Codeが起動してプラグインが読み込まれている
- [ ] 画面収録ツールの設定確認（解像度、FPS、音声入力）
- [ ] ナレーション全文を2-3回通し読みして時間を計測
- [ ] バックアップ映像（事前フル実行の録画）を用意
- [ ] GitHubリポジトリURLを確認してクロージング画面に反映
- [ ] ダッシュボードのスクリーンショットを撮影してREADMEに追加:
      1. `open ~/Desktop/content-autopilot-output/dashboard.html`
      2. Cmd+Shift+4 でスクリーンショット撮影
      3. `docs/dashboard-screenshot.png` に保存
      4. READMEの「HTMLダッシュボード」セクションに `![Dashboard](docs/dashboard-screenshot.png)` を追加
