import mysql.connector 
mydb = mysql.connector.connect(
  host="localhost",
  user="IMDB",
  password="123",
  database="IMDB",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
print("tConst:")
tconst=input()
mycursor.execute("SELECT a.*,b.averageRating FROM basics a,ratings b where a.tconst=b.tconst and a.tconst=%s",(tconst,))

myresult = mycursor.fetchall()
x=myresult[0]
print(myresult)
tconst=x[0]
titleType=x[1]
primaryTitle=x[2]
originalTitle=x[3]
isAdult=x[4]
startYear=x[5]
endYear=x[6]
runtimeMinutes=x[7]
genres=x[8]
averageRating=x[9]
file_name="%s %s %s (%s) [%s]" %(averageRating,tconst,primaryTitle,startYear,genres)
file_name=file_name.replace(":","")
print(file_name)
print(myresult)
