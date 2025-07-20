import json
import numpy as np
import cv2

# Load JSON
with open('src_points.json', 'r') as f:
    data = json.load(f)

# Extract source points from the JSON
src_points = np.float32(data[0]['points'])

# Define destination points (a clean top-down rectangle)
W, H = 1200, 800  # You can change this based on your layout
dst_points = np.float32([
    [0, 0],
    [W, 0],
    [W, H],
    [0, H]
])

# Compute homography
H_matrix, _ = cv2.findHomography(src_points, dst_points)

# Load original image/frame
img = cv2.imread('copy.jpg')  # Replace with your image path

# Warp perspective to get bird-eye view
warped = cv2.warpPerspective(img, H_matrix, (W, H))

#Save homography matrix
np.save("homography_matrix.npy", H_matrix)

# Show the result
cv2.imshow("Bird Eye View", warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('top_down_view.jpg', warped)

