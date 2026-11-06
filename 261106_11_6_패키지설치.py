# 웹스크래핑 분야에서 유명한 beautifulsoup 패키지 다운
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# 이외 pip 명령어
# pip install [패키지명] : 패키지 설치



# pip install --upgrade [패키지명] : 패키지 업그레이드
# Requirement already satisfied: beautifulsoup4 in d:\py_practice\.venv\lib\site-packages (4.15.0)
# Requirement already satisfied: soupsieve>=1.6.1 in d:\py_practice\.venv\lib\site-packages (from beautifulsoup4) (4.0.1)
# Requirement already satisfied: typing-extensions>=4.0.0 in d:\py_practice\.venv\lib\site-packages (from beautifulsoup4) (4.16.0)

# [notice] A new release of pip is available: 25.2 -> 26.3
# [notice] To update, run: python.exe -m pip install --upgrade pip



# pip uninstall [패키지명] : 패키지 삭제
# Found existing installation: beautifulsoup4 4.15.0
# Uninstalling beautifulsoup4-4.15.0:
#   Would remove:
#     d:\py_practice\.venv\lib\site-packages\beautifulsoup4-4.15.0.dist-info\*
#     d:\py_practice\.venv\lib\site-packages\bs4\*
# Proceed (Y/n)? y
#   Successfully uninstalled beautifulsoup4-4.15.0



# pip list : 설치 패키지 목록
# Package                 Version
# ----------------------- -----------
# asttokens               3.0.2
# beautifulsoup4          4.15.0
# colorama                0.4.6
# comm                    0.2.3
# debugpy                 1.8.22
# executing               2.3.0
# ipykernel               7.4.0
# ipython                 9.17.1
# ipython_pygments_lexers 1.1.1
# jedi                    0.20.0
# jupyter_client          8.10.0
# jupyter_core            5.9.1
# matplotlib-inline       0.2.2
# nest-asyncio2           1.7.4
# packaging               26.3
# parso                   0.8.7
# pip                     25.2
# platformdirs            4.13.0
# psutil                  7.2.2
# pure_eval               0.2.4
# Pygments                2.21.0
# python-dateutil         2.9.0.post0
# pyzmq                   27.2.0
# six                     1.17.0
# soupsieve               4.0.1
# stack-data              0.6.3
# tornado                 6.5.10
# traitlets               5.16.1
# wcwidth                 0.9.2


# pip show [패키지명] : 패키지 상세 정보
# Name: beautifulsoup4
# Version: 4.15.0
# Summary: Screen-scraping library
# Home-page: https://www.crummy.com/software/BeautifulSoup/bs4/
# Author-email: Leonard Richardson <leonardr@segfault.org>
# License: MIT License
# Location: d:\py_practice\.venv\Lib\site-packages
# Requires: soupsieve, typing-extensions
# Required-by: 
