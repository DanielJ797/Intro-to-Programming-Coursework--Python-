Please use the scroll wheel on the listbox to see every result

I tried to implement a graph using matplotlib, however I could not get it to work no matter how much I tried.
I would always get the error "RuntimeError: The current Numpy installation ('C:\\Users\\Danie\\AppData\\Roaming\\Python\\Python37\\site-packages\\numpy\\__init__.py') 
fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3dm3h86"



So here is the code that would have been in the plotGraph function in the menu module:

import matplotlib.pyplot as plt

plt.figure()

plt.xlabel('ISBN of each book')
plt.ylabel('Number of days since it was returned/purchased')
plt.title('Book Weeding Graph')

plt.bar(x,y)
plt.show()
