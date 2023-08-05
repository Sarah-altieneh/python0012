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
#while True:
 #   fatherName=input('enter your father name: ')
  #  motherName=input('enter your mother name: ')
  #  yourName =input('enter your name: ')
   # def printNames(name1,name2,name3):
    #    return "Your father name is :" + name1+"\n your mother name is: "+name2+" \nyour name is : "+name3
   # def lengthOfNames(name1,name2,name3):
    #    if(name1>name3 ):
     #       return(name1 +' longger than '+name3)
      #  if(name2>name3):
       #     return(name2+' longger than'+name3)
        #if(name1<name2):
         #   return(name1+' shorter than '+name3)
        #if(name2<name1):
         #   return(name2+' shorter than '+name3)            
  #  print(printNames(fatherName,motherName,yourName))
   # print(lengthOfNames(fatherName,motherName,yourName))


## home work 3
#numList=[1,3,6,8,'5','9',10,13,9,20]
#sumation=0.0
#for i in numList:
 #   sumation+=int (i)
#print ('sumation: ',sumation)
#avg=sumation/len(numList)    
#print('avg: ',avg)
#maxvalue=int(numList[0])
#minvalue=int(numList[0])
#for i in numList:
 #   if int (i)>maxvalue:
  #      maxvalue=int(i)

   # if int(i) <minvalue:
    #    minvalue=int(i)
#print ('maxvalue: ',maxvalue)
#print ('minvalue: ',minvalue)        

# home work of dec
#def getStudentInformation():
 #   studentName= input('Enter the student name: ')
  #  studentAge =int (input('Enter the student age :'))
   # studentCity=input('Enter the city  where the student live : ')
   # studentJob=input ('Enter the job of the student : ')
    #print ('Enter the parent information')
    #fatherName =input('Enter name of the student father : ')
    #motherName =input('Enter name of the student mother : ')
    #parents={'mother':motherName,'father':fatherName}
    #skillsElements = int(input("Enter the number of skills you have : "))
    #skills = []
    #for i in range(skillsElements):
     #   user_input = input("Enter the skill: ")
      #  skills.append(user_input)
    #return{
     #   'name':studentName,
      #  'age':studentAge,
       # 'city':studentCity,
        #'job':studentJob,
        #'Parents':parents,
        '#skills':skills
    #}
#classRoom={}
#newStudent='yes'
#while newStudent:
  #   if newStudent=='yes':
   #     print ('\n Enter the student information ')
    #    studentInformation = getStudentInformation()
     #   classRoom[studentInformation['name']] =studentInformation
      #  newStudent= input("Do you want to add more students? (yes/no): ")
    #elif newStudent=='no' :        
     #   print("\nClassroom Dictionary:")
      #  for student_name, student_info in classRoom.items():
       #                 print(f"Name: {student_info['name']}")
        #                print(f"Age: {student_info['age']}")
         #               print(f"City: {student_info['city']}")
          #              print(f"Job: {student_info['job']}")
           #             print("Parents:")
            #            print(f"\tmother : {student_info['Parents']['mother']}")
             #           print(f"\tfather: {student_info['Parents']['father']}")
              #          print("Skills:", ", ".join(student_info['skills']))
               #         print('-----------------------------------')
#classes home work
         