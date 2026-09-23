#[PCCE Past Exam Question] Question 9 / Folding banknotes
def solution(wallet, bill):
    w=0
    while min(wallet)<min(bill) or max(wallet)<max(bill):
        if bill[0]>bill[1]:
            bill[0]=bill[0]//2
            w=w+1
        else:
            bill[1]=bill[1]//2
            w=w+1
    answer = w
    return answer



#Hall of Fame (1)
def solution(k, score):
    w=[]
    answer= []
    for x in score:
        w.append(x)
        w.sort(reverse=True)
        if len(w)>k:
            w.pop()
        answer.append(w[-1])
    return answer



#Making strange characters
def solution(s):
    answer=''
    s=s.split(' ')
    for x in s:
        for i in range(len(x)):
            if i%2==0:
                answer= answer+x[i].upper()
            else:
                answer+= x[i].lower()
        answer+=' '
    return answer[:-1]
             


#The Three Musketeers
def solution(number):
    answer=0
    a=len(number)
    for i in range(a):
        for j in range(i+1,a):
            for k in range(j+1,a):
                if number[i]+number[j]+number[k]==0:
                    answer+=1
    return answer
