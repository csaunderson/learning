age = { "Peter": 5, "John": 10}

for i in age:
        print(i)

for i in age:
        print("Name = %s, Age = %d" %(i,age[i]))

for i, j in age.items():
        print("Name = %s, Age = %d" %(i,j))