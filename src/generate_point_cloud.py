# Depth Map을 기반으로 3D 포인트 클라우드 생성 및 시각화
import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_point_and_visualization():
	# 이미지 로드
	image = cv2.imread('input/sample.jpg')
	if image is None:
	    raise FileNotFoundError("이미지 파일을 찾을 수 없습니다.")

	# 그레이스케일 변환
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Depth Map 생성
	depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

	# 3D 포인트 클라우드 변환
	h, w = depth_map.shape[:2]
	X, Y = np.meshgrid(np.arange(w), np.arange(h))
	Z = gray.astype(np.float32) # Depth 값을 Z 축으로 사용

	# 3D 좌표 생성
	points_3d = np.dstack((X, Y, Z))

	# 3D 포인트 시각화
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(X.flatten(), Y.flatten(), Z.flatten(), c=gray.flatten(), cmap='jet', s=0.5)

	# 라벨 붙여서 출력
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Depth (Z)')
	plt.show()

	# Depth Map 결과 출력
	cv2.imshow('Depth Map', depth_map)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return depth_map