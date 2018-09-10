from datetime import datetime
#capturing the users yearOfBirthprint(mydic)
def computeAge(yearOfBirth):
    if not isinstance(yearOfBirth, int):
        raise ValueError ('invalid input')
    current=datetime.now().year
    age=current-int(yearOfBirth)
    if(age<18 and age>0):
        message="you are a minor"
    elif(age>=18 and age<36):
        message="you are a youth"
    elif(age<0):
        message="you can not have a negative age"
    else:
        message="you are an elder"

    return (message)


if __name__ == "__main__":
     yearOfBirth =int(input("Enter your year of birth: "))
     
     print(computeAge(yearOfBirth))

