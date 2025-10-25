Comento-Computer-Vision

|─ src/

|	└─ \_\_init\_\_.py					# 패키지 설정 파일

|	└─ color\_filter.py				# 적색 영역 추출

|	└─ image\_preprocessing.py	# 이미지 전처리

|	└─ generate\_depth\_map.py	# 깊이 맵 생성

|	└─ generate\_point\_cloud.py	# 3D 시각화

|─ test/
|	└─ unit\_test.py				# 기본 테스트

|	└─ test\_3d\_processing.py		# 깊이 맵 및 3D 생성 테스트

|─ input

|	└─ sample.jpg				# 깊이 맵 생성 샘플 이미지

|	└─ sample2.jpg				# 객체 탐지 샘플 이미지

|─ output

|	└─ processed\_samples/		# 데이터 전처리 결과 이미지 폴더

|		└─ image\_1.jpg

|		└─ image\_2.jpg

|		└─ image\_3.jpg

|		└─ image\_4.jpg

|		└─ image\_5.jpg

|	└─ result.jpg				# 객체 탐지 결과 이미지

|─ model

|	└─ best.pt					# 객체(차, 사람, 자전거) 탐지 모델



