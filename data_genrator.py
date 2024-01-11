# set some value for column name :- 
# id(int()),name(varchar),dob(date-time),country(varcar),phone(varchar),email(varchar),cardnum(int),address(text)
# size , according to your need (varchar >= 80,)
# if you select sql query then you can direct copy and paste into the mysql query without importing csv.
# if you want csv then you can also select csv option.
# ........................more funcations add soon..................................


from faker import Faker
import random


fake = Faker()
number_of_data = int(input("enter the number how many peples data do you want :- "))
for_why = int(input("Press 1:- For sql query \nPress 2:- for csv \n\t:-"))

def operation(for_why):
    for i in range(number_of_data):
        name = fake.name()
        raw_address = fake.address()
        address = raw_address.split("\n")[0]+" "+raw_address.split("\n")[1]
        ph_num = fake.phone_number()
        country = fake.country()
        dob = fake.date_of_birth(minimum_age=20,maximum_age=40)
        cardnum = fake.credit_card_number()

        num = random.randint(1,99)
        email = name.split(" ")[0]+name.split(" ")[1]+str(num)+"@email.com"
        if(for_why==1):
            if(i==number_of_data-1):
                f.write(f"({i+1},'{name}','{dob}','{country}','{ph_num}','{email}','{int(cardnum)}','{address}');")
            else:
                f.write(f"({i+1},'{name}',{dob},'{country}','{ph_num}','{email}',{int(cardnum)},'{address}'),\n")
        elif(for_why==2):
            f.write(f"{i+1},{name},{dob},{country},{ph_num},{email},{int(cardnum)},{address}\n")


if (for_why == 1):
    with open("suryabisht00.text" , "w") as f:
        operation(for_why)
elif (for_why == 2):
    with open("suryabisht00.csv" , "w") as f:
        operation(for_why)
