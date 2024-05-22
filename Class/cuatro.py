print("Guess the Number 🤑")

def generate_number(seed):
    seed = (seed * 1234 + 12345) % (2**10)
    return (seed % 20) + 1  

def guess_number():
    seed = 123456789 
    attempts = 0
    secret_number = generate_number(seed)
    
    while True:
        guess = int(input("di un numero de 0 a 20: "))
        attempts += 1
        
        if guess < secret_number:
            print("demasiado bajo de nuevo.")
        elif guess > secret_number:
            print("muy alto de nuevo")
        else:
            print(f"Lo conseguiste en  {attempts} intentos ")
            break

guess_number()
