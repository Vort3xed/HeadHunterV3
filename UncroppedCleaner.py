import os

directory = 'faces'

for filename in os.listdir(directory):
    if filename.endswith("_detected.jpg"):
        os.remove(os.path.join(directory, filename))