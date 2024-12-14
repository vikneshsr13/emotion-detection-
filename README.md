Features:

Emotion Analysis: Detects emotions such as happy, sad, angry, surprised, and neutral with high accuracy.

Dominant Emotion Output: Displays the most prominent emotion along with its confidence percentage.

Image Visualization: Uses Matplotlib to render the analyzed image in RGB format.

Multi-face Handling: Automatically processes multiple faces in an image and provides individual results for each.

Requirements 📃:

To run this project, ensure you have the following Python libraries installed:

opencv-python

matplotlib

deepface

Install the dependencies using:

pip install opencv-python matplotlib deepface

Usage 🚀:

Clone the repository:

git clone https://github.com/yourusername/emotion-detection.git
cd emotion-detection

Place your input image (e.g., image1.png) in the project folder.

Run the script:

python emotion.py

View the detected emotion in the terminal and the image in a popup window.

How It Works 🔧

Image Preprocessing:

The input image is read using OpenCV and converted from BGR to RGB format for accurate color rendering.

Emotion Analysis:

The DeepFace.analyze() function processes the image and detects emotions.

The output includes a dictionary of emotion percentages and the dominant emotion.

Display:

The program visualizes the image using Matplotlib and outputs the dominant emotion with its percentage.

Example Output 📷

Given an input image, the program might output:

Dominant Emotion: Happy

Confidence: 85.32%

The analyzed image is displayed in a popup window for better visualization.

Future Enhancements 🌟:

Real-time emotion detection using a webcam.

Integration with a web interface for user-friendly interaction.

Enhanced multi-face emotion reporting with bounding boxes drawn around detected faces.
