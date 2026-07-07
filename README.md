# 🚀 AI Resume Screening Platform

An AI-powered Resume Screening Platform built with **FastAPI**, **Sentence Transformers**, **PostgreSQL**, and **Streamlit**. This application helps recruiters automatically match resumes with job descriptions using semantic similarity instead of simple keyword matching.

---

## 📌 Features

- 📄 Upload resumes (PDF & DOCX)
- 💼 Create and manage job descriptions
- 🤖 AI-powered resume matching using Sentence Transformers
- 📊 Semantic similarity scoring
- 🔍 Missing skills detection
- 🗄️ PostgreSQL database support
- ⚡ FastAPI REST APIs
- 🎨 Streamlit frontend
- 🐳 Docker support
- ☁️ Ready for deployment on Render

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn

### Machine Learning
- Sentence Transformers
- Scikit-learn
- Cosine Similarity

### Frontend
- Streamlit

### Deployment
- Docker
- Docker Compose
- Render

---

# 📂 Project Structure

```
AI Resume Project
│
├── backend
│   ├── app
│   │   ├── routers
│   │   ├── ml
│   │   ├── utils
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend
│   └── streamlit_app.py
│
├── docker-compose.yml
├── render.yaml
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Screening.git
```

```bash
cd AI-Resume-Screening
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
cd backend
```

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file inside the backend folder.

Example

```
DATABASE_URL=sqlite:///./app.db
MODEL_NAME=all-MiniLM-L6-v2
```

---

## 5. Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

## 6. Run Streamlit

Open another terminal

```bash
streamlit run frontend/streamlit_app.py
```

---

# 📌 API Endpoints

### Resume

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/resumes/upload` | Upload Resume |
| GET | `/resumes/` | Get All Resumes |

---

### Jobs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/jobs/` | Create Job |
| GET | `/jobs/` | Get All Jobs |

---

### Matching

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/matches/` | Match Resume |
| GET | `/matches/` | Match History |

---

# 🤖 How AI Works

1. Resume text is extracted from PDF/DOCX.
2. Job description is stored in the database.
3. Sentence Transformer converts both texts into embeddings.
4. Cosine Similarity calculates semantic similarity.
5. The system generates:
   - Match Score
   - Missing Skills
   - Match History

---

# 📸 Screenshots

### Upload Resume

(Add screenshot here)

---

### Create Job

(Add screenshot here)

---

### Match Results

(Add screenshot here)

---

# 🐳 Docker

Build

```bash
docker-compose up --build
```

---

# ☁️ Deployment

Backend

- Render

Frontend

- Streamlit Community Cloud

Database

- PostgreSQL

---

# 🚀 Future Improvements

- User Authentication (JWT)
- Resume Ranking
- Skill Extraction using LLMs
- OpenAI/Gemini Integration
- Recruiter Dashboard
- Candidate Dashboard
- Email Notifications
- Resume Recommendations
- Admin Panel

---

# 👨‍💻 Author

**Mohammad Shoaib**

- MCA Graduate
- AI & Machine Learning Engineer
- Python Developer

GitHub:

https://github.com/mohd-Shoaib-ali

LinkedIn:

https://www.linkedin.com/in/mohammed-shoaib-b72669225/

---

