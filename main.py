import os

import cv2

# reading image
img_name = str(input("Image Names (Without Extension): "))
img_name = f'{img_name}.jpg'
image = cv2.imread(img_name)

# converting BGR image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# image inversion
inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
print(pencil_sketch)
print(type(pencil_sketch))
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch of Image", pencil_sketch)
cv2.imwrite(f'sketched_{img_name}', pencil_sketch)
print('Sketch Image Saved')


# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)


running = True
while running == True:
    try:
        cv2.waitKey(0)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        for i in range(4):
            os.system('exit')
        running = False
