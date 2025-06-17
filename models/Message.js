const mongoose = require('mongoose');

const messageSchema = new mongoose.Schema({
  role: String,         // 'user' or 'assistant'
  content: String,      // Message text
  sessionId: String,    // To identify user sessions
  timestamp: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Message', messageSchema);
