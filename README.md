# Smart City Management Simulator — Professional Development Build

Unity target: **Unity 6.3 LTS (6000.3.21f1)**
Backend: **FastAPI + PostgreSQL 17**

## Run the Unity project
1. Extract the project folder.
2. Unity Hub → Add → Add project from disk.
3. Select this folder and open it with Unity 6.3 LTS.
4. Wait until Unity finishes compiling/importing.
5. The Editor builder should generate all scenes automatically.
6. If it does not, use **Tools → Smart City → Rebuild Professional Project**.
7. Open `Assets/Scenes/MainMenu.unity` and press Play.

## Demo login
- Email: `admin@smartcity.gov`
- Password: `admin123`

The current login is intentionally local/demo-only. Production authentication should use hashed server credentials and tokens.

## Controls
- WASD / Arrow keys: camera movement
- Hold Right Mouse Button: rotate
- Mouse wheel: zoom
- In-game 1x/2x/4x buttons: simulation speed

## Implemented in this build
- Main Menu, Admin Login, Create City
- Interactive generated 3D city with residential/commercial/industrial districts
- Roads, river, bridges, parks, public facilities and moving traffic
- Pan/orbit/zoom city camera
- Day/night cycle and changing weather
- Budget/economy simulation
- Population/housing/employment simulation
- Traffic efficiency
- Electricity, water and waste simulation
- Healthcare, education, police and fire metrics
- Environment, pollution, AQI, green coverage and sustainability
- Citizen request generation and resolution
- Random city incidents/events
- Smart City Score and progression levels
- Renewable energy / smart traffic / advanced transit unlocks
- Construction management
- Public transport expansion
- Live alerts
- 30-day analytics history and graphs
- Local JSON save via Unity PlayerPrefs
- FastAPI + PostgreSQL CRUD backend scaffold
- Swagger UI through FastAPI `/docs`

## Backend
With Docker installed, from the project root run:

```bash
docker compose up
```

Then open the API docs at `http://127.0.0.1:8000/docs`.

Required CRUD endpoints are implemented:
- POST `/cities`
- GET `/cities`
- GET `/cities/{id}`
- PUT `/cities/{id}`
- DELETE `/cities/{id}`

Example POST body:
```json
{
  "city_name": "Green Valley",
  "difficulty": "Easy",
  "starting_budget": 150000
}
```

## Important development note
This source package was generated outside the Unity Editor, so it has not been compiled or Play-tested in Unity in this environment. Open it in Unity and, if the Console shows errors, send the **first red Console error**. Fix the first error before addressing later ones, because later errors may be cascading.

## Next professional polish stages
Replace generated primitive buildings/vehicles with licensed or original 3D assets, add placement ghost/grid tools, NavMesh/pathfinding, traffic signals, animated buses/emergency dispatch, map overlays, sounds, particle weather, production authentication, and full API-backed save synchronization.
