# 🍄 Clinical Medical Mycology — Bilingual Case-Based Ecosystem
# قارچ‌شناسی پزشکی بالینی — اکوسیستم دوزبانه مبتنی بر کیس

> ⚠️ **CLINICAL DISCLAIMER / سلب مسئولیت بالینی** — This is a decision-**support** tool, NOT a substitute for clinical judgment. See `DISCLAIMER.md`.

## Quick start
```bash
python3 src/validate.py
python3 src/build_cases.py
python3 src/cli.py
python3 src/flashcards.py
python3 src/atlas.py
```

## Repo map
- `book/` chapters (FA/EN)
- `data/cases/` one JSON per case
- `data/vocabulary.json` controlled bilingual vocabulary
- `schema/case.schema.json` case contract
- `src/` CLI + matcher + validators
