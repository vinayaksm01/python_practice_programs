import time
import atexit

r = [406, 420, 350, 407, 210, 100]
Non=[100,220,550,879,120,300,520,600]
sing=[400,320,800,140,520,620,320,450]
for i in range(10):
    print("**************************WELCOME TO VINAYAK HOTEL************************************************")
    print("*************************PLEASE CHOOSE YOUR CHOICE*********************************************")
    print('''    1.Rooms Availability
    2.Rent Enquiry
    3.Book Room
    4.Location of Hotel
    5.Exit''')



    class roomAvil():
        def rooms(self, choice,room_type):
            if choice == 1:
                self.choice = choice
                self.room_type=room_type
                print('Room Types')

                print('''                1.AC Delux
                2.NON-AC
                3.Single''')

    class booking(roomAvil):
        def AC_Room(self,room_type):
            self.room_type=room_type


            if room_type == 1:
                print("Avilable rooms are :", r)
                room_no = int(input('enter the room number you want :'))
                print('------------------------------------------------------------------------')
                name = input('Plz Enter your name: ')
                print('-------------------------------------------------------------------------')
                Addr = input('Plz enter your address: ')
                print('--------------------------------------------------------------------------')
                mob_no = input("Plz enter your mobile number: ")
                print('---------------------------------------------------------------------------')
                r.remove(room_no)

        def non_AC(self,room_type):
            if room_type == 2:
                print("Available rooms are: ",Non)
                self.room_type = room_type
                room_no = int(input('enter the room number you want :'))
                print('------------------------------------------------------------------------')
                name = input('Plz Enter your name: ')
                print('-------------------------------------------------------------------------')
                Addr = input('Plz enter your address: ')
                print('--------------------------------------------------------------------------')
                mob_no = input("Plz enter your mobile number: ")
                print('---------------------------------------------------------------------------')
                Non.remove(room_no)

        def single(self,room_type):
            if room_type == 3:
                print("Available rooms are: ",sing)
                self.room_type = room_type
                room_no = int(input('enter the room number you want :'))
                print('------------------------------------------------------------------------')
                name = input('Plz Enter your name: ')
                print('-------------------------------------------------------------------------')
                Addr = input('Plz enter your address: ')
                print('--------------------------------------------------------------------------')
                mob_no = input("Plz enter your mobile number: ")
                print('---------------------------------------------------------------------------')
                sing.remove(room_no)




    obj = roomAvil()
    print('================================================================================')
    choice = int(input("enter the choice : "))



    print('==================================================================================')
    obj.rooms(choice,'room_type')
    obj1 = booking()
    room_type = int(input("Choose the Room type: "))

    obj1.AC_Room(room_type)
    obj1.non_AC(room_type)
    obj1.single(room_type)
    print("Plese make the payment")
    print('''    1.Credit Card
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

                print("************THANK YOU***********")

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

                print("************THANK YOU***********")

        def payTM(self, a):
            self.a = a
            if a == 3:
                upi = input("Enter payTM UPI number : ")
                print("pleese wait payment processing.........................................")
                print("................................")
                time.sleep(10)
                print("payment successfull")

                print("*************THANK YOU*************")
                print('''           1.To Exit booking 
                2.Continue Booking''')
                opt=int(input('enter the choice: '))
                if opt == 1:
                    exit()
                elif opt == 2:
                    print('')




    c1 = payment()
    a = int(input("enter payment choice:  "))
    c1.Creadit(a)
    c1.debit(a)
    c1.payTM(a)


