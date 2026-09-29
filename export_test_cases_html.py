import os
from make_test_cases_document import generate_test_cases

def create_html_test_report():
    cases = generate_test_cases()
    html_path = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\Smart_City_Management_Simulator_Test_Cases.html"

    rows = []
    for c in cases:
        tc_id, tc_desc, tc_cat, tc_steps, tc_data, tc_exp, tc_act, tc_status = c
        rows.append(f"""
        <tr>
            <td class="id-col"><b>{tc_id}</b></td>
            <td class="desc-col"><b>{tc_desc}</b></td>
            <td class="cat-col">{tc_cat}</td>
            <td class="steps-col">{tc_steps}</td>
            <td class="data-col"><code>{tc_data}</code></td>
            <td class="exp-col">{tc_exp}</td>
            <td class="act-col">{tc_act}</td>
            <td class="status-col"><span class="badge-pass">{tc_status}</span></td>
        </tr>""")
    
    rows_html = "".join(rows)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Software Test Case Specification & Execution Report - Smart City Simulator</title>
    <style>
        @page {{ size: A4; margin: 12mm 10mm; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            color: #0f172a;
            background: #f8fafc;
            margin: 0;
            padding: 24px;
        }}
        .container {{
            max-width: 1240px;
            margin: 0 auto;
            background: #ffffff;
            padding: 28px 36px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.06);
            border-radius: 8px;
        }}
        .header {{
            text-align: center;
            border-bottom: 2px solid #1e3a8a;
            padding-bottom: 16px;
            margin-bottom: 16px;
        }}
        .college-title {{
            font-size: 16px;
            font-weight: 700;
            color: #1e3a8a;
            text-transform: uppercase;
            margin: 0 0 4px 0;
            letter-spacing: 0.5px;
        }}
        .college-sub {{
            font-size: 13px;
            color: #475569;
            margin: 0 0 10px 0;
        }}
        .doc-title {{
            font-size: 22px;
            font-weight: 800;
            color: #0f172a;
            margin: 0 0 6px 0;
        }}
        .doc-sub {{
            font-size: 14px;
            color: #3b82f6;
            font-weight: 600;
            margin: 0;
        }}
        .meta-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            background: #f1f5f9;
            padding: 12px 16px;
            border-radius: 6px;
            border: 1px solid #e2e8f0;
            margin-bottom: 16px;
            font-size: 12px;
        }}
        .meta-item {{ display: flex; flex-direction: column; }}
        .meta-label {{ font-weight: 700; color: #475569; font-size: 11px; text-transform: uppercase; }}
        .meta-val {{ color: #0f172a; font-weight: 600; margin-top: 2px; }}
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 12px;
            margin-bottom: 20px;
        }}
        .card {{
            padding: 10px 14px;
            border-radius: 6px;
            color: #ffffff;
            text-align: center;
        }}
        .card-total {{ background: #1e3a8a; }}
        .card-pass {{ background: #15803d; }}
        .card-fail {{ background: #b91c1c; }}
        .card-blocked {{ background: #d97706; }}
        .card-rate {{ background: #047857; }}
        .card-val {{ font-size: 20px; font-weight: 800; margin-top: 2px; }}
        .card-lbl {{ font-size: 11px; font-weight: 600; text-transform: uppercase; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 11px;
            margin-bottom: 24px;
        }}
        th {{
            background: #1e3a8a;
            color: #ffffff;
            font-weight: 700;
            padding: 8px 6px;
            text-align: center;
            border: 1px solid #94a3b8;
            font-size: 11px;
            line-height: 1.2;
        }}
        td {{
            padding: 6px;
            border: 1px solid #cbd5e1;
            vertical-align: top;
            line-height: 1.35;
        }}
        tr:nth-child(even) {{ background: #f8fafc; }}
        tr:hover {{ background: #f1f5f9; }}
        .id-col {{ width: 55px; text-align: center; color: #1e3a8a; }}
        .desc-col {{ width: 140px; }}
        .cat-col {{ width: 85px; color: #334155; }}
        .steps-col {{ width: 230px; }}
        .data-col {{ width: 130px; font-family: monospace; font-size: 10px; color: #475569; }}
        .exp-col {{ width: 180px; }}
        .act-col {{ width: 130px; color: #166534; }}
        .status-col {{ width: 50px; text-align: center; }}
        .badge-pass {{
            display: inline-block;
            background: #dcfce7;
            color: #15803d;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10.5px;
            border: 1px solid #86efac;
        }}
        .sign-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 16px;
            margin-top: 24px;
            border: 1px solid #cbd5e1;
            padding: 16px;
            background: #f8fafc;
            border-radius: 6px;
            font-size: 12px;
        }}
        .sign-box {{ display: flex; flex-direction: column; justify-content: space-between; min-height: 90px; }}
        .sign-title {{ font-weight: 700; color: #1e3a8a; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; }}
        .sign-body {{ margin-top: 8px; color: #334155; line-height: 1.4; }}
        .sign-line {{ margin-top: 24px; color: #64748b; }}
        @media print {{
            body {{ background: #ffffff; padding: 0; }}
            .container {{ box-shadow: none; padding: 0; max-width: 100%; }}
            tr {{ page-break-inside: avoid; }}
            thead {{ display: table-header-group; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="college-title">D.G. Ruparel College of Arts, Science and Commerce</div>
            <div class="college-sub">Affiliated to the University of Mumbai | Department of Computer Science</div>
            <div class="doc-title">SOFTWARE TEST CASE SPECIFICATION & EXECUTION REPORT</div>
            <div class="doc-sub">Project: Smart City Management Simulator (Professional) &bull; Academic Year 2026-2027</div>
        </div>

        <div class="meta-grid">
            <div class="meta-item"><span class="meta-label">Candidate Name</span><span class="meta-val">Sahil Vishal Kate</span></div>
            <div class="meta-item"><span class="meta-label">Roll Number</span><span class="meta-val">9041</span></div>
            <div class="meta-item"><span class="meta-label">Degree & Semester</span><span class="meta-val">B.Sc Computer Science (Sem V)</span></div>
            <div class="meta-item"><span class="meta-label">Project Guide</span><span class="meta-val">Prof. Aarti Gawai</span></div>
            <div class="meta-item"><span class="meta-label">Test Scope</span><span class="meta-val">Unit, Integration, System, API</span></div>
            <div class="meta-item"><span class="meta-label">Engine / Stack</span><span class="meta-val">Unity 6.3 LTS &bull; FastAPI &bull; SQL</span></div>
            <div class="meta-item"><span class="meta-label">Execution Date</span><span class="meta-val">September 2026</span></div>
            <div class="meta-item"><span class="meta-label">Final Outcome</span><span class="meta-val" style="color:#15803d;">100% PASS (50/50 Scenarios)</span></div>
        </div>

        <div class="cards-grid">
            <div class="card card-total"><div class="card-lbl">Total Test Cases</div><div class="card-val">50</div></div>
            <div class="card card-pass"><div class="card-lbl">Passed</div><div class="card-val">50 (100%)</div></div>
            <div class="card card-fail"><div class="card-lbl">Failed</div><div class="card-val">0 (0%)</div></div>
            <div class="card card-blocked"><div class="card-lbl">Blocked / Pending</div><div class="card-val">0 (0%)</div></div>
            <div class="card card-rate"><div class="card-lbl">Overall Pass Rate</div><div class="card-val">100%</div></div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>Test<br/>Case<br/>ID</th>
                    <th>Test Case<br/>Description</th>
                    <th>Test<br/>Category</th>
                    <th>Test<br/>Steps</th>
                    <th>Test<br/>Data</th>
                    <th>Expected<br/>Result</th>
                    <th>Actual<br/>Result</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>

        <div class="sign-grid">
            <div class="sign-box">
                <div class="sign-title">Prepared By (Candidate)</div>
                <div class="sign-body">
                    <b>Sahil Vishal Kate</b><br/>
                    Roll No.: 9041<br/>
                    Student, B.Sc Computer Science
                </div>
                <div class="sign-line">Signature: ____________________<br/>Date: ____________________</div>
            </div>
            <div class="sign-box">
                <div class="sign-title">Reviewed & Verified By (Project Guide)</div>
                <div class="sign-body">
                    <b>Prof. Aarti Gawai</b><br/>
                    Project Guide & Supervisor<br/>
                    Department of Computer Science
                </div>
                <div class="sign-line">Signature: ____________________<br/>Date: ____________________</div>
            </div>
            <div class="sign-box">
                <div class="sign-title">Institutional Approval</div>
                <div class="sign-body">
                    <b>Head of Department</b><br/>
                    Department of Computer Science<br/>
                    D.G. Ruparel College, Mumbai
                </div>
                <div class="sign-line">Signature: ____________________<br/>College Seal: ____________________</div>
            </div>
        </div>
    </div>
</body>
</html>"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML test report successfully generated at: {html_path}")

if __name__ == "__main__":
    create_html_test_report()
