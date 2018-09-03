from datetime import datetime
#capturing the users yearOfBirthprint(mydic)
def computeAge():
    yearOfBirth =int(input("Enter your year of birth: "))
    if not isinstance(yearOfBirth, int):
        raise ValueError 
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
    
     
     print(computeAge())

