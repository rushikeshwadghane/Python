sentemce = "Marvin, the Paranoid Android"
Letters= list(sentemce)

for char in Letters[:6]:
    print('\t',char)
print()
for char in Letters[-7:]:
    print(char)
print()

for char in Letters[12:20]:
    print('\t'*2,char)        
           
       