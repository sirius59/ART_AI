from PIL import Image
import pandas as pd

artists=pd.read_csv('C:\\Users\\cleme\\Downloads\\dataset\\artists.csv')

##name of artists
artists['name'][19]='Albrecht_Durer' #fix ASCII problems
tmp=artists['name']
name=[tmp[i].replace(' ','_') for i in range(len(tmp))]#replace space by underscore, more convinent to import images

##genre of artists
tmp=artists['genre']
genre=[tmp[i].replace(',','/') for i in range(len(tmp))]#replace coma by slash, avoid mistakes in list

##number of paintings by artists
nb_paints=artists['paintings']


for i in range(len(name)):
  for j in range(nb_paints[i]):
    img=Image.open(f'C:\\Users\\cleme\\Downloads\\dataset\\images\\{name[i]}\\{name[i]}_{j+1}.jpg')
    new=img.resize((250,250),resample=3)
    newL=new.convert('L')
    newL.save('C:\\Users\\cleme\\Downloads\\dataset\\resized\\'+str(name[i])+'_'+str(j+1)+'.jpg')