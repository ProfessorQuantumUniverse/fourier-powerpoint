# Joseph Fourier Presentation - Manim Scripts

This repository contains Manim animation scripts for a comprehensive presentation about Joseph Fourier.

## Structure

The presentation is divided into 5 main sections:

1. **01_intro.py** - Epic opening animation with Fourier's name, portrait, formulas and waves
2. **02_timeline.py** - Timeline of Fourier's life during the French Revolution
3. **03_science.py** - Animations of Fourier's main scientific theories and ideas
4. **04_applications.py** - Visual demonstrations of modern applications (JPEG compression, etc.)
5. **05_outro.py** - Epic closing animation with waves, formulas, and a memorable quote

## Requirements

- Python 3.8+
- Manim Community Edition

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Render individual scenes:

```bash
# Render intro animation
manim -pql 01_intro.py IntroScene

# Render timeline
manim -pql 02_timeline.py TimelineScene

# Render science animations
manim -pql 03_science.py FourierSeriesScene
manim -pql 03_science.py HeatEquationScene

# Render applications
manim -pql 04_applications.py JPEGCompressionScene
manim -pql 04_applications.py SignalProcessingScene

# Render outro
manim -pql 05_outro.py OutroScene
```

For high quality output, replace `-pql` with `-pqh`.

## Assets

Place the Fourier portrait SVG in the `assets/` directory as `fourier_portrait.svg`.

## Notes

- All animations are designed to be epic and visually striking
- The timeline animation provides space at the top for additional images
- Modern applications are shown chronologically after Fourier's death
- The outro features a powerful quote and comprehensive visual summary
