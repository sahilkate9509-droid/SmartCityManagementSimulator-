# Smart City — Music Instructions

## How to add your own background music

1. Create this folder structure in Unity:
   `Assets/Resources/Music/`

2. Drop any `.mp3`, `.wav`, or `.ogg` audio file into that folder

3. Rename it to: `CityTheme`
   (so it appears as `Assets/Resources/Music/CityTheme.mp3`)

4. Press Play — MusicManager will automatically find and use it.

## If no music file is present

MusicManager generates a procedural ambient drone (layered harmonic sine waves)
as a pleasant fallback. The game will never crash or error — it always has music.

## Free royalty-free city music sources

- https://freemusicarchive.org  (search "ambient city")
- https://pixabay.com/music     (search "lofi city")
- https://opengameart.org       (search "city ambient loop")

## Controlling music

- Main Menu: click "🔊 Music: ON / 🔇 Music: OFF" button
- In-game HUD: click the 🔊/🔇 icon in the top control bar
- Settings page: Music Volume slider controls the volume

Volume is saved to PlayerPrefs and persists between sessions.
