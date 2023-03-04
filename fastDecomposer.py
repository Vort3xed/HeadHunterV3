import cv2
import os

video_file = 'newtest.mp4'
cap = cv2.VideoCapture(video_file)

frames_dir = 'frames'
if not os.path.exists(frames_dir):
    os.makedirs(frames_dir)

frame_index = 0

interval = 5

success, frame = cap.read()

while success:
    frame_index += 1
    
    if frame_index % interval == 0:
        frame_file = os.path.join(frames_dir, f'frame_{frame_index:04d}.jpg')
        cv2.imwrite(frame_file, frame)
    
    success, frame = cap.read()

cap.release()