"""Simple script to run vpa"""
from video_processor import VideoProcessor

vpa = VideoProcessor()
vpa.begin_capture(0)
vpa.output_video()
