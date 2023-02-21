# take out secondary genre and the first thing that is just a number

result_data = []

o = open("data/salary_data.txt","r")
data = o.read()
data = data.splitlines()

data_list = []

for v in data:
    data_list.append(v.split())

for v in range(len(data_list)):
    del data_list[v][1] # removes "case" and "id"
    del data_list[v][8] # removes "admin"

c = open('data/clean_data.csv','w')

for i in range(len(data_list)):
    data_list[i] = ','.join(data_list[i])
    c.write(data_list[i])
    c.write("\n")

c.close()

print(data_list)