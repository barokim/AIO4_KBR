
# i = 1
# print(f"2 X {i} ={2 * i}")

# for dan in range(1, 5): #1~4까지 반복
#     for i in range(2, 6): #2~5까지 반복
#          print(f"{i} X {dan} = {i * dan}", end="  ")
#          print(f"{i+1} X {dan} = {(i+1) * dan}", end="  ") 
#          print(f"{i+2} X {dan} = {(i+2) * dan}")
#          print("===============")#end=""를 쓰면 줄바꿈이 안됨, 

for dan in range(1, 10):
    for i in range(2, 10):
        print(f"{i} X {dan} = {dan*i}", end="\t")
    print("\n")
