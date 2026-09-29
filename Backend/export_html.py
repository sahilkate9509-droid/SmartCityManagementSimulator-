"""
Generate an executive, professional HTML report of all tables in smartcity.db.
Run: python export_html.py
"""

import os
import sqlite3
import json
import webbrowser

DB_FILE = os.path.join(os.path.dirname(__file__), "smartcity.db")
HTML_FILE = os.path.join(os.path.dirname(__file__), "database_report.html")

def generate_report():
    if not os.path.exists(DB_FILE):
        print(f"Error: {DB_FILE} not found.")
        return None

    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [r[0] for r in cursor.fetchall()]

    table_data = {}
    for t in tables:
        cursor.execute(f"PRAGMA table_info({t})")
        cols = [c[1] for c in cursor.fetchall()]
        cursor.execute(f"SELECT * FROM {t}")
        rows = [list(r) for r in cursor.fetchall()]
        table_data[t] = {"columns": cols, "rows": rows}

    conn.close()

    # Generate modern HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart City Management Simulator — Database Tables</title>
    <style>
        :root {{
            --bg: #0b111e;
            --card-bg: #131c2e;
            --border: #20314d;
            --accent: #3b82f6;
            --accent-glow: rgba(59, 130, 246, 0.25);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --warning: #f59e0b;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif; }}
        body {{ background-color: var(--bg); color: var(--text-main); padding: 32px 24px; min-height: 100vh; }}
        .container {{ max-width: 1300px; margin: 0 auto; }}
        
        /* Header */
        .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 28px; padding-bottom: 20px; border-bottom: 1px solid var(--border); }}
        .header-title h1 {{ font-size: 26px; font-weight: 700; color: #fff; display: flex; align-items: center; gap: 10px; }}
        .header-title p {{ color: var(--text-muted); font-size: 14px; margin-top: 5px; }}
        .badge {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); padding: 4px 12px; border-radius: 9999px; font-size: 13px; font-weight: 600; }}
        .btn {{ background: var(--accent); color: white; border: none; padding: 9px 18px; border-radius: 6px; cursor: pointer; font-size: 14px; font-weight: 600; transition: background 0.15s; }}
        .btn:hover {{ background: #2563eb; }}
        
        /* Overview Stats */
        .stats-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 28px; }}
        .stat-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px; padding: 18px; }}
        .stat-label {{ color: var(--text-muted); font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .stat-value {{ font-size: 24px; font-weight: 700; color: #fff; margin-top: 6px; }}
        
        /* Tabs */
        .tabs {{ display: flex; gap: 8px; margin-bottom: 20px; border-bottom: 1px solid var(--border); }}
        .tab-btn {{ background: transparent; color: var(--text-muted); border: none; padding: 12px 20px; font-size: 15px; font-weight: 600; cursor: pointer; border-bottom: 2px solid transparent; transition: all 0.2s; }}
        .tab-btn.active {{ color: #60a5fa; border-bottom-color: #60a5fa; }}
        .tab-btn:hover:not(.active) {{ color: #cbd5e1; }}
        
        /* Table Card */
        .table-card {{ background: var(--card-bg); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.3); margin-bottom: 24px; display: none; }}
        .table-card.active {{ display: block; }}
        .table-header {{ padding: 16px 20px; background: rgba(255,255,255,0.02); border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }}
        .table-header h2 {{ font-size: 17px; font-weight: 600; color: #e2e8f0; }}
        .table-wrapper {{ overflow-x: auto; max-height: 520px; }}
        
        /* Table */
        table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 13.5px; }}
        th {{ background: #0e1626; color: #94a3b8; font-weight: 600; padding: 12px 16px; border-bottom: 1px solid var(--border); white-space: nowrap; position: sticky; top: 0; z-index: 1; }}
        td {{ padding: 12px 16px; border-bottom: 1px solid var(--border); color: #cbd5e1; vertical-align: middle; }}
        tr:hover td {{ background: rgba(59, 130, 246, 0.05); }}
        .empty {{ text-align: center; color: var(--text-muted); padding: 40px; font-size: 15px; }}
        .code-cell {{ font-family: monospace; font-size: 11px; max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; color: #a5b4fc; }}
        .score-pill {{ background: rgba(16, 185, 129, 0.15); color: #34d399; padding: 3px 8px; border-radius: 4px; font-weight: 600; display: inline-block; }}
        
        /* Footer */
        .footer {{ text-align: center; color: var(--text-muted); font-size: 13px; margin-top: 40px; padding-top: 20px; border-top: 1px solid var(--border); }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="header-title">
                <h1>🏙️ Smart City Management Simulator</h1>
                <p>Database Inspector & Supervisor Presentation Report &nbsp;|&nbsp; <code>smartcity.db</code> (SQLite 3)</p>
            </div>
            <div>
                <button class="btn" onclick="window.print()">🖨️ Print / Save as PDF</button>
            </div>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-label">Total Tables</div>
                <div class="stat-value">{len(tables)}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Save Slots Registered</div>
                <div class="stat-value">{len(table_data.get('city_saves', {}).get('rows', []))}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Cities Configured</div>
                <div class="stat-value">{len(table_data.get('cities', {}).get('rows', []))}</div>
            </div>
            <div class="stat-card">
                <div class="stat-label">Telemetry Snapshots</div>
                <div class="stat-value">{len(table_data.get('city_telemetry', {}).get('rows', []))}</div>
            </div>
        </div>

        <div class="tabs">
"""

    for i, t in enumerate(tables):
        active = "active" if i == 0 else ""
        row_count = len(table_data[t]["rows"])
        html += f'            <button class="tab-btn {active}" onclick="switchTab(\'{t}\')">{t} <span class="badge" style="margin-left:6px;">{row_count}</span></button>\n'

    html += """        </div>\n"""

    for i, t in enumerate(tables):
        active = "active" if i == 0 else ""
        cols = table_data[t]["columns"]
        rows = table_data[t]["rows"]

        html += f"""
        <div id="card-{t}" class="table-card {active}">
            <div class="table-header">
                <h2>Table: <code>{t}</code></h2>
                <span class="badge">{len(rows)} records</span>
            </div>
            <div class="table-wrapper">
                <table>
                    <thead>
                        <tr>
"""
        for c in cols:
            html += f"                            <th>{c}</th>\n"
        html += """                        </tr>
                    </thead>
                    <tbody>
"""
        if not rows:
            html += f'                        <tr><td colspan="{len(cols)}" class="empty">No records found in {t}</td></tr>\n'
        else:
            for r in rows:
                html += "                        <tr>\n"
                for idx, val in enumerate(r):
                    val_str = str(val) if val is not None else '<span style="color:#64748b">NULL</span>'
                    # Format JSON or long text
                    if cols[idx] in ("state_json", "raw_json") and len(val_str) > 40:
                        val_str = f'<div class="code-cell" title="{val_str}">{val_str}</div>'
                    elif cols[idx] == "smart_city_score" and isinstance(val, (int, float)):
                        val_str = f'<span class="score-pill">{val:.1f}</span>'
                    elif cols[idx] in ("budget", "starting_budget", "current_budget") and isinstance(val, (int, float)):
                        val_str = f'${val:,.2f}'
                    html += f"                            <td>{val_str}</td>\n"
                html += "                        </tr>\n"

        html += """                    </tbody>
                </table>
            </div>
        </div>
"""

    html += """
        <div class="footer">
            Smart City Management Simulator &bull; Backend Architecture: FastAPI + PostgreSQL / SQLite3 &bull; Generated for Supervisor Review
        </div>
    </div>

    <script>
        function switchTab(name) {
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.toggle('active', btn.textContent.includes(name));
            });
            document.querySelectorAll('.table-card').forEach(card => {
                card.classList.toggle('active', card.id === 'card-' + name);
            });
        }
    </script>
</body>
</html>
"""

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Report successfully created at: {HTML_FILE}")
    return HTML_FILE

if __name__ == "__main__":
    generate_report()
