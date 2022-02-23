mark_list = [
              [1,"Ananya",50],
              [2,"Akshaya",99],
              [3,"Shyam",100],
              [4,"Ariana",70],
              ]

print("|  Roll_Number  |  Student_Name  |  Marks_Obtained  |")

for item in mark_list:
    print("|",item[0]," "*(12-len(str(item[0]))),"|",
    item[1]," "*(13-len(item[1])),"|",
    item[2]," "*(15-len(str(item[2]))),"|")


print()
print("|  Roll_Number  |  Student_Name  |  Marks_Obtained  |")
for i in range(len(mark_list)):
    if i==1:
        print("|",mark_list[i][0]," "*(12-len(str(mark_list[i][0]))),"|",
        mark_list[i][1]," "*(13-len(mark_list[i][1])),"|",
        mark_list[i][2]," "*(15-len(str(mark_list[i][2]))),"|")