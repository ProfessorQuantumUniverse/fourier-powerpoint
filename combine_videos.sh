#!/bin/bash
# combine_videos.sh - Combine all rendered scenes into a single presentation video
# Usage: ./combine_videos.sh [quality_dir]
# Quality directory options: 480p15, 720p30, 1080p60, 2160p60
# Default: 1080p60

QUALITY_DIR=${1:-1080p60}
OUTPUT_FILE="fourier_presentation_${QUALITY_DIR}.mp4"

echo "================================================"
echo "Combining Fourier Presentation Videos"
echo "Quality: $QUALITY_DIR"
echo "================================================"
echo ""

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "Error: ffmpeg is not installed"
    echo "Please install it: sudo apt-get install ffmpeg"
    exit 1
fi

# Create temporary file list
VIDEO_LIST=$(mktemp)

# List of videos in order
cat > "$VIDEO_LIST" << EOF
file 'media/videos/01_intro/${QUALITY_DIR}/IntroScene.mp4'
file 'media/videos/02_timeline/${QUALITY_DIR}/TimelineScene.mp4'
file 'media/videos/03_science/${QUALITY_DIR}/FourierSeriesScene.mp4'
file 'media/videos/03_science/${QUALITY_DIR}/HeatEquationScene.mp4'
file 'media/videos/03_science/${QUALITY_DIR}/FourierTransformScene.mp4'
file 'media/videos/04_applications/${QUALITY_DIR}/ApplicationsIntroScene.mp4'
file 'media/videos/04_applications/${QUALITY_DIR}/JPEGCompressionScene.mp4'
file 'media/videos/04_applications/${QUALITY_DIR}/AudioProcessingScene.mp4'
file 'media/videos/04_applications/${QUALITY_DIR}/MRIScene.mp4'
file 'media/videos/04_applications/${QUALITY_DIR}/SignalProcessingScene.mp4'
file 'media/videos/05_outro/${QUALITY_DIR}/OutroScene.mp4'
EOF

# Check if all files exist
echo "Checking for video files..."
missing=0
while IFS= read -r line; do
    if [[ $line == file* ]]; then
        file=$(echo "$line" | sed "s/file '\(.*\)'/\1/")
        if [ ! -f "$file" ]; then
            echo "✗ Missing: $file"
            missing=$((missing + 1))
        else
            echo "✓ Found: $(basename "$file")"
        fi
    fi
done < "$VIDEO_LIST"

if [ $missing -gt 0 ]; then
    echo ""
    echo "Error: $missing video file(s) missing"
    echo "Please run ./render_all.sh first"
    rm "$VIDEO_LIST"
    exit 1
fi

echo ""
echo "Combining videos..."
ffmpeg -f concat -safe 0 -i "$VIDEO_LIST" -c copy "$OUTPUT_FILE" -y

if [ $? -eq 0 ]; then
    echo ""
    echo "================================================"
    echo "Success! Combined video created:"
    echo "  $OUTPUT_FILE"
    echo "================================================"
    echo ""
    ls -lh "$OUTPUT_FILE"
else
    echo ""
    echo "Error: Failed to combine videos"
    rm "$VIDEO_LIST"
    exit 1
fi

# Cleanup
rm "$VIDEO_LIST"

echo ""
echo "You can now add narration and background music"
echo "using your preferred video editing software."
echo ""
