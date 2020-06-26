import math,random,datetime,mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd='@vivek77',database="vivek")
cursor=db.cursor()
empty_numbers = []
datetimelist =[]
empty_list = []
paitent = []
paitentlist=[]

class Hospital:
    #creating table
    def Create_Table(self):
        cursor.execute("create table if not exists Hospital(Personid int NOT NULL AUTO_INCREMENT PRIMARY KEY,paitentId int(4),Datetime varchar(27),Name varchar(30),Age int(2),sex varchar(8)"
                   ",phone varchar(10))")

    # patientID
    def Patient_ID(self):
            # Declare a digits variable
            # which stores all digits
            digits = "01234567890"
            OTP = ""
            # length of password can be chaged
            # by changing value in range
            for i in range(4):
                OTP += digits[math.floor(random.random() * 10)]
            paitentlist.append(OTP)

    # Datetime
    def Date_Time(self):
            x = datetime.datetime.now()
            datetimelist.append(x)

    #Adding the record to the table
    def Add_Details(self,patientlist,datetimelist,name,age,sex,phone):
        details = patientlist[0],datetimelist[0],name,age,sex,phone
        insert = "insert into Hospital(paitentId,Datetime,Name,Age,sex,Phone) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert,details)
        db.commit()
        print("Record is Added")
        paitentlist.clear()
        datetimelist.clear()


class CustomerSlip(Hospital):
    def CreateTable(self):
        cursor.execute(
            "create table if not exists customerslip(personid int NOT NULL AUTO_INCREMENT PRIMARY KEY,paitentId int(4),Datetime varchar(27)"
            ",amountpaidRs varchar(50),amountbalance varchar(50),amountpaid varchar(10))")

    def Check(self,ID):
        cursor.execute("SELECT * FROM Hospital")
        result = cursor.fetchall()
        for row in result:
            empty_numbers.extend(row)
        if ID in empty_numbers:
            print("Id={:d} found".format(ID))
            empty_list.append(ID)
            sql = "SELECT Name,Age,sex FROM Hospital where paitentId={}".format(ID)
            cursor.execute(sql)
            result = cursor.fetchone()
            for i in result:
                paitent.append(i)
            print("Name=", paitent[0], "\nAge=", paitent[1], "\nSex=", paitent[2])

        else:
           print("not found")

    def Add_details(self,empty_list,datetimelist,amountrupees,amountbalance,amountpaid):
        Details = empty_list[0],datetimelist[0],amountrupees,amountbalance,amountpaid
        insert = "insert into customerslip(paitentId,Datetime,amountpaidRs,amountbalance,amountpaid) values (%s,%s,%s,%s,%s)"
        cursor.execute(insert,Details)
        db.commit()
        print("Record Added")
        empty_list.clear()
        datetimelist.clear()
        paitent.clear()
        cursor.execute("delete from customerslip where amountpaidRs = 100")
        db.commit()


