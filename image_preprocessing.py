from datasets import load_dataset
import numpy as np
import cv2

dataset = load_dataset("ethz/food101")

images = []
for i in range(5):
    # PIL 이미지를 numpy 배열로 변경
    image = dataset["train"][i]["image"]
    img = np.array(image)
    images.append(img)

for i in range(5):
    # 이미지 사이즈 조정 (224×224)
    images[i] = cv2.resize(images[i], dsize=(224, 224))
    
    # Grayscale 적용
    images[i] = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)

    # Normalize 적용
    images[i] = cv2.normalize(images[i], None, 0, 255, cv2.NORM_MINMAX)

    # Blur 적용
    images[i] = cv2.blur(images[i], (5, 5))

    # 전처리 데이터 다운로드
    cv2.imwrite(rf"C:\Users\user\Comento-Computer-Vision\processed_samples\image_{i+1}.jpg", images[i])

    # 데이터 증강1 - 좌우 반전
    images.append(cv2.flip(images[i], 1))

    # 데이터 증강2 - 이미지 중심 계산 및 45도 회전
    (h, w) = images[i].shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    images.append(cv2.warpAffine(images[i], M, (w, h)))

    # 데이터 증강3 - 색상 변화(단일 채널을 3채널로 변경)
    images.append(cv2.cvtColor(images[i], cv2.COLOR_GRAY2BGR))

for i, img in enumerate(images):
    # 이미지 출력
    cv2.imshow(f"image{i+1}", img)

cv2.waitKey(0)
cv2.destroyAllWindows()