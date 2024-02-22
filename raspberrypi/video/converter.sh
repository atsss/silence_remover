#!/bin/bash
# Convert h264 to mp4
ffmpeg -i video.h264 -c copy video.mp4

# Clean up temporary files
rm video.h264
