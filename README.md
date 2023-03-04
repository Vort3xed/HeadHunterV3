# HeadHunterV2
An AI model that finds faces in frames of a video

# Instructions:
Make sure you modify the code to set the video's file name

# Specifications:
slowDecomposer.py will take a long time because it takes every frame of the video and converts it to a jpg.

fastDecomposer.py will take a short amount of time because it takes every 5 frames of the video.

FaceRecognition.py will append use the AI to find the faces and draw a red square around them. It will also crop the photos. 

UncroppedCleaner.py will remove the junk photos in the "faces" folder that the application uses. These photos are photos that have the red square drawn, but aren't cropped to them.
