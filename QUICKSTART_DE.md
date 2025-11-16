# Fourier Präsentation - Schnellanleitung (Deutsch)

## Übersicht

Dieses Projekt enthält 5 Haupt-Skripte für eine epische Präsentation über Joseph Fourier:

1. **01_intro.py** - Epische Eingangsanimation
2. **02_timeline.py** - Zeitstrahl zur Französischen Revolution
3. **03_science.py** - Wissenschaftliche Theorien und Ideen
4. **04_applications.py** - Moderne Anwendungen (JPEG, MP3, MRI, etc.)
5. **05_outro.py** - Epische Schlussanimation

## Schnellstart

### Installation

```bash
# System-Abhängigkeiten installieren
sudo apt-get update
sudo apt-get install -y libpango1.0-dev libcairo2-dev ffmpeg
sudo apt-get install -y texlive texlive-latex-extra texlive-fonts-extra

# Python-Pakete installieren
pip install -r requirements.txt
```

### Erste Schritte

**1. Portrait hinzufügen:**
- Legen Sie Ihr Fourier-Portrait als `assets/fourier_portrait.svg` ab
- Das SVG-Format wird empfohlen
- Falls nicht vorhanden, wird ein Platzhalter verwendet

**2. Preview rendern (niedrige Qualität, schnell):**
```bash
manim -ql 01_intro.py IntroScene
```

**3. Finale Version rendern (hohe Qualität):**
```bash
manim -qh 01_intro.py IntroScene
```

## Alle Szenen

### Intro Animationen (01_intro.py)

**IntroScene** - Haupteingang
```bash
manim -qh 01_intro.py IntroScene
```
- Name mit Farbverlauf
- Animierte Wellen
- Fourier-Reihen-Formel
- Portrait (falls vorhanden)

**WaveCompositionScene** - Wellen-Kombination
```bash
manim -qh 01_intro.py WaveCompositionScene
```
- Zeigt wie Sinuswellen sich kombinieren

### Zeitstrahl (02_timeline.py)

**TimelineScene** - Hauptzeitstrahl (EMPFOHLEN)
```bash
manim -qh 02_timeline.py TimelineScene
```
- 9 wichtige Lebensereignisse
- Animierter Indikator
- Platz oben für Bilder
- Ereignisse:
  - 1768: Geburt in Auxerre
  - 1789: Französische Revolution beginnt
  - 1794: Verhaftung während der Terrorherrschaft
  - 1795: Freilassung, beginnt zu lehren
  - 1798: Napoleons Ägypten-Expedition
  - 1801: Rückkehr nach Frankreich
  - 1807: Wärmetheorie-Abhandlung
  - 1822: Veröffentlichung Hauptwerk
  - 1830: Tod in Paris

**DetailedTimelineScene** - Perioden-basiert
```bash
manim -qh 02_timeline.py DetailedTimelineScene
```

**TimelineWithPortraitsScene** - Minimalistisch
```bash
manim -qh 02_timeline.py TimelineWithPortraitsScene
```

### Wissenschaft (03_science.py)

**FourierSeriesScene** - Fourier-Reihen
```bash
manim -qh 03_science.py FourierSeriesScene
```
- Rechteckwelle-Approximation
- Progressive Annäherung
- Bis zu 25 Terme

**HeatEquationScene** - Wärmegleichung
```bash
manim -qh 03_science.py HeatEquationScene
```
- Wärmegleichung-Formel
- Wärmediffusion-Simulation
- Farbkodierte Temperatur

**FourierTransformScene** - Fourier-Transformation
```bash
manim -qh 03_science.py FourierTransformScene
```
- Zeit- zu Frequenzbereich
- Frequenzspektrum-Visualisierung

**WaveDecompositionScene** - Wellen-Zerlegung
```bash
manim -qh 03_science.py WaveDecompositionScene
```
- Komplexe Welle in Komponenten zerlegen

### Moderne Anwendungen (04_applications.py)

**ApplicationsIntroScene** - Einführung
```bash
manim -qh 04_applications.py ApplicationsIntroScene
```
- Übergang: 1830 Tod → moderne Anwendungen
- Liste der Anwendungen

**JPEGCompressionScene** - JPEG-Kompression
```bash
manim -qh 04_applications.py JPEGCompressionScene
```
- DCT-Demonstration
- 8×8 Block-Visualisierung
- Kompressionsverhältnis 10:1 bis 20:1

**AudioProcessingScene** - Audio/MP3
```bash
manim -qh 04_applications.py AudioProcessingScene
```
- Audio-Signal
- FFT-Transformation
- MP3-Kompression (90% Größenreduktion)

**MRIScene** - MRI-Bildgebung
```bash
manim -qh 04_applications.py MRIScene
```
- K-Space-Daten
- Inverse Fourier-Transformation
- Gehirn-Scan-Simulation

