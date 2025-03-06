import mysql.connector;

mydb = mysql.connector.connect(
  host= "127.0.0.1",
  user = "root",
  password= "Ckenney1",
  database = "Final"
  
)

mydb.autocommit = True
mycursor = mydb.cursor()


def start():
    
    # Get all the IDs of Parents to prevent duplicates
    parentID_query = "select Parent_Id from Parent"
    mycursor.execute(parentID_query)

    parentIDs = mycursor.fetchall()
    parentID_values = []

    for i in parentIDs:
       parentID_values.append(i[0])


    # Get all the Names of Parents to prevent duplicates
    parentName_query = "select Parent_Name from Parent"
    mycursor.execute(parentName_query)

    parentNames = mycursor.fetchall()
    parentName_values = []

    for i in parentNames:
       parentName_values.append(i[0])



    # Get all the IDs of BabySitters to prevent duplicates
    sitterID_query = "select BabySitter_Id from BabySitter"
    mycursor.execute(sitterID_query)

    sitterIDs = mycursor.fetchall()
    sitterID_values = []

    for i in sitterIDs:
       sitterID_values.append(i[0])

    # Get all the Names of Sitters to prevent duplicates
    sitterNames_query = "select BabySitter_Name from BabySitter"
    mycursor.execute(sitterNames_query)

    sitterNames = mycursor.fetchall()
    sitterName_values = []

    for i in sitterNames:
       sitterName_values.append(i[0])

    print()
    print("DBMS: LATE-NOTICE BABYSITTER MANAGEMENT SYSTEM")
    print()

    print("Select The Number Corresponding To Your Identity: \n 1. I'm A Babysitter. \n 2. I'm A Parent. \n 3. I'm A New User.")
    print()

    user = input("Enter Your Number Here:")
    print()

    if (user == "1"): 
        babysitter_name = input("Verify Your Name: ")
        babysitter_id = input("Verify Your ID: ")
        print()
        
        sitterProgram(babysitter_name, babysitter_id)


    if (user == "2"):
        parent_name = input("Verify Your Name: ")
        parent_id = input("Verify Your ID: ")
        print()
        
        parentProgram(parent_name, parent_id)

    if (user == "3"):
        print("Select The Number Corresponding To Your Identity: \n 1. I'm A Babysitter. \n 2. I'm A Parent. ")
        print()

        new_user = input("Enter Your Number Here:")
        print()

        if (new_user == "1"):
          babysitter_name = input("What Is Your Name: ")
          print()

          if(sitterName_values.__contains__(babysitter_name)):
             while(sitterName_values.__contains__(babysitter_name)):
                print()
                print("The Name You Entered Is Already Taken. It's Best To Enter Your Full Name.")
                print()
                babysitter_name = input("Re-Enter Your Name: ")
                print()
             

          babysitter_id = input("Create A Permanent, Numerical ID For Future Logins (Maximum Of 11 digits): ")
          print()

       
          if(sitterID_values.__contains__(int(babysitter_id)) or babysitter_id.isnumeric() ==  False or len(babysitter_id) > 10):
             while(sitterID_values.__contains__(int(babysitter_id)) or babysitter_id.isnumeric() ==  False or len(babysitter_id) > 10):
                print()
                print("The ID You Entered Is Either Invalid Or Taken.")
                print()
                babysitter_id = input("Enter Another Permanent, Numerical ID For Future Logins (Maximum Of 11 digits): ")
                print()

                      
          print("Tell Us More About Yourself...")
          print()
          print()

          babysitter_age = input("How Old Are You:")
          print()

          babysitter_email = input("What Is Your Email:")
          print()

          babysitter_sm = input("Enter Your Social Media Handles:")
          print()

          babysitter_pn = input("What Is Your Phone Number:")
          print()

          babysitter_zip = input("What Is Your Zip Code:")
          print()

          if(babysitter_zip.isnumeric() == False):
             while(babysitter_zip.isnumeric() ==  False):
                babysitter_zip = input("Please Enter A Valid Zip Code:")
                print()

          babysitter_years = input("How Many Years Have You Been Babysitting:")
          print()

          babysitter_pay = input("How Much Would You Like To Get Paid By The Hour:")
          print()

          babysitter_available = input("Are You Available To Babysit At The Moment? (Insert '1' if Yes, '0' if No):")
          print()

          if (babysitter_available != "1" and babysitter_available != '0'):
            while(babysitter_available != "1" and  babysitter_available != '0'):
               babysitter_available = input("Please Insert '1' if Yes, '0' if No: ")
              

          print()
          print("Your Profile Is Complete!")
          print()


          sitter_inputs = (babysitter_id, babysitter_name, babysitter_age, babysitter_email, babysitter_sm, babysitter_pn, babysitter_zip, babysitter_years, babysitter_available, babysitter_pay)
          sitter_query = "insert into BabySitter values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)"
          mycursor.execute(sitter_query, sitter_inputs)

          
          new_name = input("Verify Your Name: ")
          new_id = input("Verify Your ID: ")

          print()

          if(new_name != babysitter_name or new_id != babysitter_id):
             while(new_name != babysitter_name or new_id != babysitter_id):
                print("There Was An Error In Your Verification. Please Try Again.")
                print()

                new_name = input("Verify Your Name: ")
                new_id = input("Verify Your ID: ")
                print()
                sitterProgram(new_name, new_id)

          else:
              sitterProgram(new_name, new_id)

        

        if (new_user == "2"):
          parent_name = input("What Is Your Name: ")
          print()

          if(parentName_values.__contains__(parent_name)):
             while(parentName_values.__contains__(parent_name)):
                print()
                print("The Name You Entered Is Already Taken. It's Best To Enter Your Full Name.")
                print()
                parent_name = input("Re-Enter Your Name: ")
                print()

          parent_id = input("Create A Permanent, Numerical ID For Future Logins (Maximum Of 11 Digits): ")
          print()

          if(parentID_values.__contains__(int(parent_id)) or parent_id.isnumeric() ==  False or len(parent_id) > 10):
             while(parentID_values.__contains__(int(parent_id)) or parent_id.isnumeric() ==  False or len(parent_id) > 10):
                print()
                print("The ID You Entered Is Either Invalid Or Taken.")
                print()
                parent_id = input("Enter Another Permanent, Numerical ID For Future Logins (Maximum Of 11 digits): ")
                print()
             
           
          print("Tell Us More About Yourself...")
          print()
          print()


          parent_email = input("What Is Your Email:")
          print()

          parent_sm = input("Enter Your Social Media Handles:")
          print()

          parent_pn = input("What Is Your Phone Number:")
          print()

          parent_zip = input("What Is Your Zip Code:")
          print()

          if(parent_zip.isnumeric() == False):
             while(parent_zip.isnumeric() ==  False):
                parent_zip = input("Please Enter A Valid Zip Code:")
                print()
             

          parent_pay = input("How Much Are You Willing To Pay Per Hour:")
          print()

          parent_inNeed = input("Are You In Need Of Childcare At The Moment? (Insert '1' if Yes, '0' if No):")
          print()

          if (parent_inNeed != "1" and parent_inNeed != '0'):
            while(parent_inNeed != "1" and parent_inNeed != '0'):
              parent_inNeed = input("Please Insert '1' if Yes, '0' if No: ")
        

          print()
          print("Your Profile Is Complete!")
          print()


          newP_inputs = (parent_id, parent_name, parent_email, parent_sm, parent_pn, parent_zip, parent_inNeed, parent_pay)
          newP_query = "insert into Parent values(%s, %s, %s, %s, %s, %s, %s, %s)"
          mycursor.execute(newP_query, newP_inputs)


          print()

          new_name = input("Verify Your Name: ")
          new_id = input("Verify Your ID: ")
          print()

          if(new_name != parent_name or new_id != parent_id):
             while(new_name != parent_name or new_id != parent_id):
                print("There Was An Error In Your Verification. Please Try Again.")
                print()

                new_name = input("Verify Your Name: ")
                new_id = input("Verify Your ID: ")
                print()
                parentProgram(new_name, new_id)

          else:
              
              parentProgram(new_name, new_id)

        if(new_user != "1" and new_user != "2"):
          while(new_user != "1" and new_user != "2"):
            print("Your Input Is Invalid. Please Try Again.")
            start()


    if(user != "1" and user != "2" and user != "3"):
        while(user != "1" and user != "2" and user != "3"):
          print("Your Input Is Invalid. Please Try Again.")
          start()
           






