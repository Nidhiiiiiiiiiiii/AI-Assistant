const express = require('express');
const axios = require('axios');
const Message = require('../models/Message');

const router = express.Router();

router.post('/', async (req, res) => {
  const { message, sessionId } = req.body;

  try {
    // Save user message
    await Message.create({ role: 'user', content: message, sessionId });

    // Fetch full conversation for context
    const history = await Message.find({ sessionId }).sort({ timestamp: 1 });

    // Format for Ollama
    const messages = history.map(msg => ({
      role: msg.role,
      content: msg.content
    }));

    const ollamaResponse = await axios.post('http://localhost:11434/api/chat', {
      model: 'phi3',
      messages,
      stream: false
    });

    const reply = ollamaResponse.data.message.content;

    // Save assistant reply
    await Message.create({ role: 'assistant', content: reply, sessionId });

    res.json({ reply });

  } catch (err) {
    console.error(err.message);
    res.status(500).json({ error: 'Server Error' });
  }
});

module.exports = router;
