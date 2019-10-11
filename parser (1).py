f1 = open("derevo.ged", "r")
f2 = open("output.txt", "w")

base = {}

for line in f1.readlines():
    words = line.split(" ")
    
    if len(words) >= 3:
        x = words[1]
        y = words[2]
        
        if y[0] == "I":
            key = words[1]
            
        if x == "GIVN":
            name = words[2]
            
        if x == "SURN":
            surn = words[2]
            value = (name[:-1], surn[:-1])
            newElem = {key:value}
            base.update(newElem)
            
        if x == "HUSB":
            husb = words[2]
            
            for k, (a, b) in base.items():
                
                if k == husb[:-1]:
                    father = a + " " + b
                    
        if x == "WIFE":
            wife = words[2]
            
            for k, (a, b) in base.items():
                
                if k == wife[:-1]:
                    mother = a + " " + b
                    
        if x == "CHIL":
            chil = words[2]
            
            for k, (a, b) in base.items():
                
                if k == chil[:-1]:
                    child = a + " " + b
                    
            r = "parents(%r, %r, %r).\n" % (child, father, mother)
            f2.write(r)
            
f2.close()
f1.close()