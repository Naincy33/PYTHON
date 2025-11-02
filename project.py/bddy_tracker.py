birthdays={}

n= int(input("how many bddys uh want to enter: "))
for i in range (n):
    name= input(f" enter name{i+1}: ")
    date= input("enter dob as dd-mm-yyyy: ")

    birthdays[name]= date

search_name= input("bddy to be searched: ")
if search_name in birthdays:
    bddy=birthdays[search_name]
    parts = bddy.split("-")
    new_bddy= "/".join([parts[0], parts[1], parts[2]])

    print(f"bdyy for {search_name} is {new_bddy}")       
else:
    print("bddy not found")     