def sitterProgram(name, id):
    
    update_rating = "update BabySitter set Rating = (select AVG(Rating) from Reviews where BabySitter.BabySitter_Name = Reviews.BabySitter_Name)"
    mycursor.execute(update_rating)
    
    id_name = (id, name)
    babySitter_query = "SELECT * FROM BabySitter where BabySitter_Id = %s and BabySitter_Name = %s"


    global sitter_desc, sitter_info
    mycursor.execute(babySitter_query, id_name)
    sitter_desc = mycursor.description

    sitter_values = mycursor.fetchone()
    sitter_info = []


    if str(sitter_values) == 'None':
      print("It Appears Your Credentials Aren't In The Database. Try Again.")
      start()
    
    else:

       # sitter_values is a tuple which can't be updated. It's values are stored in a new array
      i = 0
      while i < len(sitter_values):
        sitter_info.append(sitter_values[i])
        i = i + 1


      print("Welcome " + name + "!")
      print()

      print("Enter The Number Corresponding To Your Selected Service: \n 1. Update/Display Personal Information & Availability \n 2. Find Current, Local Opportunities \n 3. See Personal Reviews")
      print()

      selected = input("Enter The Number Here:")
      print()

      if(selected == "1"):
        sitterPersonal()

      if(selected == "2"):
        findParents()

      if(selected == "3"):
        myReviews()

      if (selected != "1" and selected != "2" and selected != "3"):
        while(selected != "1" and selected != "2" and selected != "3"):
          print()
          selected = input ("Your Input Is Invalid. Please Enter A Valid Number Option: ")
          print()

          if(selected == "1"):
            sitterPersonal()

          if(selected == "2"):
            findParents()

          if(selected == "3"):
            myReviews()

