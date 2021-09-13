import numpy as np  # 数组相关的库
import matplotlib.pyplot as plt  # 绘图库
from matplotlib.ticker import MultipleLocator

count = 0
with open('new_fednova_dynamic.log', 'r') as inF:
    for line in inF:
        if 'Global Model Test accuracy' in line:
            print(line[-10:-1], ",")
            count += 1
    # do_something

print("count = ", count)

y = np.array([
 0.377000 ,
 0.389200 ,
 0.745300 ,
 0.603000 ,
 0.787000 ,
 0.621800 ,
 0.755400 ,
 0.605600 ,
 0.795800 ,
 0.610100 ,
 0.808500 ,
 0.659800 ,
 0.803600 ,
 0.673000 ,
 0.756700 ,
 0.747900 ,
 0.718600 ,
 0.764400 ,
 0.632100 ,
 0.753300 ,
 0.663000 ,
 0.768000 ,
])

y = np.array([
 0.377000 ,
 # 0.389200 ,
 0.745300 ,
 # 0.603000 ,
 0.787000 ,
 # 0.621800 ,
 0.755400 ,
 # 0.605600 ,
 0.795800 ,
 # 0.610100 ,
 0.808500 ,
 # 0.659800 ,
 0.803600 ,
 # 0.673000 ,
 0.756700 ,
 # 0.747900 ,
 0.718600 ,
 # 0.764400 ,
 0.632100 ,
 # 0.753300 ,
 0.663000 ,
 # 0.768000 ,
])



plt.figure(figsize=(10,7))
font1 = {
    'weight' : 'normal',
    'size'   : 16,
}
font2 = {
    'weight' : 'normal',
    'size'   : 16,
}
plt.legend(prop=font2)

plt.axhline(0.78)

plt.plot(np.arange(0,len(y),1)*2, y,'-',linestyle='-', color='b', label='VGG-11(Fednova_Dynamic)')
# print(len(y_org))

plt.xlabel('Rounds',fontdict=font1)
plt.ylabel('Accuracy',font1)
plt.legend(prop=font1)

plt.tight_layout()

plt.yticks(fontproperties = 'noraml', size = 15)
tlist=plt.xticks(fontproperties = 'normal', size = 15)

plt.savefig('new_fednova_dynamic.pdf')
plt.show()
print(len(y))