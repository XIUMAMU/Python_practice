### 한국 IT 전문 학원 - SW 및 빅데이터 지역 인재 양성 과정 - Python
####
#### 22/08/23  
    Practice 1 - input()과 print()를 이용한 주급 계산기 작성해보기  
#### 22/08/25  
    Practice 2   - if문을 활용한 간단한 제어문 작성해보기  
    Practice 2_1 - input()으로 수를 입력받아 해당 수가 몇번째 그룹에 속하는지 print()  
    Practice 2_2 - 주급 계산기에 초과수당과 주말근무수당 개념을 더해 더 자세한 주급 계산기 작성해보기  
    Practice 2_3 - while문을 활용한 간단한 반복문 작성해보기  
#### 22/08/29  
    Practice 3_1 - while과 input()을 이용한 간단한 구구단 출력기 작성해보기  
    Practice 3_2 - for문을 활용한 간단한 반복문 작성해보기  
    Practice 3_3 - 원하는 만큼 숫자 입력 후 그 숫자들 중 최대값, 최소값 출력해보기  
    Practice 3_4 - 여러 점수를 받아 총 학생수, 점수 합계, 평균 출력해보기  
    Practice 3_5 - 학생번호별 과목별 점수를 받아 학생별 총점, 평균과 과목별 총점, 평균 출력해보기  
#### 22/08/30  
    Practice 4_1 - 함수 정의 하여 실행해보기  
    Practice 4_2 - .upper()과 .lower()을 이용하여 자동으로 단어 앞글자는 대문자로, 나머지는 소문자로 하는  
                   함수 정의 후 이용해보기
#### 22/08/31
    Practice 5_1 - URL을 받아 파싱과 추출을 이용하여 도메인과 컨텐츠명 추출하기
    Practice 5_2 - 특정 문자열에서 원하는 부분을 추출하여 원하는 포맷으로 출력하기
                   > 참고 1 ( "\r" CR( 커서를 맨 앞으로 ) / "\n" LF( 개행 ) )
                   > 참고 2 ( c:\user\temp\test.py => \u로 인해 오류가 나고 \t는 탭으로 인식 
                                                                     => \ 를 / 로 해주거나 \\ 사용하기 )
    Practice 5_3 - 5_2의 내용을 각각 함수로 정의해보고 메인루틴 함수 정의 해보기
#### 22/09/06
    Practice 6_1 - Dictionary와 get 함수를 이용한 구문 분석 ( 구성 단어와 빈도수 측정 )
#### 22/09/07
    Practice 7_1 - 6에서 했던 코드를 이제 input이 아닌 open으로 텍스트파일을 불러와서 적용해보기
    Practice 7_2 - open으로 불러온 텍스트 파일의 줄의 수 카운트
                 / read를 이용하여 텍스트파일을 하나의 문자열로 읽어오기
#### 22/09/13
    Practice 8_1 - try/except 사용하여 숫자 타입 체커 만들어보기
#### 22/09/14
    Practice 9_1 - open과 read 복습과 실습
    Practice 9_2 - 문자열을 16진수로 출력하는 프로그램 작성해보기
    Practice 9_3 - Binary로 파일 열어보기
    Practice 9_4 - 아스키 코드 표 출력하는 프로그램 작성해보기
#### 22/09/19
    Practice 10_1 - open의 w 모드와 a 모드
    Practice 10_2 - Class의 생성과 사용
    Practice 10_3 - Class의 상속
    Practice 10_4 - Class를 이용한 학생 정보 입력 받아 성적 파일에서 성적 조회 후 출력 및 파일로 저장하기
    Practice 10_4_1 - 10_4 실습 응용 - 학생 정보 입력 받아 폼에 맞춰 출력하기
    Practice 10_4_2 - 10_4 실습 응용 - 파일에서 학생 정보를 가져오고
                                                또 다른 파일에서 성적 정보를 가져와서 폼에 맞춰 출력 및 파일로 저장하기
#### 22/09/20
    Practice 11_1 - class 복습 및 수치 연산자 메소드
#### 22/09/21
    Practice 12_1 - 수치 연산자 override 연습 - __add__, __sub__, __mul__ ( Scalar / Vector )
    Practice 12_2 - 다른 파일의 class를 현재 파일에 import
#### 22/09/27 ~ 22/09/29
    MISSION 1_01 - 랜덤한 이름과 이름 하나당 난수 (0 - 100) 4개를 각각 국어, 수학, 영어, 컴퓨터 점수로 넣어 파일로 저장 
    MISSION 1_02 - sin, cos, tan 그래프와 원, 원안의 sin 그래프 (태극) 을 문자열로 그리기
    MISSION 1_02 _ 1 : sin 그래프와 원까지는 그렸지만 나머지는 도저히 못하겠음.
    MISSION 1_02 _ 2 : 그래프를 그리는 패키지 사용 가능 하다고 하셔서 matplotlib과 turtle 중에 turtle로 선택해서 그렸음.
    MISSION 1_03 - 입력을 통해 주어진 문자열 안에 회문, Palindrome 가 있는 경우 최대 회문의 길이를 출력
    MISSION 1_03 _ 1 : 문자열 하나하나의 갯수와 그것들의 위치에 따라 회문을 찾고 길이 반환
                       ( 문제점 -> 같은 문자가 연속 2이상이 양쪽에 포함된 회문일 경우 인식을 잘 못함. )
    MISSION 1_03 _ 2 : abc가 있으면 [ab] > [abc] > [abcd] > [bc] > ... 식으로 슬라이싱을 통해 범위를 늘려가면서 확인.
                       ( 문제점 해결. 코드도 더욱 간단해졌다. )
    MISSION 1_04 - 두 수를 입력받아 최대공약수 출력
    MISSION 1_05 - 알파벳을 하나 입력받아 그보다 알파벳 순위가 낮은 모든 문자를 출력하고      예) b > :ab
                   맨뒤가 하나씩 탈락해서 마지막에 a가 하나 출력되도록 만들기                        :a
    MISSION 1_06 - 홀수를 입력받아 *로 피라미드를 출력                                     예) 3 > : *
                                                                                                  :***
    MISSION 1_07 - 알파벳을 하나 입력받아 대문자로 다음 형태로 출력                          예) b > :AA
                                                                                                  :B
    MISSION 1_08 - 파일을 통해 이름, 과목, 점수를 입력받고 합계, 평균, 석차를 구한 후 추가하여 파일로 저장
    MISSION 1_09 - 음식 이름과 가격이 있는 메뉴판이 있을 때 정해진 금액으로 살 수 있는 모든 상품의 조합과 가격을 출력
    MISSION 1_09 _ 1 : 이름은 파일에서 불러오고 가격은 난수로 부여 받고, 정해진 금액은 입력받아 사용했음.
                       for을 통해 가격을 하나하나 더해가려 하니 2가지 이상 조합이 힘들어짐.
    MISSION 1_09 _ 2 : 회문 문제에서 썼던 방식을 사용하여 슬라이싱과 sum을 통해 모든 조합과 합계를 도출해서
                       합계가 가진 돈 보다 작을 때 조합에 들어가는 메뉴와 총 가격을 출력. 2가지 이상 조합이 가능해짐.
    MISSION 1_10 - 이때까지 작성했던 문제들을 조합하여 특정 입력을 받으면 특정 기능이 실행되도록 만들기
    MISSION 1_11 - 파일명을 입력받아 임의의 텍스트파일을 열어 그 안에서 또 입력 받은 찾을단어를 바꿀단어로 바꿔
                   다른 파일로 저장하고 빈도수 출력.
