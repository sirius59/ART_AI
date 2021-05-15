from PIL import Image
import pandas as pd

artists=pd.read_csv('C:\\Users\\cleme\\Downloads\\dataset\\artists.csv')

##name of artists
name=artists.name
##genre of artists
genre=artists.genre

##number of paintings by artists
nb_paints=artists.paintings


for i in range(len(name)):
  for j in range(nb_paints[i]):
    img=Image.open(f'C:\\Users\\cleme\\Downloads\\dataset\\images\\{name[i]}\\{name[i]}_{j+1}.jpg')
    new=img.resize((500,500),resample=3)
    newL=new.convert('RGB')#RGB L=grayscale
    newL.save('C:\\Users\\cleme\\Downloads\\dataset\\resized\\'+str(name[i])+'_'+str(j+1)+'.jpg')