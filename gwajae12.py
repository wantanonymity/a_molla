import requests
r=requests.get("https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text")
r.encoding='utf8'
words=str(r.text)

a=words.find("Madam President, Mr. Secretary-General,")
b=words.rfind("Thank you very much. Thank you. (Applause.)")

before=words[a:b+len("Thank you very much. Thank you. (Applause.)")+1]
before=before.replace('<p id="',' ')
before=before.replace('</p>',' ')
before=before.replace(',',' ')
before=before.replace('.',' ')
after=before.replace('">',' ')

#print(after)
After=after.lower()
word_list=After.split()

mydict={}


for w in word_list:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1

L=[]

for k in sorted(mydict, key=mydict.__getitem__, reverse=True):
    L.append(k)

NEWLIST=[]
for i in range(20):
    NEWLIST.append(L[i])

    
print("최다빈도순으로 단어 20개를 차례로 리스트에 append 시켰음: ",NEWLIST)


