import mysql.connector 
import glob
import os
from os import system, name 
import shutil
base_dir = "."
def clear(): 
	_ = system('clear') 

clear()
folders = glob.glob("./*")


mydb = mysql.connector.connect(
  host="localhost",
  user="IMDB",
  password="123",
  database="IMDB",
  auth_plugin='mysql_native_password'
)

titleType_array = {
'1':'short',
'2':'movie',
'3':'tvMovie',
'4':'tvSeries',
'5':'tvEpisode',
'6':'tvShort',
'7':'tvMiniSeries',
'8':'tvSpecial',
'9':'video',
'10':'videoGame'
}

mycursor = mydb.cursor()
total_count = len(folders)
step = 1
step_fixed = 0
step_unfixed = 0
for dir in folders:
	clear()
	print(step,"/",total_count)
	print("fixed no:",step_fixed)
	print("unfixed no:",step_unfixed)
	step=step+1
	print(dir)
	tmp = dir.split("/")
	primaryTitle=tmp[-1]
	print(primaryTitle)
	primaryTitle=primaryTitle.replace(".","%")
	primaryTitle=primaryTitle.replace("_","%")
	primaryTitle=primaryTitle.replace("-","%")
	primaryTitle=primaryTitle.replace(" ","%")
	primaryTitle=primaryTitle.replace("(","%")
	primaryTitle=primaryTitle.replace(")","")
	primaryTitle=primaryTitle.replace("[","%")
	primaryTitle=primaryTitle.replace("]","%")
	mycursor.execute("SELECT * FROM basics where concat(primaryTitle,' ',startYear) like %s and titleType in ('movie','tvMovie') order by startYear",("%" + primaryTitle + "%",))
	myresult = mycursor.fetchall()
	i = 0
	if len(myresult)==1:
		step_fixed=step_fixed+1
		for x in myresult:
			tconst=x[0]
			titleType=x[1]
			primaryTitle=x[2]
			originalTitle=x[3]
			isAdult=x[4]
			startYear=x[5]
			endYear=x[6]
			runtimeMinutes=x[7]
			genres=x[8]
			print(i," ----> ",tconst,titleType,primaryTitle,startYear)
			i = i+1
		#  				echo $row2['averageRating']." ".$row['tconst']." ".$row['primaryTitle']." (".$row['startYear'].") [".$row['genres']."]";
		tconst=myresult[0][0]
		print(tconst)
		mycursor.execute("SELECT a.*,b.averageRating FROM basics a,ratings b where a.tconst=b.tconst and a.tconst=%s",(tconst,))
		myresult = mycursor.fetchall()
		for x in myresult:
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
			print(averageRating,"",tconst,"",primaryTitle,"(",startYear,") [",genres,"]")
			file_name="%s %s %s (%s) [%s]" %(averageRating,tconst,primaryTitle,startYear,genres)
			file_name=file_name.replace(":","")
			print(file_name)
			os.rename(os.path.join(base_dir, dir),os.path.join(base_dir, file_name))
			isExist = os.path.exists("./Fixed")
			if not isExist:
				os.makedirs("./Fixed/")
			shutil.move(os.path.join(base_dir, file_name),"./Fixed/")
	else:
			isExist = os.path.exists("./unready")
			if not isExist:
				os.makedirs("./unready/")
			shutil.move(dir,"./unready/")
			step_unfixed=step_unfixed+1
		