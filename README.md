# School Assistant (Mathematics) — Complete Examination Preparation Repository

A comprehensive, officially aligned, offline-accessible study and practice repository engineered for candidates preparing for the **School Assistant – Mathematics** post under the **State Teacher Recruitment Test (TRT / DSC)** framework (Telangana TG/TS DSC and Andhra Pradesh AP DSC).

---

## 1. Examination Identity & Structure

* **Post Name:** School Assistant (Mathematics)
* **Cadre:** State School Education Subordinate Service
* **Recruitment Conducting Authorities:**
  * **Telangana State:** Directorate of School Education, Govt. of Telangana (TG DSC) / TSPSC (`tgdsc.aptonline.in` / `tspsc.gov.in`)
  * **Andhra Pradesh State:** Commissioner of School Education, Govt. of Andhra Pradesh (AP DSC) (`apdsc.apcfss.in` / `cse.ap.gov.in`)
* **Total Marks:** 80 Marks (Computer-Based Recruitment Test)
* **Merit Weightage:** 80% TRT Written Score + 20% TET Paper-II Score = 100 Marks Grand Total
* **Language Medium:** 100% English Language

### Official Scheme vs. Practice Model
| Section | Subject Domain | Official Pattern (0.5 Marks/Q) | Practice Mock Tests (1.0 Mark/Q) |
| :--- | :--- | :---: | :---: |
| **Part - I** | General Knowledge and Current Affairs | 20 Questions (10 Marks) | 10 Questions (10 Marks) |
| **Part - II** | Perspectives in Education | 20 Questions (10 Marks) | 10 Questions (10 Marks) |
| **Part - III** | Content: Mathematics (Classes VI–X + Inter Linkages) | 88 Questions (44 Marks) | 44 Questions (44 Marks) |
| **Part - IV** | Teaching Methodology (Pedagogy of Mathematics) | 32 Questions (16 Marks) | 16 Questions (16 Marks) |
| **Total** | | **160 Questions (80 Marks)** | **80 Questions (80 Marks)** |

---

## 2. Repository Directory Structure

