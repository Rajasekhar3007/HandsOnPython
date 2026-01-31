#All inputs
StudentID=input("ID:")
Email=input("Email:")
Password=input("Password:")
Referral=input("Referral:")
Reg_No=input("Registration Number:")

num=int(Reg_No[-1])

#Process based on last digit of Registration Number
if(num%2==0):
#Even:check StudentID first
    # StudentID Validation
     if(len(StudentID)==7 and StudentID[0:3]=="CSE" and StudentID[3]=='-' and StudentID[4:].isdigit() 
     ):
         
       ID_valid=True
     else:
         
         ID_valid=False
             
    #Then check Password 
     if(len(Password)>=8 and Password[0].isupper() and (Password[1].isdigit() or Password[2].isdigit() or Password[3].isdigit() or Password[4].isdigit() or Password[5].isdigit() or Password[6].isdigit() or Password[7].isdigit())
         ):   
                
         Password_valid=True
     else:
         
        Password_valid=False
       
else:
#Odd:check Password first
    #Password Validation
    if(len(Password)>=8 and Password[0].isupper() and (Password[1].isdigit() or Password[2].isdigit() or Password[3].isdigit() or Password[4].isdigit() or Password[5].isdigit() or Password[6].isdigit() or Password[7].isdigit())):
    
       Password_valid=True
    else:
        
       Password_valid=False
       
#Then check StudentID
    if(len(StudentID)==7 and StudentID[0:3]=="CSE" and StudentID[3]=='-' and StudentID[4:].isdigit() 
        ):
        
        ID_valid=True
        
    else:
            
        ID_valid=False   
    
# Email Validation
if (Email.count("@")==1 and Email.count(".")>=1 and Email[0]!="@" and Email[-1]!="@" and Email[-4:]=='.edu'):
    
    Email_valid=True
else:
    
    Email_valid=False
  
# Referral Validation  
if(len(Referral)==6 and Referral[0:3]=="REF" and Referral[3].isdigit() and Referral[4].isdigit() and Referral[5]=='@'):
    
    Referral_valid=True
else:
    
    Referral_valid=False
    
#Final Output
if(ID_valid and Email_valid and Password_valid and Referral_valid):
    print("APPROVED")
else:
    print("REJECTED")
