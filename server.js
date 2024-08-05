// Load environment variables from .env file
require('dotenv').config();

const express = require('express');
const bodyParser = require('body-parser');
const app = express();

// Use body-parser to parse JSON bodies into JS objects
app.use(bodyParser.json());

// Endpoint to update JBunny tokens
app.post('/api/update-tokens', (req, res) => {
    const { tokens } = req.body;

    console.log(`Updating wallet with ${tokens} JBunny tokens`);

    // Simulate updating the wallet (replace this with actual logic)
    res.json({ success: true, message: ${tokens} tokens added to wallet. });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});