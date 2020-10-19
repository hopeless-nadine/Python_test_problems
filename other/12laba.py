import random #����������� ���������� "Random" ��� ��������� ������ ����
all_letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
def randomletter():
    s =""
    for i in range (5):
        s += random.choice (all_letters) #� ������� ���� ������� �������� �� ������ 5 ��������� ���� � ���������� �����
    return s

def letter(string):
    s=0
    for i in range (5):
        if string[i] in all_letters: #������� ���������, ��� ������ ������ ������ �� 5 ��������� - ��������� �����
            s = s + 1
    if s == 5:
        return True
    else:
        return False
        
while True: #����������� ����, ������ �� ������������ ������� �����
    try:
        M = float(input("������� ������ ������� (����� � ��������� �� 2 �� 5): ")) #�� ���� �������� ��� ������ float
    except (ValueError, KeyboardInterrupt, EOFError): #����� ����������� ������ ���� "������� �� �����", ���������� ctrl+c, "enter"
        print("�������� ������ �����")
    else:
        if (M - int(M) != 0.0) or not (2 <= M <= 5): #��������, �������� �� ��������� ����� �����.
            print("�������� ������ �����")
        else:
            print("������� ������ ��������� ")
            M = int(M) #� ������� ����� ������
            break

answer = -1
while answer not in (0, 1): #���������� ����� ����, �� ������������ ��������� ������� ���(0 ��� 1)
    try:
        answer = float(input("������� 0, ���� ������ ��������� ������� ���������� ���������� �������. ���� ������ ��������� ������� ��������������, ������� 1: "))
    except (ValueError, KeyboardInterrupt, EOFError):
        print("�������� ������ �����")
    else:
        if (answer not in (0, 1)) or (answer - int(answer) !=0.0):
            print("�������� ������ �����")
        else:
            print("����� �������")
            answer = int (answer)
            

a = [randomletter() for i in range(M ** 2)] #���������� ������ ���������� ������� ��� �������� �������

if answer == 1: #���������� ������� �������
    for i in range(M ** 2):
        while True:
            try:
                slovo = input("������� ����� �� 5 ��������� ����: ")
            except (KeyboardInterrupt, EOFError):
                print("�������� ������ �����")

            else:
                if len (slovo) != 5:
                    print("�������� ������ �����. ����� ������ ��������� 5 ����.") 
                elif len (slovo) == 5 and letter (slovo) is False:
                    print("�������� ������ �����. ����� ������ �������� �� ���� ���������� ��������") #����������� ������� ��� �������� ���� ��������
                else:
                    print ("����� �������")
                    a[i] = slovo
                    break
letters = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"} #������� ���������, ���������� ��� ������� ����� ���������� ��������
s = 0
for i in range (0, M**2, M):
    for j in range (M):
        print (a[i+j], end = " ") #����� �������� �������
    print ()

for i in range (M**2):
    slovo = a[i]
    for j in range (5):
        if slovo[j] in letters: #�������� ������ ����� �� ���������� �� � ������� "letters"
            s = s + 1
    a[i] = s * 10 + (5 - s) #�������� ������� ������� �� �����, �� ��� ������ �� �����
    s = 0
k=[]
for i in range (0, M**2, M): #����� ������� �� ����.
    for j in range (M):
        k.append (a[i+j])
    k = sorted(k, reverse=False) #������ ������ ������� ��������� �� ����������� � ������� ���������� ������� "sorted"
    for l in range (M):
        print (k[l], end =" ")
    print()
    k =[]
