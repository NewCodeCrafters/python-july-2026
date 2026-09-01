attempts = 0
max_attempts = 3
success = False

while attempts < max_attempts and not success:
    attempts += 1
    print(f"Attempt {attempts}...")
    success = (attempts == 3)

print("Done!" if success else "Failed after max attempts")