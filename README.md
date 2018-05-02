## Advanced Lane Lines Detection

---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Camera Calibration

The code for this step is contained in the first three code cells of the IPython notebook located in "./Advanced_Lane_Lines.ipynb".

I start by preparing "object points", which will be the (x, y, z) coordinates of the chessboard corners in the world. Here I am assuming the chessboard is fixed on the (x, y) plane at z=0, such that the object points are the same for each calibration image.  Thus, `objp` is just a replicated array of coordinates, and `obj_points` will be appended with a copy of it every time I successfully detect all chessboard corners in a test image.  `img_points` will be appended with the (x, y) pixel position of each of the corners in the image plane with each successful chessboard detection.  

I then used the output `obj_points` and `img_points` to compute the camera calibration and distortion coefficients using the `cv2.calibrateCamera()` function.  I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

Original Image| Undistorted Image
--|--

<img width="90%" height="40%" src="https://github.com/DongzhenHuangfu/CarND-Advanced-Lane-Lines/raw/master/output_images/calibration/compare_calibration1.jpg"/>

### Pipeline (single images)

#### 1. Undistort the image

To demonstrate this step, I will describe how I apply the distortion correction to one of the test images like this one:
<img width="80%" height="60%" src="https://github.com/DongzhenHuangfu/CarND-Advanced-Lane-Lines/raw/master/output_images/calibration/straight_lines1.jpg"/>

#### 2. Create a thresholded binary image

I used a combination of color and gradient thresholds to generate a binary image (thresholding steps at the third part of the code in "./Advanced_Lane_Lines.ipynb".).  Here's an example of my output for this step.

<img width="80%" height="60%" src="https://github.com/DongzhenHuangfu/CarND-Advanced-Lane-Lines/raw/master/output_images/binary/combined_straight_lines1.jpg"/>

#### 3. Transform the pictures into bird-eye views

The code for my perspective transform includes a function called `wrap()`, which appears in the 2rd Part of the IPython notebook).  The `wrap()` function takes as inputs an image (`img`). I chose the hardcode the source and destination points in the picture of the straight line so that the straight lines will look roughly straight and easy for checking.

This resulted in the following source and destination points:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 190, 720      | 240, 720      | 
| 586, 455      | 240, 0        |
| 696, 455      | 1040, 0       |
| 1130, 720     | 1040, 720     |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

<img width="90%" height="40%" src="https://github.com/DongzhenHuangfu/CarND-Advanced-Lane-Lines/raw/master/output_images/undistort_and_tranform/compare_straight_lines1.jpg"/>

#### 4. Find the lane lines and polyfit it by sliding the windows and further precious finding around detected lines.

Then I did some other stuff and fit my lane lines with a 2nd order polynomial kinda like this:

- with sliding windows:

<img width="90%" height="40%" src="https://github.com/DongzhenHuangfu/CarND-Advanced-Lane-Lines/raw/master/output_images/histogram/straight_lines1.jpg"/>

- with precious finding around detected lines:

<img width="90%" height="40%" src="https://github.com/DongzhenHuangfu/CarND-Advanced-Lane-Lines/raw/master/output_images/histogram/sprecious_straight_lines1.jpg"/>

THe relevant code is at the 5th part of the IPython notebook.

#### 5. Calculate the curvature of the lane line.

I did this in the 6th part of the IPython notebook.

#### 6. Example of the result

I implemented this step in the 7th part of the IPython notebook. Here is an example of my result on a test image:

<img width="80%" height="60%" src="https://github.com/DongzhenHuangfu/CarND-Advanced-Lane-Lines/raw/master/output_images/processed/straight_lines1.jpg"/>


---

### Pipeline (video)

#### 1. Finally I generate the output on the video using the method above.

Here's a [link to my video result](./output_videos/project_video.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  
