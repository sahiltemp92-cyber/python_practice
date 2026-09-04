with open("sample.txt", "r") as file:
    print(file.read())


try:
    with open("sample.txt", "a") as file:
        file.write("\nI love automation.")
except Exception as e:
    print(e)

try: #  Try block -> Executes if no error occurs
    with open("sample.txt", "r") as file:
        print(file.read())
except Exception as e: # Exception block -> Executes if try block fails
    print(e)

finally: # Always executes
    print("File operations completed")

# File modes
# r -> read
# w -> write
# a -> append
# x -> create
# r+ -> read and write
# w+ -> write and read
# a+ -> append and read