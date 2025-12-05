import os

# (1) txt 파일 경로 입력
file_path = input("검사할 txt 파일 경로(ctrl+shift+c)를 입력하세요: ").strip('"')

if not os.path.exists(file_path):
    print("❌ 파일을 찾을 수 없습니다.")
    exit()

# (3) 금지단어 리스트 선언
political_words = ["극우"] 
swear_words = ["시발", "병신", "fuck"] # 원하는 단어 추가

log_entries = []  # 로그 저장 리스트

# (2) 줄 단위 읽기
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# (4) 포함 여부 판단
for line_num, line in enumerate(lines, start=1):
    for word in political_words:
        if word.lower() in line.lower():  # 대소문자 무시 검색
            log_text = f"[{line_num}번째 줄] 정치적 발언 '{word}' 발견 → {line.strip()}"
            print(log_text)             # (5) 발견 로그 출력
            log_entries.append(log_text)
    for word in swear_words:
        if word.lower() in line.lower():  # 대소문자 무시 검색
            log_text = f"[{line_num}번째 줄] 비속어 '{word}' 발견 → {line.strip()}"
            print(log_text)             # (5) 발견 로그 출력
            log_entries.append(log_text)

# (6) log.txt 파일로 저장
with open("log.txt", "w", encoding="utf-8") as log_file:
    for entry in log_entries:
        log_file.write(entry + "\n")

print("\n✔ 검사 완료! log.txt 파일이 생성되었습니다.")
