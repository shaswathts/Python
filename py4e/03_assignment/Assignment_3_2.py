#print('Hey')
sc = input("Enter score: ")
score = float(sc)

if score > 1:
    print ("Invalid score")
elif score >= 0.9:
    print ("A")
elif score >= 0.8:
    print ("B")
elif score >= 0.7:
    print ("C")
elif score >= 0.6:
    print ("D")
elif score < 0.6:
    print ("F")


print("Score grade:", score)
exit()
