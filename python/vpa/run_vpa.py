"""Simple script to run vpa"""
from video_processor import VideoProcessor

VPA = VideoProcessor()
VPA.begin_capture(0)
VPA.output_video()
