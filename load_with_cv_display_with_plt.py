import cv2
import matplotlib.pyplot as plt


# Display B&W Image
img = cv2.imread('/home/atif/training_by_several_learning_process/GTSRB/test_for_VHDL_with_minimum_layer/test_image/80_speed.ppm',0)

plt.imshow(img, cmap='gray')
plt.show()


# Display RGB image
import matplotlib.image as mpimg
image = mpimg.imread('/home/atif/training_by_several_learning_process/GTSRB/test_for_VHDL_with_minimum_layer/test_image/80_speed.ppm')
plt.imshow(image)
plt.show()
