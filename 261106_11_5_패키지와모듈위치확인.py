# 라이브러리
# 재사용을 위해 개발한 코드 묶음
# 모듈 묶음이 패키지라면 패키지 묶음이 라이브러리
# 지만... 파이썬에서 라이브러리는 패키지와 혼용하는 용어

# 패키지나 모듈은 호출하려는 파일과 동일한 경로에 있거나 파이썬 라이브러리들이 모여 있는 폴더에 있어야 사용 가능
# getfile() : 모듈의 경로 확인 가능, inspect라는 모듈에 속해 있음

import inspect
import random

print(inspect.getfile(random)) # random 모듈 위치(경로)

from travel import *
print(inspect.getfile(thailand)) # thailand 모듈 위치
# 처음엔 d:\py_practice\travel\thailand.py 이었으나
# 이후 C:\ProgramData\anaconda3\Lib\travel\thailand.py 로 변경