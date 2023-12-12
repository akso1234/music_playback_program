Name = [] # 배열 생성
add = 0 #박자범위 오류와 음높이 오류의 충돌방지 변수

save1 = [] #첫 번째 저장하는 칸
save2 = [] #두 번째 저장하는 칸
save3 = [] #세 번째 저장하는 칸
save4 = [] #네 번째 저장하는 칸
save5 = [] #다섯 번째 저장하는 칸

import tkinter # tkinter 모듈
import winsound # winsound 모듈
import tkinter.messagebox # messagebox모듈
import time #sleep()을 사용하기 위한 모듈 

window = tkinter.Tk() # 창 생성

window.title("노래 프로그램")  # 창 이름을 노래 프로그램으로 정함
window.geometry("400x400") # 창 사이즈
window.resizable(False, False) # 윈도우 창 크기 조절 여부

def start(): # start함수 정의
    for i in range(len(Name)): # 0부터 Name배열의 길이 -1 까지
        LabelName = list(Name[i]) #음정 박자의 구분을 위해 한 글자씩 리스트에 저장
        x = int(LabelName[0]) #옥타브
        y = LabelName[1] #음정
        if len(LabelName) == 4: #박자판정
            if LabelName[2] == '.': #소숫점 판정
                z = (float(LabelName[3])) / 10 #박자의 값을 소수값으로 표현하기 위한 과정
            elif LabelName[2] == ',': #소숫점 판정
                z = float(int(LabelName[3]) + 10) / 10 #박자의 값을 소수값으로 표현하기 위한 과정
        elif len(LabelName) == 3: #박자의 값이 정수일 때 (즉, 길이가 3일때)
            z = int(LabelName[2]) #박자의 값을 정수로 받음.


        if x == 1: #1 옥타브
            if LabelName[1] == '도':
                winsound.PlaySound('Do.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 도 입력하면 도 재생

            elif LabelName[1] ==  '레':
                winsound.PlaySound('Re.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 레 입력하면 레 재생

            elif LabelName[1] ==  '미':
                winsound.PlaySound('Mi.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 미 입력하면 미 재생

            elif LabelName[1] ==  '파':
                winsound.PlaySound('Fa.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 파 입력하면 파 재생

            elif LabelName[1] ==  '솔':
                winsound.PlaySound('Sol.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 솔 입력하면 솔 재생

            elif LabelName[1] ==  '라':
                winsound.PlaySound('La.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 라 입력하면 라 재생

            elif LabelName[1] ==  '시':
                winsound.PlaySound('Si.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)    # 시 입력하면 시 재생

        elif x == 2:#2옥타브
            if LabelName[1] == '도':
                winsound.PlaySound('hDo.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 도 입력하면 도 재생

            elif LabelName[1] ==  '레':
                winsound.PlaySound('hRe.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 레 입력하면 레 재생

            elif LabelName[1] ==  '미':
                winsound.PlaySound('hMi.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 미 입력하면 미 재생

            elif LabelName[1] ==  '파':
                winsound.PlaySound('hFa.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 파 입력하면 파 재생

            elif LabelName[1] ==  '솔':
                winsound.PlaySound('hSol.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 솔 입력하면 솔 재생

            elif LabelName[1] ==  '라':
                winsound.PlaySound('hLa.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 라 입력하면 라 재생

            elif LabelName[1] ==  '시':
                winsound.PlaySound('hSi.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 시 입력하면 시 재생

        elif x == 3:#3 옥타브
            if LabelName[1] == '도':
                winsound.PlaySound('hhDo.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 도 입력하면 도 재생

            elif LabelName[1] ==  '레':
                winsound.PlaySound('hhRe.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)  # 레 입력하면 레 재생

            elif LabelName[1] ==  '미':
                winsound.PlaySound('hhMi.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)   # 미 입력하면 미 재생

        time.sleep(z) #박자 구현
        

def music(event): # entry값을 받을 music 함수를 선언

    Name.append(writeEntry.get()) # entry return값을 배열에 넣음.
    if Name[len(Name) -1] == '-':
        if len(Name) != 1:
            del Name[len(Name) - 2] # 마지막값을 지움
            del Name[len(Name) - 1] # append로 추가된 -를 지움
        else:
            tkinter.messagebox.showerror("오류", "아무것도 없을때는 -를 입력할 수 없습니다.")
            del Name[len(Name) - 1] # append로 추가된 -를 지움

    else:
        testNumber = list(Name[len(Name) - 1]) #Name배열의 마지막 값을 testNumber값에 리스트로 저장
        if Name[len(Name) - 1] == '' or len(testNumber) == 1: #Name에 아무것도 들어있지 않거나 한글자만 입력했을 때 
            tkinter.messagebox.showerror("오류", "입력조건이 맞지 않습니다.")
            del Name[len(Name) - 1] 
        else:
            LabelNumber = list(Name[len(Name) - 1])
            x = int(LabelNumber[0])
            y = LabelNumber[1]
            if len(LabelNumber) == 4:
                if LabelNumber[2] == '.': #소숫점 판정
                        z = LabelNumber[2]
                elif LabelNumber[2] == ',':
                        z = LabelNumber[2]
                else:
                    tkinter.messagebox.showerror("오류", "소숫점은 '.'이나 ','로 표현해주세요.")
                    del Name[len(Name) - 1]

            elif len(LabelNumber) == 3:
                z = int(LabelNumber[2])
                if z < 0 or z > 2: #z 범위 이탈 오류
                    tkinter.messagebox.showerror("오류", "박자의 범위는 0초과 2이하입니다.") #오류 메시지
                    del Name[len(Name) - 1]
                    add = add + 1
            else:
                tkinter.messagebox.showerror("오류", "입력조건이 맞지 않습니다.") #오류 메시지
                del Name[len(Name) - 1]

            if x<1 or x>3: # x가 범위 이탈 오류
                if len(LabelNumber) != 2 or len(LabelNumber) != 4:
                    if add == 1:
                        tkinter.messagebox.showerror("오류", "음높이는 hh까지입니다") #오류 메시지
                        add = 0
                        del Name[len(Name) - 1]

            elif y !='도' and y !='레' and y !='미' and y !='파' and y !='솔' and y !='라' and y !='시': # y가 범위 이탈할 때 오류
                if len(LabelNumber) == 3:
                    tkinter.messagebox.showerror("오류", "음계가 잘못되었습니다") #오류 메시지
                    del Name[len(Name) - 1]

            elif x==3:
                if  y=='파' or y=='솔' or y=='라' or y=='시': # y가 범위 이탈할 때 오류
                    tkinter.messagebox.showerror("오류", "음계가 잘못되었습니다") #오류 메시지
                    del Name[len(Name) - 1]

    writeEntry.delete(0, "end") # 엔트리에 입력된 문자열을 엔터를 칠 때마다 바로 지움

    if len(Name) > 110:
        tkinter.messagebox.showerror("label error", "라벨의 길이가 너무 깁니다")
        del Name[110]
    else:
        logLabel.config(text = ', ' .join(Name)) # 사용자에게 로그를 보여줌.
        
def reset():  # 초기화하기 위한 reset함수를 선언
    del Name[:]  # 모든 배열 값을 없애서 초기화시킴
    logLabel.config(text = " ") # 라벨 수정

def help(): # 도움말 생성 함수
    guidance = tkinter.Toplevel(window) 
    guidance.geometry("450x100") 
    guidance.title("도움말")

    guideButton1 = tkinter.Button(guidance, text = "[1]. 노래 재생", command=guide1) # 노래 재생 버튼 생성
    guideButton1.place(x = 20, y = 50) 

    guideButton2 = tkinter.Button(guidance, text = "[2]. 박자 설명", command=guide2) # 박자 설명 버튼 생성
    guideButton2.place(x = 120, y = 50)

    guideButton2 = tkinter.Button(guidance, text = "[3]. 저장 & 불러오기", command=guide3) #저장& 불러오기 버튼 생성
    guideButton2.place(x = 220, y = 50) 

    guideButton3 = tkinter.Button(guidance, text = "[4]. 도움말", command=guide4)#도움말 버튼 생성
    guideButton3.place(x = 360, y = 50) 

def guide1(): # 노래 재생 설명 함수
    guidance1 = tkinter.Toplevel(window) # 노래 재생 창 생성
    guidance1.geometry("700x400") 
    guidance1.title("노래 재생")
    
    guideLabel = tkinter.Label(guidance1, text = "[1]. 노래 재생\n")
    guideLabel.pack()
    
    guideLabel = tkinter.Label(guidance1, text = "1) 계이름 입력하기")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "*입력창에 옥타브, 계이름, 박자를 입력하고 'start!' 버튼을 누르면 계이름을 따라 음악이 재생돼요!*")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "※중요!! : 입력창에 <옥타브><계이름><박자> 이 순서대로 입력해야 하고, 중간에 띄어쓰기 하면 실행이 안돼요!※*\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "*박자와 전체적인 입력 방법은 '[2]. 박자 입력' 설명을 꼭 봐주세요!*\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "알맞게 입력하면 입력창 아래에 본인이 입력한 것을 확인할 수 있어요!\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "1도 ~ 1시 입력 : ‘1옥타브 도 ~ 시' 음 재생")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "2도 ~ 2시 입력 : ‘2옥타브 도 ~ 시’음 재생")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "3도 ~ 3미 입력 : ‘3옥타브 도 ~ 미’음 재생\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "2) 수정")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "-입력한 것을 지우고 다른 것을 입력하고 싶다면 ‘-’(마이너스)를 입력하세요!\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "3) 전체 삭제")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance1, text = "-입력한 모든 것을 지우고 다른 음악을 재생하고 싶다면 ‘reset!' 버튼을 클릭해주세요!\n")
    guideLabel.pack() # 노래 재생 설명

def guide2(): # 박자 설명 함수
    
    guidance2 = tkinter.Toplevel(window) # 박자 설명 창 생성

    guidance2.geometry("700x650")

    guidance2.title("박자 설명")

    guideLabel = tkinter.Label(guidance2, text = "[2]. 박자 설명\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "'(4분음표) = n' -> 1분동안 연주하는 4분음표 개수")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "따라서 4분음표, 즉 한 박의 길이는 n/60(초)에요\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "ex) (4분음표) = 96(보통빠르기)이면 각 음표별 길이는 \n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(온음표) : 2.4초")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(점2분음표) : 1.8초")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(2분음표) : 1.2초")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(점4분음표) : 0.9초")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(4분음표0 : 0.6초")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(8분음표) : 0.3초")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(16분음표) : 0.15초\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "*주의사항*")
    guideLabel.pack()
    
    guideLabel = tkinter.Label(guidance2, text = "이 프로그램에서는 소수점 아래 '첫째자리'까지만 지정할 수 있으며")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "음의 길이는 0초에서 2초 사이로만 지정할 수 있어요(0<(길이 범위)<2)\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "지정하려는 음의 길이가 0초에서 1초 사이면 .(온점)을 입력해야해요")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "지정하려는 음의 길이가 1초에서 2초 사이면 ,(반점)을 입력해야해요\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "(ex)")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "'(4분음표) = 96' 빠르기에서 입력창에\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "1도.6 입력 시 -> '4분음표(0.6초) 1옥타브 도' 음 재생")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "2미,2 입력 시 -> '2분음표(1.2초) 2옥타브 미'음 재생")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "3레.3 입력 시 -> '8분음표(0.3초) 3옥타브 레'음 재생\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "이때 소수점 앞 정수부분은 아무것도 입력하시면 안돼요!")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "ex) 3도0.6 입력 시 '오류'\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance2, text = "연주하려는 곡의 정확한 빠르기를 모르더라도 음의 길이를 이용해 빠르기와 박자를 마음대로 조절해보세요!")
    guideLabel.pack() # 박자 설명 내용
    

def guide3(): # 저장 & 불러오기 설명 함수
    guidance3 = tkinter.Toplevel(window) # 저장 & 불러오기 설명 창 생성
    guidance3.geometry("600x250") 
    guidance3.title("저장 & 불러오기") 

    guideLabel = tkinter.Label(guidance3, text = "[3]. 저장 & 불러오기")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance3, text = "1) 악보 저장")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance3, text = "-완성한 악보를 저장하고 싶다면 ‘save' 버튼을 클릭해주세요!\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance3, text = "save 버튼을 클릭하면 5개의 파일을 저장할 수 있는 창이 나와요")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance3, text = "FILE 1부터 5중 원하는 파일을 골라 버튼을 클릭하면 악보를 저장할 수 있어요!\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance3, text = "2) 불러오기")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance3, text = "-저장한 악보를 재생하고 싶다면‘load' 버튼을 클릭하여 저장한 악보를 불러오세요!\n")
    guideLabel.pack() 

    guideLabel = tkinter.Label(guidance3, text = "save를 통해 FILE 1에 악보를 저장했다면")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance3, text = "load 버튼을 클릭하고 FILE 1 버튼을 클릭하여 저장해 놓은 악보를 불러올 수 있어요!")
    guideLabel.pack()# 저장 & 불러오기 설명

def guide4(): # 도움말 설명 함수
    guidance4 = tkinter.Toplevel(window) # 도움말 설명 창 생성
    guidance4.geometry("400x100") 
    guidance4.title("도움말") 

    guideLabel = tkinter.Label(guidance4, text = "[3]. 도움말")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance4, text = "-도움말은 ‘?’ 버튼을 클릭하면면 언제든지 다시 볼 수 있어요!\n")
    guideLabel.pack()

    guideLabel = tkinter.Label(guidance4, text = "※타이핑만으로 간단하게 칼림바를 연주해보세요!")
    guideLabel.pack() #도움말 설명 내용



def save(): #저장 함수 총 5개까지
    selectbutton = tkinter.Toplevel(window) #새로운 창 생성
    selectbutton.title("SAVE") #창 이름
    selectbutton.geometry("290x100") #창 사이즈
    
    selectLabel = tkinter.Label(selectbutton, text = "save할 위치를 선택해주세요") #save 안내
    selectLabel.pack() #save 안내 라벨 배치

    selectButton1 = tkinter.Button(selectbutton, text = "FILE1", command=lambda:[number1save(), selectbutton.destroy()])  #첫 번째 save 버튼
    selectButton1.place(x = 20, y = 50) #버튼 위치

    selectButton2 = tkinter.Button(selectbutton, text = "FILE2", command=lambda:[number2save(), selectbutton.destroy()])  #두 번째 save 버튼
    selectButton2.place(x = 70, y = 50) #버튼 위치

    selectButton3 = tkinter.Button(selectbutton, text = "FILE3", command=lambda:[number3save(), selectbutton.destroy()])  #세 번째 save 버튼
    selectButton3.place(x = 120, y = 50) #버튼 위치
 
    selectButton4 = tkinter.Button(selectbutton, text = "FILE4", command=lambda:[number4save(), selectbutton.destroy()])  #네 번째 save 버튼
    selectButton4.place(x = 170, y = 50) #버튼 위치

    selectButton5 = tkinter.Button(selectbutton, text = "FILE5", command=lambda:[number5save(), selectbutton.destroy()])  #다섯 번째 save 버튼
    selectButton5.place(x = 220, y = 50) #버튼 위치



def load(): #저장된 배열을 불러오는 함수
    loadbutton = tkinter.Toplevel(window) #새로운 창 생성
    loadbutton.title("LOAD")  #창 이름
    loadbutton.geometry("290x100") #창 사이즈

    loadLabel = tkinter.Label(loadbutton, text = "load할 위치를 선택해주세요")  #load 안내
    loadLabel.pack() #save 안내 라벨 배치

    loadButton1 = tkinter.Button(loadbutton, text = "FILE1", command=lambda:[number1load(), loadbutton.destroy()]) #첫 번째 load 버튼
    loadButton1.place(x = 20, y = 50) #버튼 위치

    loadButton2 = tkinter.Button(loadbutton, text = "FILE2", command=lambda:[number2load(), loadbutton.destroy()]) #두 번째 load 버튼
    loadButton2.place(x = 70, y = 50) #버튼 위치

    loadButton3 = tkinter.Button(loadbutton, text = "FILE3", command=lambda:[number3load(), loadbutton.destroy()]) #세 번째 load 버튼
    loadButton3.place(x = 120, y = 50) #버튼 위치
 
    loadButton4 = tkinter.Button(loadbutton, text = "FILE4", command=lambda:[number4load(), loadbutton.destroy()]) #네 번째 load 버튼
    loadButton4.place(x = 170, y = 50) #버튼 위치

    loadButton5 = tkinter.Button(loadbutton, text = "FILE5", command=lambda:[number5load(), loadbutton.destroy()]) #다섯 번째 load 버튼
    loadButton5.place(x = 220, y = 50) #버튼 위치

def number1save(): # save 1에 넣는 코드
    if len(Name)==0:  #아무 것도 치지 않고 저장할 때 오류 메세지 출력
        tkinter.messagebox.showerror("save error", "입력된 값이 없어 저장할 수 없습니다")
    else: #입력 값이 있을 때
        del save1[:] #기존 save1 삭제
        for number in range(len(Name)): #Name 배열의 길이만큼 for문 실행
            save1.append(Name[number]) #save1에 입력값을 차례대로 넣음

def number2save(): # 세이브 2에 넣는 코드
    if len(Name)==0:
        tkinter.messagebox.showerror("save error", "입력된 값이 없어 저장할 수 없습니다")
    else:
        del save2[:]
        for number in range(len(Name)):
            save2.append(Name[number])

def number3save(): # 세이브 3에 넣는 코드
    if len(Name)==0:
        tkinter.messagebox.showerror("save error", "입력된 값이 없어 저장할 수 없습니다")
    else:
        del save3[:]
        for number in range(len(Name)):
            save3.append(Name[number])

def number4save(): # 세이브 4에 넣는 코드
    if len(Name)==0:
        tkinter.messagebox.showerror("save error", "입력된 값이 없어 저장할 수 없습니다")
    else:
        del save4[:]
        for number in range(len(Name)):
            save4.append(Name[number])


def number5save(): # 세이브 5에 넣는 코드
    if len(Name)==0:
        tkinter.messagebox.showerror("save error", "입력된 값이 없어 저장할 수 없습니다")
    else:
        del save5[:]
        for number in range(len(Name)):
            save5.append(Name[number])


def number1load(): # 로드 1에 넣는 코드
    del Name[:] #기존 입력값 삭제
    if len(save1) == 0:
        tkinter.messagebox.showerror("load error", "save1이 비어있어 불러올 수 없습니다.")
    else:
        for loadnumber in range(len(save1)): #save1의 값을 차례로 Name에 넣어줌
            Name.append(save1[loadnumber])
        logLabel.config(text = ', ' .join(Name))

def number2load(): # 로드 2에 넣는 코드
    del Name[:]
    if len(save2) == 0:
        tkinter.messagebox.showerror("load error", "save2가 비어있어 불러올 수 없습니다.")
    else:
        for loadnumber in range(len(save2)): #save2의 값을 차례로 Name에 넣어줌
            Name.append(save2[loadnumber])
        logLabel.config(text = ', ' .join(Name))

def number3load(): # 로드 3에 넣는 코드
    del Name[:]
    Name.insert(0,0)
    if len(save3) == 0:
        tkinter.messagebox.showerror("load error", "save3가 비어있어 불러올 수 없습니다.")
    else:
        for loadnumber in range(len(save3)): #save3의 값을 차례로 Name에 넣어줌
            Name.append(save3[loadnumber])
        logLabel.config(text = ', ' .join(Name))

def number4load(): # 로드 4에 넣는 코드
    del Name[:]
    Name.insert(0,0)
    if len(save4) == 0:
        tkinter.messagebox.showerror("load error", "save4가 비어있어 불러올 수 없습니다.")
    else:
        for loadnumber in range(len(save4)): #save4의 값을 차례로 Name에 넣어줌
            Name.append(save4[loadnumber])
        logLabel.config(text = ', ' .join(Name))

def number5load(): # 로드 5에 넣는 코드
    del Name[:]
    Name.insert(0,0)
    if len(save5) == 0:
        tkinter.messagebox.showerror("load error", "save5가 비어있어 불러올 수 없습니다.")
    else:
        for loadnumber in range(len(save5)): #save5의 값을 차례로 Name에 넣어줌
            Name.append(save5[loadnumber])
        logLabel.config(text = ', ' .join(Name))
                    
writeEntry = tkinter.Entry(window)  # 입력값을 받을 entry 선언
writeEntry.bind("<Return>", music)  # enter를 누르면 music 함수를 실행
writeEntry.pack()

logLabel = tkinter.Label(window, text = " ", wraplength =170) # Name 배열을 보여줌(도 레 미 …)
logLabel.pack()

saveLabel = tkinter.Label(window, text = " ") #저장여부를 확인하는 라벨
saveLabel.place(x = 100, y = 20) #라벨 위치 (임의로 정함 수정 될 예정)

startbutton = tkinter.Button(window, text="start!", command=start, cursor="hand2") # startbutton 생성
startbutton.place(x = 25, y = 350) # 버튼 위치 정하기

resetButton = tkinter.Button(window, text = "reset!" , command = reset, cursor="hand2") # 초기화 버튼 생성
resetButton.place(x = 75, y = 350) # 초기화 버튼 위치

helpButton = tkinter.Button(window, text = "?", command=help, cursor="hand2") # helpbutton 생성
helpButton.place(x = 370, y = 10) # 버튼 위치 정하기

saveButton = tkinter.Button(window, text = "save", command=save, cursor="hand2") # savebutton 생성
saveButton.place(x = 275, y =350) # 버튼 위치 정하기

loadButton = tkinter.Button(window, text = "load", command=load, cursor="hand2") # loadbutton 생성
loadButton.place(x = 325, y = 350) # 버튼 위치 정하기

window.mainloop() # 꺼질때까지 반복
