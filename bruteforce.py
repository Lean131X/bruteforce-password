import time

# Secret password
secret_password = "yaQ@"

# Characters allowed (lowercase, uppercase, numbers, symbols)
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

def crack_password(secret_password, characters):
    total_attempts = 0
    start = time.time()

    # Length 1
    for a in characters:
        total_attempts += 1
        if a == secret_password:
            return show(secret_password, a, total_attempts, start)

    # Length 2
    for a in characters:
        for b in characters:
            guess = a + b
            total_attempts += 1
            if guess == secret_password:
                return show(secret_password, guess, total_attempts, start)

    # Length 3
    for a in characters:
        for b in characters:
            for c in characters:
                guess = a + b + c
                total_attempts += 1
                if guess == secret_password:
                    return show(secret_password, guess, total_attempts, start)

    # Length 4
    for a in characters:
        for b in characters:
            for c in characters:
                for d in characters:
                    guess = a + b + c + d
                    total_attempts += 1
                    if guess == secret_password:
                        return show(secret_password, guess, total_attempts, start)

def show(secret_password, found, total_attempts, start):
    end = time.time()
    print("Password found:", found)
    print("Attempts made:", total_attempts)
    print("Time taken:", round(end - start, 4), "seconds")

crack_password(secret_password, characters)
