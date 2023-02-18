# Requirments

<br>

## Set User Info

### Print message to get pwd to start conversation
> Print requests repeatedly until program gets correct pwd. 
1. Telegram Bot requests pwd to user
    * output : `채팅방 비밀번호를 입력하세요`
    * cmd_output : `/pwd 텔레그램_챗봇_시작_비밀번호` 
2. User gives program pwd, by using command
    * ex) `/pwd 1234` 

<br>

### Print message to get user info
> If correct pwd for conversation is entered, ChatBot requires to set user info 
1. Telegram Bot requests id and pwd to get ticket by using user account
    * output : `코레일 아이디(회원번호)를 입력하세요`
    * cmd_output : `/아이디 코레일_아이디`
    
    <br>
    
    * output : `코레일 비밀번호를 입력하세요` 
    * cmd_output : `/비번 코레일_비밀번호`
2. User gives program id, by using command
    * `/아이디 5323414` 
    * `/비번 5323414` 

<br>

### Print message to get detail information for reservation
> Get information for train reservations
1. Telegram Bot requests date, time, departure station, arrival station
    * output : `출발 기차 날짜를 입력하세요`
    * cmd_output : `/h 기차_시작_시간`
    
    <br>
    
    * output : `출발 기차 시간을 입력하세요`
    * cmd_output : `/d 기차_시작_월_일`
    
    <br>
    
    * output : `출발역을 입력하세요` 
    * cmd_output : `/s 기차_출발역`
    
    <br>
    
    * output : `도착역을 입력하세요` 
    * cmd_output : `/e 기차_도착역`
    
    <br>
    
    * output : `타실 기차를 선택해주세요 ex) ktx, 새마을, 무궁화`
    * cmd_output : `/t 기차_타입`
    
    <br>
    
    * output : `상위 몇개의 기차를 타실지 선택해주세요. 2개를 선택하시면 입력하신 시간 기준 가까운 기차 2개 중 1개가 예매됩니다`
    * cmd_output : `/n 기차 개수`
2. User gives program id, by using command
    * ex) `/h 7`
    * ex) `/d 1 4`
    * ex) `/s 동대구`
    * ex) `/e 서울`
    * ex) `/t ktx`
    * ex) `/n 2`

<br><br>

## Features

### Show list of available trains
> Based on information that user entered, program shows available day schedule of starts from hour that user enterd 
* input : `/기차목록` 
<br>

### Starts reservation
> Based on information that user enterd, program runs repeatedly to get cancelation ticket. 
* input : `/예매시작` 

<br>

### Show list of command
> If user wants to modify user inforamation or info for reservation, user may forget chatbot command. In that case feature that shows list of command could help user to modify
* output : `언제나 명령어를 보기 위해서는 /명령어를 입력하세요`
* input : `/명령어` 