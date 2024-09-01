const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const app = express();
const db = new sqlite3.Database('./speedtest.db');

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

app.get('/api/speedtest', (req, res) => {
    db.all('SELECT * FROM speedtest ORDER BY timestamp DESC', [], (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ data: rows });
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
