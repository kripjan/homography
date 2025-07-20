import cv2
import numpy as np
import json

# Load homography matrix (from earlier step)
H = np.load("homography_matrix.npy")
H_inv = np.linalg.inv(H)

# Load top-down view image
top_down = cv2.imread("top_down_view.jpg")

# Load original image (camera view)
original = cv2.imread("copy.jpg")

# Load slot rectangles from JSON
with open("slots_points.json", "r") as f:
    slot_data = json.load(f)

for slot in slot_data:
    points = np.array(slot["points"], dtype=np.int32)
    cv2.polylines(top_down, [points], isClosed=True, color=(0, 255, 0), thickness=2)

cv2.imshow("Top-down with Slots", top_down)
cv2.imwrite("top_down_with_slots.jpg", top_down)

def transform_point(pt, H):
    pt_h = np.array([pt[0], pt[1], 1]).reshape(3, 1)
    warped_pt = H @ pt_h
    warped_pt /= warped_pt[2][0]
    return (int(warped_pt[0][0]), int(warped_pt[1][0]))

# Draw back-projected slots on the original image
for slot in slot_data:
    bird_pts = slot["points"]
    original_pts = [transform_point(pt, H_inv) for pt in bird_pts]
    cv2.polylines(original, [np.array(original_pts)], isClosed=True, color=(0, 0, 255), thickness=2)

cv2.imshow("Original with Projected Slots", original)
cv2.imwrite("original_with_slots.jpg", original)
cv2.waitKey(0)
cv2.destroyAllWindows()
