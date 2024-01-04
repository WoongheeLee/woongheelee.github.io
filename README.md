# cv
[my cv link](https://woongheelee.github.io)

# 내 컴퓨터에서 jekyll 테마 디버깅 하기
* 먼저 jekyll 을 사용할 수 있는 환경을 만들어두면 웹페이지 디버깅이 쉽다.
  * linux 사용자라면 https://jekyllrb.com/docs/installation/ubuntu/
  * 윈도우 사용자라면 https://jekyllrb.com/docs/installation/windows/ 를 참고하여 jekyll 실행환경을 만들어서 웹페이지 디버깅이 가능
* 깃 저장소를 다운받아서,  아래 명령어를 실행하고 나타나는 ip주소의 4000번 포트로 접속하면 된다.
```shell
bundle init
bundle exec jekyll serve
```
## 윈도우에서 설치법
1. 위 링크에서 rubyinstaller-devkit-\*\*\*-x64.exe 파일을 받는다. 
2. 프로그램을 실행해서 설치한다. 이 때 선택지는 1번을 먼저 고르고, 나머지는 엔터 입력으로 설치
3. GemFile을 만들어주고, 파일을 열어서 하단을 아래와 같이 수정
```shell
bundle init
```
```
gem "rails"
gem "kramdown-parser-gfm"
gem "jekyll"
```
4. 그런 후 bundle install 명령어로 위 환경 의존적인 것들을 설치해준다.
5. 설치가 완료되면 bundle exec jekyll serve를 하면 끝

# 아이콘 바꾸기
* 이 테마에는 [font awesome](https://fontawesome.com/)이라는 아이콘을 사용한다.
* 아이콘 모양을 바꾸고 싶다면 [w3school](https://www.w3schools.com/icons/default.asp)의 아이콘을 둘러보고 마음에 드는 걸로 바꾸면 쉽다.

# 기타 
* 추가로 originalREADME.md 를 참고