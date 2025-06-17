# Personal AI Assistant with Context Retention

A sophisticated conversational AI assistant that maintains context across conversations, learns user preferences, adapts communication style, and provides personalized assistance using Google Gemini.

## 🎯 Project Overview

This project implements a multi-level memory system that builds a comprehensive user profile over time, handling various request types while maintaining conversation continuity and personalizing interactions.

## 🏗️ System Architecture

### Phase 1: Core Assistant Infrastructure

#### User Profile Management
- Unique user identification system
- Comprehensive profile schema including:
  - Demographics (optional)
  - Preferences (topics, communication style)
  - Interaction patterns
  - Task history
  - Knowledge domains
- Secure storage with encryption

#### Request Classification Engine
- Multi-label classification for:
  - Information queries
  - Task management
  - Calculations/analysis
  - Recommendations
  - Casual conversation
  - Learning requests
- Intent detection with confidence scores
- Entity extraction and slot filling

#### Session Management
- Conversation threading
- Context window management
- Session persistence across devices
- Conversation branching support

### Phase 2: Memory Architecture 

#### Short-term Memory (Working Memory)
- Current conversation context (last 10-15 exchanges)
- Active task states
- Temporary variables and calculations
- Recent entity mentions
- Implementation: Redis with TTL

#### Long-term Memory Systems

**Declarative Memory:**
- User facts and preferences
- Learned information
- Custom knowledge base

**Procedural Memory:**
- Task completion patterns
- User-specific workflows
- Successful solution strategies

**Episodic Memory:**
- Complete conversation histories
- Significant events/milestones
- Emotional context markers

#### Semantic Memory Network
- Knowledge graph of user interests
- Concept relationships
- Domain-specific vocabularies
- Cross-reference system

### Phase 3: Personalization Engine 

#### Communication Style Adaptation
- Analyze user's language patterns:
  - Formality level
  - Vocabulary complexity
  - Sentence structure
  - Emoji/punctuation usage
- Mirror appropriate style elements
- Gradual adaptation over time

#### Preference Learning
- Track interaction patterns:
  - Topic preferences
  - Response length preferences
  - Detail level requirements
  - Time-of-day patterns
- Build preference vectors
- A/B test response strategies

#### Proactive Assistance
- Reminder system with smart scheduling
- Habit detection and reinforcement
- Contextual suggestions
- Predictive task completion

## 🛠️ Technical Stack

- **LLM:** Google Gemini Pro
- **Memory Store:** Redis + PostgreSQL
- **Knowledge Graph:** Neo4j or ArangoDB
- **Backend:** FastAPI with WebSocket support
- **Frontend:** React with chat UI library
- **Task Queue:** Celery
- **Monitoring:** ELK stack

## 📦 Deliverables

### 1. Core Assistant System
- Chat interface (web/CLI)
- User profile dashboard
- Memory visualization tool
- Admin panel for monitoring

### 2. Demonstration Scenarios
- Multi-day conversation continuity
- Style adaptation examples
- Preference learning showcase
- Complex task completion
- Knowledge retention demo

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone <repository-url>
cd personal-ai-assistant

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and configuration

# Start Redis server
redis-server

# Initialize database
python init_db.py

# Run the application
 uvicorn app.main:app --reload
```

## 🔐 Privacy & Security

This assistant implements privacy-preserving techniques and secure storage for user data. All personal information is encrypted and stored locally by default. Users have full control over their data and can request deletion at any time.

---

**Note:** This is an educational project focused on building advanced conversational AI systems with memory capabilities. Always ensure compliance with privacy regulations and ethical AI practices when deploying such systems.
