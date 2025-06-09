# Write a program to mine a log file and find out whether it contains ‘python’.
def check_log():
    with open("log.txt" , "r") as f:
        content = f.read()

    if ("python") in content.lower():
        print("The log file contain the word 'python'.")
    else:
        print("The log file does not contain the word 'python'.")
check_log()