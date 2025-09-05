#taking input amount from the user
amount=int(input("enter the amount you want to withdraw"))

#calculating the number of notes detormotiation
note1=amount//100
note2=(amount%100)//50
notes3=((amount%100)%50)//10

#printing the text
print("notes of 100 dollar:" , note1)
print("notes of 50 dollar:" , note2)
print("notes of 10 dollar:" , notes3)