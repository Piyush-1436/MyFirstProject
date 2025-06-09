# break is used to exit a loop immediately, even if the loop condition is still True./

for i in range(10):
    if i == 5:
        break
    print(i)

# The continue statement skips the current iteration of the loop and moves to the next iteration

for i in range(1, 6):
    if i == 3:          # Skip this iteration 
        continue
    print(i)

x = 10
if x > 5:
    pass  # Do nothing for now | It instructs to “do nothing”.
