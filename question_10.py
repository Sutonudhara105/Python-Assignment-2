princ = int(input("Input Principal Amount"))
if princ<200000:
    intr = princ*10/100
elif 200000<princ<1000000:
    intr = princ*12/100 
else:
    intr = princ*15/100  
print(f"Interest on {princ} is : {intr}")
