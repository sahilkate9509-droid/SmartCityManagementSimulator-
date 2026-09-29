using System.IO;
using UnityEngine;
public class MusicManager : MonoBehaviour
{
    // ── Singleton ─────────────────────────────────────────────────────────────
    static MusicManager _inst;

    public static bool IsPlaying =>
        _inst != null && _inst._src != null &&
        _inst._src.isPlaying && !_inst._muted;

    // ── PlayerPrefs keys ──────────────────────────────────────────────────────
    const string PREF_VOL   = "MusicVol";
    const string PREF_MUTED = "MusicMuted";
    const string CLIP_RES   = "Music/CityTheme";

    AudioSource _src;
    bool        _muted;
    float       _vol = 0.75f;

    // ─────────────────────────────────────────────────────────────────────────
    // Auto-boot before any scene
    // ─────────────────────────────────────────────────────────────────────────
    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
    static void AutoBoot()
    {
        if (_inst != null) return;
        var go = new GameObject("[MusicManager]");
        DontDestroyOnLoad(go);
        go.AddComponent<MusicManager>();
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Lifecycle
    // ─────────────────────────────────────────────────────────────────────────
    void Awake()
    {
        if (_inst != null && _inst != this) { Destroy(gameObject); return; }
        _inst = this;
        DontDestroyOnLoad(gameObject);

        _src              = gameObject.AddComponent<AudioSource>();
        _src.loop         = true;
        _src.playOnAwake  = false;
        _src.spatialBlend = 0f; // full 2D stereo sound across speakers

        // Default volume 0.75
        _vol   = Mathf.Clamp(PlayerPrefs.GetFloat(PREF_VOL, 0.75f), 0.1f, 1.0f);
        _muted = PlayerPrefs.GetInt(PREF_MUTED, 0) == 1;
        _src.volume = _muted ? 0f : _vol;

        // 1. Try Resources
        AudioClip clip = Resources.Load<AudioClip>(CLIP_RES);

        // 2. Try loading WAV file directly from disk
        if (clip == null)
        {
            string diskWav = Path.Combine(Application.dataPath, "Resources", "Music", "CityTheme.wav");
            clip = LoadWavFromDisk(diskWav);
        }

        // 3. Fallback to procedural melodic simulation theme
        if (clip == null)
        {
            clip = BuildMelodicClip();
            Debug.Log("[MusicManager] Procedural city soundtrack active.");
        }
        else
        {
            Debug.Log("[MusicManager] CityTheme loaded successfully.");
        }

        _src.clip = clip;
        if (!_muted)
        {
            _src.Play();
        }
    }

    void OnDestroy()
    {
        if (_inst == this) _inst = null;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Public API
    // ─────────────────────────────────────────────────────────────────────────

    /// <summary>Start music if not already playing.</summary>
    public static void Play()
    {
        if (_inst == null) AutoBoot();
        if (_inst == null || _inst._src == null) return;
        if (!_inst._muted && !_inst._src.isPlaying && _inst._src.clip != null)
            _inst._src.Play();
    }

    /// <summary>Ensure music starts unmuted and actively playing.</summary>
    public static void EnsurePlaying()
    {
        if (_inst == null) AutoBoot();
        if (_inst == null) return;
        _inst._muted = false;
        PlayerPrefs.SetInt(PREF_MUTED, 0);
        if (_inst._src != null)
        {
            _inst._src.volume = _inst._vol;
            if (!_inst._src.isPlaying && _inst._src.clip != null)
                _inst._src.Play();
        }
    }

    /// <summary>Mute / unmute music.</summary>
    public static void Toggle()
    {
        if (_inst == null || _inst._src == null) return;
        _inst._muted = !_inst._muted;
        PlayerPrefs.SetInt(PREF_MUTED, _inst._muted ? 1 : 0);
        _inst._src.volume = _inst._muted ? 0f : _inst._vol;

        if (!_inst._muted)
        {
            if (!_inst._src.isPlaying && _inst._src.clip != null)
                _inst._src.Play();
        }
    }

    /// <summary>Set music volume 0–1 and save to PlayerPrefs.</summary>
    public static void SetVolume(float v)
    {
        if (_inst == null || _inst._src == null) return;
        v = Mathf.Clamp01(v);
        _inst._vol = v;
        PlayerPrefs.SetFloat(PREF_VOL, v);
        if (!_inst._muted) _inst._src.volume = v;
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Direct WAV Byte Parser (Zero dependencies, instant disk loading)
    // ─────────────────────────────────────────────────────────────────────────
    static AudioClip LoadWavFromDisk(string path)
    {
        try
        {
            if (!File.Exists(path)) return null;
            byte[] fileBytes = File.ReadAllBytes(path);
            if (fileBytes.Length < 44) return null;

            // Check RIFF and WAVE header
            if (fileBytes[0] != 'R' || fileBytes[1] != 'I' || fileBytes[2] != 'F' || fileBytes[3] != 'F')
                return null;
            if (fileBytes[8] != 'W' || fileBytes[9] != 'A' || fileBytes[10] != 'V' || fileBytes[11] != 'E')
                return null;

            int channels      = 1;
            int sampleRate    = 44100;
            int bitsPerSample = 16;
            int dataOffset    = -1;
            int dataSize      = 0;

            int pos = 12;
            while (pos + 8 <= fileBytes.Length)
            {
                string chunkId  = System.Text.Encoding.ASCII.GetString(fileBytes, pos, 4);
                int   chunkSize = System.BitConverter.ToInt32(fileBytes, pos + 4);
                pos += 8;

                if (chunkId == "fmt ")
                {
                    channels      = System.BitConverter.ToInt16(fileBytes, pos + 2);
                    sampleRate    = System.BitConverter.ToInt32(fileBytes, pos + 4);
                    bitsPerSample = System.BitConverter.ToInt16(fileBytes, pos + 14);
                }
                else if (chunkId == "data")
                {
                    dataOffset = pos;
                    dataSize   = chunkSize;
                    break;
                }
                pos += chunkSize;
            }

            if (dataOffset < 0 || bitsPerSample != 16 || channels < 1) return null;

            int bytesPerSample    = bitsPerSample / 8;
            int totalSamples      = dataSize / bytesPerSample;
            int samplesPerChannel = totalSamples / channels;

            float[] audioData = new float[totalSamples];
            for (int i = 0; i < totalSamples; i++)
            {
                short sample = System.BitConverter.ToInt16(fileBytes, dataOffset + i * 2);
                audioData[i] = sample / 32768.0f;
            }

            AudioClip clip = AudioClip.Create("CityThemeWav", samplesPerChannel, channels, sampleRate, false);
            clip.SetData(audioData, 0);
            return clip;
        }
        catch (System.Exception ex)
        {
            Debug.LogWarning("[MusicManager] Error reading WAV: " + ex.Message);
            return null;
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Procedural Melodic City Soundtrack (Upbeat chords + melodic bells + bass)
    // ─────────────────────────────────────────────────────────────────────────
    static AudioClip BuildMelodicClip()
    {
        const int   RATE = 44100;
        const float LEN  = 16f;
        int         samples = (int)(RATE * LEN);
        float[]     data    = new float[samples];

        // 4 bars of chord progression (Cmaj7 -> Am7 -> Fmaj7 -> G7)
        float[][] chordFreqs = new float[][]
        {
            new float[] { 261.63f, 329.63f, 392.00f, 493.88f }, // Cmaj7
            new float[] { 220.00f, 261.63f, 329.63f, 392.00f }, // Am7
            new float[] { 174.61f, 220.00f, 261.63f, 329.63f }, // Fmaj7
            new float[] { 196.00f, 246.94f, 293.66f, 349.23f }, // G7
        };

        float[] bassFreqs = { 130.81f, 110.00f, 87.31f, 98.00f };
        float[] bellScale = { 523.25f, 587.33f, 659.25f, 783.99f, 880.00f, 1046.50f };

        for (int s = 0; s < samples; s++)
        {
            float t = (float)s / RATE;
            int bar = Mathf.FloorToInt(t / 4f) % 4;
            float tBar = t % 4f;

            float val = 0f;

            // 1. Warm chord pad (electric piano / synth pad)
            float chordEnv = Mathf.Clamp01(tBar / 0.15f) * Mathf.Clamp01((4f - tBar) / 0.2f);
            foreach (float f in chordFreqs[bar])
            {
                val += 0.08f * chordEnv * Mathf.Sin(2f * Mathf.PI * f * t);
            }

            // 2. Walking bassline
            float bassEnv = Mathf.Exp(-(tBar % 1f) * 3f);
            float bFreq = bassFreqs[bar];
            val += 0.18f * bassEnv * (Mathf.Sin(2f * Mathf.PI * bFreq * t) + 0.35f * Mathf.Sin(4f * Mathf.PI * bFreq * t));

            // 3. Cheerful melodic bells / chimes on 8th notes
            float beat = t * 2f; // 120 BPM
            float beatFrac = beat - Mathf.Floor(beat);
            int step = Mathf.FloorToInt(beat) % bellScale.Length;
            float bellFreq = bellScale[step];
            float bellEnv = Mathf.Exp(-beatFrac * 9f);
            val += 0.12f * bellEnv * Mathf.Sin(2f * Mathf.PI * bellFreq * t);

            // Smooth 0.5s loop boundary crossfade
            float env = 1f;
            if (t < 0.5f) env = t / 0.5f;
            else if (t > LEN - 0.5f) env = (LEN - t) / 0.5f;

            data[s] = Mathf.Clamp(val * env, -0.95f, 0.95f);
        }

        var clip = AudioClip.Create("CityMelodicAmbient", samples, 1, RATE, false);
        clip.SetData(data, 0);
        return clip;
    }
}
