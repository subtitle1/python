- 액세스 키, 비밀 액세스 키 준비해놓기

- 터미널 준비하기
```
  mkdir deploy
  cp app.py deploy/application.py
  cp -r templates deploy/templates
  pip freeze > deploy/requirements.txt (requirements.txt 파일에 사용한 라이브러리 적어 달라는 명령어)
  cd deploy
```

- appication.py 세팅하기
```python
  application = app = Flask(__name__)
  app.run()
```

- deploy 폴더 안에! 패키지 설치하기
```
  pip install awsebcli
```

- 보안 자격증명
```
  eb init
```

- 초기 설정
```
  eb create myweb
```
- 코드 수정 & 업데이트
```
  eb deploy myweb
```
