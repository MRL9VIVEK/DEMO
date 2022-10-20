nam = [{"name" : "sumit" , "house" : "villa"},
        {"name" : "viv" , "house" : "flat"},
        {"name" : "rahul" , "house" : "mansion"}]
nam.sort(key = lambda nam: nam["house"])
print(nam)