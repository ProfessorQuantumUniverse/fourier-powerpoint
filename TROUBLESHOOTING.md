# Troubleshooting Guide

Common issues and solutions for the Fourier presentation Manim scripts.

## Installation Issues

### "manim: command not found"

**Problem:** Manim is not installed or not in PATH

**Solution:**
```bash
pip install manim
# or
pip3 install manim
```

Verify installation:
```bash
manim --version
```

### "FileNotFoundError: [Errno 2] No such file or directory: 'latex'"

**Problem:** LaTeX is not installed (required for mathematical formulas)

**Solution:**
```bash
sudo apt-get update
sudo apt-get install -y texlive texlive-latex-extra texlive-fonts-extra texlive-science
```

### "pangocairo >= 1.30.0 is required"

**Problem:** Missing system dependencies

**Solution:**
```bash
sudo apt-get install -y libpango1.0-dev libcairo2-dev
```

### "FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'"

**Problem:** FFmpeg is not installed (required for video encoding)

**Solution:**
```bash
sudo apt-get install -y ffmpeg
```

## Rendering Issues

### Scene renders but looks wrong/incomplete

**Problem:** Using cached data from previous render

**Solution:**
```bash
# Add --disable_caching flag
manim -qh --disable_caching script.py SceneName

# Or delete cache
rm -rf media/
```

### "No scenes found"

**Problem:** Scene name is incorrect or doesn't exist

**Solution:**
List all scenes in a file:
```bash
manim script.py --scene_names
```

### Rendering is very slow

**Problem:** High quality settings take time

**Solution:**
- Use `-ql` for quick previews
- Reduce frame count in loops
- Use `--disable_caching` to avoid cache overhead
- Render overnight for high quality

### "Memory error" during rendering

**Problem:** Not enough RAM for complex scenes

**Solution:**
- Close other applications
- Use lower quality settings
- Simplify the scene (reduce objects)
- Render in smaller batches

## Display Issues

### Math formulas show error symbols

**Problem:** LaTeX syntax error in MathTex

**Solution:**
Check LaTeX syntax. Common issues:
- Missing `r` prefix: `MathTex(r"x^2")` not `MathTex("x^2")`
- Unescaped backslashes
- Invalid LaTeX commands

Example:
```python
# Wrong
formula = MathTex("\frac{1}{2}")

# Correct
formula = MathTex(r"\frac{1}{2}")
```

### Text appears too large/small

**Problem:** Font size not appropriate for resolution

**Solution:**
Adjust `font_size` parameter:
```python
text = Text("Hello", font_size=48)  # Adjust number
```

### Colors look wrong

**Problem:** Color gradient or color name issue

**Solution:**
Use predefined colors or hex values:
```python
# Predefined
text.set_color(BLUE)

# Hex
text.set_color("#3498db")

# Gradient
text.set_color_by_gradient(BLUE, RED)
```

## Portrait Issues

### Portrait doesn't show up

**Problem:** SVG file not found or incorrectly named

**Solution:**
1. Check filename: Must be exactly `fourier_portrait.svg`
2. Check location: Must be in `assets/` directory
3. Check file permissions: `chmod 644 assets/fourier_portrait.svg`

Full path should be:
```
/path/to/project/assets/fourier_portrait.svg
```

### Portrait looks distorted

**Problem:** SVG scaling issue or complex SVG

**Solution:**
Adjust scale in the code:
```python
portrait = SVGMobject("assets/fourier_portrait.svg")
portrait.scale(1.5)  # Adjust this value
```

Or convert to PNG:
```python
portrait = ImageMobject("assets/fourier_portrait.png")
portrait.scale(2)
```

### "Error loading SVG"

**Problem:** SVG file is corrupted or too complex

**Solution:**
1. Open SVG in Inkscape or similar editor
2. Simplify the paths (Path > Simplify)
3. Save as "Plain SVG" (not Inkscape SVG)
4. Or convert to PNG and use ImageMobject

## Script Automation Issues

### "./render_all.sh: Permission denied"

**Problem:** Script is not executable

**Solution:**
```bash
chmod +x render_all.sh combine_videos.sh
```

### "command not found: ./render_all.sh"

