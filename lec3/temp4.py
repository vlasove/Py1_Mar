while True:
    password = input()
    if len(password) <= 8:
        print("FAIL. TRY AGAIN")
        continue
    else:
        print("SUCCESS!")
        break
    
print("OUT OF WHILE LOOP")


