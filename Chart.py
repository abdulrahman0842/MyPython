import matplotlib.pyplot as plt
import pandas as pd
   
Data = {'Country': ['USA','Canada','Germany','UK','France'],
        'GDP_Per_Capita': [45000,42000,52000,49000,47000]
       }
df = pd.DataFrame(Data,columns=['Country','GDP_Per_Capita'])

New_Colors = ['green','blue','purple','brown','teal']
plt.bar(df['Country'], df['GDP_Per_Capita'], color=New_Colors)
plt.title('Country Vs GDP Per Capita', fontsize=14)
plt.xlabel('Country', fontsize=14)
plt.ylabel('GDP Per Capita', fontsize=14)
plt.grid(True)
plt.show()
