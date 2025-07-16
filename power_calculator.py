def calculate_power(base, exponent):
    """
    반복문을 사용하여 제곱을 계산하는 함수
    ** 연산자나 pow() 함수를 사용하지 않고 직접 구현
    
    매개변수:
    base (float): 제곱할 기본 숫자 (밑)
    exponent (int): 제곱할 횟수 (지수)
    
    반환값:
    float: 계산된 제곱 결과
    
    예시: calculate_power(3.0, 4) = 3.0 * 3.0 * 3.0 * 3.0 = 81.0
    """
    
    # 결과를 저장할 변수, 1로 초기화
    # 1로 초기화하는 이유: 어떤 수에 1을 곱해도 원래 수가 나오기 때문
    # 예: 1 * 3 * 3 * 3 * 3 = 81
    result = 1
    
    # 지수가 0인 경우 처리 (어떤 수의 0제곱은 1)
    if exponent == 0:
        return 1
    
    # 지수가 음수인 경우 처리
    if exponent < 0:
        # 음수 지수는 1을 양수 지수로 나눈 것과 같음
        # 예: 2^(-3) = 1 / (2^3) = 1 / 8 = 0.125
        positive_exponent = -exponent  # 음수를 양수로 변환
        for i in range(positive_exponent):
            result = result * base
        return 1 / result  # 1을 결과로 나눔
    
    # 양수 지수인 경우: 지수만큼 반복하여 곱셈 수행
    # range(exponent): 0부터 exponent-1까지 반복
    # 예: exponent=4이면 0, 1, 2, 3 총 4번 반복
    for i in range(exponent):
        # 현재 result에 base를 곱해서 다시 result에 저장
        # 첫 번째 반복: result = 1 * base
        # 두 번째 반복: result = base * base
        # 세 번째 반복: result = base * base * base
        # 이런 식으로 계속 반복...
        result = result * base
    
    # 최종 계산 결과 반환
    return result

def main():
    """
    프로그램의 메인 함수
    사용자로부터 입력을 받고 제곱 계산을 수행
    """
    
    # try-except: 오류가 발생할 수 있는 코드를 안전하게 실행
    try:
        # 사용자로부터 첫 번째 숫자 입력받기
        # input()은 항상 문자열(string)로 입력받음
        number_input = input("Enter number: ")
        
        # 문자열을 실수(float)로 변환
        # float()는 "3.14", "5", "2.0" 등을 숫자로 변환
        # 만약 "abc" 같은 문자가 들어오면 ValueError 발생
        number = float(number_input)
        
        # 사용자로부터 지수 입력받기
        exponent_input = input("Enter exponent: ")
        
        # 문자열을 정수(int)로 변환
        # int()는 "3", "5", "-2" 등을 정수로 변환
        # 만약 "3.14" 같은 소수나 "abc" 같은 문자가 들어오면 ValueError 발생
        exponent = int(exponent_input)
        
        # 위에서 만든 함수를 호출하여 제곱 계산 수행
        result = calculate_power(number, exponent)
        
        # 결과 출력 처리
        # 계산 결과가 정수인지 확인 (소수점 이하가 0인지 확인)
        if result == int(result):
            # 정수로 출력 (예: 81.0 → 81)
            print(f"Result: {int(result)}")
        else:
            # 실수로 출력 (예: 3.14159...)
            print(f"Result: {result}")
            
    # 예외 처리: ValueError는 형변환 실패 시 발생
    except ValueError as e:
        # 오류 메시지를 분석하여 어떤 입력에서 오류가 발생했는지 판단
        
        # 오류 메시지를 문자열로 변환하여 "float" 단어가 포함되어 있는지 확인
        if "float" in str(e) or "could not convert string to float" in str(e):
            # 숫자 입력에서 오류가 발생한 경우
            print("Invalid number input.")
        else:
            # 그 외의 경우는 지수 입력에서 오류가 발생한 것
            print("Invalid exponent input.")

# 파이썬 프로그램의 시작점
# 이 파일이 직접 실행될 때만 main() 함수 호출
# 다른 파일에서 import 할 때는 실행되지 않음
if __name__ == "__main__":
    main()