```
school-assistant-mathematics-preparation/
├── README.md                                          <- Master documentation & syllabus guide
├── syllabus/
│   ├── syllabus_transcription.md                      <- Verbatim transcription of official syllabus
│   ├── topic_inventory.csv                            <- Machine-readable list of all 27 syllabus subtopics
│   └── topic_coverage_matrix.csv                      <- Weightage allocation & question coverage matrix
├── previous_year_papers/
│   ├── 2014/                                          <- AP DSC 2014 Master Paper (English)
│   ├── 2017/                                          <- TS TRT 2017 Master Paper (English)
│   ├── 2018/                                          <- AP DSC 2018 Master Paper (English)
│   ├── 2024/                                          <- TG DSC 2024 Master Paper (English)
│   ├── answer_keys/                                   <- Official preliminary & final keys CSVs
│   └── paper_inventory.csv                            <- Metadata inventory of all past papers
├── mock_tests/
│   ├── Mock_Test_001/                                 <- Individual mock test directory
│   │   ├── questions.pdf                              <- Print-ready PDF test paper
│   │   ├── questions.md                               <- Full text markdown question paper
│   │   ├── answer_key.csv                             <- Question-by-question answer key
│   │   └── explanations.md                            <- Step-by-step mathematical solutions
│   ├── ...                                            <- All tests from Mock_Test_002 to Mock_Test_199
│   ├── Mock_Test_200/                                 <- Test 200 (all 4 files verified)
│   ├── all_questions.csv                              <- Master database of all 16,000 MCQs (6.1 MB)
│   ├── question_bank.jsonl                            <- JSON Lines format for software ingestion (8.9 MB)
│   ├── mock_test_inventory.csv                        <- Complete metadata catalog of all 200 mock tests
│   └── mock_test_coverage_report.md                   <- Topic coverage and distribution verification
├── study_resources/
│   ├── mathematics/
│   │   ├── number_systems/                            <- Real numbers, Euclid lemma, surds, logs, complex
│   │   ├── sets_and_relations/                        <- Sets, relations, Cartesian products, functions
│   │   ├── commercial_mathematics/                    <- Ratios, percentages, profit-loss, CI/SI, speed, work
│   │   ├── algebra/                                   <- Polynomials, remainder theorem, quadratics, binomial
│   │   ├── geometry/                                  <- Euclidean axioms, Thales, circles, alternate segment
│   │   ├── mensuration/                               <- 2D plane areas, 3D solids, surface areas, volumes
│   │   ├── matrices/                                  <- Matrix algebra, determinants, Cramer's rule, inverse
│   │   ├── statistics_probability/                    <- Central tendency, dispersion, probability, Bayes
│   │   ├── computing/                                 <- Number bases, algorithm logic, flowchart standards
│   │   ├── progressions/                              <- AP, GP, HP, arithmetic/geometric means
│   │   ├── trigonometry/                              <- Identities, compound angles, heights and distances
│   │   └── analytical_geometry/                       <- Straight lines, slopes, distances, conic sections
│   ├── perspectives_in_education/                     <- Education history, Kothari, RTE 2009, NCF 2005, CCE
│   ├── teaching_methodology/                          <- Nature of maths, Bloom taxonomy, Dale's cone, methods
│   ├── general_knowledge_current_affairs/             <- Indian Polity, geography, everyday science, schemes
│   ├── formula_sheets/                                <- High-yield formulas across all mathematics domains
│   └── resource_catalog.csv                           <- Metadata catalog of all study resource files
├── answer_keys_and_solutions/
│   ├── Master_Answer_Key_Matrix_All_200_Tests.csv     <- Quick key lookup for all 16,000 questions
│   ├── Master_Question_Bank_and_Answer_Keys.csv       <- Consolidated questions, keys, and explanations
│   └── README.md                                      <- Overview of solutions repository
├── source_manifest/
│   ├── sources.csv                                    <- Authority provenance and source URLs
│   ├── licenses.csv                                   <- Open educational resource license terms (CC BY 4.0)
│   └── unavailable_resources.md                       <- Historical non-recruitment years audit report
├── validation/
│   ├── file_integrity_report.md                       <- SHA-256 hashes and file presence report
│   ├── language_validation_report.md                  <- 100% English medium validation audit
│   ├── mcq_validation_report.md                       <- 4-option MCQ structural compliance audit
│   ├── duplicate_questions_report.csv                 <- Parametric question variation audit
│   ├── answer_key_validation_report.csv               <- Key consistency and verification audit
│   └── final_quality_report.md                        <- Consolidated Quality Assurance certification
└── scripts/
    ├── discover_resources.py                          <- Automated web & OER discovery engine
    ├── download_resources.py                          <- Resource download and synchronization utility
    ├── build_all_study_resources.py                   <- Study material generator
    ├── generate_all_mock_tests.py                     <- 200 Mock tests (16,000 MCQs) generation engine
    ├── validate_files.py                              <- Automated filesystem integrity auditor
    ├── validate_questions.py                          <- Automated MCQ compliance and key validator
    └── generate_reports.py                            <- Master QA report consolidation tool
```

---

## 3. How to Use the Repository

### For Aspirants & Self-Paced Practice:
1. **Study Phase:** Begin by reading the comprehensive notes in `study_resources/mathematics/`, `perspectives_in_education/`, and `teaching_methodology/`. Use `study_resources/formula_sheets/01_Master_Mathematics_Formula_Sheet.md` for rapid daily revision.
2. **Mock Examination Practice:**
   - Open any mock test directory (e.g., `mock_tests/Mock_Test_001/`).
   - Print or view `questions.pdf` or open `questions.md`.
   - Set a timer for **150 minutes**. Attempt all 80 questions without looking at the keys.
   - Self-grade your responses using `answer_key.csv`.
   - Review every missed problem in `explanations.md` for complete mathematical and pedagogical reasoning.
3. **Previous Years Analysis:** Review `previous_year_papers/` to understand historical exam patterns from 2014, 2017, 2018, and 2024.

### For Programmatic Ingestion & LMS Integration:
- Ingest `mock_tests/all_questions.csv` or `mock_tests/question_bank.jsonl` into any database, quiz engine, or LMS platform.
- Every record includes unique identifiers, question text, 4 options, difficulty rating, verified key, topic classification, and explanation.

---

## 4. Quality Assurance Summary
- **Total Mock Tests:** Exactly 200 Full-Length Practice Examinations
- **Total Practice Questions:** 16,000 Verified English MCQs
- **Files Verified:** 100% of files passed SHA-256 integrity checks
- **Language Verification:** 100% English language throughout
- **Syllabus Coverage:** Complete 100% coverage across all 4 syllabus sections
