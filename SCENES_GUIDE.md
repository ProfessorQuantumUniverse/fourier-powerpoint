# Fourier Presentation - Detailed Scene Guide

This guide provides detailed information about each animation scene and how to use them.

## Table of Contents
1. [Introduction Animations](#introduction-animations)
2. [Timeline Animations](#timeline-animations)
3. [Science Animations](#science-animations)
4. [Applications Animations](#applications-animations)
5. [Outro Animations](#outro-animations)
6. [Rendering Guide](#rendering-guide)
7. [Customization Tips](#customization-tips)

---

## Introduction Animations

### File: `01_intro.py`

#### IntroScene
**Purpose:** Epic opening with Fourier's name, waves, and formulas

**Features:**
- Dramatic title animation with color gradient
- Animated Fourier waves in background
- Fourier series formula display
- Portrait integration (place `fourier_portrait.svg` in `assets/` folder)
- Epic fade-out transition

**Render command:**
```bash
manim -pqh 01_intro.py IntroScene
```

**Duration:** ~25 seconds

#### WaveCompositionScene
**Purpose:** Demonstrate how sine waves combine to form complex patterns

**Features:**
- Individual sine wave components
- Visual combination of waves
- Mathematical formulas for each component
- Step-by-step build-up

**Render command:**
```bash
manim -pqh 01_intro.py WaveCompositionScene
```

**Duration:** ~20 seconds

---

## Timeline Animations

### File: `02_timeline.py`

#### TimelineScene
**Purpose:** Main timeline showing Fourier's life during the French Revolution

**Features:**
- Elegant horizontal timeline
- 9 key life events with dates
- Animated indicator moving from point to point
- Color-coded events
- Space above timeline for adding images in post-production

**Render command:**
```bash
manim -pqh 02_timeline.py TimelineScene
```

**Duration:** ~35 seconds

**Key Events Shown:**
1. 1768 - Born in Auxerre, France
2. 1789 - French Revolution Begins
3. 1794 - Arrested During Terror
4. 1795 - Released, Begins Teaching
5. 1798 - Joins Napoleon's Egypt Expedition
6. 1801 - Returns to France, Prefect of Isère
7. 1807 - Submits Heat Theory Paper
8. 1822 - Publishes Analytical Theory of Heat
9. 1830 - Dies in Paris

#### DetailedTimelineScene
**Purpose:** Alternative timeline showing broader historical periods

**Features:**
- Period-based visualization (Youth, Revolution, Napoleon, Restoration)
- Color-coded era boxes
- Date ranges for each period

**Render command:**
```bash
manim -pqh 02_timeline.py DetailedTimelineScene
```

**Duration:** ~25 seconds

#### TimelineWithPortraitsScene
**Purpose:** Simplified timeline with maximum space for overlays

**Features:**
- Clean, minimal design
- Major milestones only
- Explicit note about space for images
- Perfect for video editing with additional content

**Render command:**
```bash
manim -pqh 02_timeline.py TimelineWithPortraitsScene
```

**Duration:** ~15 seconds

---

## Science Animations

### File: `03_science.py`

#### FourierSeriesScene
**Purpose:** Demonstrate Fourier series approximating a square wave

**Features:**
- Target square wave visualization
- Individual sine components
- Progressive approximation (1, 2, 3, 5, 7, 9, 11, 15, 19, 25 terms)
- Visual comparison showing convergence
- Mathematical formulas

**Render command:**
```bash
manim -pqh 03_science.py FourierSeriesScene
```

**Duration:** ~45 seconds

**Key Concept:** Any periodic function can be represented as a sum of sines and cosines

#### HeatEquationScene
**Purpose:** Visualize the heat equation and heat diffusion

**Features:**
- Heat equation formula with component explanations
- Animated heat diffusion simulation
- Color-coded temperature representation (blue=cold, red=hot)
- 60-frame simulation showing temperature evolution

**Render command:**
```bash
manim -pqh 03_science.py HeatEquationScene
```

**Duration:** ~40 seconds

**Formula Shown:** ∂u/∂t = α ∂²u/∂x²

#### FourierTransformScene
**Purpose:** Introduce the Fourier transform concept

**Features:**
- Fourier transform formula
- Time domain signal visualization
- Frequency domain representation
- Animated transformation with arrow
- Frequency peak identification

**Render command:**
```bash
manim -pqh 03_science.py FourierTransformScene
```

**Duration:** ~35 seconds

**Key Concept:** Transforms signals from time domain to frequency domain

#### WaveDecompositionScene
**Purpose:** Show complex wave decomposition into simple components

**Features:**
- Complex wave formation
- "Explosion" into component waves
- Recombination animation
- Color-coded components

**Render command:**
```bash
manim -pqh 03_science.py WaveDecompositionScene
```

**Duration:** ~25 seconds

---

## Applications Animations

### File: `04_applications.py`

#### ApplicationsIntroScene
**Purpose:** Transition from Fourier's death to modern applications

**Features:**
- Death date notation (1830)
- "Legacy lives on" transition text
- List of modern applications with icons
- Smooth transition to applications

**Render command:**
```bash
manim -pqh 04_applications.py ApplicationsIntroScene
```

**Duration:** ~20 seconds

#### JPEGCompressionScene
**Purpose:** Demonstrate JPEG compression using DCT

**Features:**
- 8×8 image block visualization
- Discrete Cosine Transform (DCT) representation
- Frequency coefficient display
- Compression ratio information
- Visual explanation of energy concentration

**Render command:**
```bash
manim -pqh 04_applications.py JPEGCompressionScene
```

**Duration:** ~30 seconds

**Key Stats:** 10:1 to 20:1 typical compression ratio

#### AudioProcessingScene
**Purpose:** Show audio processing and MP3 compression

**Features:**
- Audio waveform in time domain
- FFT transformation
- Frequency spectrum visualization
- MP3 compression strategy explanation
- 90% size reduction highlight

**Render command:**
```bash
manim -pqh 04_applications.py AudioProcessingScene
```

**Duration:** ~35 seconds

#### MRIScene
**Purpose:** Demonstrate MRI imaging using Fourier transforms

**Features:**
- K-space data visualization
- Inverse Fourier transform
- Simulated MRI brain image
- Life-saving technology emphasis

**Render command:**
```bash
manim -pqh 04_applications.py MRIScene
```

**Duration:** ~35 seconds

#### SignalProcessingScene
**Purpose:** Show wireless communications applications

**Features:**
- Frequency spectrum with multiple channels
- WiFi, Bluetooth, 5G visualization
- OFDM (Orthogonal Frequency Division Multiplexing) explanation
- Orthogonal carrier demonstration

**Render command:**
```bash
manim -pqh 04_applications.py SignalProcessingScene
```

**Duration:** ~40 seconds

---

## Outro Animations

### File: `05_outro.py`

#### OutroScene
**Purpose:** Main epic closing scene

**Features:**
- Waves gathering and converging
- Portrait appearance
- Name and dates
- Famous Fourier quote: "Nature is an inexhaustible source of truths"
- Key formulas display
- Epic final fade

**Render command:**
```bash
manim -pqh 05_outro.py OutroScene
```

**Duration:** ~40 seconds

#### LegacyMontageScene
**Purpose:** Show breadth of Fourier's impact

**Features:**
- Impact areas radiating from center
- Mathematics, Physics, Engineering, Medicine, Technology, Communications
- Connected network visualization

**Render command:**
```bash
manim -pqh 05_outro.py LegacyMontageScene
```

**Duration:** ~25 seconds

#### WaveConvergenceScene
**Purpose:** Beautiful wave convergence animation

**Features:**
- Waves from all directions
- Convergence to center
- Rotating mandala pattern
- "Forever Transforming Our World" message

**Render command:**
```bash
manim -pqh 05_outro.py WaveConvergenceScene
```

**Duration:** ~30 seconds

#### FullOutroSequence
**Purpose:** Complete outro combining all elements

**Features:**
- Wave gathering
- Portrait and name
- Quote
- Legacy items
- Epic final fade

**Render command:**
```bash
manim -pqh 05_outro.py FullOutroSequence
```

**Duration:** ~60 seconds

---

## Rendering Guide

### Quality Presets

**Low Quality (Preview):**
```bash
manim -ql script.py SceneName
```
- Resolution: 480p
- Frame rate: 15 fps
- Fast rendering for previews

**Medium Quality:**
```bash
manim -qm script.py SceneName
```
- Resolution: 720p
- Frame rate: 30 fps

**High Quality (Presentation):**
```bash
manim -qh script.py SceneName
```
- Resolution: 1080p
- Frame rate: 60 fps
- Recommended for final videos

**Production Quality (4K):**
```bash
manim -qk script.py SceneName
```
- Resolution: 2160p (4K)
- Frame rate: 60 fps
- Maximum quality

### Additional Options

**Render without opening video:**
```bash
manim -ql --disable_caching script.py SceneName
```

**Render transparent background:**
```bash
manim -ql --transparent script.py SceneName
```

**Render last frame only (for thumbnails):**
```bash
manim -ql -s script.py SceneName
```

### Batch Rendering

To render all scenes in a file:
```bash
manim -ql script.py
```

---

## Customization Tips

### Colors

Change color schemes by modifying these gradient lines:
```python
.set_color_by_gradient(BLUE, PURPLE, RED)
```

Available colors: `BLUE`, `RED`, `GREEN`, `YELLOW`, `ORANGE`, `PURPLE`, `PINK`, `TEAL`, `GOLD`, `GRAY`, `WHITE`, etc.

### Timing

Adjust animation speed:
```python
self.play(Animation, run_time=2)  # Change 2 to desired seconds
self.wait(1)  # Change 1 to desired pause duration
```

### Text and Formulas

**Modify text:**
```python
title = Text("Your Text Here", font_size=72, color=BLUE)
```

**Modify LaTeX formulas:**
```python
formula = MathTex(r"your \LaTeX here", font_size=48)
```

### Adding the Portrait

1. Place your Fourier portrait SVG file in the `assets/` folder
2. Name it `fourier_portrait.svg`
3. The scripts will automatically use it instead of the placeholder

If you have a PNG/JPG instead:
```python
portrait = ImageMobject("assets/fourier_portrait.jpg")
portrait.scale(2)
```

### Background Color

Change the background color in any scene:
```python
self.camera.background_color = "#0a0a0a"  # Dark background
# Or
self.camera.background_color = "#ffffff"  # White background
```

### Combining Videos

After rendering, combine videos using ffmpeg:
```bash
# Create a file list
cat > videos.txt << EOF
file 'media/videos/01_intro/1080p60/IntroScene.mp4'
file 'media/videos/02_timeline/1080p60/TimelineScene.mp4'
file 'media/videos/03_science/1080p60/FourierSeriesScene.mp4'
# ... add more scenes
EOF

# Concatenate
ffmpeg -f concat -safe 0 -i videos.txt -c copy final_presentation.mp4
```

---

## Tips for Best Results

1. **Render in high quality only after testing** - Use `-ql` for previews, `-qh` for finals
2. **Check timing** - Adjust `run_time` and `wait()` calls to match your narration
3. **Add the portrait** - The animations look much better with the actual SVG portrait
4. **Customize colors** - Match your institution's or presentation's color scheme
5. **Export individual scenes** - Easier to edit and combine in video editing software
6. **Add music and narration** - Use video editing software to add audio tracks
7. **Test on different screens** - Ensure text is readable at various sizes

---

## Troubleshooting

**LaTeX errors:**
- Ensure `texlive` is installed
- Check formula syntax in `MathTex()` calls

**Import errors:**
- Run `pip install -r requirements.txt`
- Verify manim installation: `manim --version`

**Slow rendering:**
- Use lower quality for testing
- Reduce frame counts in loops
- Disable caching: `--disable_caching`

**Portrait not showing:**
- Check file name: `assets/fourier_portrait.svg`
- Verify SVG format
- Check file permissions

---

## Contact and Contributions

Feel free to customize these animations for your presentation. All scenes are designed to be modular and can be mixed, matched, or modified as needed.

Enjoy creating your epic Fourier presentation! 🌊📐✨
