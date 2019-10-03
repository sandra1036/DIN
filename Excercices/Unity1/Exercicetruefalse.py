
#mark
#<5 -> "fail"
#5<m<=6 -> good
#6<m<=8 -> "quite good"
#m>8-> "astonishing"

m=float(input("Mark:"))
if m<5 :
   print("fail") 
elif 5<m<=6 :
    print("good")
elif 6<m<=8 :
    print("quite good")
elif m>8 :
    print("Astonishing")


