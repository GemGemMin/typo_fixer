import tkinter as tk
import tkinter.font
from PIL import ImageTk, Image



dic1 = {1:[1,3,4,5,9,11,18],2:[-1,2,3,4,8,10,17],3:[1,2,4,5,6,9,10,11,12,13,14],4:[-3,-2,-1,1,2,8,9],5:[-4,-3,-2,-1,1,7,8],6:[-5,-4,-1,4,5,6,9,13],7:[-4,1,2,6,7,9,10],8:[-5,-1,1,5],9:[-6,-2,-1,4],10:[-9,-8,-4,1,9],11:[-10,-9-5,-1,8],12:[-11,-10,-9,-7,-6,-5,2,3,4,6,7],13:[-10,-9,-8,-6,-5,-1,1],14:[-11,-10,-9,-7,-6,-2,-1],15:[-12,-3,-6,2,3],16:[-9,-13,1],17:[-10,-14,-5,-1,-2],18:[-6,-12,1,-3],19:[-18,-9,-13,-1]} 
# 1=ㄱ 2=ㄲ 3=ㄴ 4=ㄷ 5=ㄸ 6=ㄹ 7=ㅁ 8=ㅂ 9=ㅃ 10=ㅅ 11=ㅆ 12=ㅇ 13=ㅈ 14=ㅉ 15=ㅊ 16=ㅋ 17=ㅌ 18=ㅍ 19=ㅎ
dic2 = {1:[1,2,3,4,6,18,20],2:[-1,1,2,4,5,19],3:[-2,-1,1,2,4,18],4:[-3,-2,-1,2,3,17],5:[-4,-2,2,4,8],6:[-4,15],7:[-6,-4,-2,2,6],8:[-6,-2,13],9:[-4,-2,4,5,9],10:[-9,-8,-7,-6,-5,-3,-1,1,2,3,4,5,6,7,8,9,10,11],11:[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10],12:[-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9],13:[-8,-6,-4],14:[-9,-5,4,5],15:[-14,-12,-10,-8,-6,-2,-1,4],16:[-14,-11,-7,-2,1,3,5],17:[-16,-15,-14,-12,-11,-8,-1,2,4],18:[-9,-4],19:[-18,-14,-10,-5],20:[-19,-18,-15,-14,-11,-6,-1,1],21:[-20,-19,-17,-15,-13]}
# 1=ㅏ 2=ㅐ 3=ㅑ 4=ㅒ 5=ㅓ 6=ㅔ 7=ㅕ 8=ㅖ 9=ㅗ 10=ㅘ 11=ㅙ 12=ㅚ 13=ㅛ 14=ㅜ 15=ㅝ 16=ㅞ 17=ㅟ 18=ㅠ 19=ㅡ 20=ㅢ 21=ㅣ
dic3={0:[],1:[6,18,20,6,26],2:[-1,5,17,19,5,25,-1],3:[4,18,5,24-2,16],4:[13,18,3,12,17,20,21,19],5:[12,11,19,20,18,16,2],6:[11,10,18,19,17,15,1,-5,13,2,20,2,21,-1],7:[15,-6,-3,14,1],8:[-1,-7,11,13,19,15,18],9:[-2,12,14,17,18,10],10:[7,12,-3,-9,9,6,-6,11,-2,17,24,15,13,16],11:[6,11,-4,-10,8,5,-7,10,-3,16,12,15,-1],12:[-5,-11,7,9,-4,15,11,14],13:[-6,-12,6,3,-9,8,-5,14,11,12,10,13,-1],14:[-7,-13,5,7,-6,13,9,12],15:[-8,-14,4,6,-7,12,8,11,-1],16:[1,6,-12,8,9],17:[5,-1,-13],18:[4,-2,-14,-17,-10,9],19:[-18,-11,8],20:[-19,-12,7],21:[1,-14,4,2,5,-13,-20],22:[-5,-15,-6,-18,-1],23:[-19,-2,-15,2,3],24:[-8,-20,1],25:[-1,-9,-21,-4,-2],26:[-3,-5,-18],27:[-8,-26,-19,-1]}



from bs4 import BeautifulSoup

import requests


def ApiCount (wd):
    url="https://opendict.korean.go.kr/api/search?certkey_no=284&key=6311184377912AA20D7FBE5F8470420D&target_type=search&part=word&q="+wd+"&sort=dict&start=1&num=10"

    req = requests.get(url)

    html = req.text

    soup = BeautifulSoup(html, 'html.parser')



    codenumber = soup.find_all('total')
    return codenumber[0].text   


