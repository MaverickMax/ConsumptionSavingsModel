from numpy import random 

#y = random.randint(1,10) * 10000
fv = 1
#p = (random.randint(80,99))/100
#b = (random.randint(80,99))/100
y = 20000
p = 0.95
b=0.9
print(f'An individual lives for two periods. In period 1, they earn an income of {y}.')
print('In period 2, they earn no income. In order to consume in period 2, they must buy bonds in period 1.')
print(f'One bond pays ${fv} in period 2, and can be purchased for price ${p} in period 1.')
print("The individual's objective is to maximize the present value of their utility:\nu(c1,c2) = ln*c1 + B*ln*c2")
print(f"where c1 is consumption period 1, c2 is consumption in period 2, and B = {b} is the invididual's subjective time discount factor.")

print('1. How many bonds will the person buy in period 1? \n2. How much will the person consume in period 1? \n3. How much will the person consume in period 2? \n4. What is the interest rate on bonds?')

bonds = 1
c2 = y/((p/b)+p)
c1 = c2*(p/b)
r =( (1-p)/p)*100

input('Press Enter to view solution')
print(f'Solution: \n1. b = {bonds}\n2. c1 = {c1}\n3. c2 = {c2}\n4. r ={r}')
