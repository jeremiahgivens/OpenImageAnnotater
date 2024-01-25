# OpenImageAnnotater 
This is an open source repository for an image annotating tool. Currently we support working with yolov8 and yolov5 models. If you would like to add new supported formats or new features, please submit a pull request.

## Features
* Label images and export to yolov8 and yolov5 object detection training format.
* Combine training sets.
* Import video as individual frames.
* Use existing yolov8 or yolov5 model to assist in training. The idea behind this feature is based on the itterative nature of training an object detection model. The usual worflow is normally something along the lines of: get labeled data, train model, evaluate, get more labeled data that represents what the model is struggling with, train, repeat. However, once your model has been trained initially, it may do well on most images, but still struggle with some. This means that when we are in the process of labeling more data to train our model, we can run each image through the existing model and have it predict where we would like to put our labels. Sometimes these will be wrong and we will have to annotate manually, but many times the model will get it perfect and all you must do is confirm. This significantly reduces the time it takes annotate images! 

