import time

def mac(pattern_data, filter_data):
    score = 0.0
    for i in range(len(pattern_data)):
        for j in range(len(pattern_data[i])):
            score += pattern_data[i][j] * filter_data[i][j]
    return score

def compare_scores(score_a, score_b):
    EPSILON = 1e-9
    if abs(score_a - score_b) < EPSILON:
        return "UNDECIDED"
    elif score_a > score_b:
        return "A"
    else:
        return "B"

def input_matrix():
    matrix = []
    for i in range(3):
        while True:
            try:
                row = list(map(int, input(f"라인{i+1} 입력: ").strip().split()))
                if len(row) != 3:
                    print("잘못된 입력입니다. 3개의 정수를 입력해주세요.")
                    continue
            except ValueError:
                print("잘못된 입력입니다. 3개의 정수를 입력해주세요.")
                continue
            matrix.append(row)
            break
    return matrix

def mode_selection():
    while True:
        print("모드를 선택하세요:")
        print("1. 사용자 입력(3x3 행렬)")
        print("2. data.json 분석")
        mode = input("선택: ").strip()
        if mode in ['1', '2']:
            return int(mode)
        else:
            print("잘못된 입력입니다. 1 또는 2를 입력해주세요.")

def measure_mac(pattern_data, filter_data):
    repeat = 10
    start = time.perf_counter()
    for _ in range(repeat):
        mac(pattern_data, filter_data)
    end = time.perf_counter()
    return (end - start)*1000/repeat

def header(title, comment="", length=42):
    print("-"*length)
    print(title)
    print("-"*length)
    if comment:
        print(comment)
        print("-"*length)

def main():
    while True:
        mode = mode_selection()
        if mode == 1:
            header("[1] 필터 입력", "스페이스로 구분하여 3x3 행렬을 입력하세요.")
            print("필터A")
            filter_data_a = input_matrix()
            print("")
            print("필터B")
            filter_data_b = input_matrix()
            header("[2] 패턴 입력", "스페이스로 구분하여 3x3 행렬을 입력하세요.")
            print("패턴")
            pattern_data = input_matrix()
            header("[3] MAC 결과")
            score_a = mac(pattern_data, filter_data_a)
            score_b = mac(pattern_data, filter_data_b)
            avg_time = measure_mac(pattern_data, filter_data_a)
            result = compare_scores(score_a, score_b)
            print("A 점수:", score_a)
            print("B 점수:", score_b)
            print("연산 시간(평균/10회):", avg_time, "ms")
            print("판정:", result)

        elif mode == 2:
            print("아직 지원하지 않음.")

if __name__ == "__main__":
    main()