**SignalProcessingScene** - Drahtlose Kommunikation
```bash
manim -qh 04_applications.py SignalProcessingScene
```
- WiFi, 5G, Bluetooth
- Frequenzspektrum
- OFDM-Erklärung

### Outro (05_outro.py)

**OutroScene** - Haupt-Abschluss (EMPFOHLEN)
```bash
manim -qh 05_outro.py OutroScene
```
- Wellen sammeln sich
- Portrait
- Name und Daten
- Zitat: "Nature is an inexhaustible source of truths"
- Episches Fade-out

**LegacyMontageScene** - Vermächtnis-Übersicht
```bash
manim -qh 05_outro.py LegacyMontageScene
```
- Einfluss-Bereiche

**WaveConvergenceScene** - Wellen-Konvergenz
```bash
manim -qh 05_outro.py WaveConvergenceScene
```
- Wellen von allen Seiten
- Mandala-Muster

**FullOutroSequence** - Vollständige Sequenz
```bash
manim -qh 05_outro.py FullOutroSequence
```
- Kombiniert alle Outro-Elemente

## Empfohlene Szenen für komplette Präsentation

```bash
# 1. Intro
manim -qh 01_intro.py IntroScene

# 2. Zeitstrahl
manim -qh 02_timeline.py TimelineScene

# 3. Wissenschaft - Fourier-Reihen
manim -qh 03_science.py FourierSeriesScene

# 4. Wissenschaft - Wärmegleichung
manim -qh 03_science.py HeatEquationScene

# 5. Wissenschaft - Fourier-Transformation
manim -qh 03_science.py FourierTransformScene

# 6. Anwendungen - Intro
manim -qh 04_applications.py ApplicationsIntroScene

# 7. Anwendungen - JPEG
manim -qh 04_applications.py JPEGCompressionScene

# 8. Anwendungen - Audio
manim -qh 04_applications.py AudioProcessingScene

# 9. Anwendungen - MRI
manim -qh 04_applications.py MRIScene

# 10. Anwendungen - Kommunikation
manim -qh 04_applications.py SignalProcessingScene

# 11. Outro
manim -qh 05_outro.py OutroScene
```

## Qualitätsstufen

- `-ql` = Low Quality (480p, 15fps) - Schnelle Vorschau
- `-qm` = Medium Quality (720p, 30fps)
- `-qh` = High Quality (1080p, 60fps) - **Empfohlen für Präsentation**
- `-qk` = 4K Quality (2160p, 60fps) - Maximale Qualität

## Videos kombinieren

Nach dem Rendern können Sie die Videos kombinieren:

```bash
# Dateiliste erstellen
cat > videos.txt << EOF
file 'media/videos/01_intro/1080p60/IntroScene.mp4'
file 'media/videos/02_timeline/1080p60/TimelineScene.mp4'
file 'media/videos/03_science/1080p60/FourierSeriesScene.mp4'
file 'media/videos/03_science/1080p60/HeatEquationScene.mp4'
file 'media/videos/03_science/1080p60/FourierTransformScene.mp4'
file 'media/videos/04_applications/1080p60/ApplicationsIntroScene.mp4'
file 'media/videos/04_applications/1080p60/JPEGCompressionScene.mp4'
file 'media/videos/04_applications/1080p60/AudioProcessingScene.mp4'
file 'media/videos/04_applications/1080p60/MRIScene.mp4'
file 'media/videos/04_applications/1080p60/SignalProcessingScene.mp4'
file 'media/videos/05_outro/1080p60/OutroScene.mp4'
EOF

# Kombinieren
ffmpeg -f concat -safe 0 -i videos.txt -c copy fourier_presentation.mp4
```

## Anpassungen

### Farben ändern

In den Python-Dateien:
```python
.set_color_by_gradient(BLUE, PURPLE, RED)  # Ihre Farben
```

### Timing anpassen

```python
self.play(Animation, run_time=2)  # Dauer ändern
self.wait(1)  # Pause ändern
```

### Text ändern

```python
title = Text("Ihr Text hier", font_size=72)
```

### Formeln ändern

```python
formula = MathTex(r"Ihre \LaTeX Formel hier")
```

## Tipps

1. **Zuerst in niedriger Qualität testen** (`-ql`)
2. **Portrait hinzufügen** - viel besser mit echtem SVG
3. **Farben anpassen** - an Ihre Präsentation anpassen
4. **Musik und Narration hinzufügen** - in Videobearbeitungssoftware
5. **Einzelne Szenen exportieren** - einfacher zu bearbeiten

## Ausgabepfade

Videos werden gespeichert unter:
- `media/videos/[script]/[quality]/[scene].mp4`

Beispiel:
- `media/videos/01_intro/1080p60/IntroScene.mp4`

## Weitere Hilfe

Siehe `SCENES_GUIDE.md` für detaillierte Informationen zu jeder Szene.

Viel Erfolg mit Ihrer epischen Fourier-Präsentation! 🌊📐✨
