import numpy as np
import pytest
import cv2
from src.generate_point_cloud import generate_3d_point_and_visualization
from src.generate_depth_map import generate_depth_map

# 테스트 코드
def test_generate_3d_point_and_visualization():
	image = cv2.imread('input/sample.jpg')
	depth_map = generate_3d_point_and_visualization()
	assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다."
	assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."

def test_generate_depth_map():
	image = cv2.imread('input/sample.jpg')
	depth_map = generate_depth_map()
	assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다."
	assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."