import argparse, os, csv, time
import cv2
from ultralytics import YOLO

def detect_person():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=str, required=True, help="입력 영상")
    parser.add_argument("--weights", type=str, default="model/yolov8n.pt", help="YOLO 모델")
    parser.add_argument("--output", type=str, default="output/detect_person", help="결과 영상")
    parser.add_argument("--conf", type=float, default=0.5, help="탐지 임계값")
    parser.add_argument("--imgsz", type=int, default=640, help="입력 이미지 크기")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    # 모델 로드
    model = YOLO(args.weights)
    names = model.names
    person_ids = [k for k, v in names.items() if v == "person"]
    person_id = person_ids[0] if person_ids else None

    # 입력 영상 열기
    cap = cv2.VideoCapture(args.video)
    if not cap.isOpened():
        raise RuntimeError("영상 파일을 열 수 없습니다.")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    base = os.path.splitext(os.path.basename(args.video))[0]

    # 주석 영상 출력 설정
    w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out_path = os.path.join(args.output, f"{base}_annotated.mp4")
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(out_path, fourcc, fps, (w, h))

    # CSV 로그 파일 생성 및 헤더 작성
    csv_path = os.path.join(args.output, f"{base}_person_times.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer_csv = csv.writer(f)
        writer_csv.writerow(["t_sec", "persons"])

    frame_idx = 0
    t0 = time.time()
    last_sec = 0

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model.predict(frame, imgsz=args.imgsz, conf=args.conf, classes=0, verbose=False)[0]
        persons = 0

        # 사람 수 세기
        if results.boxes is not None:
            for box in results.boxes:
                cls = int(box.cls[0])
                if (person_id is None) or (cls == person_id):
                    persons += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    confv = float(box.conf[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                    cv2.putText(frame, f"person {confv:.2f}", (x1, max(12, y1-6)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        # 사람 수(Persons) 라벨 표시
        cv2.putText(frame, f"Persons: {persons}", (10, 28),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        # 현재 영상 시간(초) 계산 후 정수 변환(1초 단위 기록용)
        t_sec = frame_idx / fps
        current = int(t_sec)

        # 사람이 존재하면, 1초마다 csv 파일에 기록
        if persons > 0 and current != last_sec:
            t_sec = round(frame_idx / fps, 3)
            with open(csv_path, "a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([round(t_sec, 1), persons])
            last_sec = current

        # 처리된 영상 출력
        writer.write(frame)
        cv2.imshow("Person Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame_idx += 1

    cap.release()
    writer.release()
    cv2.destroyAllWindows()

    print(f"[완료] CSV 로그: {csv_path}")
    print(f"[완료] 주석 영상: {out_path}")
    print(f"[정보] 총 프레임: {frame_idx}, 처리시간: {time.time()-t0:.1f}s")

if __name__ == "__main__":
    detect_person()
