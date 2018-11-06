import requests
r=requests.get("https://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text")
r.encoding='utf8'
words=str(r.text)

a=words.find("Madam President, Mr. Secretary-General,")
b=words.rfind("Thank you very much. Thank you. (Applause.)")

before=words[a:b+len("Thank you very much. Thank you. (Applause.)")]

before=before.replace('<p id="',' ')
before=before.replace('</p>',' ')
after=before.replace('">',' ')

#print(after)
After=after.lower()
word_list=After.split()

mydict={}
#word_list에 트럼프 연설문

for w in word_list:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1

#print(sorted(mydict, key=mydict.__getitem__, reverse=True))

#for i in range(1,21):
#    print("%s:%s"%(sorted(mydict, key=mydict.__getitem__, reverse=True)[i+1],mydict[i]))


for k in sorted(mydict, key=mydict.__getitem__, reverse=True):

    print("%s:%s"%(k,mydict[k]))
