Comento-Computer-Vision

|─ src/

|	└─ \_\_init\_\_.py				# 패키지 설정 파일

|	└─ color\_filter.py			# 적색 영역 추출

|	└─ image\_preprocessing.py		# 이미지 전처리

|	└─ generate\_depth\_map.py		# 깊이 맵 생성

|	└─ generate\_point\_cloud.py	# 3D 시각화

|	└─ detect\_person\_video.py		# 사람 탐지 및 기록

|─ test/
|	└─ unit\_test.py				# 기본 테스트

|	└─ test\_3d\_processing.py		# 깊이 맵 및 3D 생성 테스트

|	└─ test\_detect\_person.py		# 사람 탐지 모델 입력 영상 및 기록 테스트

|─ input

|	└─ sample.jpg				# 깊이 맵 생성 샘플 이미지

|	└─ sample2.jpg				# 객체 탐지 샘플 이미지

|	└─ detect\_person\_sample.mp4	# 사람 탐지 샘플 영상

|	└─ detect\_person\_sample2.mp4	#  사람 탐지 샘플 영상2

|─ output

|	└─ processed\_samples/		# 데이터 전처리 결과 이미지 폴더

|		└─ image\_1.jpg

|		└─ image\_2.jpg

|		└─ image\_3.jpg

|		└─ image\_4.jpg

|		└─ image\_5.jpg

|	└─ result.jpg				# 객체 탐지 결과 이미지

|	└─ detect\_person/			# 사람 탐지 및 기록, 주석 영상 폴더

|		└─ detect\_person\_sample\_annotated.mp4

|		└─ detect\_person\_sample\_person\_times.csv

|		└─ detect\_person\_sample2\_annotated.mp4

|		└─ detect\_person\_sample2\_person\_times.csv

|─ model

|	└─ best.pt				# 객체(차, 사람, 자전거) 탐지 모델

|	└─ yolov8n.pt				# 사전 학습된 사람 탐지 모델



1차 업무

 - 빨간색 영역 감지 및 필터링

 - 크기 조정, 색상 변환, 노이즈 제거, 데이터 증강 등 이미지 전처리



2차 업무

 - 깊이 맵 생성 및 3D 시각화

 - 위 코드 단위 테스트



3차 업무

 - roboflow에서 차, 사람, 자전거 데이터셋 생성 후 YOLOv8 모델 학습

 - 학습한 모델 파일을 추가하여 차, 사람, 자전거 객체 탐지



4차 업무

 - 경량 보안 모니터링 프로젝트

 - 사전 학습된 YOLOv8n 모델을 활용하여 사람 탐지 및 주석 영상 출력, 로그 기록

