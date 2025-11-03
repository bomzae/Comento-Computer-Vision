import os, sys, csv
import pytest
import src.detect_person_video as dpv

# 영상을 불러오지 못한 경우
def test_video_not_found(monkeypatch, tmp_path):
    # 존재하지 않는 영상 경로 전달
    monkeypatch.setattr(sys, "argv", [
        "detect_person.py",
        "--video", str(tmp_path / "no_video.mp4"),
        "--output", str(tmp_path),
        "--weights", "model/yolov8n.pt",
    ])

    with pytest.raises(RuntimeError):
        dpv.detect_person()

# 기록용 CSV 파일 생성 및 헤더 작성 여부 확인
def test_csv_file_created(monkeypatch, tmp_path):
    monkeypatch.setattr(sys, "argv", [
        "detect_person.py",
        "--video", "input/detect_person_sample.mp4",
        "--output", str(tmp_path),
        "--weights", "model/yolov8n.pt",
        "--conf", "0.5",
        "--imgsz", "640",
    ])

    dpv.detect_person()

    csv_files = [f for f in os.listdir(tmp_path) if f.endswith("_person_times.csv")]
    assert csv_files, "CSV 파일이 생성되지 않았습니다."

    csv_path = os.path.join(str(tmp_path), csv_files[0])
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["t_sec", "persons"], "CSV 헤더가 잘못되었습니다."