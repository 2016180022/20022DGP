# Mitterent

## 발표 링크
- 1. [1차 발표](https://youtu.be/6IkFQ4MS9Wc)
- 2. [2차 발표](https://youtu.be/ZcLfMwPtFSI)
- 3. [최종 발표](https://youtu.be/X_nYUUvX1Vw)

## 목차
- 1. 게임의 소개 
	- 1.1 High Concept
	- 1.2 핵심 메카닉
- 2. Scene의 수 및 각각의 이름
- 3. 각 Scene 별 항목
	- <span style="color:red">3.1 메인 화면</span>
	- 3.2 플레이 화면
		- 3.2.1 노말 스테이지
		- <span style="color:red">3.2.2 보스 스테이지</span>
	- <span style="color:green">3.3 메뉴 화면</span>
- 4. 개발 범위
- 5. 필요한 기술
	- 5.1 맵 타일링 및 스크롤링
	- 5.2 플레이어 및 적 캐릭터 이동/공격/피격 이미지 출력
	- 5.3 플레이어 및 적 캐릭터 공격/피격/죽음 판정
	- 5.4 적 캐릭터 AI 구현
	- <span style="color:green">5.5 메뉴화면 출력</span>
	- <span style="color:red">5.6 게임 데이터 저장</span>
- 6. 추가 구현 사항
  
  
  
  
## 1. 게임의 소개
제목: Mitterent(사격)  
  
**게임 로고**

![로고](https://github.com/2016180022/20022DGP/blob/master/img/logo_2.png?raw=true)  
  

원 게임명: 메탈슬러그  
![메탈슬러그3 메인 화면](https://lh3.googleusercontent.com/-PpZvHUTNczo/Wn3jrRALIxI/AAAAAAAAh-Q/F5GBSoUC400h3_zFxwfuFVRZ4Jq1KSgQQCHMYCw/s0/5a1c2cde5a1feb8b5a8079e909163a4277224370.png)  
![메탈슬러그3 플레이 화면](https://image.playonestore.com/images/data/item/1542864883/1543196413_9328_3.jpg)  
게임의 목적: 적들을 사살하고 스테이지의 끝까지 도달하여 스테이지를 클리어  
게임의 방법: 적들의 공격을 회피하고, 공격으로 처치하여 스테이지의 끝까지 도달  
  
### 1.1 High Concept  
![High concept](https://github.com/2016180022/20022DGP/blob/master/img/high_concept.PNG?raw=true)  
  
### 1.2 핵심 메카닉  
![핵심 메카닉 요약](https://github.com/2016180022/20022DGP/blob/master/img/jook_chang.PNG?raw=true)  
1.익스텐드 없는 잔기제 방식(목숨이 하나이고, 피격하면 바로 사망하는 방식)  
2. 보스를 제외한 모든 유닛의 체력은 1  
3. 일대 다수 상황에서 수적 열세를 극복  
이 세가지 핵심 메카닉이 High Concept에 해당하는 '액션'을 부각시켜주고 '반복'을 유도  
  
  
  
  
## 2. Scene의 수 및 각각의 이름  
![Mitterent 플로우차트](https://github.com/2016180022/20022DGP/blob/master/img/scene_flowchart.png?raw=true)  
기본 화면은 3종류의 화면이며, 각각 메인 화면, 플레이 화면, 메뉴 화면으로 지정  
  
  
  

## 3. 각 Scene 별 항목  
  
<span style="color:red">### 3.1 메인 화면</span>  
게임을 시작하고, 플레이 화면으로 가기 전 단계  
화면에 표시할 객체: 게임 로고, 대기 이미지(추가 구현)  
처리할 이벤트: 모든 키 및 마우스 입력을 받고, 플레이 화면으로 이동  
이동가능한 Scene: 플레이 화면  
  
### 3.2 플레이 화면  
플레이어와 적 캐릭터를 표시하고 맵을 스크롤링하는 게임 진행을 위한 단계  
화면에 표시할 객체: 맵, UI, 플레이어 및 적 캐릭터, 탄환 및 아이템 등의 오브젝트  
처리할 이벤트: 플레이어 및 적 캐릭터 이동 및 공격/피격 이벤트, 사망 판정, 메뉴 화면 출력  
이동가능한 Scene: 메뉴 화면, 메인 화면
  
#### 3.2.1 노말 스테이지  
![노말 스테이지](https://github.com/2016180022/20022DGP/blob/master/img/normal_sta.png?raw=true)  
플레이어와 적 캐릭터, 탄환 표시, 맵 스크롤링, 각종 이벤트 판정  
<span style="color:red">#### 3.2.2 보스 스테이지  </span>
![보스 스테이지](https://github.com/2016180022/20022DGP/blob/master/img/boss_stage.png?raw=true)  
플레이어와 보스 캐릭터, 보스의 패턴 표시, 각종 이벤트 판정  
승리 시, 축하 문구와 승리 모션 출력 후 메인 화면으로 이동  
  
<span style="color:green">### 3.3 메뉴 화면  </span>
사망 시 플레이 화면의 update를 중지하고 메뉴 화면 출력
엔터 키 입력으로 다시 플레이 화면으로 전환 가능
이동가능한 Scene: 플레이 화면  
  
  
## 4. 개발 범위  
![개발 범위](https://github.com/2016180022/20022DGP/blob/master/img/devel_range.PNG?raw=true)  
  
<span style="color:red">**특수 공격 예시)**</span>  
![특수 공격](https://github.com/2016180022/20022DGP/blob/master/img/special_attack.png?raw=true)  
  
<span style="color:red">**보스 패턴 예시)**</span>
![보스 패턴](https://github.com/2016180022/20022DGP/blob/master/img/boss_pattern.png?raw=true)  

  
  
## 5. 필요한 기술  
  
### 5.1 맵 타일링 및 스크롤링  
스테이지 별 맵 타일링  
플레이어 위치에 따라 맵 스크롤링  
  
### 5.2 플레이어 및 적 캐릭터 이동/공격/피격 이미지 출력  
타일 모양에 따른 플레이어 위치 변경(평지, 비탈길, 언덕, 낭떠러지)  
회피 구현  
플레이어 및 적 캐릭터 공격시 탄환 이미지 및 공격 모션 출력  
플레이어 및 적 캐릭터 사망시 사망 이미지 출력  
  
### 5.3 플레이어 및 적 캐릭터 공격/피격/죽음 판정  
탄환 이미지 등 공격 이펙트들의 충돌 판정  
Hp 계산, 죽음 판정  
  
### 5.4 적 캐릭터 AI 구현  
기본적인 등장/이동 루틴  
플레이어를 공격하는 루틴  
<span style="color:red">보스의 공격 패턴</span>
  
### 5.5 메뉴 화면 출력  
메뉴 화면으로 이동  
메뉴 화면 출력시 게임 일시정지  
  
<span style="color:red">### 5.6 게임 데이터 저장</span>  
인게임 재화 및 스코어 데이터 저장  
  
**다른 과목에서 배웠던 기술**  
4.3.1의 충돌 판정 - 윈도우 프로그래밍  

**이 과목에서 배울 것으로 기대되는 기술**  
4.5.2의 게임 일시정지, 4.6의 게임 데이터 저장  
  
**다루지 않는 것 같아서 수업에 다루어 달라고 요청할 기술**  
4.1.2의 캐릭터 위치에 따른 맵 스크롤링  
  
  
<span style="color:red">## 6. 추가 구현 사항</span>
  
### 6.1 캐릭터 추가
기본 캐릭터가 저격병 컨셉의 캐릭터이기 때문에, 시원시원한 플레이에 제약이 있음  
또 다른 재미를 즐길 수 있는, 기본적으로 이동속도가 빠르고 점프를 사용 가능한 근접 전투 캐릭터 추가 계획

### 6.2 인게임 재화 추가
적을 처치하거나 스테이지를 클리어하면 재화를 획득하고, 그 재화로 새로운 캐릭터를 해금하거나 새로운 스킨을 획득하거나 하는 기능 추가 계획

### 6.3 스테이지 추가
새로운 스테이지와 그에 해당하는 보스 몬스터 추가 계획
  
  
  
  
  
made by. 2016180022 박찬얼