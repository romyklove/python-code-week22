for i in ['red', 'orange', 'black', 'purple']:
    print(i)

num_v=0
num_c=0
_string= input("please enter your name: ")
for i in _string.strip():
    if i in ['a','e','i','o','u']:
      print(f"{i} is a vowel")
      num_v+=1
    else:
      print(f"{i} is a consonant")
      num_c+=1

print(f" number od vowel: {num_v}")
print(f"number of consonant is: {num_c}")


