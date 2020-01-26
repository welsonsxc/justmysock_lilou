import base64

f = open("sources", "r")
temp = ""
for i in f:
    temp = temp + i
f.close()
temp = base64.b64encode(temp.encode("utf-8"))
# print(str(temp, "utf-8"), end="")
f = open("Lilou", "w")
f.write(str(temp, "utf-8"))
f.close()
