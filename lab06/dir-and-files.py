#1
import os
path = '/Users/Наркес/Desktop/PP2'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

#2
import os

path = r'C:\Users\Наркес\Desktop\PP2'
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))

#3
import os
print("Test exists or not:")
path = r'C:\Users\Наркес\Desktop\PP2\lab02'
print(os.path.exists(path))

#4
with open(r"text.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
    
#5
color = ['Hi!', 'My', 'name', 'is', 'Aliya']
with open('task_5.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('task_5.txt')
print(content.read())

#6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#7
with open('1.txt','r') as firstfile, open('2.txt','a') as secondfile:
      
    for line in firstfile:
         secondfile.write(line)
         
#8
import os
os.remove("file.txt")