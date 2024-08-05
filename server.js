const express = require('express');
const bodyParser = require('body-parser');
const app = express();

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Endpoint to update JBunny tokens
app.post('/api/update-tokens', (req, res) => {
    const { tokens } = req.body;
    // Add your logic here to update the user's wallet
    console.log(`Updating wallet with ${tokens} JBunny tokens`);

    // Dummy response
    res.json({ success: true, message: ${tokens} tokens added to wallet. });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
