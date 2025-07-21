This project demonstrates how to:
- Perform homography on an image
- Generate a top-down (bird's-eye) view
- Mark slots on the top view
- Project those marked slots back onto the original camera view using inverse homography

-----------`homography.py`
- Loads 4 corner points (`src_points.json`) from the original image
- Defines a destination plane (real-world scaled size)
- Applies homography using `cv2.findHomography()` and `cv2.warpPerspective()`
- Saves `homography_matrix.npy` and `top_down_view.jpg`

[Ultralytics Parking Solution] is used to draw the slots and save it as .json file

----------`inverse_homography.py`
- Loads `slots.json` and the inverse of the homography matrix
- Transforms each rectangular slot into a polygon in the original view
- Draws those polygons on `frame.jpg` and saves as `original_with_slots.jpg`
