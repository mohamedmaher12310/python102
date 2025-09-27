import datetime
date_array=[]
person_data={
"khalid": "1-2-1989",
    "Nouf": "2-09-2004",
    "Ali": "9-12-2009"
}
def check_birth_date(date):
    arr=date.split('-')
    index = 0
    for iterr in arr:

        arr[index]=int(iterr)
        index+=1
    if 1<=arr[0]<=31:
        pass
    else:
        print("Invalid date")
        return False
    if 1<=arr[1]<=12:
        pass
    else:
        print("Invalid date")
        return False
    if arr[2]>=0:
        pass
    else:
        print("Invalid date")
        return False
    global date_array
    date_array = arr[:]
    #print(date_array)
    return True



def data_center():
    oldest_person =0
    youngest_person=0
    min_age = 100
    max_age =0
    for key in person_data:
        if check_birth_date(person_data[key]):
            #to get oldest person
#            oldest_year = datetime.datetime.now().year
#            if oldest_year >date_array[2]:
#                oldest_year = date_array[2]
#                oldest_person = key
            #calculate age
            age = datetime.datetime.now().year - date_array[2]
            if min_age> age:
                min_age=age
                youngest_person = key
            if max_age < age:
                max_age = age
                oldest_person = key

            date = datetime.date(date_array[2], date_array[1], date_array[0])
            day_of_week = date.strftime("%A")
            print(f"{key} is {age} years old and he/she was born on {day_of_week}")
        else:
            print(key)
            return
    print(f"The oldest one is {oldest_person}")
    print(f"The youngest one is {youngest_person} ")
    print(f"Total People: {len(person_data)}")


def my_program():
    while 1:
        name = input("Please enter the name and the date of birth of the person first the name:\n")
        day_of_birth = input("Please enter the date of birth in format dd-mm-yyyy\n")
        person_data[name]=day_of_birth
        out_of_loop = input("Please to add data of another person please press 's' :\n")
        if out_of_loop != 's':
            break

    data_center()


my_program()