# 📚 NeuraLib

AI-powered reading platform with personalized book recommendations

---

## Features

- 🔐 JWT Authentication
- 📖 Book & Category Management
- 🤖 AI-Powered Recommendations
- 📊 Reading Progress Tracking
- 🔔 Notifications

## Tech Stack

- Python / Django / Django REST Framework
- PostgreSQL
- Docker

## Installation

### Local Setup

```bash
# Clone repository
git clone https://github.com/ThompsonShell/NeuraLib.git
cd NeuraLib

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

### Docker Setup

```bash
# Build and run
docker-compose up --build
```

## Roadmap

**Phase 1** - User authentication & database setup  
**Phase 2** - Book management & user profiles  
**Phase 3** - AI recommendation engine  
**Phase 4** - Notifications & testing

## Author

**Thompson Khorazmiy**  
Backend Developer | AI Enthusiast

GitHub: [@ThompsonShell](https://github.com/ThompsonShell)

---

⭐ Star this repo if you find it useful!