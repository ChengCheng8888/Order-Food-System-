#Tey Jing Teng/Kong Wei Cheng
#TP064508/TP065917

#--------------All Menu--------------
def loginAOFS():
    print("---------Welcome to AOFS login page---------")
    option02 = input('''
    1. New User
    2. Register User
    3. Admin
    4. Exit

Please enter your selection: ''')
    
    if option02 == "1":
        loginAdmin()
        
    elif option02 == "2":
        loginDeliveryS()
        
    elif option02 == "3":
        mainmenu()
        
    elif option02 == "4":
        exit()
        
    else:
        print("Invalid choice, please choose again")
        loginAOFS()

#----------------------Admin list information----------------
Adminlist_n = [ "AdminAOFS" ]
Adminlist_p = [ "7123" ]

#------------Login Admin-----------------------
def loginAdmin():
    
    print("---------Welcome to Admin page---------")
    AName = input("Please enter the admin's ID:")
    APassword = input("Please enter the admin's password:")

    if (AName in Adminlist_n and APassword in Adminlist_p):
        Adminoption02 = input('''
        1. Add Food Item Category-wise
        2. Modify Food Item
        3. Display All record
        4. Search spectific customer record
        5. Order Delivery Management
        6. Exit

Please enter your selection: ''')

        if Adminoption02 == "6":
            exit()
            
        elif Adminoption02 == "1":
            AddFoodCW()
            
        elif Adminoption02 == "2":
            ModifyFI()
            
        elif Adminoption02 == "3":
            Displayrec()
            
        elif Adminoption02 == "4":
            Searchsr()
            
        elif Adminoption02 == "5":
            DeliveryM()
            
        else:
            print("Invalid choice, plesase choose again")
            loginAdmin()
    else:
        print("Wrong Admin information")
        loginAOFS()
        
#----------------Delivery Staff list information-------------------
DeliverySlist_n = [ "DeliverySAOFS" ]
DeliverySlist_p = [ "9999" ]

#---------------Login Delivery Staff----------------- 
def loginDeliveryS():
    
    print("---------Welcome to Delivery staff page---------")
    DSName = input("Please enter the delivery staff's ID:")
    DSPassword = input("Please enter the delivery staff's password:")

    if (DSName in DeliverySlist_n and DSPassword in DeliverySlist_p):
        DeliverySoption02 = input('''
        1. View and select Orders for Delivery
        2. Update Delivey Status
        3. Exit

Please enter your selection: ''')
        
        if DeliverySoption02 == "3":
            exit()
            
        elif DeliverySoption02 == "1":
            ViewSOD()
            
        elif DeliverySoption02 == "2":
            UpadteDS()
            
        else:
            print("Invalid choice, plesase choose again")
            loginDeliveryS()
            
    else:
        print("Wrong Delivery Staff information")
        loginAOFS()
        
#------------------Add Food Item in certain category (Admin)-------------------
def AddFoodCW():
    
    print("---------Three category of food in AOFS---------")
    Foodoption = input('''
    1. Breakfast
    2. Lunch
    3. Dinner
    4. Exit
    
Which category of food want to add item: ''')

    if(Foodoption == "1"):
    
        Bfast_list = []
        Bfast = input("What food of breakfast want to add:")
        Bfast_list.append(Bfast)
            
        with open("Breakfast.txt","a") as a:
            a.write(";".join(Bfast_list)+"\n")
            a.close()
            print("Successful adding the breakfast")
            AddFoodCW()
            
    elif(Foodoption == "2"):
        
        Lch_list = []
        Lch = input("What food of lunch want to add:")
        Lch_list.append(Lch)
           
        with open("Lunch.txt","a") as b:
            b.write(";".join(Lch_list)+"\n")
            b.close()
            print("Successful adding the lunch")
            AddFoodCW()
            
    elif(Foodoption == "3"):
        
        Dner_list = []
        Dner = input("What food of dinner want to add:")
        Dner_list.append(Dner)
            
        with open("Dinner.txt","a") as c:
            c.write(";".join(Dner_list)+"\n")
            c.close()
            print("Successful adding the dinner")
            AddFoodCW()
            
    elif(Foodoption == "4"):
        exit()
        
    else:
        print("Please enter the option between 1-3")
        AddFoodCW()
    
