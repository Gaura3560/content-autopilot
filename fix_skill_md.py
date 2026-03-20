#!/usr/bin/env python3
"""SKILL.md を編集するスクリプト（マルチバイト文字対応）"""

import shutil

SOURCE = '/Users/sudotakao/content-autopilot/plugins/content-autopilot/skills/daily-autopilot/SKILL.md'
AGI_LAB_DEST = '/Users/sudotakao/agi-lab-skills-marketplace/plugins/content-autopilot/skills/daily-autopilot/SKILL.md'

with open(SOURCE, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# Change 1: Add "実行の最優先事項" section after frontmatter
# ============================================================
execution_priority_section = """## 実行の最優先事項

このスキルが起動したら、以下を**この順番通りに**実行する。
状態機械の分岐ロジックに従うが、**各ステップの "Output to user:" は必ずそのまま出力すること。**
省略・要約・言い換えは厳禁。

重要: 各python3コマンドは必ずBashツールで実行する。出力をJSONとしてパースし、次のステップに使う。

"""

# Insert after the title line
content = content.replace(
    '# Daily Autopilot — 完全自律コンテンツ生成\n',
    '# Daily Autopilot — 完全自律コンテンツ生成\n\n' + execution_priority_section
)

# ============================================================
# Change 2: Add ${CLAUDE_PLUGIN_ROOT} note after 起動条件 section
# ============================================================
plugin_root_note = """
NOTE: `${CLAUDE_PLUGIN_ROOT}` はClaude Codeが自動的に解決する環境変数。
手動テスト時は以下で代替可能:
```
PLUGIN_DIR=~/content-autopilot/plugins/content-autopilot
```

"""

content = content.replace(
    '## 状態機械（全判断を自動化）',
    plugin_root_note + '## 状態機械（全判断を自動化）'
)

# ============================================================
# Change 3: Add SETUP state (Step 0) at beginning of state machine
# ============================================================
content = content.replace(
    "```\nSTATE: BANNER (Step 0/8)",
    "```\nSTATE: SETUP (Step 0)\n"
    "  → mkdir -p ~/Desktop/content-autopilot-output\n"
    "  → (出力先ディレクトリを確保)\n"
    "  → STATE: BANNER\n"
    "\nSTATE: BANNER (Step 0/8)"
)

# ============================================================
# Change 4: Add 線形フロー section after the state machine code block
# ============================================================
linear_flow_section = """
## 線形フロー（クイックリファレンス）

1. `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/autopilot.py --mode execute` → JSONパース
2. WebSearch(query) → トピック自動選択
3. コンテンツ生成（note + X + Instagram）→ ファイル保存
4. `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/grader.py {note_file} --json` → score < 75 なら自動修正
5. `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/pre_publish.py {note_file} --json` → 失敗項目を自動修正
6. `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/record_history.py --topic ... --stage ... --category ... --date ...`
7. `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dashboard.py` → `open ~/Desktop/content-autopilot-output/dashboard.html`
8. `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/autopilot.py --mode summary` → Intelligence Report表示

"""

# Insert after the closing ``` of the state machine and before 進捗表示ルール
content = content.replace(
    '\n## 進捗表示ルール',
    linear_flow_section + '## 進捗表示ルール'
)

# Write back
with open(SOURCE, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated: {SOURCE}")

# Copy to agi-lab repo
shutil.copy2(SOURCE, AGI_LAB_DEST)
print(f"Copied to: {AGI_LAB_DEST}")

print("\nDone!")
