# TASK: number guess game
# 1. Lower bound = 1, upper bound = 100
# 2. Generate an integer between lower and upper bounds - N
# # 3. In a while loop:
## 3. Ask user for a guess between lower and upper bounds - G
## 4. Check if G is lower or upper from N
## 5. If U:
### 6. Print "Too high"
## 7. If L:
### 8. Print "Too low"
## 9. If C:
### 10. Congratulate the user and show the number of guesses user have made

from random import randrange

min = 1
max = 100
eded = randrange(min, max)
count = 0
while True:
    try:
        myguess = int(input(f"{min}-{max} arasi eded de: "))
        count += 1
        if count == 7:
            print("Sansini kaybettin")
            break
        if myguess < min or myguess > max:
            print("Out of range")
            continue
        if myguess > eded:
            max = myguess
            print("Too high")
            continue
        elif myguess < eded:
            min = myguess
            print("Too low")
        else:
            print(f"Congrats! {myguess} is correct. You found ")
            break
    except:
        print("Invalid input")