
# My CV
[CV Link](https://woongheelee.github.io)  

---

# 로컬에서 Jekyll 테마 디버깅하기  

로컬 환경에서 Jekyll을 설정하면 웹페이지 디버깅이 훨씬 간편해집니다.

## 1. Jekyll 환경 설정  

- **Linux 사용자**: [Ubuntu 설치 가이드](https://jekyllrb.com/docs/installation/ubuntu/)를 참고하세요.  
- **Windows 사용자**: [Windows 설치 가이드](https://jekyllrb.com/docs/installation/windows/)를 참고하세요.  

환경 설정 후, 디버깅할 깃 저장소를 클론하고 아래 명령어를 사용해 서버를 실행합니다:  

```shell
bundle init  
bundle exec jekyll serve  
```  
터미널에 표시되는 IP 주소의 **4000번 포트**로 접속하면 사이트에 접근할 수 있습니다.

---

## 2. Windows에서 설치 방법  

1. [RubyInstaller 페이지](https://jekyllrb.com/docs/installation/windows/)에서 `rubyinstaller-devkit-***-x64.exe` 파일을 다운로드합니다.  
2. 다운로드한 파일을 실행하여 설치합니다.
   - 설치 중 첫 번째 선택지에서는 **1번 옵션**을 선택하세요.  
   - 이후의 단계는 **Enter 키**를 눌러 진행합니다.  

3. 아래 명령어를 실행해 `Gemfile`을 생성합니다:  
   ```shell
   bundle init  
   ```  
   생성된 `Gemfile`을 열어 하단에 다음 내용을 추가합니다:  

   ```
   gem "rails"  
   gem "kramdown-parser-gfm"  
   gem "jekyll"  
   ```

4. 의존성 패키지들을 설치하려면 다음 명령어를 실행합니다:  
   ```shell
   bundle install  
   ```

5. 설치가 완료되면 Jekyll 서버를 실행합니다:  
   ```shell
   bundle exec jekyll serve  
   ```  

---

# 아이콘 바꾸기  

이 테마에서는 [Font Awesome](https://fontawesome.com/)의 아이콘을 사용합니다.  
아이콘을 변경하고 싶다면 [W3Schools 아이콘 페이지](https://www.w3schools.com/icons/default.asp)에서 원하는 아이콘을 선택해 교체할 수 있습니다.

---

# 기타 참고 사항  

저장소에 포함된 `originalREADME.md` 파일을 참고하면 추가적인 정보를 확인할 수 있습니다.
