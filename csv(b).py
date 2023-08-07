import csv

with open("C:\\Users\\sobha\\Desktop\\uNeu11.csv",'w',newline="") as csvFile:
            wr=csv.writer(csvFile)
            n=1
            listtA=[]
            while n!=0:
                    listtN=[]
                    name=input("Enter name:")
                    familienName=str(input("Enter familienName:"))
                    alter=input("Enter alter:")
                    listtN=[f"{name},{familienName},{alter}"]
                    listtA.append(listtN)
                    n=int(input("Enter n:"))
            
            wr.writerow(["Name","FAmilienName","Alter"])
            wr.writerows(listtA)


with open("C:\\Users\\sobha\\Desktop\\uNeu11.csv",'r') as csL:
    lesen=csv.reader(csL)
    for i in lesen:
        print(i)

           
        


