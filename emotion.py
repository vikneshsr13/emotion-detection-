from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

# Read image (ensure the file path is correct)
img = cv2.imread('image1.png')

# Convert BGR to RGB
img_rgb = img[:, :, ::-1]

# Display the image using matplotlib
plt.imshow(img_rgb)
plt.axis('off')  # Hide axis
plt.show()

# Analyze emotions using DeepFace
result = DeepFace.analyze(img_rgb, actions=['emotion'])

# If multiple faces are detected, DeepFace returns a list
if isinstance(result, list):
    # Take the first face's result
    result = result[0]

# Extract the dominant emotion and its percentage
dominant_emotion = result['dominant_emotion']
emotion_percentage = result['emotion'][dominant_emotion]

# Print the dominant emotion with its percentage
print(f"Dominant Emotion: {dominant_emotion}, Percentage: {emotion_percentage:.2f}%")
