file_name = "animal.txt"
data = open(file_name)
an = "lion"
ampt = ""
for each in data.readlines():
    print("bruh",each.replace("cat",f"{an}"))
    ampt = ampt + each.replace("cat",f"{an}")
    
with open(f"animal2+{an}", 'w') as file_object:
    file_object.write(ampt)