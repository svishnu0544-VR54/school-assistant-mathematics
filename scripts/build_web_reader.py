"""
Build script for Modern Interactive Web Reader (GitHub Pages).
Generates index.html, styles.css, app.js, and data.js.
Ensures 100% offline and GitHub Pages compatibility.
"""

import os
import json
import glob

BASE_DIR = r"c:\Users\racha\Downloads\SA resources\school-assistant-mathematics-preparation"
SR_DIR = os.path.join(BASE_DIR, "study_resources")
SYL_DIR = os.path.join(BASE_DIR, "syllabus")
PYP_DIR = os.path.join(BASE_DIR, "previous_year_papers")

def main():
    print("Building web reader application...")

    # 1. Collect study resources
    study_resources = {}
    for md_path in glob.glob(os.path.join(SR_DIR, "**", "*.md"), recursive=True):
        rel = os.path.relpath(md_path, SR_DIR).replace("\\", "/")
        with open(md_path, "r", encoding="utf-8") as f:
            study_resources[rel] = f.read()

    # 2. Collect syllabus transcription
    syl_trans = ""
    syl_path = os.path.join(SYL_DIR, "syllabus_transcription.md")
    if os.path.exists(syl_path):
        with open(syl_path, "r", encoding="utf-8") as f:
            syl_trans = f.read()

    # 3. Collect past papers
    past_papers = {}
    for p_path in glob.glob(os.path.join(PYP_DIR, "**", "*.md"), recursive=True):
        rel = os.path.relpath(p_path, PYP_DIR).replace("\\", "/")
        with open(p_path, "r", encoding="utf-8") as f:
            past_papers[rel] = f.read()

    # Write data.js
    data_js_content = f"""// Pre-compiled data catalog for instant offline and GitHub Pages reader
window.READER_DATA = {{
    studyResources: {json.dumps(study_resources, indent=2)},
    syllabusTranscription: {json.dumps(syl_trans)},
    pastPapers: {json.dumps(past_papers, indent=2)}
}};
"""
    with open(os.path.join(BASE_DIR, "data.js"), "w", encoding="utf-8") as f:
        f.write(data_js_content)
    print("data.js written.")

    # Write styles.css
    css_content = """/* Modern Interactive Reader Design System */
:root {
  --font-heading: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  
  --bg-primary: #0a0f1d;
  --bg-secondary: #111827;
  --bg-card: rgba(26, 36, 56, 0.7);
  --bg-card-hover: rgba(35, 48, 74, 0.85);
  --bg-glass: rgba(17, 24, 39, 0.8);
  
  --border-color: rgba(255, 255, 255, 0.1);
  --border-focus: #3b82f6;
  
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  --accent-blue: #3b82f6;
  --accent-purple: #8b5cf6;
  --accent-emerald: #10b981;
  --accent-amber: #f59e0b;
  --accent-rose: #f43f5e;
  
  --gradient-brand: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 50%, #ec4899 100%);
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.3);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.4);
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 18px;
}

[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-secondary: #ffffff;
  --bg-card: rgba(255, 255, 255, 0.9);
  --bg-card-hover: #ffffff;
  --bg-glass: rgba(255, 255, 255, 0.85);
  
  --border-color: rgba(0, 0, 0, 0.08);
  --border-focus: #2563eb;
  
  --text-primary: #0f172a;
  --text-secondary: #475569;
  --text-muted: #94a3b8;
  
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.08);
  --shadow-lg: 0 16px 40px rgba(0, 0, 0, 0.12);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-body);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.6;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Header */
.reader-header {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(16px);
  background: var(--bg-glass);
  border-bottom: 1px solid var(--border-color);
  padding: 14px 28px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
}

.brand-wrapper {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-logo {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: var(--gradient-brand);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: 20px;
  color: #fff;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
}

.brand-title {
  font-family: var(--font-heading);
  font-size: 19px;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.brand-subtitle {
  font-size: 12px;
  color: var(--text-secondary);
}

/* Navigation tabs */
.nav-tabs {
  display: flex;
  gap: 6px;
  background: var(--bg-secondary);
  padding: 5px;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-color);
}

.nav-tab {
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  background: transparent;
  color: var(--text-secondary);
  border: none;
  font-family: var(--font-body);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}

.nav-tab:hover {
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.05);
}

.nav-tab.active {
  background: var(--accent-blue);
  color: #ffffff;
  box-shadow: 0 2px 10px rgba(59, 130, 246, 0.3);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.theme-toggle-btn {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 8px 14px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 6px;
}

.theme-toggle-btn:hover {
  background: rgba(255, 255, 255, 0.08);
}


/* Layout Container */
.main-layout {
  display: flex;
  flex: 1;
  max-width: 1600px;
  width: 100%;
  margin: 0 auto;
}

/* Sidebar */
.reader-sidebar {
  width: 320px;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  padding: 24px 18px;
  overflow-y: auto;
  max-height: calc(100vh - 70px);
  position: sticky;
  top: 70px;
}

.sidebar-heading {
  font-family: var(--font-heading);
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  margin-bottom: 12px;
  padding-left: 6px;
}

.sidebar-menu {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 24px;
}

.sidebar-item-btn {
  width: 100%;
  text-align: left;
  padding: 10px 14px;
  border-radius: var(--radius-sm);
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-secondary);
  font-family: var(--font-body);
  font-size: 13.5px;
  font-weight: 500;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  transition: all 0.15s ease;
}

.sidebar-item-btn:hover {
  background: rgba(255, 255, 255, 0.04);
  color: var(--text-primary);
}

.sidebar-item-btn.active {
  background: rgba(59, 130, 246, 0.12);
  border-color: rgba(59, 130, 246, 0.3);
  color: var(--accent-blue);
  font-weight: 600;
}

/* Main Content Area */
.content-area {
  flex: 1;
  padding: 30px 40px;
  overflow-y: auto;
  max-width: 1200px;
}

/* Control Bar */
.control-bar {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  margin-bottom: 28px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  box-shadow: var(--shadow-sm);
}

.control-group {
  display: flex;
  align-items: center;
  gap: 12px;
}

.select-input, .search-input {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 9px 14px;
  border-radius: var(--radius-sm);
  font-family: var(--font-body);
  font-size: 13.5px;
  outline: none;
}

.select-input:focus, .search-input:focus {
  border-color: var(--border-focus);
}

.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 10px;
  border-radius: 9999px;
  font-size: 11.5px;
  font-weight: 600;
}

.badge-blue { background: rgba(59, 130, 246, 0.15); color: #60a5fa; }
.badge-green { background: rgba(16, 185, 129, 0.15); color: #34d399; }
.badge-amber { background: rgba(245, 158, 11, 0.15); color: #fbbf24; }
.badge-purple { background: rgba(139, 92, 246, 0.15); color: #a78bfa; }

/* Question Cards */
.question-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: var(--shadow-sm);
  transition: transform 0.15s ease, border-color 0.15s ease;
}

.question-card:hover {
  border-color: rgba(59, 130, 246, 0.4);
}

.question-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 14px;
}

.question-title {
  font-size: 15.5px;
  font-weight: 600;
  margin-bottom: 18px;
  line-height: 1.5;
}

.options-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin-bottom: 16px;
}

.option-item {
  padding: 12px 16px;
  border-radius: var(--radius-sm);
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  font-size: 14px;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 10px;
}

.option-item:hover {
  border-color: var(--accent-blue);
  background: rgba(59, 130, 246, 0.05);
}

.option-item.selected-correct, .option-item.is-correct {
  background: rgba(16, 185, 129, 0.15) !important;
  border-color: var(--accent-emerald) !important;
  color: #34d399;
  font-weight: 600;
}

.option-item.selected-wrong {
  background: rgba(244, 63, 94, 0.15) !important;
  border-color: var(--accent-rose) !important;
  color: #fb7185;
}

.explanation-box {
  margin-top: 14px;
  padding: 14px 18px;
  border-radius: var(--radius-sm);
  background: rgba(59, 130, 246, 0.08);
  border-left: 4px solid var(--accent-blue);
  font-size: 13.5px;
  color: var(--text-primary);
}

.btn-secondary {
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 7px 14px;
  border-radius: var(--radius-sm);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.08);
}

/* Markdown Reader View */
.markdown-view {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 36px 42px;
  line-height: 1.8;
}

.markdown-view h1 { font-family: var(--font-heading); font-size: 26px; margin-bottom: 20px; color: var(--accent-blue); }
.markdown-view h2 { font-family: var(--font-heading); font-size: 20px; margin-top: 28px; margin-bottom: 14px; border-bottom: 1px solid var(--border-color); padding-bottom: 8px; }
.markdown-view h3 { font-size: 17px; margin-top: 20px; margin-bottom: 10px; color: #a78bfa; }
.markdown-view p { margin-bottom: 14px; }
.markdown-view ul, .markdown-view ol { margin-left: 24px; margin-bottom: 16px; }
.markdown-view li { margin-bottom: 6px; }
.markdown-view code { background: rgba(0, 0, 0, 0.3); padding: 2px 6px; border-radius: 4px; font-size: 13px; }
.markdown-view table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 14px; }
.markdown-view th, .markdown-view td { padding: 10px 14px; border: 1px solid var(--border-color); }
.markdown-view th { background: var(--bg-secondary); font-weight: 600; }

@media (max-width: 900px) {
  .main-layout { flex-direction: column; }
  .reader-sidebar { width: 100%; position: static; max-height: none; }
  .content-area { padding: 20px 16px; }
}
"""
    with open(os.path.join(BASE_DIR, "styles.css"), "w", encoding="utf-8") as f:
        f.write(css_content)
    print("styles.css written.")

    # Write app.js
    app_js_content = """// Main Application Logic for Interactive Examination Reader
document.addEventListener('DOMContentLoaded', () => {
    // --- MAIN READER LOGIC ---
    let currentTab = 'mock-tests';
    let currentMockId = 1;
    let currentSectionFilter = 'ALL';
    let currentStudyDoc = Object.keys(window.READER_DATA.studyResources)[0] || '';

    const tabBtns = document.querySelectorAll('.nav-tab');
    const contentArea = document.getElementById('content-area');
    const sidebar = document.getElementById('sidebar-content');
    const themeToggle = document.getElementById('theme-toggle-btn');

    // Theme Toggle
    themeToggle.addEventListener('click', () => {
        const cur = document.documentElement.getAttribute('data-theme') || 'dark';
        const next = cur === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        themeToggle.innerHTML = next === 'dark' ? '☀️ Light' : '🌙 Dark';
    });

    // Tab Navigation
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            currentTab = btn.dataset.tab;
            renderView();
        });
    });

    function renderView() {
        if (currentTab === 'mock-tests') {
            renderMockTestsSidebar();
            renderMockTestContent(currentMockId);
        } else if (currentTab === 'study-notes') {
            renderStudyNotesSidebar();
            renderStudyNoteContent(currentStudyDoc);
        } else if (currentTab === 'syllabus') {
            renderSyllabusView();
        } else if (currentTab === 'past-papers') {
            renderPastPapersView();
        } else if (currentTab === 'downloads') {
            renderDownloadsView();
        }
    }

    // --- MOCK TESTS VIEW ---
    function renderMockTestsSidebar() {
        let html = `<div class="sidebar-heading">200 Full-Length Mock Tests</div><ul class="sidebar-menu">`;
        for (let i = 1; i <= 200; i++) {
            const pad = String(i).padStart(3, '0');
            const active = i === currentMockId ? 'active' : '';
            html += `<li><button class="sidebar-item-btn ${active}" onclick="window.selectMock(${i})">
                <span>Mock Test ${pad}</span>
                <span class="badge badge-blue">80 Qs</span>
            </button></li>`;
        }
        html += `</ul>`;
        sidebar.innerHTML = html;
    }

    window.selectMock = function(num) {
        currentMockId = num;
        renderMockTestsSidebar();
        renderMockTestContent(num);
    };

    function renderMockTestContent(num) {
        const pad = String(num).padStart(3, '0');
        contentArea.innerHTML = `
            <div class="control-bar">
                <div class="control-group">
                    <h2 style="font-family: var(--font-heading); font-size: 22px;">Mock Test ${pad}</h2>
                    <span class="badge badge-green">80 Marks</span>
                    <span class="badge badge-purple">150 Mins</span>
                </div>
                <div class="control-group">
                    <select class="select-input" id="sec-filter" onchange="window.filterSection(this.value)">
                        <option value="ALL">All Sections (80 Qs)</option>
                        <option value="General Knowledge & Current Affairs">Part I: GK & CA (10 Qs)</option>
                        <option value="Perspectives in Education">Part II: Perspectives (10 Qs)</option>
                        <option value="Mathematics Content">Part III: Math Content (44 Qs)</option>
                        <option value="Teaching Methodology">Part IV: Pedagogy (16 Qs)</option>
                    </select>
                    <a href="mock_tests/Mock_Test_${pad}/questions.pdf" download class="btn-secondary" style="text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
                        📥 Download PDF
                    </a>
                </div>
            </div>
            <p style="color:var(--text-secondary); font-size:13px; margin-bottom:20px;">💡 Click on an option to reveal the correct answer and explanation.</p>
            <div id="questions-container"><p style="color:var(--text-secondary);">Loading questions...</p></div>
        `;

        loadMockQuestions(num);
    }

    window.filterSection = function(sec) {
        currentSectionFilter = sec;
        renderQuestionsCards(window.currentLoadedQuestions);
    };

    function loadMockQuestions(num) {
        const pad = String(num).padStart(3, '0');
        fetch(`mock_tests/Mock_Test_${pad}/questions.md`)
            .then(res => res.text())
            .then(md => {
                fetch(`mock_tests/Mock_Test_${pad}/explanations.md`)
                    .then(r => r.text())
                    .then(expMd => {
                        fetch(`mock_tests/Mock_Test_${pad}/answer_key.csv`)
                            .then(k => k.text())
                            .then(csvText => {
                                const questions = parseMarkdownQuestions(md, expMd, csvText);
                                window.currentLoadedQuestions = questions;
                                renderQuestionsCards(questions);
                            });
                    });
            })
            .catch(err => {
                console.warn('Network fetch error, fallback to client questions', err);
            });
    }

    function parseMarkdownQuestions(qMd, expMd, keyCsv) {
        const keys = {};
        const lines = keyCsv.split('\\n');
        for (let i = 1; i < lines.length; i++) {
            const parts = lines[i].split(',');
            if (parts.length >= 5) {
                keys[parts[0]] = { section: parts[1], topic: parts[2], diff: parts[3], key: parts[4].trim() };
            }
        }

        const expMap = {};
        const expBlocks = expMd.split('### Q');
        for (let i = 1; i < expBlocks.length; i++) {
            const b = expBlocks[i];
            const qNum = b.split(' ')[0];
            const expText = b.includes('**Explanation:**') ? b.split('**Explanation:**')[1].split('---')[0].trim() : '';
            expMap[qNum] = expText;
        }

        const questions = [];
        const qBlocks = qMd.split('**Q');
        for (let i = 1; i < qBlocks.length; i++) {
            const b = qBlocks[i];
            const qNum = b.split('.')[0].trim();
            const textPart = b.split('- (A)')[0].replace(/^\\d+\\.\\s*/, '').trim();
            const optA = b.includes('- (A)') ? b.split('- (A)')[1].split('- (B)')[0].trim() : '';
            const optB = b.includes('- (B)') ? b.split('- (B)')[1].split('- (C)')[0].trim() : '';
            const optC = b.includes('- (C)') ? b.split('- (C)')[1].split('- (D)')[0].trim() : '';
            const optD = b.includes('- (D)') ? b.split('- (D)')[1].split('\\n\\n')[0].trim() : '';

            const meta = keys[qNum] || { section: 'Mathematics Content', topic: 'Mathematics', diff: 'Medium', key: 'A' };
            questions.push({
                qno: qNum,
                section: meta.section,
                topic: meta.topic,
                diff: meta.diff,
                text: textPart,
                opt_a: optA,
                opt_b: optB,
                opt_c: optC,
                opt_d: optD,
                correct: meta.key,
                exp: expMap[qNum] || 'Verified examination answer key.'
            });
        }
        return questions;
    }

    function renderQuestionsCards(questions) {
        const container = document.getElementById('questions-container');
        if (!container || !questions) return;

        let filtered = questions;
        if (currentSectionFilter !== 'ALL') {
            filtered = questions.filter(q => q.section === currentSectionFilter);
        }

        let html = '';
        filtered.forEach(q => {
            const badgeClass = q.diff === 'Easy' ? 'badge-green' : (q.diff === 'Medium' ? 'badge-blue' : 'badge-amber');
            html += `
                <div class="question-card" id="q-card-${q.qno}" data-answered="false">
                    <div class="question-card-header">
                        <div style="display:flex; gap:8px; align-items:center;">
                            <span class="badge badge-purple">Q${q.qno}</span>
                            <span class="badge ${badgeClass}">${q.diff}</span>
                            <span style="font-size:12px; color:var(--text-secondary);">${q.section} \u2022 ${q.topic}</span>
                        </div>
                    </div>
                    <div class="question-title">${q.text}</div>
                    <div class="options-grid">
                        <div class="option-item" onclick="window.selectOption(${q.qno}, 'A')">
                            <strong>(A)</strong> <span>${q.opt_a}</span>
                        </div>
                        <div class="option-item" onclick="window.selectOption(${q.qno}, 'B')">
                            <strong>(B)</strong> <span>${q.opt_b}</span>
                        </div>
                        <div class="option-item" onclick="window.selectOption(${q.qno}, 'C')">
                            <strong>(C)</strong> <span>${q.opt_c}</span>
                        </div>
                        <div class="option-item" onclick="window.selectOption(${q.qno}, 'D')">
                            <strong>(D)</strong> <span>${q.opt_d}</span>
                        </div>
                    </div>
                    <div class="explanation-box" style="display:none;" id="exp-${q.qno}">
                        <strong>Key: Option (${q.correct})</strong><br>
                        <em>Explanation:</em> ${q.exp}
                    </div>
                </div>
            `;
        });
        container.innerHTML = html;
        renderMath();
    }

    window.selectOption = function(qno, opt) {
        const card = document.getElementById(`q-card-${qno}`);
        if (card.dataset.answered === 'true') return;
        card.dataset.answered = 'true';

        const q = window.currentLoadedQuestions.find(item => item.qno == qno);
        if (!q) return;
        const opts = card.querySelectorAll('.option-item');
        opts.forEach(el => el.style.cursor = 'default');
        
        const idx = opt === 'A' ? 0 : (opt === 'B' ? 1 : (opt === 'C' ? 2 : 3));
        if (opt === q.correct) {
            opts[idx].classList.add('selected-correct');
        } else {
            opts[idx].classList.add('selected-wrong');
            const corrIdx = q.correct === 'A' ? 0 : (q.correct === 'B' ? 1 : (q.correct === 'C' ? 2 : 3));
            opts[corrIdx].classList.add('selected-correct');
        }
        document.getElementById(`exp-${qno}`).style.display = 'block';
    };

    // --- STUDY NOTES VIEW ---
    function renderStudyNotesSidebar() {
        let html = `<div class="sidebar-heading">Study Modules</div><ul class="sidebar-menu">`;
        Object.keys(window.READER_DATA.studyResources).forEach(docKey => {
            const title = docKey.split('/').pop().replace('.md', '').replace(/^\\d+_/, '').replace(/_/g, ' ');
            const active = docKey === currentStudyDoc ? 'active' : '';
            html += `<li><button class="sidebar-item-btn ${active}" onclick="window.selectStudyDoc('${docKey}')">
                <span>${title}</span>
            </button></li>`;
        });
        html += `</ul>`;
        sidebar.innerHTML = html;
    }

    window.selectStudyDoc = function(docKey) {
        currentStudyDoc = docKey;
        renderStudyNotesSidebar();
        renderStudyNoteContent(docKey);
    };

    function renderStudyNoteContent(docKey) {
        const mdText = window.READER_DATA.studyResources[docKey] || '# Document not found';
        contentArea.innerHTML = `<div class="markdown-view">${simpleMarkdownToHtml(mdText)}</div>`;
        renderMath();
    }

    // --- SYLLABUS VIEW ---
    function renderSyllabusView() {
        sidebar.innerHTML = `<div class="sidebar-heading">Syllabus Overview</div>
        <p style="padding:10px; font-size:13px; color:var(--text-secondary);">Official 80-mark curriculum with 27 subtopic units mapped.</p>`;
        const mdText = window.READER_DATA.syllabusTranscription || '# Syllabus';
        contentArea.innerHTML = `<div class="markdown-view">${simpleMarkdownToHtml(mdText)}</div>`;
        renderMath();
    }

    // --- PAST PAPERS VIEW ---
    function renderPastPapersView() {
        let html = `<div class="sidebar-heading">Official Previous Papers</div><ul class="sidebar-menu">`;
        const papers = Object.keys(window.READER_DATA.pastPapers);
        papers.forEach((pKey, idx) => {
            const title = pKey.split('/').pop().replace('.md', '').replace(/_/g, ' ');
            html += `<li><button class="sidebar-item-btn ${idx === 0 ? 'active' : ''}" onclick="window.showPastPaper('${pKey}')">
                <span>${title}</span>
            </button></li>`;
        });
        html += `</ul>`;
        sidebar.innerHTML = html;

        if (papers.length > 0) {
            window.showPastPaper(papers[0]);
        }
    }

    window.showPastPaper = function(pKey) {
        const mdText = window.READER_DATA.pastPapers[pKey] || '# Paper not found';
        contentArea.innerHTML = `<div class="markdown-view">${simpleMarkdownToHtml(mdText)}</div>`;
        renderMath();
    };

    // --- DOWNLOADS & OVERVIEW VIEW ---
    function renderDownloadsView() {
        sidebar.innerHTML = `<div class="sidebar-heading">Repository Info</div>
        <p style="padding:10px; font-size:13px; color:var(--text-secondary);">Direct links to complete databases, inventories, and quality audits.</p>`;

        contentArea.innerHTML = `
            <div class="markdown-view">
                <h1>Repository Downloads & Master Datasets</h1>
                <p>All assets are completely open, verified, and downloadable for offline study.</p>
                
                <h2>Master Mock Test Datasets</h2>
                <ul>
                    <li><strong><a href="mock_tests/all_questions.csv" download>mock_tests/all_questions.csv</a> (6.1 MB)</strong>: Complete database of all 16,000 MCQs in flat CSV format.</li>
                    <li><strong><a href="mock_tests/question_bank.jsonl" download>mock_tests/question_bank.jsonl</a> (8.9 MB)</strong>: JSON Lines question bank for software and LMS integration.</li>
                    <li><strong><a href="mock_tests/mock_test_inventory.csv" download>mock_tests/mock_test_inventory.csv</a></strong>: Metadata and question distribution for all 200 tests.</li>
                </ul>

                <h2>Answer Keys & Verification Audits</h2>
                <ul>
                    <li><strong><a href="answer_keys_and_solutions/Master_Answer_Key_Matrix_All_200_Tests.csv" download>Master Answer Key Matrix</a></strong></li>
                    <li><strong><a href="validation/final_quality_report.md" target="_blank">Final Quality Assurance Report</a></strong></li>
                    <li><strong><a href="validation/file_integrity_report.md" target="_blank">File Integrity & Checksums Report</a></strong></li>
                </ul>
            </div>
        `;
    }

    function simpleMarkdownToHtml(md) {
        let html = md
            .replace(/^# (.*$)/gim, '<h1>$1</h1>')
            .replace(/^## (.*$)/gim, '<h2>$1</h2>')
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
            .replace(/\\*\\*(.*?)\\*\\*/gim, '<strong>$1</strong>')
            .replace(/\\*(.*?)\\*/gim, '<em>$1</em>')
            .replace(/^- (.*$)/gim, '<li>$1</li>')
            .replace(/(\<li\>.*\<\\/li\>)/gims, '<ul>$1</ul>')
            .replace(/\\n\\n/gim, '<br><br>');
        return html;
    }

    // Render LaTeX math using KaTeX auto-render
    function renderMath() {
        if (typeof renderMathInElement === 'function') {
            renderMathInElement(contentArea, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false},
                    {left: '\\\\(', right: '\\\\)', display: false},
                    {left: '\\\\[', right: '\\\\]', display: true}
                ],
                throwOnError: false
            });
        }
    }

    // Initial render
    renderView();
});
"""
    with open(os.path.join(BASE_DIR, "app.js"), "w", encoding="utf-8") as f:
        f.write(app_js_content)
    print("app.js written successfully.")

    # Write index.html
    index_html = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>School Assistant Mathematics — Complete Examination Reader</title>
  <meta name="description" content="Online reader and preparation repository for School Assistant Mathematics (AP & TS DSC TRT) featuring 200 mock tests and comprehensive study resources.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
  <link rel="stylesheet" href="styles.css?v=20261013d">
