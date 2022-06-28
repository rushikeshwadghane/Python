word = "bottels"
for beer_num in range(10,0,-1):
    print(beer_num,word,"of beer on the wall")
    print(beer_num,word,"of beer.")
    print("Take one down.")
    print("Take it around.")
    if beer_num==1:
        print("No more bottels of beer on the wall.")
    else:
        new_num = beer_num-1
        if new_num == 1:
            word= "bottel"
        print(new_num,word,"Of beer on the wall.")    
print()