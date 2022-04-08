critics={}
myfile = open("critics.csv","r")
lines = myfile.readlines()

for line in lines: 
    line = line.strip()
    line = line.split(",")
    
    name = ""
    ratings = {}
    i = 0

    while i < len(line) - 1:

        if i == 0:
            name = line[i]
        else:
            if i % 2 != 0:
                if i < len(line):
                    ratings[line[i]] = line[i+1]
                
        i = i + 1

    critics[name] = ratings
    
print(critics)
