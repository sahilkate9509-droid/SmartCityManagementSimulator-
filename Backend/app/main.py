from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import init_db, get_db, get_db_info
from .routers import cities, auth
from . import models, schemas

# Initialize database schema automatically on launch
init_db()

app = FastAPI(
    title="Smart City Management Simulator API",
    version="1.0.0",
    description="Production Cloud Database and Simulation Backend for Smart City Management Simulator."
)

# Enable CORS for Unity Editor, Desktop builds, WebGL clients, and web dashboards
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(cities.router)

from fastapi.responses import HTMLResponse, RedirectResponse

@app.get("/", include_in_schema=False)
def root_redirect():
    return RedirectResponse(url="/dashboard")

@app.get("/dashboard", response_class=HTMLResponse, tags=["General"])
def dashboard(db: Session = Depends(get_db)):
    saves = db.query(models.CitySave).order_by(models.CitySave.slot_index.asc()).all()
    cities_list = db.query(models.City).all()
    telemetry_count = db.query(models.CityTelemetry).count()

    saves_html = ""
    for s in saves:
        saves_html += f"""
        <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:20px; margin-bottom:16px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h3 style="margin:0; color:#38bdf8; font-size:20px;">Slot {s.slot_index}: {s.city_name}</h3>
                <span style="background:#0284c7; color:#fff; padding:4px 12px; border-radius:20px; font-size:12px;">{s.difficulty}</span>
            </div>
            <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(140px, 1fr)); gap:12px; margin-top:16px;">
                <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8;">BUDGET</div>
                    <div style="font-size:18px; font-weight:bold; color:#4ade80;">${s.budget:,.2f}</div>
                </div>
                <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8;">POPULATION</div>
                    <div style="font-size:18px; font-weight:bold; color:#f8fafc;">{s.population:,}</div>
                </div>
                <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8;">HAPPINESS</div>
                    <div style="font-size:18px; font-weight:bold; color:#fbbf24;">{s.happiness:.1f}%</div>
                </div>
                <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8;">SUSTAINABILITY</div>
                    <div style="font-size:18px; font-weight:bold; color:#34d399;">{s.sustainability:.1f}%</div>
                </div>
                <div style="background:rgba(0,0,0,0.25); padding:10px; border-radius:8px;">
                    <div style="font-size:11px; color:#94a3b8;">SMART SCORE</div>
                    <div style="font-size:18px; font-weight:bold; color:#a78bfa;">{s.smart_city_score:.1f}</div>
                </div>
            </div>
            <div style="margin-top:12px; font-size:12px; color:#64748b;">
                Day {s.day}, Year {s.year} &bull; Title: {s.progression_title} &bull; Updated: {s.updated_at}
            </div>
        </div>
        """

    if not saves_html:
        saves_html = "<div style='color:#94a3b8; padding:20px; text-align:center;'>No save slots yet.</div>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart City Database Dashboard</title>
        <meta charset="utf-8">
        <style>
            body {{ font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Oxygen,Ubuntu,sans-serif; background:#0f172a; color:#f8fafc; margin:0; padding:32px; }}
            .container {{ max-width:960px; margin:0 auto; }}
            .header {{ display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #334155; padding-bottom:20px; margin-bottom:28px; }}
            .badge {{ background:#10b981; color:#fff; padding:6px 14px; border-radius:24px; font-size:13px; font-weight:600; }}
            .card {{ background:#1e293b; border-radius:16px; padding:24px; margin-bottom:24px; border:1px solid #334155; }}
            a.btn {{ background:#3b82f6; color:#fff; text-decoration:none; padding:8px 16px; border-radius:8px; font-size:13px; font-weight:500; display:inline-block; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div>
                    <h1 style="margin:0 0 6px 0; font-size:26px;">🏙️ Smart City Simulator — Live Database</h1>
                    <div style="color:#94a3b8; font-size:14px;">Database: {get_db_info().get('engine', 'sqlite').upper()} | Location: smartcity.db</div>
                </div>
                <div class="badge">&#x2714; SERVER ONLINE</div>
            </div>

            <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; margin-bottom:24px;">
                <div class="card" style="margin:0; padding:18px;">
                    <div style="color:#94a3b8; font-size:12px;">ACTIVE SAVE SLOTS</div>
                    <div style="font-size:28px; font-weight:bold; color:#38bdf8; margin-top:4px;">{len(saves)}</div>
                </div>
                <div class="card" style="margin:0; padding:18px;">
                    <div style="color:#94a3b8; font-size:12px;">REGISTERED CITIES</div>
                    <div style="font-size:28px; font-weight:bold; color:#4ade80; margin-top:4px;">{len(cities_list)}</div>
                </div>
                <div class="card" style="margin:0; padding:18px;">
                    <div style="color:#94a3b8; font-size:12px;">TELEMETRY RECORDS</div>
                    <div style="font-size:28px; font-weight:bold; color:#fbbf24; margin-top:4px;">{telemetry_count}</div>
                </div>
            </div>

            <div class="card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;">
                    <h2 style="margin:0; font-size:18px;">💾 Cloud Save Slots</h2>
                    <a href="/docs" class="btn" target="_blank">Open API Docs &rarr;</a>
                </div>
                {saves_html}
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.get("/health", tags=["General"])
def health():
    return {"ok": True, "database": get_db_info()}

@app.get("/api/status", response_model=schemas.SystemHealthResponse, tags=["General"])
def system_status(db: Session = Depends(get_db)):
    active_saves = db.query(models.CitySave).count()
    return {
        "status": "online",
        "service": "Smart City Management Simulator API",
        "version": "1.0.0",
        "database": get_db_info(),
        "active_cloud_saves": active_saves
    }
