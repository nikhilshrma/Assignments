#Q1

l=f.readlines()
n=int(input("Enter the no. of last n lines of a file"))
c=0
for i in l:
    c+=1
print(c)
print(l[c-n:c])

#Q2
f=open("/home/harsh/PycharmProjects/Acadview-assignments/n","r")
s=f.read()
l=s.split()
print(l)
dict={}
for i in l:
    dict[i]=l.count(i)
print(dict)

#Q3
m=open("/home/harsh/PycharmProjects/Acadview-assignments/m","r+")
f=open("/home/harsh/PycharmProjects/Acadview-assignments/n","r")
m.writelines(f.read())


#Q4
f=open("/home/harsh/PycharmProjects/Acadview-assignments/n","r")
m=open("/home/harsh/PycharmProjects/Acadview-assignments/m","r")
o=open("/home/harsh/PycharmProjects/Acadview-assignments/o","a")
a=f.readlines()
b=m.readlines()
c=0
d=0
for i in a:
    c+=1
for i in b:
    d+=1
print(c,d)
f.seek(0,0)
m.seek(0,0)
if(c<d):
    c=d
for i in range(c):
    o.write(f.readline()+m.readline())

p=open("/home/harsh/PycharmProjects/Acadview-assignments/p","a+")
q=open("/home/harsh/PycharmProjects/Acadview-assignments/q","r+")
import random
for i in range(10):
    p.write(str(random.randint(1,10000))+'\n')
p.seek(0,0)
print(p.read())
p.seek(0,0)
l=[]
for i in range(10):
    l.append(int(p.readline()))
l.sort()
q.write(str(l))
q.seek(0,0)
print(q.read())