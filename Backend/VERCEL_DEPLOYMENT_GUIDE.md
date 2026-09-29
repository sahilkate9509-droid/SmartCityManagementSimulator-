# Deploying Smart City Backend to Vercel (Step-by-Step)

This guide shows you how to deploy the **Smart City Simulator Backend** to **Vercel** as high-speed Serverless Python functions.

---

## 🚀 Option 1: Deploy via GitHub (Recommended - 2 Minutes)

### Step 1: Push your project to GitHub
If not already pushed:
```bash
git add Backend/
git commit -m "Configure Vercel serverless backend"
git push
```

### Step 2: Import into Vercel
1. Go to [https://vercel.com/new](https://vercel.com/new) and log in.
2. Select your GitHub repository.
3. In **Project Settings**:
   - **Framework Preset**: Leave as *Other* (or *Python*).
   - **Root Directory**: Click *Edit* and select **`Backend`**.
4. In **Environment Variables**, add:
   - **Name**: `DATABASE_URL`
   - **Value**: Your cloud PostgreSQL connection string (from Supabase, Neon, or Vercel Postgres):
     ```
     postgresql://postgres:[PASSWORD]@db.[REF].supabase.co:5432/postgres?sslmode=require
     ```
     *(If not provided, it will automatically use an in-memory SQLite database in `/tmp`)*.
5. Click **Deploy**.

Within ~60 seconds, your backend will be live at:
`https://your-project-name.vercel.app`

---

## 💻 Option 2: Deploy via Vercel CLI

From your terminal inside the `Backend` directory:
```powershell
cd Backend
npx vercel
```
1. Follow the on-screen prompts:
   - Set up and deploy? **Yes**
   - Which scope? Select your personal account.
   - Link to existing project? **No**
   - Project name? **`smartcity-backend`**
   - Directory located? **`./`**
2. Deploy to production:
   ```powershell
   npx vercel --prod
   ```

---

## 🗄️ Database Options for Vercel

Because Vercel is a serverless platform, each serverless invocation is stateless. For production data persistence across save slots, use a free cloud PostgreSQL database:

| Provider | Setup Time | Free Tier | URL Format |
|---|---|---|---|
| **Neon.tech** | 60 sec | 100% Free Serverless Postgres | `postgresql://user:pass@ep-xyz.neon.tech/neondb?sslmode=require` |
| **Supabase** | 60 sec | 500 MB Free Cloud Postgres | `postgresql://postgres:pass@db.ref.supabase.co:5432/postgres?sslmode=require` |
| **Vercel Storage** | 30 sec | 1-Click "Storage" tab in Vercel | Automatically sets `POSTGRES_URL` |

Simply paste the connection string into your Vercel Project **Settings ➔ Environment Variables** as `DATABASE_URL`.

---

## 🎮 Step 3: Connect Unity to Your Live Vercel API

Once your Vercel backend is deployed:
1. Copy your Vercel URL (e.g. `https://smartcity-backend.vercel.app`).
2. In Unity, select the **CityManager** or **Networking** GameObject with the `CityApiClient` script.
3. Paste the URL into the **Base Url** field:
   ```
   https://smartcity-backend.vercel.app
   ```
4. Now all city saves, slot states, and telemetry will automatically sync live to the cloud!
