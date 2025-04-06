PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

user_age = int(input("Enter your Age"))

if (user_age >= PETURKSBOUIPO_AGE):
    print(f" You can vote in Peturksbouipo ✅")
else:
    print(f"You can't vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}❎")    
if (user_age >= STANLAU_AGE):
    print("You can vote in stanlau ✅")    
else:
    print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE} ❎.")    
if (user_age >= MAYENGUA_AGE):
    print("You can vote in Mayengua ✅")  
else:
    print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE} ❎.")     