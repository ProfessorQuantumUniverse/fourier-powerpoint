#!/bin/bash
# render_all.sh - Render all recommended scenes for the full presentation
# Usage: ./render_all.sh [quality]
# Quality options: ql (low), qm (medium), qh (high), qk (4k)
# Default: qh (high quality)

QUALITY=${1:-qh}

echo "================================================"
echo "Fourier Presentation - Rendering All Scenes"
echo "Quality: $QUALITY"
echo "================================================"
echo ""

# Check if manim is installed
if ! command -v manim &> /dev/null; then
    echo "Error: manim is not installed"
    echo "Please run: pip install -r requirements.txt"
    exit 1
fi

# Array of scenes to render
declare -a scenes=(
    "01_intro.py:IntroScene"
    "02_timeline.py:TimelineScene"
    "03_science.py:FourierSeriesScene"
    "03_science.py:HeatEquationScene"
    "03_science.py:FourierTransformScene"
    "04_applications.py:ApplicationsIntroScene"
    "04_applications.py:JPEGCompressionScene"
    "04_applications.py:AudioProcessingScene"
    "04_applications.py:MRIScene"
    "04_applications.py:SignalProcessingScene"
    "05_outro.py:OutroScene"
)

total=${#scenes[@]}
current=0

# Render each scene
for scene in "${scenes[@]}"; do
    current=$((current + 1))
    IFS=':' read -r script scene_name <<< "$scene"
    
    echo ""
    echo "[$current/$total] Rendering $scene_name from $script..."
    echo "------------------------------------------------"
    
    manim -$QUALITY --disable_caching "$script" "$scene_name"
    
    if [ $? -ne 0 ]; then
        echo "Error rendering $scene_name"
        exit 1
    fi
    
    echo "✓ Completed $scene_name"
done

echo ""
echo "================================================"
echo "All scenes rendered successfully!"
echo "================================================"
echo ""
echo "Videos are located in the media/videos/ directory"
echo ""
echo "To combine all videos into one file, run:"
echo "  ./combine_videos.sh"
echo ""
