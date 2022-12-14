'''

# FileNotFound
with open("my_file.txt") as file:
    file.read()

# KeyError
a_dictionary = {"key", "value"}
value = a_dictionary["non_existent_key"]

# IndexError
language_list = ["Java", "Python", "C#"]
language = language_list[3]

# TypeError
text = "abc"
print(text + 5)

'''

# try: something that might cause an exception

# except: do this if there was an exception

# else: do this if there were no exceptions

# finally: do this no matter what happens

########################################################################################################################

# FileNotFound

try:
    file = open("my_file.txt")
    a_dictionary = {"key", "value"}
#   value = a_dictionary["non_existent_key"]
# except:  # do not use bare except
#     print("No such file.")
#     file = open("my_file.txt", "w")
except FileNotFoundError:
    file = open("my_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
 #  raise KeyError #raise our own Exceptions


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = weight / height ** 2
print(bmi)
