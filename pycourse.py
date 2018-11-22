import re
import time
import random


class login():
    def log(self,usr_name,passwd):
        self.usr_name=usr_name
        self.passwd=passwd




        n = re.fullmatch("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", passwd)
        if n == None:
            print("plz enter one upper case one lower case and one special charecter")
            passwd = input("plese renter the passaword : ")

        secrete_num = random.randint(1, 200000)
        print('plese wait OTP is sending......')
        time.sleep(5)
        print("plz enter the shown OTP in Box")
        print(secrete_num)

        otp = int(input('enter the OTP : '))

        if otp == secrete_num:

            class student():
                def getstd_details(self, std_name, std_id, cls_room):
                    self.std_name = std_name
                    self.std_id = std_id
                    self.cls_room = cls_room
                    print("--------------------------------------------------------------------------------")

                def std_display(self):
                    print("The student id is : ", std_id)
                    print("The student name is: ", std_name)
                    print("The student class room is: ", cls_room)
                    print("*********************************************************************************")

            obj = student()
            print("Enter the student details ")
            std_id = input("Enter the student id : ")
            m = re.fullmatch("[a-zA-Z0-9]*", std_id)

            std_name = input("Enter the student name : ")
            n = re.fullmatch("[a-zA-Z]*", std_name)
            if n == None:
                print("plz enter the valid name it should contain the alphabetic values")
                std_name = input("Enter the student name : ")

            cls_room = input("Enter the class room :")
            obj.getstd_details(std_name, std_id, cls_room)
            obj.std_display()
            print("************************************************************************************")
            print("The following course offered are follows : ")
            print(''' 1.python
             2.Django
             3.selenium
                      ''')
            z = 900
            b = 9
            c = 'Python'
            e = 1000
            f = 5
            d = "Django"
            g = 1200
            h = 10
            x = "selenium"

            class course(student):
                def course_offered(self, choice):
                    if choice == 1:
                        print("hi......", std_name)
                        print("Your student id is :")
                        print("course you opted is :", c)
                        print("the course fee is Rs.", z)
                        print("Duration is :", b, "hrs")
                    elif choice == 2:
                        print("hi......", std_name)
                        print("Your student id is :", std_id)
                        print("course you opted is :", d)
                        print("the course fee is Rs.", e)
                        print("Duration is :", f, "hrs")
                    elif choice == 3:
                        print("hi......", std_name)
                        print("Your student id is :", std_id)
                        print("course you opted is :", x)

                        print("the course fee is Rs.", g)
                        print("Duration is :", h, "hrs")
                        print("=============================================================")

            obj1 = course()
            choice = int(input('enter which course you want to join : '))
            print("==========================================================================")
            obj1.course_offered(choice)
            print("==========================================================================")
            print("Plese make the payment")
            print('''1.Credit Card
            2.Debit Card
            3.payTM
                ''')

            class payment():
                def Creadit(self, a):
                    self.a = a
                    if a == 1:
                        name = input("enter the name on card : ")
                        cnum = input("enter card number : ")
                        exp_date = input("enter the card exp date : ")
                        cvv = input("enter the cvv : ")
                        print("pleese wait payment processing :................................... ")
                        print("................................")
                        time.sleep(10)
                        print("payment successfull")

                        print("************ALL THE BEST***********")

                def debit(self, a):
                    self.a = a
                    if a == 2:
                        name = input("enter the name on card : ")
                        cnum = input("enter card number : ")
                        exp_date = input("enter the card exp date : ")
                        cvv = input("enter the cvv : ")
                        print("pleese wait payment processing :..................................... ")
                        print("................................")
                        time.sleep(10)
                        print("payment successfull")

                        print("************ALL THE BEST***********")

                def payTM(self, a):
                    self.a = a
                    if a == 3:
                        upi = input("Enter payTM UPI number : ")
                        print("pleese wait payment processing.........................................")
                        print("................................")
                        time.sleep(10)
                        print("payment successfull")

                        print("*************ALL THE BEST*************")

            c1 = payment()
            a = int(input("enter payment choice:  "))
            c1.Creadit(a)
            c1.debit(a)
            c1.payTM(a)

        else:
            print('You entered the Wrong OTP')
wel = login()
usr_name = input('enter the user name:')
passwd = input('enter the passaword : ')
print('=========================================================================================')


wel.log(usr_name, passwd)













