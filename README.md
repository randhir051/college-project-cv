# Ontology and Computer Vision

Setup
- Install OpenCV and Numpy
- Go to `Projects\Core`
- Run `python detect_walking.py walk.mp4`
  - Gives the output of person walking in each frame
- Pipe the previous output to `python predict.py`
  - This predicts the movement based on the current X-Y and past X-Y
- The final command will be `python detect_walking.py walk.mp4 | python predict.py`