**Problem:** Not in correct directory or path issue

**Solution:**
```bash
# Make sure you're in the project directory
cd /path/to/fourier-powerpoint

# Run with bash explicitly
bash render_all.sh qh
```

### Scripts fail on Windows

**Problem:** Bash scripts require Unix-like environment

**Solution:**
Use Git Bash, WSL, or run commands manually:
```bash
# Instead of ./render_all.sh, run:
manim -qh 01_intro.py IntroScene
manim -qh 02_timeline.py TimelineScene
# ... etc
```

## Video Combination Issues

### "ffmpeg: command not found"

**Problem:** FFmpeg not installed

**Solution:**
```bash
sudo apt-get install ffmpeg
```

### "No such file or directory" when combining

**Problem:** Videos not rendered yet or wrong quality setting

**Solution:**
1. Render all videos first: `./render_all.sh qh`
2. Use correct quality directory: `./combine_videos.sh 1080p60`

Quality directory mapping:
- `-ql` → `480p15`
- `-qm` → `720p30`
- `-qh` → `1080p60`
- `-qk` → `2160p60`

### Combined video has sync issues

**Problem:** Different frame rates or codecs

**Solution:**
Re-encode all videos to same format first:
```bash
for f in *.mp4; do
    ffmpeg -i "$f" -c:v libx264 -preset slow -crf 22 "${f%.mp4}_normalized.mp4"
done
```

## Performance Issues

### Rendering takes hours

**Normal behavior:**
- High quality (`-qh`, `-qk`) rendering is computationally intensive
- Complex scenes with many objects take longer
- Expected times:
  - Low quality: 1-5 minutes per scene
  - High quality: 10-30 minutes per scene
  - 4K quality: 30-60 minutes per scene

**Tips:**
- Render overnight for full presentation
- Use `-ql` for testing and previews
- Render on a more powerful computer
- Use cloud computing for 4K renders

### Computer freezes during render

**Problem:** System running out of resources

**Solution:**
- Close other applications
- Reduce quality settings
- Add more RAM
- Render one scene at a time
- Enable swap space

## Code Modification Issues

### Changes don't appear in render

**Problem:** Cached files being used

**Solution:**
```bash
# Clear cache
rm -rf media/

# Or use --disable_caching
manim -qh --disable_caching script.py SceneName
```

### "IndentationError" after editing

**Problem:** Python indentation is incorrect

**Solution:**
- Python uses 4 spaces for indentation
- Don't mix tabs and spaces
- Check your editor settings
- Use consistent indentation

### "NameError: name 'X' is not defined"

**Problem:** Missing import or typo

**Solution:**
Check that imports are present:
```python
from manim import *
import numpy as np
```

## Getting Help

If you encounter an issue not listed here:

1. **Check Manim documentation:** https://docs.manim.community/
2. **Search Manim GitHub issues:** https://github.com/ManimCommunity/manim/issues
3. **Check the error message carefully** - it usually indicates the problem
4. **Test with a simple scene first** to isolate the issue
5. **Update Manim:** `pip install --upgrade manim`

## Common Error Messages

### "ModuleNotFoundError: No module named 'manim'"
→ Manim not installed: `pip install manim`

### "cairo.Error: invalid matrix (not invertible)"
→ Usually a scaling issue. Check for `scale(0)` or invalid transformations

### "ValueError: not enough values to unpack"
→ Check function parameters and return values

### "IndexError: list index out of range"
→ Array access issue, check loop bounds

### "AttributeError: 'X' object has no attribute 'Y'"
→ Typo in method name or wrong object type

## Debug Mode

To see more detailed error messages:
```bash
# Add -v flag for verbose output
manim -qh -v DEBUG script.py SceneName

# Or check log files
tail -f manim.log
```

## Reset Everything

If all else fails, complete reset:
```bash
# Remove all generated files
rm -rf media/ __pycache__/

# Reinstall dependencies
pip uninstall manim
pip install manim

# Test with simple example
manim -ql 01_intro.py WaveCompositionScene
```

---

Still having issues? Check:
- Python version: `python3 --version` (should be 3.8+)
- Manim version: `manim --version`
- System: `uname -a` or `ver` (Windows)

Include this information when seeking help!