def sitterPersonal():
     
    i = 2

    print("Your Displayed Name: " + sitter_info[1] + " | Your Current ID: " + str(sitter_info[0]))
    print()

    # Display of current info - parent_desc contains column names, parent_info contains column values
    while i < len(sitter_info) - 1:
      for x in range(2, len(sitter_desc) - 1):
          print(str(i - 1) + ". " + str(sitter_desc[x][0]) + ":" + str(sitter_info[i]))
          i = i + 1

    print("9. Delete Profile")
    print()


    selected = input("Enter The Number Corresponding To Your Desired Profile Change: ")
    print()



    if(selected == "1"):
    

      newAge = input("Enter Your New Age: ")
      print()

      info = (newAge, sitter_info[0], sitter_info[1])
      newID_query = "update BabySitter set Age = %s where BabySitter_Id = %s and BabySitter_Name = %s"
      mycursor.execute(newID_query, info)

      
      print()
      print("Your Age Has Been Updated To " + newAge)
      print()

      sitter_info[2] = newAge
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        sitterPersonal()

      elif (continue_option == 'N'):
        sitterProgram(sitter_info[1], sitter_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
              sitterPersonal()

            elif (continue_option == 'N'):
                
              sitterProgram(sitter_info[1], sitter_info[0])


    if(selected == "2"):
    

      newEmail = input("Enter Your New Email: ")
      print()

      info = (newEmail, sitter_info[0], sitter_info[1])
      newID_query = "update BabySitter set Email = %s where BabySitter_Id = %s and BabySitter_Name = %s"
      mycursor.execute(newID_query, info)

      
      print()
      print("Your Email Has Been Updated To " + newEmail)
      print()

      sitter_info[3] = newEmail
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        sitterPersonal()

      elif (continue_option == 'N'):
        sitterProgram(sitter_info[1], sitter_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
              sitterPersonal()

            elif (continue_option == 'N'):
                
              sitterProgram(sitter_info[1], sitter_info[0])


    if(selected == "3"):
    

      newSm = input("Enter Your New Social Media Handles: ")
      print()

      info = (newSm, sitter_info[0], sitter_info[1])
      newID_query = "update BabySitter set Social_Media = %s where BabySitter_Id = %s and BabySitter_Name = %s"
      mycursor.execute(newID_query, info)

      
      print()
      print("Your Social Media Handles Have Been Updated To " + newSm)
      print()

      sitter_info[4] = newSm
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        sitterPersonal()

      elif (continue_option == 'N'):
        sitterProgram(sitter_info[1], sitter_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
              sitterPersonal()

            elif (continue_option == 'N'):
                
              sitterProgram(sitter_info[1], sitter_info[0])


    if(selected == "4"):
    

      newPN = input("Enter Your New Phone Number: ")
      print()

      info = (newPN, sitter_info[0], sitter_info[1])
      newID_query = "update BabySitter set Phone_Number = %s where BabySitter_Id = %s and BabySitter_Name = %s"
      mycursor.execute(newID_query, info)

      
      print()
      print("Your Phone Number Has Been Updated To " + newPN)
      print()

      sitter_info[5] = newPN
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        sitterPersonal()

      elif (continue_option == 'N'):
        sitterProgram(sitter_info[1], sitter_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
              sitterPersonal()

            elif (continue_option == 'N'):
                
              sitterProgram(sitter_info[1], sitter_info[0])


    if(selected == "5"):
        newZC = input("Enter Your New Zip Code: ")
        print()

        if(newZC.isnumeric() == False):
              while(newZC.isnumeric() ==  False):
                  newZC = input("Please Enter A Valid Zip Code:")
                  print()

        id_info = (newZC, sitter_info[0], sitter_info[1])
        newID_query = "update BabySitter set Zip_Code = %s where BabySitter_Id = %s and BabySitter_Name = %s"
        mycursor.execute(newID_query, id_info)

        
        print()
        print("Your Zip Code Has Been Updated To " + newZC)
        print()

        sitter_info[6] = newZC
        


        print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
        print()

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()


        if (continue_option == 'Y'):
          sitterPersonal()

        elif (continue_option == 'N'):
          sitterProgram(sitter_info[1], sitter_info[0])
          
        else:
            
            while(continue_option != 'Y' or continue_option != 'N'):

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()
              
              if (continue_option == 'Y'):
                  
                  sitterPersonal()

              elif (continue_option == 'N'):
                  
                  sitterProgram(sitter_info[1], sitter_info[0])


    if(selected == "6"):
    

      newYears = input("Enter Your Updated Years Of Experience: ")
      print()

      info = (newYears, sitter_info[0], sitter_info[1])
      newID_query = "update BabySitter set Experience_Years = %s where BabySitter_Id = %s and BabySitter_Name = %s"
      mycursor.execute(newID_query, info)

      
      print()
      print("Your Years Of Experience Has Been Updated To " + newYears)
      print()

      sitter_info[7] = newYears
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        sitterPersonal()

      elif (continue_option == 'N'):
        sitterProgram(sitter_info[1], sitter_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
              sitterPersonal()

            elif (continue_option == 'N'):
                
              sitterProgram(sitter_info[1], sitter_info[0])

    elif(selected == "7"):
      
      print("Are You Currently Available To Babysit?")
      print()

      newStatus = input("Insert '1' if yes, '0' if no: ")
      print()

      if newStatus == "1":

        info = (newStatus, sitter_info[0], sitter_info[1])
        newID_query = "update BabySitter set Current_Availability = %s where BabySitter_Id = %s and BabySitter_Name = %s"
        mycursor.execute(newID_query, info)

        
        print()
        print("Your Current Availability Status Has Been Updated. Parents Should Be Contacting You Shortly!")
        print()

        sitter_info[8] = newStatus
        


        print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
        print()

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()


        if (continue_option == 'Y'):
          sitterPersonal()

        elif (continue_option == 'N'):
          sitterProgram(sitter_info[1], sitter_info[0])
          
        else:
            
            while(continue_option != 'Y' or continue_option != 'N'):

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()
              
              if (continue_option == 'Y'):
                  
                  sitterPersonal()

              elif (continue_option == 'N'):
                  
                  sitterProgram(sitter_info[1], sitter_info[0])


      elif newStatus == "0":

        info = (newStatus, sitter_info[0], sitter_info[1])
        newID_query = "update BabySitter set Current_Availability = %s where BabySitter_Id = %s and BabySitter_Name = %s"
        mycursor.execute(newID_query, info)
         
        print()
        print("Your Current Availability Status Has Been Updated. Set Your Status To '1' Whenever You Are Ready To Work.")
        print()

        sitter_info[8] = newStatus
        


        print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
        print()

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()


        if (continue_option == 'Y'):
          sitterPersonal()

        elif (continue_option == 'N'):
          sitterProgram(sitter_info[1], sitter_info[0])
          
        else:
            
            while(continue_option != 'Y' or continue_option != 'N'):

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()
              
              if (continue_option == 'Y'):
                  
                  sitterPersonal()

              elif (continue_option == 'N'):
                  
                  sitterProgram(sitter_info[1], sitter_info[0])

      else:
         
          while(newStatus != '1' or newStatus != '0'):
            
            print("Please Insert One Of The Two Number Options To Update Your Current Availability Status.")
            print()

            newStatus = input("Insert '1' if Yes, '0' if No: ")
            print()

            if newStatus == "1":

              info = (newStatus, sitter_info[0], sitter_info[1])
              newID_query = "update BabySitter set Current_Availability = %s where BabySitter_Id = %s and BabySitter_Name = %s"
              mycursor.execute(newID_query, info)

              
              print()
              print("Your Current Availability Status Has Been Updated. Parents Should Be Contacting You Shortly!")
              print()

              sitter_info[8] = newStatus
              


              print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
              print()

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()


              if (continue_option == 'Y'):
                sitterPersonal()

              elif (continue_option == 'N'):
                sitterProgram(sitter_info[1], sitter_info[0])
                
              else:
                  
                  while(continue_option != 'Y' or continue_option != 'N'):

                    continue_option = input("Insert 'Y' or 'N':")
                    print()
                    print()
                    
                    if (continue_option == 'Y'):
                        
                        sitterPersonal()

                    elif (continue_option == 'N'):
                        
                        sitterProgram(sitter_info[1], sitter_info[0])


            elif newStatus == "0":

              info = (newStatus, sitter_info[0], sitter_info[1])
              newID_query = "update BabySitter set Current_Availability = %s where BabySitter_Id = %s and BabySitter_Name = %s"
              mycursor.execute(newID_query, info)
              
              print()
              print("Your Current Availability Status Has Been Updated. Set Your Status To '1' Whenever You Are Ready To Work.")
              print()

              sitter_info[8] = newStatus
              


              print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
              print()

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()


              if (continue_option == 'Y'):
                sitterPersonal()

              elif (continue_option == 'N'):
                sitterProgram(sitter_info[1], sitter_info[0])
                
              else:
                  
                  while(continue_option != 'Y' or continue_option != 'N'):

                    continue_option = input("Insert 'Y' or 'N':")
                    print()
                    print()
                    
                    if (continue_option == 'Y'):
                        
                        sitterPersonal()

                    elif (continue_option == 'N'):
                        
                        sitterProgram(sitter_info[1], sitter_info[0])
          
    if(selected == "8"):

      newPay = input("Enter The Updated Hourly Pay You Wish To Receive: ")
      print()

      info = (newPay, sitter_info[0], sitter_info[1])
      newID_query = "update BabySitter set Suggested_Hourly_Pay = %s where BabySitter_Id = %s and BabySitter_Name = %s"
      mycursor.execute(newID_query, info)

      
      print()
      print("Your Hourly Pay Has Been Updated To " + newPay)
      print()

      sitter_info[9] = newPay
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        sitterPersonal()

      elif (continue_option == 'N'):
        sitterProgram(sitter_info[1], sitter_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
              sitterPersonal()

            elif (continue_option == 'N'):
                
              sitterProgram(sitter_info[1], sitter_info[0])

        
    elif(selected == "9"):
      print("Are You Sure You Would Like To Delete Your Profile? ")
      print()

      option = input("If So Insert 'Y', If Not Enter 'N':")
      print()

      if (option == 'Y'):
        
        id = (sitter_info[0], )
        name = (sitter_info[1], )

        reviews_query = "delete from Reviews where BabySitter_Name = %s"
        mycursor.execute(reviews_query, name)

        delete_query = "delete from BabySitter where BabySitter_Id = %s"
        mycursor.execute(delete_query, id)

        print("Your Profile Has Been Deleted. You Have Been Logged Out.")
        print()
        print()
        start()
    
      elif (option == 'N'):
          print("Ok, Delete Your Profile At Your Convenience")
          print()
          sitterPersonal()

      else:
         while(option != 'Y' or option != 'N'):
            option = input("Please Insert 'Y', Or 'N':")
            print()
            print()
            
            if (option == 'Y'):
                  
              id = (sitter_info[0], )
              name = (sitter_info[1], )

              reviews_query = "delete from Reviews where BabySitter_Name = %s"
              mycursor.execute(reviews_query, name)

              delete_query = "delete from BabySitter where BabySitter_Id = %s"
              mycursor.execute(delete_query, id)

              print("Your Profile Has Been Deleted. You Have Been Logged Out.")
              print()
              print()
              start()
                

            elif (option == 'N'):
              print("Ok, Delete Your Profile At Your Convenience")
              print()
              sitterPersonal()

    
    if (selected != "1" and selected != "2" and selected != "3" and selected != "4" and selected != "5" and selected != "6" and selected != "7" and selected != "8" and selected != "9"):
       print()
       print("Your Input Is Invalid. Please Try Again") 
       print()
       sitterPersonal()
      # sitterProgram(sitter_info[1], sitter_info[0])


def findParents():
   
    parent_input = (sitter_info[6], )

    parent_query = "Select Parent_Name, Hourly_Pay from Parent where Zip_Code = %s and In_Need = 1"
    mycursor.execute(parent_query, parent_input)

    parent_values = mycursor.fetchall()
    this_info = []
    parents = []

    x = 0

    # parent_values is a list of tuple which can't be updated. It's values are stored in a new array
    while x < len(parent_values):
      this_info.append(parent_values[x])
      x = x + 1

    for x in this_info:
      parents.append(x[0])

    z = 1
 

    for i in this_info:
      print(str(z) + ". " + i[0])
      print()

      print("Hourly Pay: " + i[1])
      print()
      print("Children: ")
      print()


      query_value = (i[0], )

      child_query = "Select Child_Name, Allergies, Diseases, Medications, Disabilities, Intrests from Child_Needs where Parent_Name = %s"
      mycursor.execute(child_query, query_value)

      child_values = mycursor.fetchall()

      for n in child_values:
         print("  " + n[0] + ":")

         print("   " + "Allergies: " + n[1])
         print("   " + "Diseases: " + n[2])
         print("   " + "Medications: " + n[3])
         print("   " + "Disabilities: " + n[4])
         print("   " + "Interests: " + n[5])
         print()


      print()
      z = z + 1
      

    if (len(this_info) == 0):
        print()
        print("There Are No Local, Parents In Need Of Childcare At The Moment. Returnng To The Main Menu.")
        print()
        sitterProgram(sitter_info[1], sitter_info[0])

    else:

        print()
        print("Enter The Number Corresponding To The Parent You Wish To Contact/View.")
        print()

        selected = input("Enter The Number Here: ")
        print()


        for i in range(len(parents)):
          
          if(selected == str(i + 1)):
            
            contact_inputs = (parents[i], )
            contact_query = "Select Email, Social_Media, Phone_Number from Parent where Parent_Name = %s"
            mycursor.execute(contact_query, contact_inputs)

            contact_desc = mycursor.description
            contact_values = mycursor.fetchone()
            contact_info = []



            x = 0
            while (x < len(contact_values)):
                contact_info.append(contact_values[x])
                x = x + 1

            print(parents[i] + "'s Contact Information:")
            print()

            for o in range(len(contact_values)):
                print(str(contact_desc[o][0]) + ": " + contact_values[o])

            print()


          if (selected.isnumeric() == False):
            print()
            print("Your Input Is Invalid. Please Try Again.")
            print()
            findParents()

          elif(selected.isnumeric() == True and (int(selected) > len(parents) or int(selected) < 0)):
            print()
            print("Your Input Is Invalid. Please Try Again.")
            print()
            findParents()

    print()
    print("Would You Like To View More Parents (Y) Or Return To The Menu (N)?")
    print()
    

    continue_option = input("Insert 'Y' or 'N':")
    print()
    print()


    if (continue_option == 'Y'):
      findParents()

    elif (continue_option == 'N'):
      sitterProgram(sitter_info[1], sitter_info[0])
      
    else:
        
        while(continue_option != 'Y' or continue_option != 'N'):

          continue_option = input("Insert 'Y' or 'N':")
          print()
          print()
          
          if (continue_option == 'Y'):
              
              findParents()

          elif (continue_option == 'N'):
              
              sitterProgram(sitter_info[1], sitter_info[0])


def myReviews():
   
  name = (sitter_info[1], )
  review_query = "Select Parent_Name, Review, Rating from Reviews where BabySitter_Name = %s"     
  mycursor.execute(review_query, name) 
    
  reviews = mycursor.fetchall()

  if(str(reviews) == "[]"):
     print("You Have Yet To Recieve A Review From A Parent. Returning To The Main Menu.")
     print()
     sitterProgram(sitter_info[1], sitter_info[0])

  else:
    print("Below Are The Reviews You Have Recieved From Your Previous Opportunities.")
    print()
    for i in reviews:

      print("Parent: " + i[0])
      print("Review: " + i[1])
      print("Rating: " + str(i[2]))
      print()
  

def parentProgram(name, id):
    
    update_rating = "update BabySitter set Rating = (select AVG(Rating) from Reviews where BabySitter.BabySitter_Name = Reviews.BabySitter_Name)"
    mycursor.execute(update_rating)

    id_name = (id, name)
    parent_query = "SELECT * FROM Parent where Parent_Id = %s and Parent_Name = %s"


    global parent_desc, parent_info
    mycursor.execute(parent_query, id_name)
    parent_desc = mycursor.description

   
    parent_values = mycursor.fetchone()
    parent_info = []


    if str(parent_values) == 'None':
      print("It Appears Your Credentials Aren't In The Database. Try Again.")
      start()
    
    else:

      # parent_values is a tuple which can't be updated. It's values are stored in a new array
      i = 0
      while i < len(parent_values):
        parent_info.append(parent_values[i])
        i = i + 1

      
      print("Welcome " + name + "!")
      print()

      print("Enter The Number Corresponding To Your Selected Service: \n \n 1. Update/Display Personal Information & Childcare Status \n 2. Add, Delete or Update Children \n 3. View All The Available BabySitters in Your Area \n 4. Access The Ratings & Reviews Of Available BabySitters \n 5. Write a Review")
      print()

      selected = input("Enter The Number Here:")
      print()

      if(selected == "1"):
        parentPersonal()

      if(selected == "2"):
        updateChildren()

      if(selected == "3"):
        findBabySitters()
         
      if(selected == "4"):
        displayReviews()

      if(selected == "5"):
        writeReview()

      if (selected != "1" and selected != "2" and selected != "3" and selected != "4" and selected != "5"):
        while(selected != "1" and selected != "2" and selected != "3" and selected != "4" and selected != "5"):
          print()
          selected = input ("Your Input Is Invalid. Please Enter A Valid Number Option: ")
          print()

          if(selected == "1"):
            parentPersonal()

          if(selected == "2"):
            updateChildren()

          if(selected == "3"):
            findBabySitters()
            
          if(selected == "4"):
            displayReviews()

          if(selected == "5"):
            writeReview()



  
def parentPersonal():
    
    i = 2

    print("Your Displayed Name: " + parent_info[1] + " | Your Current ID: " + str(parent_info[0]))
    print()

    # Display of current info - parent_desc contains column names, parent_info contains column values
    while i < len(parent_info):
      for x in range(2, len(parent_desc)):
          print(str(i - 1) + ". " + str(parent_desc[x][0]) + ":" + str(parent_info[i]))
          i = i + 1

    print("7. Delete Profile")
    print()

    selected = input("Enter The Number Corresponding To Your Desired Profile Change: ")
    print()



    if(selected == "1"):
    

      newEmail = input("Enter Your New Email: ")
      print()

      id_info = (newEmail, parent_info[0], parent_info[1])
      newID_query = "update Parent set Email = %s where Parent_Id = %s and Parent_Name = %s"
      mycursor.execute(newID_query, id_info)

      
      print()
      print("Your Email Has Been Updated To " + newEmail)
      print()

      parent_info[2] = newEmail
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        parentPersonal()

      elif (continue_option == 'N'):
        parentProgram(parent_info[1], parent_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
                parentPersonal()

            elif (continue_option == 'N'):
                
                parentProgram(parent_info[1], parent_info[0])


    elif (selected == "2"):

      newSm = input("Enter Your Updated Social Media Handles: ")
      print()

      id_info = (newSm, parent_info[0], parent_info[1])
      newID_query = "update Parent set Social_Media = %s where Parent_Id = %s and Parent_Name = %s"
      mycursor.execute(newID_query, id_info)

      
      print()
      print("Your Social Media Handles Have Been Updated To " + newSm)
      print()

      parent_info[3] = newSm
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()

      if (continue_option == 'Y'):
        parentPersonal()

      elif (continue_option == 'N'):
        parentProgram(parent_info[1], parent_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
                parentPersonal()

            elif (continue_option == 'N'):
                
                parentProgram(parent_info[1], parent_info[0])


    elif (selected == "3"):

      newPN = input("Enter Your New Phone Number: ")
      print()

      id_info = (newPN, parent_info[0], parent_info[1])
      newID_query = "update Parent set Phone_Number = %s where Parent_Id = %s and Parent_Name = %s"
      mycursor.execute(newID_query, id_info)

      
      print()
      print("Your Phone Number Has Been Updated To " + newPN)
      print()

      parent_info[4] = newPN
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        parentPersonal()

      elif (continue_option == 'N'):
        parentProgram(parent_info[1], parent_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
                parentPersonal()

            elif (continue_option == 'N'):
                
                parentProgram(parent_info[1], parent_info[0])


    elif(selected == "4"):

      newZC = input("Enter Your New Zip Code: ")
      print()

      if(newZC.isnumeric() == False):
             while(newZC.isnumeric() ==  False):
                newZC = input("Please Enter A Valid Zip Code:")
                print()

      id_info = (newZC, parent_info[0], parent_info[1])
      newID_query = "update Parent set Zip_Code = %s where Parent_Id = %s and Parent_Name = %s"
      mycursor.execute(newID_query, id_info)

      
      print()
      print("Your Zip Code Has Been Updated To " + newZC)
      print()

      parent_info[5] = newZC
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        parentPersonal()

      elif (continue_option == 'N'):
        parentProgram(parent_info[1], parent_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
                parentPersonal()

            elif (continue_option == 'N'):
                
                parentProgram(parent_info[1], parent_info[0])


    elif(selected == "5"):
      
      print("Are You Currently In Need Of A Babysitter?")
      print()

      newStatus = input("Insert '1' if yes, '0' if no: ")
      print()

      if newStatus == "1":

        id_info = (newStatus, parent_info[0], parent_info[1])
        newID_query = "update Parent set In_Need = %s where Parent_Id = %s and Parent_Name = %s"
        mycursor.execute(newID_query, id_info)

        
        print()
        print("Your Childcare Status Has Been Updated. Babysitters Should Be Contacting You Shortly!")
        print()

        parent_info[6] = newStatus
        


        print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
        print()

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()


        if (continue_option == 'Y'):
          parentPersonal()

        elif (continue_option == 'N'):
          parentProgram(parent_info[1], parent_info[0])
          
        else:
            
            while(continue_option != 'Y' or continue_option != 'N'):

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()
              
              if (continue_option == 'Y'):
                  
                  parentPersonal()

              elif (continue_option == 'N'):
                  
                  parentProgram(parent_info[1], parent_info[0])


      elif newStatus == "0":

        id_info = (newStatus, parent_info[0], parent_info[1])
        newID_query = "update Parent set In_Need = %s where Parent_Id = %s and Parent_Name = %s"
        mycursor.execute(newID_query, id_info)
         
        print()
        print("Your Childcare Status Has Been Updated. Set Your Status To '1' Whenever You Are In Need Of Assistance.")
        print()

        parent_info[6] = newStatus
        


        print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
        print()

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()


        if (continue_option == 'Y'):
          parentPersonal()

        elif (continue_option == 'N'):
          parentProgram(parent_info[1], parent_info[0])
          
        else:
            
            while(continue_option != 'Y' or continue_option != 'N'):

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()
              
              if (continue_option == 'Y'):
                  
                  parentPersonal()

              elif (continue_option == 'N'):
                  
                  parentProgram(parent_info[1], parent_info[0])

      else:
         
          while(newStatus != '1' or newStatus != '0'):
            
            print("Please Insert One Of The Two Number Options To Update Your Childcare Status.")
            print()

            newStatus = input("Insert '1' if Yes, '0' if No: ")
            print()

            if newStatus == "1":

              id_info = (newStatus, parent_info[0], parent_info[1])
              newID_query = "update Parent set In_Need = %s where Parent_Id = %s and Parent_Name = %s"
              mycursor.execute(newID_query, id_info)

              
              print()
              print("Your Childcare Status Has Been Updated. Babysitters Should Be Contacting You Shortly!")
              print()

              parent_info[6] = newStatus
              


              print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
              print()

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()


              if (continue_option == 'Y'):
                parentPersonal()

              elif (continue_option == 'N'):
                parentProgram(parent_info[1], parent_info[0])
                
              else:
                  
                  while(continue_option != 'Y' or continue_option != 'N'):

                    continue_option = input("Insert 'Y' or 'N':")
                    print()
                    print()
                    
                    if (continue_option == 'Y'):
                        
                        parentPersonal()

                    elif (continue_option == 'N'):
                        
                        parentProgram(parent_info[1], parent_info[0])


            elif newStatus == "0":

              id_info = (newStatus, parent_info[0], parent_info[1])
              newID_query = "update Parent set In_Need = %s where Parent_Id = %s and Parent_Name = %s"
              mycursor.execute(newID_query, id_info)
              
              print()
              print("Your Childcare Status Has Been Updated. Set Your Status To '1' Whenever You Are In Need Of Assistance.")
              print()

              parent_info[6] = newStatus
              


              print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
              print()

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()


              if (continue_option == 'Y'):
                parentPersonal()

              elif (continue_option == 'N'):
                parentProgram(parent_info[1], parent_info[0])
                
              else:
                  
                  while(continue_option != 'Y' or continue_option != 'N'):

                    continue_option = input("Insert 'Y' or 'N':")
                    print()
                    print()
                    
                    if (continue_option == 'Y'):
                        
                        parentPersonal()

                    elif (continue_option == 'N'):
                        
                        parentProgram(parent_info[1], parent_info[0])
          


    elif(selected == "6"):

      newPay = input("What Is The New Amount You Are Willing To Pay Your Babysitters Per Hour: ")
      print()

      id_info = (newPay, parent_info[0], parent_info[1])
      newID_query = "update Parent set Hourly_Pay = %s where Parent_Id = %s and Parent_Name = %s"
      mycursor.execute(newID_query, id_info)

      
      print()
      print("Your Payment Status Has Been Updated To " + newPay + ".") 
      print()

      parent_info[7] = newPay
      


      print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        parentPersonal()

      elif (continue_option == 'N'):
        parentProgram(parent_info[1], parent_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
                parentPersonal()

            elif (continue_option == 'N'):
                
                parentProgram(parent_info[1], parent_info[0])
    
    elif(selected == "7"):
      print("Are You Sure You Would Like To Delete Your Profile? ")
      print()

      option = input("If So Insert 'Y', If Not Enter 'N':")
      print()

      if (option == 'Y'):
        
        id = (parent_info[0], )

        reviews_query = "delete from Reviews where Parent_Id = %s"
        mycursor.execute(reviews_query, id)

        needs_query = "delete from Child_Needs where Parent_Id = %s"
        mycursor.execute(needs_query, id)

        child_query = "delete from Child where Parent_Id = %s"
        mycursor.execute(child_query, id)

        delete_query = "delete from Parent where Parent_Id = %s"
        mycursor.execute(delete_query, id)

        print("Your Profile Has Been Deleted. You Have Been Logged Out.")
        print()
        print()
        start()
    
      elif (option == 'N'):
          print("Ok, Delete Your Profile At Your Convenience")
          print()
          parentPersonal()

      else:
         while(option != 'Y' or option != 'N'):
            option = input("Please Insert 'Y', Or 'N':")
            print()
            print()
            
            if (option == 'Y'):
                
                id = (parent_info[0], )

                reviews_query = "delete from Reviews where Parent_Id = %s"
                mycursor.execute(reviews_query, id)

                needs_query = "delete from Child_Needs where Parent_Id = %s"
                mycursor.execute(needs_query, id)

                child_query = "delete from Child where Parent_Id = %s"
                mycursor.execute(child_query, id)

                delete_query = "delete from Parent where Parent_Id = %s"
                mycursor.execute(delete_query, id)

                print("Your Profile Has Been Deleted. You Have Been Logged Out.")
                print()
                print()
                start()
            

            elif (option == 'N'):
                print("Ok, Delete Your Profile At Your Convenience")
                print()
                parentPersonal()


    if (selected != "1" and selected != "2" and selected != "3" and selected != "4" and selected != "5" and selected != "6" and selected != "7"):
       print()
       print("Your Input Is Invalid. Please Try Again") 
       print()
       parentProgram(parent_info[1], parent_info[0])

def updateChildren():


    theParent = (parent_info[1], )
    allChildren_query = "Select * from Child where Parent_Name = %s"


    global child_desc, child_info
    mycursor.execute(allChildren_query, theParent)
    child_desc = mycursor.description

  
    child_values = mycursor.fetchall()
    child_info = []


    # child_values is a tuple which can't be updated. It's values are stored in a new array
    x = 0
  
    while x < len(child_values):
      child_info.append(child_values[x])
      x = x + 1



    
    print("Enter The Number Corresponding To The Status Of Your Children: \n \n 1. Add Children \n 2. Delete Children \n 3. Update Child Information ")
    print()

    selected = input("Enter The Number Here:")
    print()
    print()


    if(selected == "1"):
      

      child_name = input("Enter The Name Of Your Child: ")
      print()

      child_age = input("How Old Is Your Child: ")
      print()

      child_gender = input("What Is Your Child's Gender: ")
      print()

      child_BO = input("How Is This Child Related To Their Siblings (Youngest, Oldest, Single, etc): ")
      print()

      print()
      print("Your Child Has Been Added. You Can Now Specify " + child_name + "'s Needs.")
      print()


      child_inputs = (parent_info[0], parent_info[1], child_name, child_age, child_gender, child_BO)
      child_query = "insert into Child values(%s, %s, %s, %s, %s, %s)"
      mycursor.execute(child_query, child_inputs)

      needs_inputs = (parent_info[0], parent_info[1], child_name)
      needs_query = "insert into Child_Needs values(%s, %s, %s, 'None', 'None', 'None', 'None', 'None')"
      mycursor.execute(needs_query, needs_inputs)

      print()
      print("Would You Like To Update Additional Child Information (Y) Or Return To The Menu (N)?")
      print()

      continue_option = input("Insert 'Y' or 'N':")
      print()
      print()


      if (continue_option == 'Y'):
        updateChildren()

      elif (continue_option == 'N'):
        parentProgram(parent_info[1], parent_info[0])
        
      else:
          
          while(continue_option != 'Y' or continue_option != 'N'):

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()
            
            if (continue_option == 'Y'):
                
                updateChildren()

            elif (continue_option == 'N'):
                
                parentProgram(parent_info[1], parent_info[0])


    elif(selected == "2"):
       
      i = 1

      if len(child_info) == 0:
        print("You Haven't Entered Any Children Into The Database. Therefore, None Can Be Deleted.")
        print()
        print()

        print("Would You Like To Add A Child (Y) Or Return To The Menu (N)?")
        print()

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()


        if (continue_option == 'Y'):
          updateChildren()

        elif (continue_option == 'N'):
          parentProgram(parent_info[1], parent_info[0])
          
        else:
            
            while(continue_option != 'Y' or continue_option != 'N'):

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()
              
              if (continue_option == 'Y'):
                  
                  updateChildren()

              elif (continue_option == 'N'):
                  
                  parentProgram(parent_info[1], parent_info[0])
      
      else:
          
          print("Enter The Number Corresponding To The Child You Wish To Remove.")
          print()

          y = 1

          # Stores the names of the children to match with input
          remove_array = []

          # child_info is an array of tuples conatining the information of each child
          for x in child_info:
              print(str(y) + ". " + str(x[2]))
              remove_array.append(str(x[2]))
              y = y + 1

          print()
          removed = input("Enter The Number Here: ")
        
          for i in range(len(remove_array)):
              if removed == str(i + 1):

                rmNeeds_inputs = (parent_info[0], remove_array[i])
                rmNeeds_query = "delete from Child_Needs where Parent_Id = %s and Child_Name = %s"
                mycursor.execute(rmNeeds_query, rmNeeds_inputs)
                
                remove_inputs = (parent_info[0], remove_array[i])
                remove_query = "delete from Child where Parent_Id = %s and Child_Name = %s"
                mycursor.execute(remove_query, remove_inputs)

                print()
                print(remove_array[i] + " Is No Longer Displayed As One Of Your Children. " +  remove_array[i] + "'s Needs Have Been Removed As Well.")
                print()
          

          print()
          print("Would You Like To Update Additional Child Information (Y) Or Return To The Menu (N)?")
          print()

          continue_option = input("Insert 'Y' or 'N':")
          print()
          print()


          if (continue_option == 'Y'):
            updateChildren()

          elif (continue_option == 'N'):
            parentProgram(parent_info[1], parent_info[0])
            
          else:
              
              while(continue_option != 'Y' or continue_option != 'N'):

                continue_option = input("Insert 'Y' or 'N':")
                print()
                print()
                
                if (continue_option == 'Y'):
                    
                    updateChildren()

                elif (continue_option == 'N'):
                    
                    parentProgram(parent_info[1], parent_info[0])


    elif(selected == "3"):
      
      if len(child_info) == 0:
        print("You Haven't Entered Any Children Into The Database. Therefore, None Can Be Updated.")
        print()
        print()

        print("Would You Like To Add A Child (Y) Or Return To The Menu (N)?")
        print()

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()


        if (continue_option == 'Y'):
          updateChildren()

        elif (continue_option == 'N'):
          parentProgram(parent_info[1], parent_info[0])
          
        else:
            
            while(continue_option != 'Y' or continue_option != 'N'):

              continue_option = input("Insert 'Y' or 'N':")
              print()
              print()
              
              if (continue_option == 'Y'):
                  
                  updateChildren()

              elif (continue_option == 'N'):
                  
                  parentProgram(parent_info[1], parent_info[0])
      else:
    
        print("Enter The Number Corresponding To Your Service: \n \n 1. Update A Child's Age \n 2. Update A Child Needs")
        print()

        update_select = input("Enter The Number Here:")
        print()
        print()


        if update_select == "1":
          
          print("Enter The Number Corresponding To The Child You Wish To Update.")
          print()

          y = 0

          # Stores the names of the children to match with input
          update_array = []


          # child_info is an array of tuples conatining the information of each child
          while(y < len(child_info)):
            for x in child_info:
                print(str(y + 1) + ". " + str(x[2]))
                update_array.append(str(x[2]))
                y = y + 1


          print()
          updated = input("Enter The Number Here: ")
          print()


          for i in range (len(update_array)):
              if updated == str(i + 1):
                
                selected_inputs = (parent_info[0], update_array[i])
                child_query = "Select * from Child where Parent_Id = %s and Child_Name = %s"
                mycursor.execute(child_query, selected_inputs)


                
                oneChild_values = mycursor.fetchone()
                oneChild_info = []


                z = 0
              
                # needs_values is a tuple which can't be updated. It's values are stored in a new array
                while z < len(oneChild_values):
                  oneChild_info.append(oneChild_values[z])
                  z = z + 1
                
                newAge = input("Enter " + update_array[i] + "'s" + " Updated Age: ")
                print()

                id_info = (newAge, parent_info[0], update_array[i])
                newID_query = "update Child set Age = %s where Parent_Id = %s and Child_Name = %s"
                mycursor.execute(newID_query, id_info)

              
                print()
                print(update_array[i] + "'s" + " Age Is Now Set To " + newAge)
                print()

                oneChild_info[3] = newAge


                print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
                print()

                continue_option = input("Insert 'Y' or 'N':")
                print()
                print()


                if (continue_option == 'Y'):
                  updateChildren()

                elif (continue_option == 'N'):
                  parentProgram(parent_info[1], parent_info[0])
                
                else:
                      
                      while(continue_option != 'Y' or continue_option != 'N'):

                        continue_option = input("Insert 'Y' or 'N':")
                        print()
                        print()
                        
                        if (continue_option == 'Y'):
                            
                            updateChildren()

                        elif (continue_option == 'N'):
                            
                            parentProgram(parent_info[1], parent_info[0])


              if (updated.isnumeric() == False):
                print()
                print("Your Input Is Invalid. Please Try Again.")
                print()
                updateChildren()
                break

              elif(updated.isnumeric() == True and (int(updated) > len(update_array) or int(updated) < 0)):
                print()
                print("Your Input Is Invalid. Please Try Again.")
                print()
                updateChildren()
                break
     

        

        elif update_select == "2":

          print("Enter The Number Corresponding To The Child You Wish To Update.")
          print()

          y = 0

          # Stores the names of the children to match with input
          update_array = []


          # child_info is an array of tuples conatining the information of each child
          while(y < len(child_info)):
            for x in child_info:
                print(str(y + 1) + ". " + str(x[2]))
                update_array.append(str(x[2]))
                y = y + 1


          print()
          updated = input("Enter The Number Here: ")
          print()



          global needs_desc, needs_info
          for i in range (len(update_array)):
              if updated == str(i + 1):
                
                selected_inputs = (parent_info[0], update_array[i])
                needs_query = "Select * from Child_Needs where Parent_Id = %s and Child_Name = %s"
                mycursor.execute(needs_query, selected_inputs)

                needs_desc = mycursor.description

              
                needs_values = mycursor.fetchone()
                needs_info = []


                z = 0
              
                # needs_values is a tuple which can't be updated. It's values are stored in a new array
                while z < len(needs_values):
                  needs_info.append(needs_values[z])
                  z = z + 1


                # Display of needs info - needs_desc contains column names, needs_info contains column values
                o = 3
                while o < len(needs_info):
                  for x in range(3, len(needs_desc)):
                    print(str(o - 2) + ". " + str(needs_desc[x][0]) + ":" + str(needs_info[o]))
                    o = o + 1
                        
                print()
                selected_num = input("Enter The Number Corresponding To Your Desired Update: ")
                print()

                
                if(selected_num == "1"):
                  
                  newAllergies = input("Enter " + update_array[i] + "'s" + " Updated Allergies: ")
                  print()

                  id_info = (newAllergies, parent_info[0], update_array[i])
                  newID_query = "update Child_Needs set Allergies = %s where Parent_Id = %s and Child_Name = %s"
                  mycursor.execute(newID_query, id_info)

                
                  print()
                  print(update_array[i] + "'s" + " Allergies Is Now Set To " + newAllergies)
                  print()

                  needs_info[2] = newAllergies
                  


                  print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
                  print()

                  continue_option = input("Insert 'Y' or 'N':")
                  print()
                  print()


                  if (continue_option == 'Y'):
                    updateChildren()

                  elif (continue_option == 'N'):
                    parentProgram(parent_info[1], parent_info[0])
                    
                  else:
                      
                      while(continue_option != 'Y' or continue_option != 'N'):

                        continue_option = input("Insert 'Y' or 'N':")
                        print()
                        print()
                        
                        if (continue_option == 'Y'):
                            
                            updateChildren()

                        elif (continue_option == 'N'):
                            
                            parentProgram(parent_info[1], parent_info[0])


                if (selected_num == "2"):

                  newDiseases = input("Enter " + update_array[i] + "'s" + " Updated Diseases: ")
                  print()

                  id_info = (newDiseases, parent_info[0], update_array[i])
                  newID_query = "update Child_Needs set Diseases = %s where Parent_Id = %s and Child_Name = %s"
                  mycursor.execute(newID_query, id_info)

                
                  print()
                  print(update_array[i] + "'s" + " Diseases Is Now Set To " + newDiseases)
                  print()

                  needs_info[3] = newDiseases
                  


                  print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
                  print()

                  continue_option = input("Insert 'Y' or 'N':")
                  print()
                  print()


                  if (continue_option == 'Y'):
                    updateChildren()

                  elif (continue_option == 'N'):
                    parentProgram(parent_info[1], parent_info[0])
                    
                  else:
                      
                      while(continue_option != 'Y' or continue_option != 'N'):

                        continue_option = input("Insert 'Y' or 'N':")
                        print()
                        print()
                        
                        if (continue_option == 'Y'):
                            
                            updateChildren()

                        elif (continue_option == 'N'):
                            
                            parentProgram(parent_info[1], parent_info[0])
              

                elif(selected_num == "3"):

                  newMedications = input("Enter " + update_array[i] + "'s" + " Updated Medications: ")
                  print()

                  id_info = (newMedications, parent_info[0], update_array[i])
                  newID_query = "update Child_Needs set Medications = %s where Parent_Id = %s and Child_Name = %s"
                  mycursor.execute(newID_query, id_info)

                
                  print()
                  print(update_array[i] + "'s" + " Medications Is Now Set To " + newMedications)
                  print()

                  needs_info[4] = newMedications
                  


                  print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
                  print()

                  continue_option = input("Insert 'Y' or 'N':")
                  print()
                  print()


                  if (continue_option == 'Y'):
                    updateChildren()

                  elif (continue_option == 'N'):
                    parentProgram(parent_info[1], parent_info[0])
                    
                  else:
                      
                      while(continue_option != 'Y' or continue_option != 'N'):

                        continue_option = input("Insert 'Y' or 'N':")
                        print()
                        print()
                        
                        if (continue_option == 'Y'):
                            
                            updateChildren()

                        elif (continue_option == 'N'):
                            
                            parentProgram(parent_info[1], parent_info[0])


                  
                elif(selected_num == "4"):

                  newDisabilities = input("Enter " + update_array[i] + "'s" + " Updated Disabilities: ")
                  print()

                  id_info = (newDisabilities, parent_info[0], update_array[i])
                  newID_query = "update Child_Needs set Disabilities = %s where Parent_Id = %s and Child_Name = %s"
                  mycursor.execute(newID_query, id_info)

                
                  print()
                  print(update_array[i] + "'s" + " Disabilities Is Now Set To " + newDisabilities)
                  print()

                  needs_info[5] = newDisabilities
                  


                  print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
                  print()

                  continue_option = input("Insert 'Y' or 'N':")
                  print()
                  print()


                  if (continue_option == 'Y'):
                    updateChildren()

                  elif (continue_option == 'N'):
                    parentProgram(parent_info[1], parent_info[0])
                    
                  else:
                      
                      while(continue_option != 'Y' or continue_option != 'N'):

                        continue_option = input("Insert 'Y' or 'N':")
                        print()
                        print()
                        
                        if (continue_option == 'Y'):
                            
                            updateChildren()

                        elif (continue_option == 'N'):
                            
                            parentProgram(parent_info[1], parent_info[0])

                
                
                elif(selected_num == "5"):

                  newIntrests = input("Enter " + update_array[i] + "'s" + " Updated Intrests: ")
                  print()

                  id_info = (newIntrests, parent_info[0], update_array[i])
                  newID_query = "update Child_Needs set Intrests = %s where Parent_Id = %s and Child_Name = %s"
                  mycursor.execute(newID_query, id_info)

                
                  print()
                  print(update_array[i] + "'s" + " Intrests Is Now Set To " + newIntrests)
                  print()

                  needs_info[6] = newIntrests
                  


                  print("Would You Like To Update Something Else (Y) Or Return To The Menu (N)?")
                  print()

                  continue_option = input("Insert 'Y' or 'N':")
                  print()
                  print()


                  if (continue_option == 'Y'):
                    updateChildren()

                  elif (continue_option == 'N'):
                    parentProgram(parent_info[1], parent_info[0])
                    
                  else:
                      
                      while(continue_option != 'Y' or continue_option != 'N'):

                        continue_option = input("Insert 'Y' or 'N':")
                        print()
                        print()
                        
                        if (continue_option == 'Y'):
                            
                            updateChildren()

                        elif (continue_option == 'N'):
                            
                            parentProgram(parent_info[1], parent_info[0])
                
                
                elif (selected_num != "1" and selected_num != "2" and selected_num != "3" and selected_num != "4" and selected_num != "5"):
                  print()
                  print("Your Input Is Invalid. Please Try Again") 
                  print()
                  updateChildren()
              
              if (updated.isnumeric() == False):
                print()
                print("Your Input Is Invalid. Please Try Again.")
                print()
                updateChildren()

              elif(updated.isnumeric() == True and (int(updated) > len(update_array) or int(updated) < 0)):
                print()
                print("Your Input Is Invalid. Please Try Again.")
                print()
                updateChildren()

        elif (update_select != "1" and update_select != "2"):
                  
            print()
            print("Your Input Is Invalid. Please Try Again") 
            print()
            updateChildren()

    elif(selected != "1" and selected !=  "2" and selected != "3"):
                    
            print()
            print("Your Input Is Invalid. Please Try Again") 
            print()
            updateChildren()

    

def findBabySitters():


  sitters_input = (parent_info[5], )

  sitters_query = "Select BabySitter_Name, Age, Experience_Years, Suggested_Hourly_Pay, Rating from BabySitter where Zip_Code = %s and Current_Availability = 1"
  mycursor.execute(sitters_query, sitters_input)

  sitters_desc = mycursor.description


  sitters_values = mycursor.fetchall()
  sitters_columns = []
  sitters_info = []


  x = 0

  # sitter_values is a list of tuple which can't be updated. It's values are stored in a new array
  while x < len(sitters_values):
    sitters_info.append(sitters_values[x])
    x = x + 1


  o = 0

  # column names
  while o < len(sitters_desc):
    sitters_columns.append(sitters_desc[o][0])
    o = o + 1
  
  sitters_columns[2] = "Years Of Experience"
  sitters_columns[3] = "Suggested Hourly Pay"
  sitters_columns[4] = "Average Rating"


  z = 1
  babysitter_names = []



  # List of Babysitters
  for i in sitters_info:
    print(str(z) + ". " + i[0])
    print()

    babysitter_names.append(i[0])

    y = 1


    # Displays selected Babysitter column names + values
    while (y < len(i)):
      print(str(sitters_columns[y]) + ": " + str(i[y]))
      y = y + 1

    print()
    z = z + 1

  if (len(sitters_info) == 0):
     print()
     print("There Are No Local, Available BabySitters At The Moment. Returning To The Main Menu.")
     print()
     parentProgram(parent_info[1], parent_info[0])

  else:

    print()
    print("Enter The Number Corresponding To The BabySitter You Wish To Contact/View.")
    print()

    selected = input("Enter The Number Here: ")
    print()

    for i in range(len(babysitter_names)):
        
        if(selected == str(i + 1)):
          
          contact_inputs = (babysitter_names[i], )
          contact_query = "Select Email, Social_Media, Phone_Number from BabySitter where BabySitter_Name = %s"
          mycursor.execute(contact_query, contact_inputs)

          contact_desc = mycursor.description
          contact_values = mycursor.fetchone()
          contact_info = []

          x = 0
          while (x < len(contact_values)):
              contact_info.append(contact_values[x])
              x = x + 1

          print(babysitter_names[i] + "'s Contact Information:")
          print()

          for i in range(len(contact_values)):
              print(str(contact_desc[i][0]) + ": " + contact_values[i])

          print()

        if (selected.isnumeric() == False):
          print()
          print("Your Input Is Invalid. Please Try Again.")
          print()
          findBabySitters()

        elif(selected.isnumeric() == True and (int(selected) > len(babysitter_names) or int(selected) < 0)):
          print()
          print("Your Input Is Invalid. Please Try Again.")
          print()
          findBabySitters()
          
          
    print()
    print("Would You Like To View More BabySitters (Y) Or Return To The Menu (N)?")
    print()
    

    continue_option = input("Insert 'Y' or 'N':")
    print()
    print()


    if (continue_option == 'Y'):
      findBabySitters()

    elif (continue_option == 'N'):
      parentProgram(parent_info[1], parent_info[0])
      
    else:
        
        while(continue_option != 'Y' or continue_option != 'N'):

          continue_option = input("Insert 'Y' or 'N':")
          print()
          print()
          
          if (continue_option == 'Y'):
              
              findBabySitters()

          elif (continue_option == 'N'):
              
              parentProgram(parent_info[1], parent_info[0])



def displayReviews():


  sitters_input = (parent_info[5], )

  sitters_query = "Select BabySitter_Name from BabySitter where Zip_Code = %s and Current_Availability = 1"
  mycursor.execute(sitters_query, sitters_input)


  sitters_values = mycursor.fetchall()
  sitters_info = []


  x = 0

  # sitter_values is a list of tuple which can't be updated. It's values are stored in a new array
  while x < len(sitters_values):
    sitters_info.append(sitters_values[x])
    x = x + 1

  
  z = 1
  babysitter_names = []
  

  # List of Babysitters
  for i in sitters_info:
    print(str(z) + ". " + i[0])
    babysitter_names.append(i[0])

    z = z + 1

  if (len(sitters_info) == 0):
    print()
    print("There Are No Local, Available BabySitters At The Moment. Sorry For The Inconvience.")
    print()
    parentProgram(parent_info[1], parent_info[0])

  else:
    print()
    print("Enter The Number Corresponding To Which BabySitter's Reviews You Wish To Display.")   
    print()

    selected = input("Enter the Number Here: ")
    print()
    

    for o in range(0, len(babysitter_names)):     

      if(selected == str(o + 1)):
          
          sitter_input = (babysitter_names[o], )
          sitter_query =  "Select Parent_Name, Phone_Number, Rating, Review from Parent natural join Reviews where Reviews.BabySitter_Name = %s"
          mycursor.execute(sitter_query, sitter_input)

          sitter_desc = mycursor.description
          sitter_values = mycursor.fetchall()
          sitter_info = []
          sitter_columns = []
        
          # sitter_values is a list of tuple which can't be updated. It's values are stored in a new array
          if str(sitter_values) == "[]":
            print(babysitter_names[o] + " Doesn't Have Any Reviews Yet.")
            print()
            print()

            print("Would You Like To View Another BabySitter's Reviews (Y) Or Return To The Menu (N)?")
            print()
            

            continue_option = input("Insert 'Y' or 'N':")
            print()
            print()


            if (continue_option == 'Y'):
              displayReviews()

            elif (continue_option == 'N'):
              parentProgram(parent_info[1], parent_info[0])
              
            else:
                
                while(continue_option != 'Y' or continue_option != 'N'):

                  continue_option = input("Insert 'Y' or 'N':")
                  print()
                  print()
                  
                  if (continue_option == 'Y'):
                      
                    displayReviews()

                  elif (continue_option == 'N'):
                      
                    parentProgram(parent_info[1], parent_info[0]) 
            

            
          else:
            x = 0
            while x < len(sitter_values):
              sitter_info.append(sitter_values[x])
              x = x + 1

        
            z = 0

            print("These Are " + babysitter_names[o] + "'s Reviews: ")
            print()
            

            # column names
            while z < len(sitter_desc):
              sitter_columns.append(sitter_desc[z][0])
              z = z + 1

            
            
            
            # column name updated to indicate the parent's phone #
            for i in sitter_info:
              sitter_columns[1] = i[0] + "'s " + sitter_columns[1]
            
              for a in range(len(sitter_info[0])):
                print(sitter_columns[a] + ": " + str(i[a]))
                
              print()
              print()
              sitter_columns[1] = "Phone_Number"
              

          print()

          print("Would You Like To View Another BabySitter's Reviews (Y) Or Return To The Menu (N)?")
          print()
          

          continue_option = input("Insert 'Y' or 'N':")
          print()
          print()


          if (continue_option == 'Y'):
            displayReviews()

          elif (continue_option == 'N'):
            parentProgram(parent_info[1], parent_info[0])
            
          else:
              
              while(continue_option != 'Y' or continue_option != 'N'):

                continue_option = input("Insert 'Y' or 'N':")
                print()
                print()
                
                if (continue_option == 'Y'):
                    
                  displayReviews()

                elif (continue_option == 'N'):
                    
                  parentProgram(parent_info[1], parent_info[0]) 

      if (selected.isnumeric() == False):
          print()
          print("Your Input Is Invalid. Please Try Again.")
          print()
          displayReviews()

      elif(selected.isnumeric() == True and (int(selected) > len(babysitter_names) or int(selected) < 0)):
            print()
            print("Your Input Is Invalid. Please Try Again.")
            print()
            displayReviews()
     

     
def writeReview():
  
  print()
  sitter_name = input("What Is The Name Of The BabySitter You Wish To Review: ")
  print()

  sitter_review = input("Summarize How Well Of A Job " + sitter_name + " Did: ")
  print()

  sitter_rating = input("On A Scale Of 1 - 5 ('1' Being The Lowest), rate " + sitter_name + "'s Service:")
  print()

  if(sitter_rating.isnumeric() == False):
     while(sitter_rating.isnumeric() == False):
        
        print("Please Enter Numerical Values Only. Try Again")
        print()
        sitter_rating = input("On A Scale Of 1 - 5 ('1' Being The Lowest), rate " + sitter_name + "'s Service:")
  else:
     print()
     print("Your Review Is Complete And Will Now Be Displayable For Other Parents To View.")
     print()


  sitter_inputs = (parent_info[0], parent_info[1], sitter_name, sitter_rating, sitter_review)
  sitter_query = "insert into Reviews values (%s, %s, %s, %s, %s)"
  mycursor.execute(sitter_query, sitter_inputs)


  print()
  print("Would You Like To View Another BabySitter's Reviews (Y) Or Return To The Menu (N)?")
  print()

  continue_option = input("Insert 'Y' or 'N':")
  print()
  print()


  if (continue_option == 'Y'):
    writeReview()

  elif (continue_option == 'N'):
    parentProgram(parent_info[1], parent_info[0])
    
  else:
      
      while(continue_option != 'Y' or continue_option != 'N'):

        continue_option = input("Insert 'Y' or 'N':")
        print()
        print()
        
        if (continue_option == 'Y'):
          writeReview()

        elif (continue_option == 'N'):
          parentProgram(parent_info[1], parent_info[0]) 
  
          
start()