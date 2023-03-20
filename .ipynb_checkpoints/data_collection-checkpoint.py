{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e78bcae5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import os\n",
    "\n",
    "def capture_faces(user_id, num_images):\n",
    "    # Create a directory to save the face images for the given user_id\n",
    "    save_dir = f'faces/{user_id}'\n",
    "    os.makedirs(save_dir, exist_ok=True)\n",
    "\n",
    "    # Load the pre-trained face detection model\n",
    "    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n",
    "\n",
    "    # Open the camera\n",
    "    cap = cv2.VideoCapture(0)\n",
    "\n",
    "    # Capture and save the face images\n",
    "    count = 0\n",
    "    while count < num_images:\n",
    "        ret, frame = cap.read()\n",
    "        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))\n",
    "\n",
    "        for (x, y, w, h) in faces:\n",
    "            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)\n",
    "            face_img = gray[y:y+h, x:x+w]\n",
    "            cv2.imwrite(f'{save_dir}/face_{count}.jpg', face_img)\n",
    "            count += 1\n",
    "\n",
    "        cv2.imshow('Face Capture', frame)\n",
    "        key = cv2.waitKey(1) & 0xFF\n",
    "\n",
    "        # Break the loop if the 'q' key is pressed\n",
    "        if key == ord('q'):\n",
    "            break\n",
    "\n",
    "    # Release the camera and close the window\n",
    "    cap.release()\n",
    "    cv2.destroyAllWindows()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb3c3c22",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