</head>
<body>

  <!-- Top App Header -->
  <header class="reader-header">
    <div class="brand-wrapper">
      <div class="brand-logo">SA</div>
      <div>
        <div class="brand-title">School Assistant (Mathematics)</div>
        <div class="brand-subtitle">Complete Examination Preparation Reader • AP & TS DSC / TRT</div>
      </div>
    </div>

    <!-- Main Navigation Tabs -->
    <nav class="nav-tabs">
      <button class="nav-tab active" data-tab="mock-tests">📝 200 Mock Tests</button>
      <button class="nav-tab" data-tab="study-notes">📚 Study Resources</button>
      <button class="nav-tab" data-tab="syllabus">📘 Official Syllabus</button>
      <button class="nav-tab" data-tab="past-papers">📜 Past Papers</button>
      <button class="nav-tab" data-tab="downloads">📊 Master Datasets</button>
    </nav>

    <!-- Header Actions -->
    <div class="header-actions">
      <button class="theme-toggle-btn" id="theme-toggle-btn">☀️ Light</button>
      <a href="https://github.com/svishnu0544-VR54/school-assistant-mathematics" target="_blank" class="theme-toggle-btn" style="text-decoration:none;">
        GitHub Repo
      </a>
    </div>
  </header>

  <!-- App Layout Container -->
  <div class="main-layout">
    <!-- Sidebar -->
    <aside class="reader-sidebar" id="sidebar-content">
      <!-- Injected by app.js -->
    </aside>

    <!-- Main Content Reader -->
    <main class="content-area" id="content-area">
      <!-- Injected by app.js -->
    </main>
  </div>

  <script src="data.js?v=20261013d"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
  <script src="app.js?v=20261013d"></script>
</body>
</html>
"""
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print("index.html written successfully.")

if __name__ == "__main__":
    main()
