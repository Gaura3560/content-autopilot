---
name: content-vault
description: Content backup, versioning, and archive management — automatically backup content before modifications, maintain version history, enable rollback, and archive old content. The safety net for refresh, recycle, and edit operations.
---

# Content Vault

Never lose content — automatic backups, version history, and one-click rollback.

## When to Activate

- User says `/vault` or `/vault status`
- User says `/vault backup {file_path}`
- User says `/vault rollback {file_path}`
- Auto-triggered before /refresh, /recycle, or major edits

## Prerequisites

- Content files to manage

## Data: content-vault/

Location: `~/.content-autopilot/vault/`

```
~/.content-autopilot/vault/
  index.json                           # Master index of all versions
  2026-03-20/
    note_2026-03-20_v1.md             # Original
    note_2026-03-20_v2_refresh.md     # After refresh
  2026-03-15/
    x_2026-03-15_v1.md                # Original
```

### index.json

```json
{
  "version": "1.0",
  "entries": [
    {
      "file": "note_2026-03-20.md",
      "versions": [
        {
          "version": 1,
          "timestamp": "2026-03-20T10:00:00Z",
          "type": "original",
          "path": "vault/2026-03-20/note_2026-03-20_v1.md",
          "char_count": 3200
        },
        {
          "version": 2,
          "timestamp": "2026-03-25T15:00:00Z",
          "type": "refresh",
          "path": "vault/2026-03-20/note_2026-03-20_v2_refresh.md",
          "char_count": 3800,
          "changes": "Updated 5 data points, added new section"
        }
      ]
    }
  ]
}
```

## Commands

### `/vault` or `/vault status` — Show vault overview
### `/vault backup {file_path}` — Manual backup
### `/vault history {file_path}` — Show version history for a file
### `/vault rollback {file_path} {version}` — Restore a previous version
### `/vault diff {file_path} v1 v2` — Show differences between versions
### `/vault cleanup` — Remove old versions (keep last 5 per file)

## Workflow

### Auto-Backup (triggered by other skills)

When `/refresh`, `/recycle`, or edits modify content:
```
Auto-backup triggered:
  File: {filename}
  Reason: {refresh / recycle / edit}
  Saved: vault/{date}/{filename}_v{N}.md
  Previous version preserved.
```

### Manual Backup

`/vault backup note_2026-03-20.md`:
```
Backed up: note_2026-03-20.md
  Version: v{N}
  Location: vault/2026-03-20/note_2026-03-20_v{N}.md
  Size: {chars} chars
```

### Version History

`/vault history note_2026-03-20.md`:
```
Version History: note_2026-03-20.md
============================================

v1 — 2026-03-20 10:00 — original (3,200 chars)
v2 — 2026-03-25 15:00 — refresh (+600 chars, 5 data updates)
v3 — 2026-04-01 09:00 — seo optimization (+200 chars)

Current: v3

Rollback: /vault rollback note_2026-03-20.md v1
Diff: /vault diff note_2026-03-20.md v1 v3
============================================
```

### Rollback

`/vault rollback note_2026-03-20.md v1`:
```
Rollback: note_2026-03-20.md
  Current: v3 (4,000 chars)
  Restoring: v1 (3,200 chars)

  This will:
  1. Save current version as v4 (safety backup)
  2. Restore v1 content to the output file

  Proceed? (yes / no)
```

### Diff View

`/vault diff note_2026-03-20.md v1 v2`:
```
Diff: v1 → v2

  Added: 3 paragraphs (+600 chars)
  Modified: 5 data points
  Removed: 1 outdated section

  Key changes:
  + Section "2026 Q1 Updates" (new)
  ~ "AI market: $150B" → "$210B" (updated)
  ~ "100M users" → "300M users" (updated)
  - Old comparison table (removed, outdated)
```

### Vault Overview (`/vault status`)

```
============================================
  Content Vault Status
============================================

Total files tracked: {count}
Total versions stored: {count}
Vault size: ~{size}

Recently modified:
  {filename} — v{N} ({date}, {reason})
  {filename} — v{N} ({date}, {reason})

Files with most versions:
  {filename}: {N} versions
  {filename}: {N} versions

Storage recommendation:
  {count} files have 10+ versions — run /vault cleanup to keep last 5

============================================
```

## Integration with Other Skills

- **content-refresh**: Auto-backup before refresh
- **content-recycle**: Auto-backup before recycle modifications
- **seo-optimizer**: Auto-backup before SEO edits
- **auto-linker**: Auto-backup before link insertion
- **readability-tuner**: Auto-backup before readability adjustments

## Quality Gate

- [ ] Auto-backup triggers before any content modification
- [ ] Version numbering is sequential and consistent
- [ ] Rollback preserves current version as safety backup
- [ ] Diff clearly shows what changed between versions
- [ ] Cleanup doesn't delete the original (v1) or latest version
- [ ] Index.json is always in sync with actual files
