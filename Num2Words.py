# PROGRAM TO CONVERT NUMBERS INTO WORDS (num2words):

def num2words(n):
    
    # Listing out indiviual digits as integers for easier recognition
    lst = list(n)
    a = [0]*len(lst)
    i=0
    for k in lst:
        a[i] = int(k)
        i+=1
    
    # Database for converting each digits into words 
    ones = [' ','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'] 
    tens = [' ',' ','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    dig2 = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    
    # Condition to satisfy numbers within the range 10-19 due to their unique words
    if int(n) in range(10,20):
        return dig2[n-10]
    
    # Condition to satisfy 1 digit numbers
    elif len(a)==1 and int(n)!=0:
        o = ones[a[0]]
        return (o)
    
    #Condition to satisfy 2 digit numbers
    elif len(a)==2:
        t = tens[a[0]]
        o = ones[a[1]]
        return (t+' '+o)
    
    #Condition to satisfy 3 digit numbers
    elif len(a)==3:
        h = ones[a[0]]+' Hundred'
        t = tens[a[1]]
        o = ones[a[2]]
        return (h+' '+t+' '+o)
    
    # Condition to satisfy zero
    elif int(n)==0:
        k = 'Zero'
        return k
    
    # Error condiiton specific to this program
    else:
        err = 'Error --> This program converts numbers from 0 to 999 into words,\n\t  Please provide a number within the specified range.'
        return err
    
# Main program for execution
num = input('Enter a number between 0 and 999: ')
output = num2words(num)
print(output)

