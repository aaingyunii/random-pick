# 추첨 프로그램 - 파이썬

- 최종 임시 발표 대비 조별 발표자 선정 프로그램

- https://github.com/dj-twenty-six/101/issues/22

### 개발환경 - Docker(Python 3.12.0)

- https://hub.docker.com/_/python

```bash
$ docker pull python:3.12.0

$  docker images
REPOSITORY  TAG       IMAGE ID       CREATED        SIZE
python      3.12.0    17e65561fd2c   2 weeks ago    1.02GB

# 도커 컨테이너 생성 및 진입
$ docker run -it --name random-pick -p 8080:80 python:3.12.0 bash

# vim 설치
$ apt update
$ apt install vim

# vi 테스트
$ vi
```

### 개발 및 테스트

```bash
# 파이썬 파일 생성
$ mkdir code
$ vi code/random_pick.py

# 코드 작성 후 실행
$ chmod +x random_pick.py
$ ls -al # 실행 가능여부 확인 후

$ python code/random_pick.py
팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):
 강민정
팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):
 김하현
팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):
 박수빈
팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):
 심재호
팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):
 안인균
팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):
 이주선
팀원 한명씩 입력 후 엔터 (종료: 빈칸  엔터키):

발표자는 김하현 입니다

```

![image](https://github.com/dj-twenty-six/101/assets/31847834/56dfeb38-78f6-42b5-b259-2d108dda185e)


### 소스코드 복사

```bash
# 컨테이너로부터 작성된 파이썬 파일을
# 로컬 환경으로 가져오기

$ docker cp random-pick:root/code/random_pick.py ~/code/random-pick/
Successfully copied 2.05kB to /home/user1/code/random-pick/

# random-pick -> 생성된 컨테이너의 이름 혹은 컨테이너 ID 입력
# root/code/random_pick.py -> 컨테이너 속 복사 파일
# ~/code/random-pick/ -> 로컬 저장소 위치

```