window= tk.Tk()
window.title("키보드 위치를 고려한 오타 수정기")
window.geometry("740x493+100+100")
window.config(background='white')

font=tkinter.font.Font(family="맑은 고딕", size=20)
image=ImageTk.PhotoImage(Image.open('Logo.jpg'))
label_background=tk.Label(window, image=image)
label_background.place(x=0, y=220)

def adding(event):
    Gs=0
    Input1 = entry.get()
    List1 = list(Input1)
    List3 = list(Input1)                #입력받은 단어를 리스트꼴로 바꿈
    List2 = list(Input1)
    sun1=0
    sun2 = 0
    sun3 = 0
    for i in List1:                     # 입력받은 글자가 완성된 글자인지 확인
        if ord(i) > 55203 or ord(i) <44032 :
            print('완성된 글자가 아닙니다')
            break
        else :
            e = int(ApiCount(Input1))
        
            if 10>e :                # 입력받은 글자가 사전에 없으면 초성비교시작!
                Q=ord(i)
                cho=int(((Q-44032)/588)+1) #입력받은 글자의 초성을 알아냄
                Cho=dic1[cho] 
            
                for j in Cho:          # 초성바꿈
                    Em1="" 
                    ori1=List1[sun1]      
                    List1[sun1]=chr(Q+(588*j)) # 초성의 10진수 값 확인
                    d1=list()
                    c1=len(Input1)
                    while c1>=0:   
                        d1.append(c1)
                        c1=c1-1
                        d1.sort()
                    d1.pop()
                    for k in d1:
                        Em1=Em1+List1[k]
                    Cek1=int(ApiCount(Em1))
                    if Cek1>=20:
                        listbox.insert(sun1, Em1)
                sun1=sun1+1
                List1 = list(Input1)  
            
            if 10>e:                # 입력받은 글자가 사전에 없으면 종성비교시작!
                Q=ord(i)
                Jon=(Q-44032)%28        # 입력받은 글자의 종성을 파악
                jong=dic3[Jon] 
            
                for j in jong:          # 종성바꿈
                    Em3="" 
                    ori3=List3[sun3]      
                    List3[sun3]=chr(Q+j) # 첫글자의 종성부터 비교시작
                    d3=list()
                    c3=len(Input1)
                    while c3>=0:   
                        d3.append(c3)
                        c3=c3-1
                        d3.sort()
                    d3.pop()
                    for k in d3:
                        Em3=Em3+List3[k]
                    Cek3=int(ApiCount(Em3))
                    if Cek3>=20:
                        listbox.insert(sun1+sun3+1,Em3)
                sun3=sun3+1
                List3 = list(Input1)
            
            if 10>e :                # 입력받은 글자가 사전에 없으면 중성비교시작!
                Q=ord(i)
                Joo=int((((Q-44032)-(cho-1)*588)/28)+1) # 입력받은 글자의 중성 파악
                Joong=dic2[Joo] 
            
                for j in Joong:          # 초성바꿈
                    Em2="" 
                    ori2=List2[sun2]      
                    List2[sun2]=chr(Q+(j*28)) # 중성의 10진수 값 확인
                    d2=list()
                    c2=len(Input1)
                    while c2>=0:   
                        d2.append(c2)
                        c2=c2-1
                        d2.sort()
                    d2.pop()
                    for k in d2:
                        Em2=Em2+List2[k]
                    Cek2=int(ApiCount(Em2))
                    if Cek2>=20:
                        listbox.insert(sun1+sun3+sun2+2,Em2)
                sun2=sun2+1
                List2 = list(Input1)
            
            else:                     #입력받은 글자가 사전에 있다면 바로 출력
                label_change.config(text=Input1)  
                break

def CurSelet(evt):
    value=str((listbox.get(listbox.curselection())))
  
    label_change.config(text=""+value)
    

    
entry=tk.Entry(window, font=font, width= 15)
entry.place(x=150, y=100)
entry.bind("<Return>",adding)

listbox=tk.Listbox(window, font=font,height=7)
listbox.place(x=420, y=100)
listbox.bind('<Return>', CurSelet)

label_entry=tk.Label(window,text="입력창",font=font)
label_entry.place(x=50, y=100)

label=tk.Label(window, text="출력창",font=font)
label.place(x=50,y=150)

label_change=tk.Label(window, font=font)
label_change.place(x=150,y=150)






