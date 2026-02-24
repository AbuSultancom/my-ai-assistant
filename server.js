const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8080;
const DATA_FILE = path.join(__dirname, 'student_state.json');

// Ensure state structure is complete
const getInitialState = () => ({
    last_update: new Date(),
    student_answers: {},
    questions: [],
    teacher_feedback: "Welcome back, Abdulhameed! Ready for more challenges?",
    current_lesson: 1,
    unlocked_lessons: [1]
});

if (!fs.existsSync(DATA_FILE)) {
    fs.writeFileSync(DATA_FILE, JSON.stringify(getInitialState()));
}

const server = http.createServer((req, res) => {
    // CORS headers for local access
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }

    if (req.method === 'GET' && (req.url === '/' || req.url === '/index.html')) {
        fs.readFile(path.join(__dirname, 'portal.html'), (err, data) => {
            res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            res.end(data);
        });
    } else if (req.method === 'GET' && req.url === '/api/state') {
        const state = fs.readFileSync(DATA_FILE);
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(state);
    } else if (req.method === 'POST' && req.url === '/api/submit') {
        let body = '';
        req.on('data', chunk => { body += chunk.toString(); });
        req.on('end', () => {
            const state = JSON.parse(fs.readFileSync(DATA_FILE));
            const submission = JSON.parse(body);
            state.student_answers[submission.lesson || state.current_lesson] = submission.answer;
            state.last_update = new Date();
            state.teacher_feedback = "I've received your solution! Let me analyze it...";
            fs.writeFileSync(DATA_FILE, JSON.stringify(state, null, 2));
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true }));
        });
    } else if (req.method === 'POST' && req.url === '/api/ask') {
        let body = '';
        req.on('data', chunk => { body += chunk.toString(); });
        req.on('end', () => {
            const state = JSON.parse(fs.readFileSync(DATA_FILE));
            const questionData = JSON.parse(body);
            state.questions.push({ text: questionData.text, timestamp: new Date() });
            state.teacher_feedback = "Good question! I'm drafting a detailed explanation for you.";
            fs.writeFileSync(DATA_FILE, JSON.stringify(state, null, 2));
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ success: true }));
        });
    } else {
        res.writeHead(404);
        res.end();
    }
});

server.listen(PORT, '0.0.0.0', () => {
    console.log(`OpenClaw Academy Server running at http://localhost:${PORT}`);
});
