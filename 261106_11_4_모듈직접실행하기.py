# 모듈을 직접 실행할지 아니면 별도 파일을 호출해서 실행할지는 다음과 같이 구분
# if __name__ == "__main__": # 직접 실행하는 경우
#     pass
# else: # 외부에서 호출해 실행하는 경우
#     pass

# __name__: 현재 모듈(작성한 파이썬 파일)의 이름을 값으로 가지는 내장 변수
# 모듈이 직접 실행되는 경우 __name__의 값: __main__

# thailand.py 파일에 아래 내용 추가
# class ThailandPackage:
#     def detail(self):
#         print("[태국 3박 5일 패키지] 방콕, 파타야 여행(야시장 투어) 50만 원")

# if __name__ == "__maim__": # 모듈 직접 실행
#     print("thailand 모듈 직접 실행")
#     print("이 문장은 모듈을 직접 실행할 때만 출력돼요.")
#     trip_to = ThailandPackage()
#     trip_to = detail()
# else: # 외부에서 모듈 호출
#     print("외부에서 thailand 모듈 호출")


# 추가 후 이 파일에서 실행
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()