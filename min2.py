#take mark as inpuut for user
print("Enter Marks Obtained in 4 subjects")
math=int(input("math"))
english=int(input("english"))
science=int(input("science"))
hindi=int(input("hindi"))

#Let's calculate the percentage of the marks
sum = math+english+science+hindi
print("sum of math,english,science and hindi",sum)

perc=(sum/400)*100

print(perc)