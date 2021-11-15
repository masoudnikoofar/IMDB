import mysql.connector 
import glob
import os
from os import system, name 
import shutil
base_dir = "./"
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
for dir in folders:
	clear()
	print(step,"/",total_count)
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
	print(primaryTitle) 
	mycursor.execute("SELECT * FROM basics where concat(primaryTitle,' ',startYear) like %s and titleType in ('movie','tvMovie') order by startYear",("%" + primaryTitle + "%",))
	myresult = mycursor.fetchall()
	i = 0
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
	movie_index=input("Which One?:")
	if movie_index=="":
		isExist = os.path.exists("./unready")
		if not isExist:
			os.makedirs("./unready/")
		shutil.move(dir,"./unready/")
		continue
	if movie_index.startswith("tt"):
		tconst=movie_index	
	else:
		tconst=myresult[int(movie_index)][0]
	print(tconst)
	mycursor.execute("SELECT a.*,b.averageRating FROM basics a,ratings b where a.tconst=b.tconst and a.startYear is not null and a.tconst=%s",(tconst,))
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
		#shutil.move(os.path.join(base_dir, file_name),".")
