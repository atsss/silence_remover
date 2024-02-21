#!/bin/bash
# Combine video and audio using ffmpeg
ffmpeg -i video.h264 -i audio.wav -c:v copy -c:a aac output.mp4

# Clean up temporary files
# rm video.h264 audio.wav
