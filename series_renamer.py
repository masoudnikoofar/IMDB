import mysql.connector 
import glob
import os
from os import system, name 
import shutil
season_no = 3
base_dir = "/run/media/masoud/09126907530/Series/100/season3/"
def clear(): 
	_ = system('clear') 

#clear()
files = glob.glob("/run/media/masoud/09126907530/Series/100/season3/*.mkv")
print(files)

mydb = mysql.connector.connect(
  host="localhost",
  user="IMDB",
  password="123",
  database="IMDB"
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
i=1;
for file in files:
	#clear()
	#print(file)
	tmp = file.split(".")
	extention=tmp[-1]
	#primaryTitle=primaryTitle.replace(".","%")
	#mycursor.execute("SELECT * FROM basics where concat(primaryTitle,' ',startYear) like %s and titleType='movie' order by startYear",("%" + primaryTitle + "%",))
	mycursor.execute("select a.tconst,a.primaryTitle,a.titleType,b.episodeNumber,b.seasonNumber from basics a , episodes b where a.tconst=b.tconst and episodeNumber=%s and b.parentTconst='tt2661044' and titleType='tvEpisode' and b.seasonNumber=%s order by 3",(i,season_no))	
	myresult = mycursor.fetchall()
	
	i = i+1
	if len(myresult)==1:
		for x in myresult:
			tconst=x[0]
			primaryTitle=x[1]
			episodeNumber=str(x[3]).zfill(2)
			seasonNumber=str(x[4]).zfill(2)
			file_name="S%sE%s - %s.%s" %(seasonNumber,episodeNumber,primaryTitle,extention) 	
			file_name=file_name.replace(":","")
			#print(file_name)
			#os.rename(os.path.join(base_dir, file),os.path.join(base_dir, file_name))
			#shutil.move(os.path.join(base_dir, file_name),"/run/media/masoud/09126907530/Movies/Fixed")
			old=os.path.join(base_dir, file)
			new=os.path.join(base_dir, file_name)
			command = 'mv "%s" "%s"' %(old,new)
			print(command)