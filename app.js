// Main Application Logic for Interactive Examination Reader
document.addEventListener('DOMContentLoaded', () => {
    // --- MAIN READER LOGIC ---
    let currentTab = 'mock-tests';
    let currentMockId = 1;
    let currentSectionFilter = 'ALL';
    let studyMode = true; // true = show answers directly, false = exam test mode
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
                    <button class="btn-secondary" onclick="window.toggleStudyMode()">
                        ${studyMode ? '📖 Reader Mode (Keys Shown)' : '✍️ Practice Test Mode'}
                    </button>
                    <a href="mock_tests/Mock_Test_${pad}/questions.pdf" download class="btn-secondary" style="text-decoration:none; display:inline-flex; align-items:center; gap:4px;">
                        📥 Download PDF
                    </a>
                </div>
            </div>
            <div id="questions-container"><p style="color:var(--text-secondary);">Loading questions...</p></div>
        `;

        loadMockQuestions(num);
    }

    window.filterSection = function(sec) {
        currentSectionFilter = sec;
        renderQuestionsCards(window.currentLoadedQuestions);
    };

    window.toggleStudyMode = function() {
        studyMode = !studyMode;
        renderMockTestContent(currentMockId);
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
        const lines = keyCsv.split('\n');
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
            const textPart = b.split('- (A)')[0].replace(/^\d+\.\s*/, '').trim();
            const optA = b.includes('- (A)') ? b.split('- (A)')[1].split('- (B)')[0].trim() : '';
            const optB = b.includes('- (B)') ? b.split('- (B)')[1].split('- (C)')[0].trim() : '';
            const optC = b.includes('- (C)') ? b.split('- (C)')[1].split('- (D)')[0].trim() : '';
            const optD = b.includes('- (D)') ? b.split('- (D)')[1].split('\n\n')[0].trim() : '';

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
                <div class="question-card" id="q-card-${q.qno}">
                    <div class="question-card-header">
                        <div style="display:flex; gap:8px; align-items:center;">
                            <span class="badge badge-purple">Q${q.qno}</span>
                            <span class="badge ${badgeClass}">${q.diff}</span>
                            <span style="font-size:12px; color:var(--text-secondary);">${q.section} • ${q.topic}</span>
                        </div>
                    </div>
                    <div class="question-title">${q.text}</div>
                    <div class="options-grid">
                        <div class="option-item ${studyMode && q.correct === 'A' ? 'is-correct' : ''}" onclick="window.selectOption(${q.qno}, 'A')">
                            <strong>(A)</strong> <span>${q.opt_a}</span>
                        </div>
                        <div class="option-item ${studyMode && q.correct === 'B' ? 'is-correct' : ''}" onclick="window.selectOption(${q.qno}, 'B')">
                            <strong>(B)</strong> <span>${q.opt_b}</span>
                        </div>
                        <div class="option-item ${studyMode && q.correct === 'C' ? 'is-correct' : ''}" onclick="window.selectOption(${q.qno}, 'C')">
                            <strong>(C)</strong> <span>${q.opt_c}</span>
                        </div>
                        <div class="option-item ${studyMode && q.correct === 'D' ? 'is-correct' : ''}" onclick="window.selectOption(${q.qno}, 'D')">
                            <strong>(D)</strong> <span>${q.opt_d}</span>
                        </div>
                    </div>
                    <div class="explanation-box" style="${studyMode ? '' : 'display:none;'}" id="exp-${q.qno}">
                        <strong>Key: Option (${q.correct})</strong><br>
                        <em>Explanation:</em> ${q.exp}
                    </div>
                    ${!studyMode ? `<button class="btn-secondary" style="margin-top:8px;" onclick="document.getElementById('exp-${q.qno}').style.display='block'">Show Explanation</button>` : ''}
                </div>
            `;
        });
        container.innerHTML = html;
    }

    window.selectOption = function(qno, opt) {
        if (studyMode) return;
        const q = window.currentLoadedQuestions.find(item => item.qno == qno);
        if (!q) return;
        const card = document.getElementById(`q-card-${qno}`);
        const opts = card.querySelectorAll('.option-item');
        opts.forEach(el => el.classList.remove('selected-correct', 'selected-wrong'));
        
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
            const title = docKey.split('/').pop().replace('.md', '').replace(/^\d+_/, '').replace(/_/g, ' ');
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
    }

    // --- SYLLABUS VIEW ---
    function renderSyllabusView() {
        sidebar.innerHTML = `<div class="sidebar-heading">Syllabus Overview</div>
        <p style="padding:10px; font-size:13px; color:var(--text-secondary);">Official 80-mark curriculum with 27 subtopic units mapped.</p>`;
        const mdText = window.READER_DATA.syllabusTranscription || '# Syllabus';
        contentArea.innerHTML = `<div class="markdown-view">${simpleMarkdownToHtml(mdText)}</div>`;
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
            .replace(/^\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
            .replace(/^\*(.*?)\*/gim, '<em>$1</em>')
            .replace(/\n\n/gim, '<br><br>');
        return html;
    }

    // Initial render
    renderView();
});
