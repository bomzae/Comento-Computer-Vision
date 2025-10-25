from ultralytics import YOLO

# 학습된 모델 불러오기 (Colab에서 다운로드한 best.pt 경로)
model = YOLO(r"C:\Users\user\Comento-Computer-Vision\model\best.pt")

# 샘플 이미지에서 객체 탐지
results = model.predict(
    source=r"C:\Users\user\Comento-Computer-Vision\input\sample2.jpg",
    conf=0.25,   # confidence threshold
    save=False,
)

# 결과 저장
for r in results:
   r.save(filename=r"C:\Users\user\Comento-Computer-Vision\output/result.jpg")