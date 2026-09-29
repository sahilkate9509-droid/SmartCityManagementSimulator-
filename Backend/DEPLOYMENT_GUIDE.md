# 🚀 Cloud Database & Backend Deployment Guide

This guide explains how to deploy the **Smart City Management Simulator Backend & Database** to production cloud platforms.

---

## 📋 Architecture Overview

The backend is built with:
- **FastAPI**: High-performance Python asynchronous REST API.
- **SQLAlchemy 2.0**: Object-relational mapping with connection pooling and auto-reconnect.
- **PostgreSQL 16**: Production database storing full game save slots, simulation snapshots, and telemetry.
- **SQLite Fallback**: Zero-config local database (`smartcity.db`) used automatically when offline or during local development.

---

## 🌐 Deployment Option 1: Render.com (Recommended — 100% Free & Automated)

Render provides free hosting for web services and managed PostgreSQL databases.

### Steps:
1. **Push your code to GitHub / GitLab**.
2. Go to [Render Dashboard](https://dashboard.render.com/) and sign up.
3. Click **New +** → **Blueprint**.
4. Select your repository. Render will automatically detect [`render.yaml`](./render.yaml).
5. Render will provision:
   - A managed **PostgreSQL Database** (`smartcity-db`)
   - A Python Web Service (`smartcity-api`)
6. Once deployed, Render gives you a public HTTPS URL (e.g. `https://smartcity-api.onrender.com`).
7. In the game Settings or Unity inspector, set **API Base URL** to your Render URL.

---

## ⚡ Deployment Option 2: Supabase (Free Cloud PostgreSQL) + Any Host

If you want a generous free managed PostgreSQL database with a visual dashboard:

### 1. Create Database on Supabase
1. Go to [supabase.com](https://supabase.com) and create a free project.
2. Go to **Project Settings** → **Database** → **Connection string** → **URI**.
3. Copy your connection string:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT].supabase.co:5432/postgres?sslmode=require
   ```

### 2. Deploy FastAPI App (Render, Railway, or Fly.io)
1. Set the environment variable `DATABASE_URL` to your Supabase connection string.
2. Start command:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
3. The app automatically creates all tables on Supabase upon first launch!

---

## 🐳 Deployment Option 3: Docker Compose (VPS / Self-Hosted)

For running on an Ubuntu/Debian VPS (DigitalOcean Droplet, AWS EC2, Hetzner, Linode):

1. **Install Docker & Docker Compose** on your server:
   ```bash
   curl -fsSL https://get.docker.com | sh
   ```
2. **Clone your project** to the server and enter `Backend/`:
   ```bash
   cd SmartCityManagementSimulator_Professional/Backend
   ```
3. **Start the database and backend**:
   ```bash
   docker compose up -d --build
   ```
4. **Check status**:
   ```bash
   docker compose ps
   curl http://localhost:8000/api/status
   ```
5. Your database is now persisted in the Docker volume `smartcity_pgdata` with automated container restarts.

---

## 💻 Local Development (Zero Configuration)

To run locally on your computer:
1. Open PowerShell / Terminal in `Backend/`:
   ```bash
   pip install -r requirements.txt
   uvicorn app.main:app --reload --port 8000
   ```
2. Open Swagger API documentation:
   👉 **http://127.0.0.1:8000/docs**
3. Open Database Health Status:
   👉 **http://127.0.0.1:8000/api/status**

---

## 🎮 Unity Client Configuration

In Unity:
1. Open [`Assets/Scripts/Networking/CityApiClient.cs`](../Assets/Scripts/Networking/CityApiClient.cs).
2. The `baseUrl` default is `http://127.0.0.1:8000` for local development.
3. To switch to your cloud server, set `CityApiClient.Instance.baseUrl = "https://your-app.onrender.com"` or change it in the Inspector.
4. When saving games in Unity, slots are automatically synchronized to your cloud database!