#-----------------Modify Food Item (Admin)------------------
def ModifyFI():
    
    print("---------Three category of food in AOFS---------")
    Modifyoption02 = input('''
    1. Breakfast
    2. Lunch
    3. Dinner
    4. Exit
Which category of food item need to modify: ''')
        
    if(Modifyoption02 == "1"):
        Breakfast_list = []
        a = open("Breakfast.txt","r")
        for rec in a:
            Breakfast_list.append(rec.strip())
        print(Breakfast_list)
        OBfast = input("What item of breakfast want to change:")            
        ind = -1
        for cnt in range(len(Breakfast_list)):
            if (OBfast in Breakfast_list[cnt]):
                ind = cnt
                break
        if (ind != -1):
            Breakfast_list[ind] = input("The item will change with:")
            with open("Breakfast.txt","w") as a:  
                for x in Breakfast_list:
                    rec = x +"\n"
                    a.write(rec)
            print("Modify successful")
                    
        else:
            print("Please enter the correct food"+"\n")
        
            
    elif(Modifyoption02 == "2"):
        Lunch_list = []
        b = open("Lunch.txt","r")
        for rec in b:
            Lunch_list.append(rec.strip())
        print(Lunch_list)
        OLch = input("What item of lunch want to change:")            
        ind = -1
        for cnt in range(len(Lunch_list)):
            if (OLch in Lunch_list[cnt]):
                ind = cnt
                break
        if (ind != -1):
            Lunch_list[ind] = input("The item will change with:")
            
        else:
            print("Please enter the correct food"+"\n")
            ModifyFI()
        with open("Lunch.txt","w") as b:  
            for x in Lunch_list:
                rec = x +"\n"
                b.write(rec)
            print("Modify successful")
            
    elif(Modifyoption02 == "3"):
        Dinner_list = []
        c = open("Dinner.txt","r")
        for rec in c:
            Dinner_list.append(rec.strip())
        print(Dinner_list)
        ODner = input("What item of dinner want to change:")            
        ind = -1
        for cnt in range(len(Dinner_list)):
            if (ODner in Dinner_list[cnt]):
                ind = cnt
                break
        if (ind != -1):
            Dinner_list[ind] = input("The item will change with:")
            
        else:
            print("Please enter the correct food"+"\n")
            ModifyFI()
        with open("Dinner.txt","w") as c:  
            for x in Dinner_list:
                rec = x +"\n"
                c.write(rec)
            print("Modify successful")
            
    elif(Modifyoption02 == "4"):       
        exit()
        
    else:
        print("Please enter the option between 1-3")
        ModifyFI()
      
#-------------------Display all record (Admin)----------------------
def Displayrec():
    Displayoption = input('''
    1. Breafast
    2. Lunch
    3. Dinner
    4. Customer Order and Customer Payment
    5. Exit
    
Please enter your selection: ''')

    if(Displayoption == "1"):
        print("These record are for Breakfast"+"\n")
        with open("Breakfast.txt","r") as a: 
            print(a.read())
            Displayrec()
            
    elif(Displayoption == "2"):
        print("These record are for Lunch"+"\n")
        with open("Lunch.txt","r") as b: 
            print(b.read())
            Displayrec()
            
    elif(Displayoption == "3"):
        print("These record are for Dinner"+"\n")
        with open("Dinner.txt","r") as c:
            print(c.read())
            Displayrec()
            
    elif(Displayoption == "4"):
        print("These record are for Customer order and Customer Payment"+"\n")
        with open("customerOrderdetail.txt","r") as db:
            print(db.read())
            Displayrec()
            
    elif(Displayoption == "5"):
        exit()
        
    else:
        print("Invalid choice, please choose again")
        Displayrec()
        
