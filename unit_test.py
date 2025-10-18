# pytest를 활용한 기본 Unit Test

import numpy as np
import pytest
import cv2

# 깊이 맵 생성 샘플 함수
def generate_depth_map(image):
	if image is None:
		raise ValueError("입력된 이미지가 없습니다.")
	grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# 가짜 깊이 맵 적용
	depth_map = cv2.applyColorMap(grayscale, cv2.COLORMAP_JET)
	depth_map = depth_map.tolist()
	return depth_map

# 테스트 코드
def test_generate_depth_map():
	image = np.zeros((100, 100, 3), dtype=np.uint8) # 검정색 빈 이미지
	depth_map = generate_depth_map(image)
	assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다."
	assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."