import os
import sys
import unittest
import json

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

TEST_DB = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_smartcity.db"))
os.environ["DATABASE_URL"] = f"sqlite:///{TEST_DB}"

try:
    import fastapi
    import sqlalchemy
    from fastapi.testclient import TestClient
    HAS_DEPS = True
except ImportError:
    HAS_DEPS = False

class TestBackendAPI(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(TEST_DB):
            try:
                os.remove(TEST_DB)
            except Exception:
                pass
    @unittest.skipUnless(HAS_DEPS, "FastAPI / SQLAlchemy dependencies not installed in global environment")
    def test_legacy_city_flow(self):
        from Backend.app.main import app
        from Backend.app.database import Base, engine

        Base.metadata.create_all(bind=engine)
        client = TestClient(app)

        # 1. Health check
        res = client.get("/health")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["ok"])
        self.assertIn("database", res.json())

        # 2. Create City
        res = client.post("/cities", json={
            "city_name": "Metropolis",
            "difficulty": "Easy",
            "starting_budget": 200000.0
        })
        self.assertEqual(res.status_code, 201)
        data = res.json()
        self.assertTrue(data["success"])
        city_id = data["city_id"]

        # 3. Get City
        res = client.get(f"/cities/{city_id}")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["city_name"], "Metropolis")

        # 4. Update City
        res = client.put(f"/cities/{city_id}", json={
            "population": 2500,
            "happiness": 88.0
        })
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["population"], 2500)

        # 5. Delete City
        res = client.delete(f"/cities/{city_id}")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["success"])

    @unittest.skipUnless(HAS_DEPS, "FastAPI / SQLAlchemy dependencies not installed in global environment")
    def test_cloud_save_slot_and_telemetry(self):
        from Backend.app.main import app
        from Backend.app.database import Base, engine

        Base.metadata.create_all(bind=engine)
        client = TestClient(app)

        # Dummy CityState JSON mimicking Unity client
        mock_city_state = {
            "cityId": 1,
            "cityName": "Neo-Veridia",
            "difficulty": "Medium",
            "budget": 125000.0,
            "population": 450,
            "happiness": 82.5,
            "sustainability": 74.0,
            "smartCityScore": 95.0,
            "houses": 8,
            "powerPlants": 2,
            "waterFacilities": 2,
            "hospitals": 1,
            "policeStations": 1,
            "roads": 14
        }
        state_str = json.dumps(mock_city_state)

        # 1. Save to slot 0
        save_payload = {
            "slot_index": 0,
            "city_name": "Neo-Veridia",
            "difficulty": "Medium",
            "day": 12,
            "year": 2026,
            "budget": 125000.0,
            "population": 450,
            "happiness": 82.5,
            "sustainability": 74.0,
            "smart_city_score": 95.0,
            "level": 2,
            "progression_title": "Growing Town",
            "state_json": state_str
        }
        res = client.post("/cities/save-slot", json=save_payload)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["success"])
        self.assertEqual(res.json()["slot_index"], 0)

        # 2. List slots
        res = client.get("/cities/slots")
        self.assertEqual(res.status_code, 200)
        slots = res.json()
        self.assertGreaterEqual(len(slots), 1)
        self.assertEqual(slots[0]["city_name"], "Neo-Veridia")

        # 3. Load slot 0
        res = client.get("/cities/slots/0")
        self.assertEqual(res.status_code, 200)
        slot_data = res.json()
        self.assertEqual(slot_data["city_name"], "Neo-Veridia")
        self.assertEqual(slot_data["state_json"], state_str)

        # 4. Record simulation telemetry
        telemetry_payload = {
            "slot_index": 0,
            "in_game_day": 12,
            "in_game_year": 2026,
            "budget": 125000.0,
            "population": 450,
            "happiness": 82.5,
            "sustainability": 74.0,
            "traffic_efficiency": 78.0,
            "pollution": 12.0,
            "crime_rate": 8.5,
            "power_balance": 450.0,
            "water_balance": 600.0
        }
        res = client.post("/cities/telemetry", json=telemetry_payload)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json()["in_game_day"], 12)

        # 5. Fetch telemetry history
        res = client.get("/cities/telemetry/0")
        self.assertEqual(res.status_code, 200)
        history = res.json()
        self.assertGreaterEqual(len(history), 1)

        # 6. Check system status API
        res = client.get("/api/status")
        self.assertEqual(res.status_code, 200)
        status_data = res.json()
        self.assertEqual(status_data["status"], "online")
        self.assertGreaterEqual(status_data["active_cloud_saves"], 1)

        # 7. Delete slot 0
        res = client.delete("/cities/slots/0")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["success"])

        # 8. Verify slot is gone
        res = client.get("/cities/slots/0")
        self.assertEqual(res.status_code, 404)

    def test_requirements_file_exists(self):
        req_path = os.path.join(os.path.dirname(__file__), "..", "requirements.txt")
        self.assertTrue(os.path.exists(req_path))

if __name__ == "__main__":
    unittest.main()