#-------------------Order Delivery Management(Admin)-----------------
def DeliveryM():
    print("---------Management Delivery Staff page---------")
    AdminD = input('''
    1. Add Delivery Staff
    2. Modify Delivery Staff
    3. Search Delivery Staff
    4. Delete Delivery Staff
    5. Assgin orders to Delivery Staff page
    6. Exit
    
Please enter your selection: ''')

    if(AdminD == "1"):
        DeliveryS_list = []
        DeliveryS = input("What delivery staff need to add: ")
        DeliverySS = input("Enter the delivery staff status(Available/Unavailalbe): ")
        DeliveryIlist = [DeliveryS,DeliverySS]
        DeliveryS_list.append(DeliveryIlist)
        
        with open("DeliveryS.txt","a") as d:
            for DeliveryIlist in DeliveryS_list:
                rec = ";".join(DeliveryIlist)+"\n"
                d.write(rec)
                print("Successful adding the delivery staff")
                
    elif(AdminD == "2"):
        DeliveryS_list = []
        d = open("DeliveryS.txt","r")
        for rec in d:
            DeliveryS_list.append(rec.strip().split(";"))
        print(DeliveryS_list)
        ODelivery = input("Which delivery staff need to modify: ")
        ind = -1
        for cnt in range(len(DeliveryS_list)):
            if (ODelivery in DeliveryS_list[cnt][0]):
                ind = cnt
                break
        if (ind != -1):
            DeliveryS_list[ind][0] = input("The delivery staff will change to:")
            
        else:
            print("Please enter the correct delivery staff.")
            DeliveryM()
        with open("DeliveryS.txt","w") as d: 
                for mylist in DeliveryS_list:
                    rec = ";".join(mylist)+"\n"
                    d.write(rec)
        print("Modify successful")
            
    elif(AdminD == "3"):
        d = open("DeliveryS.txt","r") 
        SDelivery = input("You want search for which delivery staff: ")            
        if(SDelivery in d.read()):
            print("The delivery staff in AOFS.")
            DeliveryM()
        else:
            print("The delivery staff does not exist.")
            DeliveryM()
            
    elif(AdminD == "4"):
        DeliveryS_list = []
        with open("DeliveryS.txt","r") as d:
            for rec in d:
                DeliveryS_list.append(rec.strip().split(";"))
                
        print(DeliveryS_list)
        
        SD = input("Insert the delivery staff that need to delete")
        ind = -1
        for x in range(len(DeliveryS_list)):
            if(SD in DeliveryS_list[x][0]):
                ind = x
                break
        if (ind != -1):
            DeliveryS_list.pop(ind)
        else:
            print("Can not find the staff.")
            DeliveryM()
        with open("DeliveryS.txt","w") as d:
            for DeliveryIlist in DeliveryS_list:
                rec = ";".join(DeliveryIlist)+"\n"
                d.write(rec)
                print("Successful delete the staff.")
                
    elif(AdminD == "5"):
        Customerorder_list = []
        with open("customerOrderdetail.txt","r") as db:
            for rec in db:
                Customerorder_list.append(rec.strip().split(","))
        print(Customerorder_list)
        assign = input("Please enter the customer name that want to assign to delivery staff delivered page: ")
        c = -1
        for cnt in range(len(Customerorder_list)):
            if(assign == Customerorder_list[cnt][2]):
                c = cnt
                break
        if(c != -1):
            with open("delivery.txt","a") as vv:
                vv.write(";".join(Customerorder_list[cnt])+"\n")
                vv.close()
                print("Successful assign to delivery page")
        else:
            print("Please enter the correct customer name.")
            
    elif(AdminD == "6"):
        exit()
        
    else:
        print("Invalid choice, please choose again")
        DeliveryM()

#----------------Search spectific record(Admin)------------------------
def Searchsr():
    print("---------This is the page for search certain customer order.---------")
    record_list = []
    with open("customerOrderdetail.txt","r") as db:
        search = input("Please enter the customer that you want to show: ")    
        for order in db:
            CustomerR = order.strip().split(",")
            record_list.append(CustomerR)
        c = -1
        for cnt in range(len(record_list)):
            if(search == record_list[cnt][2]):
                c = cnt
                break
        if(c != -1):
            print(record_list[cnt][0].center(10)+record_list[cnt][1].center(10)+record_list[cnt][2].center(10)+record_list[cnt][3].center(10)+record_list[cnt][4].center(10))       
        else:
            print("Record does not exist.")
            loginAdmin()
            
#----------------Update Delivey Status(Delivery Staff)------------------
def UpadteDS():
    DeliveryS_list = []
    with open("DeliveryS.txt","r") as d:
        for rec in d:
            DeliveryS_list.append(rec.strip().split(";"))
            
    print(DeliveryS_list)
    Staff = input("Please enter the Staff that his/her status need to modify: ")
    ind = -1
    for cnt in range(len(DeliveryS_list)):
        if (Staff in DeliveryS_list[cnt][0]):
            ind = cnt
            break
    if (ind != -1):
        DeliveryS_list[ind][1] = input("Please enter new status for the staff(Available/Unavailable/Delivered): ")
    else:
        print("Record not found...")
    with open("DeliveryS.txt","w") as d:
        for DeliveryIlist in DeliveryS_list:
            rec = ";".join(DeliveryIlist)+"\n"
            d.write(rec)
            
