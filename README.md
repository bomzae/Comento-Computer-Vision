# computer vision project
Huggin Face 데이터셋에서 이미지 5장을 받아와 전처리 수행(image_preprocessing.py)
1. 224X224로 이미지 resize
2. GrayScale 적용해 1채널로 변경, Normalize 적용
3. Blur 필터로 이미지 흐리게 만들어 노이즈 제거
4. 좌우 반전, 회전, 채널 수 변화로 데이터 증강
5. 3번까지 처리된 이미지 5장 preprocessed_samples 폴더에 저장