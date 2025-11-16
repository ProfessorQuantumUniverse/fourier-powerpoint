# Joseph Fourier Presentation - Manim Scripts

This repository contains comprehensive Manim animation scripts for an epic presentation about Joseph Fourier, covering his life, scientific contributions, and lasting impact on modern technology.

## 🌊 Overview

The presentation is divided into 5 main sections with multiple scenes:

1. **01_intro.py** - Epic opening animation with Fourier's name, portrait, formulas and waves
2. **02_timeline.py** - Timeline of Fourier's life during the French Revolution
3. **03_science.py** - Animations of Fourier's main scientific theories and ideas
4. **04_applications.py** - Visual demonstrations of modern applications (JPEG, MP3, MRI, WiFi, etc.)
5. **05_outro.py** - Epic closing animation with waves, formulas, and a memorable quote

## 📚 Documentation

- **[QUICKSTART_DE.md](QUICKSTART_DE.md)** - Schnellanleitung auf Deutsch
- **[SCENES_GUIDE.md](SCENES_GUIDE.md)** - Detailed guide for all scenes (English)

## 🚀 Quick Start

### Installation

**System dependencies:**
```bash
sudo apt-get update
sudo apt-get install -y libpango1.0-dev libcairo2-dev ffmpeg
sudo apt-get install -y texlive texlive-latex-extra texlive-fonts-extra
```

**Python packages:**
```bash
pip install -r requirements.txt
```

### Rendering

**Test a single scene (low quality, fast):**
```bash
manim -ql 01_intro.py IntroScene
```

**Render high quality for presentation:**
```bash
manim -qh 01_intro.py IntroScene
```

**Render all scenes automatically:**
```bash
./render_all.sh qh
```

**Combine all videos into one:**
```bash
./combine_videos.sh 1080p60
```

## 🎬 Recommended Scenes for Full Presentation

1. **01_intro.py** → IntroScene
2. **02_timeline.py** → TimelineScene
3. **03_science.py** → FourierSeriesScene
4. **03_science.py** → HeatEquationScene
5. **03_science.py** → FourierTransformScene
6. **04_applications.py** → ApplicationsIntroScene
7. **04_applications.py** → JPEGCompressionScene
8. **04_applications.py** → AudioProcessingScene
9. **04_applications.py** → MRIScene
10. **04_applications.py** → SignalProcessingScene
11. **05_outro.py** → OutroScene

Total duration: ~6 minutes of pure animation

## 🎨 Assets

Place your Fourier portrait in the `assets/` directory:
- Filename: `fourier_portrait.svg`
- Format: SVG (recommended) or PNG/JPG
- The scripts will automatically use it if available, otherwise show a placeholder

## ⚙️ Quality Presets

- `-ql` = Low (480p, 15fps) - Fast preview
- `-qm` = Medium (720p, 30fps)
- `-qh` = High (1080p, 60fps) - **Recommended**
- `-qk` = 4K (2160p, 60fps) - Maximum quality

## 📁 Scene Overview

### Introduction (01_intro.py)
- **IntroScene**: Epic opening with name, waves, and formulas
- **WaveCompositionScene**: Demonstrates wave combination

### Timeline (02_timeline.py)
- **TimelineScene**: Main timeline with 9 key events (1768-1830)
- **DetailedTimelineScene**: Period-based view
- **TimelineWithPortraitsScene**: Minimal design for overlay work

### Science (03_science.py)
- **FourierSeriesScene**: Square wave approximation
- **HeatEquationScene**: Heat equation visualization with diffusion
- **FourierTransformScene**: Time to frequency domain transformation
- **WaveDecompositionScene**: Complex wave decomposition

### Applications (04_applications.py)
- **ApplicationsIntroScene**: Transition to modern era
- **JPEGCompressionScene**: DCT and image compression
- **AudioProcessingScene**: FFT and MP3 compression
- **MRIScene**: Medical imaging with Fourier transforms
- **SignalProcessingScene**: WiFi, 5G, and OFDM

### Outro (05_outro.py)
- **OutroScene**: Main epic ending with quote
- **LegacyMontageScene**: Impact areas visualization
- **WaveConvergenceScene**: Beautiful wave convergence
- **FullOutroSequence**: Complete outro sequence

## 🛠️ Customization

All scripts are fully customizable:
- Change colors by modifying gradient calls
- Adjust timing with `run_time` and `wait()` parameters
- Modify text and formulas
- Add your own content

See [SCENES_GUIDE.md](SCENES_GUIDE.md) for detailed customization instructions.

## 📊 Output

Videos are saved to:
```
media/videos/[script]/[quality]/[scene].mp4
```

Example:
```
media/videos/01_intro/1080p60/IntroScene.mp4
```

## 🎵 Next Steps

After rendering:
1. Combine videos with `./combine_videos.sh`
2. Add narration in your video editing software
3. Add background music
4. Adjust timing if needed
5. Export final presentation

## ✨ Features

- **Epic animations** - Designed to be visually striking
- **Scientifically accurate** - Proper formulas and concepts
- **Modern applications** - Shows real-world impact
- **Modular design** - Mix and match scenes
- **High quality** - Up to 4K 60fps output
- **German + English** - Documentation in both languages

## 🎓 Educational Content

The presentation covers:
- Fourier's biography during the French Revolution
- Fourier Series and Transform theory
- Heat equation and diffusion
- Modern applications:
  - JPEG/DCT compression
  - MP3/audio processing
  - MRI medical imaging
  - Wireless communications (WiFi, 5G)
  - Signal processing

## 🤝 Contributing

Feel free to:
- Modify scenes for your needs
- Add new animations
- Improve existing code
- Share your versions

## 📝 License

See LICENSE file for details.

## 💡 Tips

1. Start with low quality renders to test
2. Add the actual Fourier portrait SVG for best results
3. Customize colors to match your presentation theme
4. Use the automated scripts for batch rendering
5. Add transitions and music in post-production

---

**Viel Erfolg mit Ihrer epischen Fourier-Präsentation!** 🌊📐✨

**Good luck with your epic Fourier presentation!** 🌊📐✨
