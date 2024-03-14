import math
name=input("Input your name:\n")
print("Hello,",name)
print("sum=",sum([1,2,3]))
print("sum=",sum((1,2,3)))
print("min=",min(1,2,3))
print("max=",max([1,2,3]))
print("max=",max(1,2,3)) 
print(math.e)

#  n   => n+nn+nnn                   3   =>  3+33+333=369
n=int(input("Input n:")) #3
resultat=n+(n*10+n)+(n*100+n*10+n)
print(resultat)

n=input("Input n:") #3
resultat=eval(f"{n}+{n}{n}+{n}{n}{n}")
print(resultat)

