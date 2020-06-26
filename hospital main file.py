from Hospital import *

def main():
        while  1:
            num = int(input("----\nenter 1 for Admission:\nenter 2 for Bill Payment:"))
            if num == 1:
                object = Hospital()
                object.Create_Table()
                object.Patient_ID()
                object.Date_Time()
                name = input("enter patient name:")
                age = int(input("enter age:"))
                sex = input("If male =m,female=f,other=o:")
                phone = input("enter phonenumber:")
                object.Add_Details(paitentlist, datetimelist, name, age, sex,phone)
            elif num == 2:
                object1 = CustomerSlip()
                object1.CreateTable()
                ID = int(input("enter paitent ID:"))
                object1.Check(ID)
                object1.Date_Time()
                amountrupees = input("enter paid amount :")
                amountbalance = input("enter balance amount to pay:")
                amountpaid = input("paid =yes or discount = %:")
                object1.Add_details(empty_list, datetimelist, amountrupees, amountbalance, amountpaid)

            else:
                print("1 for Admission:\n2 for Bill Payment")
if __name__ == '__main__': main()