#----------------View and select Orders for Delivery(Delivery Staff)------------------
def ViewSOD():
    print("Welcome to assign order page"+"\n")
    DeliveryS_list = []
    with open("DeliveryS.txt","r") as d:
        for rec in d:
            DeliveryS_list.append(rec.strip().split(";"))

    DSVName = input("Please enter your delivery staff name: ")
    indd = -1
    for cntt in range(len(DeliveryS_list)):
        if (DSVName in DeliveryS_list[cntt][0]):
            indd = cntt
            break
    if (indd != -1):
        deliverylist = []
        with open("delivery.txt","r") as vv:
            for rec in vv:
                deliverylist.append(rec.strip().split(";"))
        print(deliverylist)
        d.close()
        Dorder = input("Enter the customer name that you want to delivery: ")
        ind = -1
        for cnt in range(len(DeliveryS_list)):
            if (Dorder in deliverylist[cnt][2]):
                ind = cnt
                break
        if (ind != -1):
            list = []
            listnew = (DeliveryS_list[cntt][0],deliverylist[cnt])
            list.append(listnew)
            with open("StaffDelivery.txt","a") as dd:
                for listnew in list:
                    recc = (";".join(map(str,listnew))+"\n")
                    dd.write(recc)
                    print("Assign order successful.")
        else:
            print("Please enter the correct customer name."+"\n")
    else:
        print("Please enter the correct staff name."+"\n")

# Main Menu (For Login and Regisiter)
def mainmenu():
    choice = input("\n"+"<<<---- Welcome to APU ONLINE FOOD SERVICES (AOFS) ---->>>\n\n1: Login\n2: New Register\nPlease select your option: ")
    if choice =="1":
       login_customer()
    elif choice == "2":
        register_customer()
    else:
        print ("Invalid Option ")
    mainmenu()


# Three Meals
def Food_Item_Menu():
    option = input("\n\n"+"<<<<<------------- AOFS Three Meals ------------->>>>>\n\nStep 1:Please take a look our menu\nStep 2:After step 1,Please place your order (click 4)\n\n1: Breakfast\n2: Lunch\n3: Dinner\n4: Order \n5. Exit program\nPlease pick an option: ")

    if option == "5":
        mainmenu()
    elif option =="4":
        orderpage()
    elif option == "2":
        print("\n"+">>>>>>>>>>-------------- The Lunch Menu ----------------<<<<<<<<<<"+"\n")
        lunch=[]
        with open("Lunch.txt","r") as b:
            for cnt in b:
                lunch1 = cnt.strip().split("|")
                lunch.append(lunch1)
            print(b.read())
        for price in range(len(lunch)):
          print(lunch[price][0].center(30) + "|".center(30) +"RM11")

        Food_Item_Menu()

    elif  option == "3":
        print("\n"+">>>>>>>>>>-------------- The Dinner Menu ----------------<<<<<<<<<<"+"\n")
        dinner=[]
        with open("Dinner.txt","r") as c:
            for cnt in c:
              dinner1= cnt.strip().split("|")
              dinner.append(dinner1)
            print(c.read())
        for price in range(len(dinner)):
          print(dinner[price][0].center(30) + "|".center(30) +"RM12")
       
        Food_Item_Menu()

    elif  option == "1":
        print("\n"+">>>>>>>>>>-------------- The Breakfast Menu ----------------<<<<<<<<<<"+"\n")
        with open ("Breakfast.txt","r")as a:
            breakfast=[]
            for cnt in a:
              breakfast1= cnt.strip().split("|")
              breakfast.append(breakfast1)
            print(a.read())
        for price in range(len(breakfast)):
          print(breakfast[price][0].center(30) + "|".center(30) +"RM10")
        Food_Item_Menu()
    else:
        pass
    Food_Item_Menu()



#customer login
def login_customer():
    print("\n"+"Login into your account!"+"\n")
    customer_info = open("customerLoginInfo.txt","r")
    login_name = str(input("Please enter your username:"))
    password = str(input("Please enter your password:"))
    login_info = login_name + "," + password + "\n"
    
    for correct_info in customer_info:
        if login_info == correct_info:
            print("Login successful")
            Food_Item_Menu()
    print("Wrong Info, Please try again !!!")
    mainmenu()



#new customer register 
def register_customer():
    customername = open("customerUsernames.txt", "r+")
    print("Register a new account")
    name = input ("Please enter your name:")

    for exist_name in customername:
        if name in exist_name:
            print("The Name already exists")
            register_customer()

    password1 = input(str("Please enter your password: "))
    password2 = input(str("Please comfirm your password : "))
            #!= not equal
    if password1 != password2:
         print("Incorrect password confirmation")
         register_customer()

    else:
        if len (password1) <5:
            print("Your password is too short, please input more than 6 characters.")
            register_customer()
        else:
            print("Your registration is successful!")
            db = open("customerLoginInfo.txt","a")
            db.write(name + "," + password1 + "\n")
            db.close()
            db = open("customerUsernames.txt","a")
            db.write(name + "\n")
            db.close()
            login_customer()



