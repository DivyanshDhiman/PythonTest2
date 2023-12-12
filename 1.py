print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
print(" Type 1 to Add a record.")   
print(" Type 2 to Search a record.")   
print(" Type 3 to Update a record.")   
print(" Type 4 to Sort the record alphabtically.")   
print(" Type 5 to Delete a record")   
print(" Type 6 to Quit") 


phoneDirectory = {}

x=int(input("What would you like to do?"))


while(x!=6):
    if(x==1):
        a=int(input("How many records do you want to add?"))
        i=1
        while(i<=a):
            b=input("Write name")
            c=int(input("Enter you 10-digit number."))
            i=i+1
            phoneDirectory.update({b:c})
        print(phoneDirectory)
        

 
    elif x==2:
        print("You chose 2. That means you want to search a record")
        e=input("Which record do you want to search?")
        if e in phoneDirectory:
                print (phoneDirectory[e])
        else:
                print("this item is not available in the dictionary")

    elif x==3:
        print(phoneDirectory)
        
  
    elif x==4:
        print("You chose 4, which means you want to sort the records.")
        q=list(phoneDirectory.keys())
        q.sort
        sort_directory={i:dict[i] for i in q}
        print(sort_directory)

    elif x==5:
        print("You chose 5. That means you want to delete a record.")
        f=int(input("How many records do you want to delete?"))
        i=1
        while(i<=f):
            g=input("which record do you want to delete?")
            i=i+1
            if g in phoneDirectory:
                phoneDirectory.pop(g)
                print(phoneDirectory)

    print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
    print(" Type 1 to Add a record.")   
    print(" Type 2 to Search a record.")   
    print(" Type 3 to Update a record.")   
    print(" Type 4 to Sort the record alphabtically.")   
    print(" Type 5 to Delete a record")   
    print(" Type 6 to Quit") 


    x=int(input("What would you like to do?"))