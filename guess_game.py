secret_number = 42
attempts = 0

while True:
    guess = int(input("Угадай число от 1 до 100: "))
    attempts +=1
    if guess == secret_number:
        print(f"Угадал! Тебе понадобилось {attempts} попыток.")
        break
    elif guess < secret_number:
        print("Моё число больше ⬆️")
    else:
        print("Моё число меньше ⬇️")
