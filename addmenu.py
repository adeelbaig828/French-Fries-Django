import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Resturent.settings')

import django
django.setup()

from Main.models import MenuItem,Categories
import pandas as pd

df = pd.read_csv('menu.csv',sep=',',encoding = "ISO-8859-1")
# print(df['Name'])

def Populate(N):
    name=df['Name']
    name_fr=df['Name fr']
    desc=df['Desc']
    desc_fr = df['Desc fr']
    price = df['Price']
    cat_id=df['Catergory']
    for i in range(N):
        cat = Categories.objects.get(c_id=cat_id[i])
        if name_fr[i] == ' ' or bool(name_fr[i]) == False:
            cunn_add = MenuItem.objects.get_or_create(m_name=name[i],m_name_fr=name[i],m_category=cat,m_desc=desc[i],m_desc_fr=desc_fr[i],m_price=price[i])
        else:
            cunn_add = MenuItem.objects.get_or_create(m_name=name[i],m_name_fr=name_fr[i],m_category=cat,m_desc=desc[i],m_desc_fr=desc_fr[i],m_price=price[i])


#main

if __name__=='__main__':
    print("Starting Populating program")
    Populate(df.count().max())
    print("population crated successfully")