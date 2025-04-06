ADULT_AGE = 18

def age_check():
   user_age = int(input("How old is this person?: "))
   if (user_age >= ADULT_AGE):
      print("True")
   else:
      print("False")

age_check()      