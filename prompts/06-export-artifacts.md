# Prompt 06: Export Artifacts

> Use when the user asks for `/tnfd export`, Excel, PDF, DOCX, workpaper, or preliminary report.

## Rules

- Export only from saved LEA state.
- Do not infer new conclusions during export.
- If a field is missing, write `Evidence gap` or `Pending`.
- Pending case claims must remain pending.

## Export Options

| Command | Output |
|---|---|
| `/tnfd export` | Excel workbook and report fallback |
| `/tnfd export excel` | Excel workbook only |
| `/tnfd export pdf` | DOCX/PDF report only |
| `/tnfd export all` | Excel + DOCX/PDF |

## Required Response

```markdown
## Partner Brief
合伙人，导出只读取已保存状态，不重新推断结论。

## Export Result
| Artifact | Path | Status | Note |
|---|---|---|---|

## Export Limitations
...
```
