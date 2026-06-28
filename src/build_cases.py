import os, json, glob, re
from common import ROOT

BOOK_EN_DIR = os.path.join(ROOT, "book", "en")
CASES_DIR = os.path.join(ROOT, "data", "cases")
INDEX_PATH = os.path.join(ROOT, "data", "index.json")

START = "CASE_METADATA_JSON_START"
END = "CASE_METADATA_JSON_END"

BLOCK_RE = re.compile(
    r"CASE_METADATA_JSON_START\\s*(\\{.*?\\})\\s*CASE_METADATA_JSON_END",
    re.DOTALL,
)

def extract_case_json_from_markdown(md_text, filename):
    m = BLOCK_RE.search(md_text)
    if not m:
        raise ValueError(f"No metadata block found in {filename}")
    raw = m.group(1).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON metadata in {filename}: {e}")

def build_cases_from_book_en():
    os.makedirs(CASES_DIR, exist_ok=True)
    written = []

    md_files = sorted(glob.glob(os.path.join(BOOK_EN_DIR, "*.md")))
    if not md_files:
        print("No chapters found in book/en/ (nothing to extract).")
        return written

    for path in md_files:
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        case = extract_case_json_from_markdown(text, name)

        if "case_id" not in case or not case["case_id"]:
            raise ValueError(f"{name}: metadata JSON must include non-empty case_id")

        out_path = os.path.join(CASES_DIR, case["case_id"] + ".json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(case, f, ensure_ascii=False, indent=2)

        written.append(out_path)
        print(f"Extracted {case['case_id']} from {name}")

    return written

def build_index():
    cases = []
    for p in sorted(glob.glob(os.path.join(CASES_DIR, "*.json"))):
        c = json.load(open(p, encoding="utf-8"))
        cases.append({
            "case_id": c.get("case_id"),
            "chapter": (c.get("book_ref") or {}).get("chapter"),
            "title_en": (c.get("book_ref") or {}).get("title_en", ""),
            "title_fa": (c.get("book_ref") or {}).get("title_fa", ""),
            "organism_code": (c.get("diagnosis") or {}).get("organism_code"),
            "archetype": c.get("case_archetype"),
            "status": c.get("status", "draft"),
            "file": os.path.relpath(p, ROOT),
        })

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump({"count": len(cases), "cases": cases}, f, ensure_ascii=False, indent=2)

    print(f"Wrote data/index.json ({len(cases)} cases).")

if __name__ == "__main__":
    build_cases_from_book_en()
    build_index()
