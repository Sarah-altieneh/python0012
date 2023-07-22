#take 3 input from the user as a string and check if the string have l or u or both and replace it with *and print the new string
#3 input checks if prime or not or even or odd 
#all the above must be inside a while loop 
#x=0
#while x<3:
 #   checkString=input ('enter a string: ')
  #  for i in range(len(checkString)):
   #      if ((checkString[i]=='l') or checkString[i]=='u'):
    #          checkString=checkString[0:i]+'*'+checkString[i+1:]
    #print(checkString)          

  #  num=int(input('enter the number: '))
   # if (num%2)==0:
    #    print('the number ia even')
   # else : 
    # print('the number is odd') 
        
   # prime=int(input('enter the number : '))
    #for i in range (2,prime):
     #   if (prime%i)==0:
      #      print ('not prime')
       #     break
    #else :
     #   print('prime')   
    #x=x+1        

#home work 2
while True:
    fatherName=input('enter your father name: ')
    motherName=input('enter your mother name: ')
    yourName =input('enter your name: ')
    def printNames(name1,name2,name3):
        return "Your father name is :" + name1+"\n your mother name is: "+name2+" \nyour name is : "+name3
    def lengthOfNames(name1,name2,name3):
        if(name1>name3 ):
            return(name1 +' longger than '+name3)
        if(name2>name3):
            return(name2+' longger than'+name3)
        if(name1<name2):
            return(name1+' shorter than '+name3)
        if(name2<name1):
            return(name2+' shorter than '+name3)            
    print(printNames(fatherName,motherName,yourName))
    print(lengthOfNames(fatherName,motherName,yourName))

            


 
    
   