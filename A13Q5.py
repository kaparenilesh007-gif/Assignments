def CheckGrade(no):
    Grade = 0


    if no>= 75 and no<=100:
        Grade = "Distinction"
    elif no >=60 and no<=74:
        Grade = "Fisrt Class"
    elif no >=50 and no<=59:
        Grade = "Second Class"
    else:
        Grade = "Fail"
    return Grade

def main():
    Marks = int(input("Enter Obtained Marks: "))
    Ret = CheckGrade(Marks)
    print("Your Grade is: ",Ret)


if __name__=="__main__":
    main()
