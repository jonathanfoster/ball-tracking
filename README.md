# Ball Tracking

This project uses OpenCV to track ball movement. The process for tracking is as follows:

  * Convert color to HSV
  * Create a pixel mask to identify the ball using upper and lower color bounds
  * Erode and dilate the mask to reduce noise
  * Indentify contours and draw a circle around the ball

## Prerequisites

  * [Python 2.7](https://www.python.org/)
  * [OpenCV](http://opencv.org/)

## Getting Started
    
Run the ball tracking script against the example video:

    $ python ball_tracking.py --video ball_tracking_example.mp4
