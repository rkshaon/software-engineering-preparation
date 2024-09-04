import cv2


def cartoonify_image(image_path, save_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 600))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.adaptiveThreshold(
        gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    cv2.imwrite(save_path, cartoon)

    print(f"Cartoon image saved at: {save_path}")


save_path = "/home/shaon/Desktop/personal/cartoon_image.jpg"
image_path = "/home/shaon/Desktop/personal/rkshaon1.jpg"

cartoonify_image(image_path, save_path)
