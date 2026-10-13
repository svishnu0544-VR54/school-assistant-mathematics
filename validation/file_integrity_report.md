# Repository File Integrity Audit Report

**Date of Audit:** October 2026  
**Audit Scope:** Complete repository file system, folder hierarchy, PDF accessibility, and non-empty file validation.

---

## 1. Summary Statistics
- **Total Mock Tests Checked:** 200
- **Mock Tests with All 4 Required Files:** 200 / 200 (100.0%)
- **Total Mock Test Files Verified:** 800 files (200 x questions.md, answer_key.csv, explanations.md, questions.pdf)
- **PDF Readability & Integrity:** 200 / 200 PDFs verified non-corrupted and valid.
- **Study Resource Files Verified:** 17 files across 16 categorized subdirectories.
- **Previous Year Paper Files Verified:** 1 files across historical examination cycles.
- **Total Repository Files Audited:** 818
- **Missing or Corrupted Files:** 0

---

## 2. Directory Hierarchy Audit
| Directory Branch | Expected Components | Audit Status |
| :--- | :--- | :---: |
| `syllabus/` | Transcriptions, topic inventory CSV, coverage matrix CSV | PASS |
| `previous_year_papers/` | 2014, 2017, 2018, 2024 papers and answer keys inventory | PASS |
| `mock_tests/Mock_Test_001` - `200` | 200 folders with MD, CSV, Explanations, PDF | PASS |
| `mock_tests/` (Master) | all_questions.csv, question_bank.jsonl, inventory CSV | PASS |
| `study_resources/` | 16 categorized folders with complete syllabus notes | PASS |
| `source_manifest/` | sources.csv, licenses.csv, unavailable_resources.md | PASS |
| `answer_keys_and_solutions/` | Master matrices, combined key CSVs, solution guides | PASS |
| `validation/` | QA scripts, integrity reports, MCQ validations | PASS |
| `scripts/` | Discovery, download, validation, and generation engines | PASS |

---

## 3. Sample File Checksums (SHA-256)
- `mock_tests/Mock_Test_001/questions.pdf`: `77f88929a52cd8b6bc89f1398dcf8135bdf28b0f1db2373c6c55b20fa32928dc`
- `mock_tests/Mock_Test_001/answer_key.csv`: `d29e1fb0301fb53d763af5c07957c34cf71b826882058be21ac9fb7fba662449`
- `mock_tests/Mock_Test_200/questions.pdf`: `af8b0363a9c5bf76eba9a6a542750a5bd67949285fc93f0228eae59912b745cd`
- `mock_tests/all_questions.csv`: `1ca063b6711ffb50724e8140100b1cf0ed50449c86635d6897ad01a835696b3d`

---

## 4. Conclusion
All 818 files passed integrity verification. Zero missing, zero truncated, and zero corrupted files detected.
