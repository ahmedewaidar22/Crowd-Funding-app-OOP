############################################Member############

class Member:
    def __init__(self,First_name,Last_name,Email,Password,Mobile_phone):
        self.First_name=First_name
        self.Last_name=Last_name
        self.Email=Email
        self.Password=Password
        self.Mobile_phone=Mobile_phone
        f = open("demofile2.txt", "a")
        f.write( self.Email+"|"+self.Password+"|"+self.First_name+"|"+self.Last_name+"|"+self.Mobile_phone+"\n")
        f.close()
    
    def allinformation(self):
        a_file = open("demofile2.txt")
        file_contents = a_file.read()

        print(file_contents)
    def SIGNIN(Email,password):
        with open('demofile2.txt') as f:
           for line in f:
              
               x = line.split("|", 1)
               y = x[1].split("|", 1)
               if x[0]==Email and y[0]==password:
                   print("enter")
                   return True
               else:
                   pass
                  
               if 'str' in line:
                 
                  break
              
############################################project############
class Project:
    def __init__(self, title, details, total_target, start_time, end_time, author):
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = str(start_time)
        self.end_time =str(end_time)
        self.author = author
        f = open("file2.txt", "a")
        f.write( self.author+"|"+self.title+"|"+self.details+"|"+self.total_target+"|"+self.start_time+"|"+self.end_time+"\n")
        f.close()
    
        
        
    

#############################validation#########################
import re
import datetime


def validation(First_name,Last_name,email,passwd,confirm_passwd,NUM):
    vall=True
    if isinstance(First_name, str)==True:
        print("yes")
    else:
        vall=False

    if isinstance(Last_name, str)==True:
        print("yes")
    else:
        vall=False   
    #
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
            print("Valid Email")
     
    else:
            print("Invalid Email")
            vall=False
    #password validation

    val=True
    if len(passwd) < 6:
            print('length should be at least 6')
            val = False
              
    if len(passwd) > 20:
            print('length should be not be greater than 8')
            val = False
              
    if not any(char.isdigit() for char in passwd):
            print('Password should have at least one numeral')
            val = False
              
    if not any(char.isupper() for char in passwd):
            print('Password should have at least one uppercase letter')
            val = False
    if(val==True):
        print("ok")
    else:
        print("notokdsa")

    if(confirm_passwd==passwd):
        print("yes")
    else:
        vall=False
        
    regex = '^0201[0125][0-9]{8}'

    if(re.fullmatch(regex, NUM)):
             print("Valid Email")
    else:
        vall=False
    if vall==True:
        mumber=Member(First_name,Last_name,email,passwd,NUM)
        return True
    else:
        return False
    

#########################MAIN##########################################
enter=input("Enter your Signin 0 or signup 1");


if(enter=="0"):
    username=input("Enter your username ");
    password=input("Enter your password");
   
    if Member.SIGNIN(username, password) ==True:
        title=input("Enter yoour title");
        details=input("Enter yoour details");
        total_target=input("Enter your total_target");
        start_time=input("What is your B'day? (in DD/MM/YYYY) ")  
        sstart_time=datetime.datetime.strptime(start_time,"%d/%m/%Y").date()
        end_time=input("What is your B'day? (in DD/MM/YYYY) ")  
        eend_time=datetime.datetime.strptime(end_time,"%d/%m/%Y").date()
        Project(title,details,total_target,sstart_time,eend_time,username)
        
    else:
        print("didnt")
elif(enter=="1"):
    First_name=input("Enter yoour First name");
    Last_name=input("Enter yoour Last name");
    email=input("Enter your email");
    passwd=input("Enter your passwd");
    confirm_passwd=input("confrim passwd");
    NUM=input("Enter your passwd");
    validation(First_name,Last_name,email,passwd,confirm_passwd,NUM)




