from PIL import Image
import pandas as pd

artists=pd.read_csv('C:\\Users\\cleme\\Downloads\\dataset_resized\\artists.csv')

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
    img=Image.open(f'C:\\Users\\cleme\\Downloads\\dataset_resized\\resized\\{name[i]}_{j+1}.jpg')
    blanche=Image.open('C:\\Users\\cleme\\Downloads\\dataset_resized\\resized\\photo_blanche.jpg')
    if img.size[0]>562 or img.size[1]>562:
        img.thumbnail((562,562))
        img_copy = img.copy()
        position = (0,0)
        blanche.paste(img_copy, position)
        blanche.save('C:\\Users\\cleme\\Downloads\\dataset_resized\\resized\\thumbnail\\'+str(name[i])+'_'+str(j+1)+'.jpg')
    else:
        img_copy = img.copy()
        position = (0,0)
        blanche.paste(img_copy, position)
        blanche.save('C:\\Users\\cleme\\Downloads\\dataset_resized\\resized\\thumbnail\\'+str(name[i])+'_'+str(j+1)+'.jpg')
    #img.save('C:\\Users\\cleme\\Downloads\\dataset_resized\\resized\\thumbnail\\'+str(name[i])+'_'+str(j+1)+'.jpg')