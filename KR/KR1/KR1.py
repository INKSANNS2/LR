sorted_str =input("Введите анаграммы через запятую: ")
str=sorted_str.lower()
sort=str.split(", ")
a=sort[0]
b=sort[1]
a= ''.join(sorted(a))
b= ''.join(sorted(b))
a=a.replace(" ","")
b=b.replace(" ","")
if a==b:
    print("Это анаграмма")
else:
    print("Это не анаграмма")