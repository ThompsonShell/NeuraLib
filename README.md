# 📚 NeuraLib

## 🚀 Features

- 🔐 **JWT Authentication** - secure login & registration
- 📖 **Book & Category Management** - CRUD operations for books and categories
- 🤖 **AI-Powered Recommendations** - personalized book suggestions
- 📊 **Reading Progress Tracking** - track your reading journey
- 🔔 **Notifications** - stay updated on new books or reminders

---

## 🛠 Tech Stack

- **Backend:** Python / Django / Django REST Framework  
- **Database:** PostgreSQL  
- **Containerization:** Docker  

---

## 💻 Installation

### 1️⃣ Local Setup

```bash
# Clone repository
git clone https://github.com/ThompsonShell/NeuraLib.git
cd NeuraLib

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