# Order Page. Take Order in Breakfast, Lunch & Dinner
def orderpage():
    select = input ("\n"+"<<<---- Choose Your Meals ---->>>\n\n1: Breakfast Meals \n2: Lunch Meals\n3: Dinner Meals\n4: Give Feedback\n5: Exit\nPlease enter your meals: ")
    if select =="1":
        breakfast()
    elif select =="2":
        lunch()
    elif select == "3":
       dinner()
    elif select =="4":
        feedback()
    elif select == "5":
      mainmenu()
    else:
        pass


# Breakfast
def breakfast():
   print("\n"+">>>---- The Breakfast Menu (RM10) ----<<<")
   a = open ("Breakfast.txt","r") 
   print(a.read())

   orderitem = input("Enter the Food Name: ")
   comfirm_order= input("Confirm order (Yes/No): ")

   if comfirm_order =="Yes":
     
     input("Please enter Bank Name: ")
     input("Please enter your Dedit Card/Credit Car Number:") 
     input("Please enter the PIN Number: ")
     customername =input("Please enter the name of the consignee: ") 
     address =  input("Please enter your pickup address: ")
     phonenumber = input("Please enter consignee phone number: ")

     db = open("customerOrderdetail.txt","a")
     db.write("Payment Successful" +"," + orderitem+" RM10" +"," + customername + "," + address + "," + phonenumber + "\n")
     db.close()
     print("\n"+"Successful adding the order")
     print("Payment:Successful\n\nBreakfast Meal\nOrder:",orderitem + "\nName:",customername +"\nPhone Number:",phonenumber +"\nAddress:",address)
     orderpage()
   elif comfirm_order =="No":
        orderpage()
   else:
         print("Invalid Comment")

                
# Lunch
def lunch():
    print("\n"+">>>---- The Lunch Menu (RM11) ----<<<")
    b = open ("Lunch.txt","r") 
    print(b.read())

    orderitem = input("Enter the Food Name: ")
    comfirm_order= input("Confirm order (Yes/No): ")

    if comfirm_order =="Yes":
     
     input("Please enter Bank Name: ")
     input("Please enter your Dedit Card/Credit Car Number:") 
     input("Please enter the PIN Number: ")
     customername =input("Please enter the name of the consignee: ") 
     address =  input("Please enter your pickup address: ")
     phonenumber = input("Please enter consignee phone number: ")

     db = open("customerOrderdetail.txt","a")
     db.write("Payment Successful" +"," + orderitem+" RM11" +"," + customername + "," + address + "," + phonenumber + "\n")
     db.close()

     print("\n"+"Successful adding the order")
     print("Payment:Successful\n\nLunch Meal\nOrder:",orderitem + "\nName:",customername +"\nPhone Number:",phonenumber +"\nAddress:",address)
     orderpage()
    elif comfirm_order =="No":
        orderpage()
    else:
         print("Invalid Comment")



# Dinner
def dinner():
    print("\n"+">>>---- The Dinner Menu (RM12) ----<<<"+"\n")
    c = open ("Dinner.txt","r") 
    print(c.read())

    orderitem = input("Enter the Food Name: ")
    comfirm_order = input("Confirm order (Yes/No): ")

    if comfirm_order =="Yes":
    
     input("Please enter Bank Name: ")
     input("Please enter your Dedit Card/Credit Car Number:") 
     input("Please enter the PIN Number: ")
     customername =input("Please enter the name of the consignee: ") 
     address =  input("Please enter your pickup address: ")
     phonenumber = input("Please enter consignee phone number: ")

     db = open("customerOrderdetail.txt","a")
     db.write("Payment Successful" +"," + orderitem + " RM12" +"," + customername + "," + address + "," + phonenumber + "\n")
     db.close()

     print("\n"+"Successful adding the order")
     print("Payment:Successful\n\nDinner Meal\nOrder:",orderitem + "\nName:",customername +"\nPhone Number:",phonenumber +"\nAddress:",address)
     orderpage()
    elif comfirm_order =="No":
        orderpage()
    else:
         print("Invalid Comment")


#Feedback
def feedback():
    feedback=[]
    feedback = open ("customer_Feedback.txt","a")
    print("\n"+"Welcome to Feedback Section ^-^\nWe would love to hear your thoughts,suggestions,concerns or problems with anything so we can improve!\n")
    customer_feedback = input("Feedback for AOFS: ")
    feedback.write(customer_feedback+"\n")
    feedback.close()
    print("\n"+"Dear AOFS Customer\nThank You for your Feedback & Response ^.^ \n\nAPU ONLINE FOOD SERVICES (AOFS)")

    mainmenu()
        
#-------------End of AOFS-------------------------            
loginAOFS()






    
