class multiplefunctions():
        def subfields_in_ai():
            print("Sub Fields in are AI are:")
            fields=("Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing")
            for item in fields:
             print(item)
        def oddeven():
            num=int(input("Enter the Number:"))
            if((num%2)==0):
                print("52452 is Even Number")
            else:
                print("52452 is odd Number")
        def Marriageeligible():
             Gender = input("Enter the Gender:")
             age = int(input("Enter the age:"))
             if(age==18):
              print("Female Eligible for Marriage")
             elif(age>21):
              print("Eligible")
             else:
              print("Not Eligible")
        def percent():
            sub1=int(input("Enter the Subject1:"))
            sub2=int(input("Enter the Subject2:"))
            sub3=int(input("Enter the Subject3:"))
            sub4=int(input("Enter the Subject4:"))
            sub5=int(input("Enter the Subject5:"))
            total = sub1 + sub2 + sub3 + sub4 + sub5
            print("Total=",total)
            percentage = (total/500)*100
            print("Percentage=",percentage)
        def triangle():
            hei=int(input("Enter the Height:"))
            bre=int(input("Enter the Breadth:"))
            Area= (hei*bre)/2
            print("Area=",Area)
            height1=int(input("Enter the Height1:"))
            height2=int(input("Enter the Height2:"))
            breadth=int(input("Enter the Breadth:"))
            perimeter = height1+height2+breadth
            print("perimeter of a triangle",perimeter)
        