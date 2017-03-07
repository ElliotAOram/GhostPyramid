"""Simple script to run vpa"""
from video_processor import VideoProcessor

VPA = VideoProcessor([0,255,0], threshold=75)
VPA.begin_capture(0)
VPA.process_and_output_video()
