"""
Quick Database Inspector for Smart City Management Simulator
Run: python view_db.py
"""

import os
import sqlite3
import json

DB_FILE = os.path.join(os.path.dirname(__file__), "smartcity.db")

def sync_from_unity():
    """Detects and imports any city saves stored in Unity PlayerPrefs into SQLite."""
    try:
        import winreg
        reg_path = r"Software\Unity\UnityEditor\DefaultCompany\SmartCityManagementSimulator_Professional"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path)
        saves_found = []
        i = 0
        while True:
            try:
                name, val, _ = winreg.EnumValue(key, i)
                if "Slot" in name and not name.endswith("_Meta") and "_Meta_" not in name:
                    if isinstance(val, bytes):
                        text = val.decode("utf-8", errors="ignore").rstrip("\x00")
                        try:
                            data = json.loads(text)
                            slot_idx = 0
                            for s in range(5):
                                if f"Slot{s}" in name:
                                    slot_idx = s
                                    break
                            saves_found.append((slot_idx, data, text))
                        except Exception:
                            pass
                i += 1
            except OSError:
                break

        if saves_found and os.path.exists(DB_FILE):
            conn = sqlite3.connect(DB_FILE)
            cur = conn.cursor()
            for slot_idx, d, raw_json in saves_found:
                city_name = d.get("cityName", f"City Slot {slot_idx}")
                diff = d.get("difficulty", "Easy")
                day = d.get("day", 1)
                year = d.get("year", 2026)
                budget = d.get("budget", 150000.0)
                pop = d.get("population", 120)
                hap = d.get("happiness", 55.0)
                sus = d.get("sustainability", 30.0)
                score = d.get("smartCityScore", 0.0)
                level = d.get("level", 1)
                title = d.get("progressionTitle", "Small Town")
                cur.execute("""
                    INSERT INTO city_saves (slot_index, city_name, difficulty, day, year, budget, population, happiness, sustainability, smart_city_score, level, progression_title, state_json)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(slot_index) DO UPDATE SET
                        city_name=excluded.city_name,
                        budget=excluded.budget,
                        population=excluded.population,
                        happiness=excluded.happiness,
                        sustainability=excluded.sustainability,
                        smart_city_score=excluded.smart_city_score,
                        state_json=excluded.state_json
                """, (slot_idx, city_name, diff, day, year, budget, pop, hap, sus, score, level, title, raw_json))
            conn.commit()
            conn.close()
    except Exception:
        pass

def view_database():
    sync_from_unity()
    if not os.path.exists(DB_FILE):
        print(f"Database file not found at: {DB_FILE}")
        return

    print("=" * 60)
    print("  SMART CITY MANAGEMENT SIMULATOR - DATABASE INSPECTOR")
    print(f"  Location: {DB_FILE}")
    print("=" * 60)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # 1. List Tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables = [r[0] for r in cursor.fetchall()]
    print(f"\n[+] Tables in database: {', '.join(tables)}")

    # 2. City Saves (Slots 0 - 4)
    print("\n" + "-" * 60)
    print("  TABLE: city_saves (Cloud Save Slots)")
    print("-" * 60)
    try:
        cursor.execute("SELECT id, slot_index, city_name, difficulty, day, year, budget, population, happiness, sustainability, smart_city_score, updated_at FROM city_saves ORDER BY slot_index ASC")
        saves = cursor.fetchall()
        if not saves:
            print("  (No save slots saved yet. Play the game and save, or use the API)")
        else:
            for s in saves:
                print(f"  * Slot {s[1]}: '{s[2]}' ({s[3]})")
                print(f"    - Day: {s[4]} | Year: {s[5]}")
                print(f"    - Budget: ${s[6]:,.2f} | Population: {s[7]:,}")
                print(f"    - Happiness: {s[8]:.1f}% | Sustainability: {s[9]:.1f}% | Smart Score: {s[10]:.1f}")
                print(f"    - Last Updated: {s[11]}")
    except Exception as e:
        print(f"  Error reading city_saves: {e}")

    # 3. Cities Table (Legacy/Created Cities)
    print("\n" + "-" * 60)
    print("  TABLE: cities (Registered Cities)")
    print("-" * 60)
    try:
        cursor.execute("SELECT id, city_name, difficulty, starting_budget, current_budget, population, happiness, sustainability, smart_city_score FROM cities")
        cities = cursor.fetchall()
        if not cities:
            print("  (No cities registered yet)")
        else:
            for c in cities:
                print(f"  * [{c[0]}] {c[1]} ({c[2]}): Budget=${c[4]:,.2f}, Pop={c[5]}, Happiness={c[6]:.1f}%, Score={c[8]:.1f}")
    except Exception as e:
        print(f"  Error reading cities: {e}")

    # 4. Telemetry
    print("\n" + "-" * 60)
    print("  TABLE: city_telemetry (Historical Time-Series)")
    print("-" * 60)
    try:
        cursor.execute("SELECT COUNT(*) FROM city_telemetry")
        count = cursor.fetchone()[0]
        print(f"  Total Telemetry records: {count}")
    except Exception as e:
        print(f"  Error reading telemetry: {e}")

    print("\n" + "=" * 60)
    conn.close()

if __name__ == "__main__":
    view_database()
