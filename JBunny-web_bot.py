require('dotenv').config();
const express = require('express');
const { Web3 } = require('web3'); // or another blockchain library
const app = express();
app.use(express.json());

// Initialize Web3 or another blockchain library
const web3 = new Web3(new Web3.providers.HttpProvider('https://your-blockchain-node-url'));

app.post('/reward-crypto', async (req, res) => {
    const { user, receiverAddress, amount } = req.body;
    
    // Ensure request validation
    if (!receiverAddress  !amount  !user) {
        return res.status(400).json({ success: false, message: 'Invalid request' });
    }

    try {
        // Example for Ethereum; adjust as necessary for your blockchain
        const walletAddress = process.env.WALLET_ADDRESS;
        const walletPrivateKey = process.env.WALLET_PRIVATE_KEY;

        // Unlock wallet
        web3.eth.accounts.wallet.add(walletPrivateKey);

        // Create transaction object
        const tx = {
            from: walletAddress,
            to: receiverAddress,
            value: web3.utils.toWei(amount.toString(), 'ether'), // adjust unit based on your token
            gas: 2000000
        };

        // Send transaction
        const receipt = await web3.eth.sendTransaction(tx);

        res.json({ success: true, message: Rewarded ${amount} tokens to ${receiverAddress}, receipt });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ success: false, message: 'Failed to reward tokens' });
    }
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
