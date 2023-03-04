import moviepy.editor as mp

# Path to input video file
video_path = "newtest.mp4"

# Create a VideoFileClip object from the input video
clip = mp.VideoFileClip(video_path)

# Extract audio from the video and save it as a WAV file
audio_path = "test.wav"
clip.audio.write_audiofile(audio_path)

# Extract frames from the video and save them as PNG files
frame_dir = "frames/new"
clip.write_images_sequence(frame_dir + "frame%04d.png")