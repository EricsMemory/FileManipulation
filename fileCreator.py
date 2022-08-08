import os
fileName = input("What is the name of your file? ")
filePath = input("Which directory would you like to save the file in? ")

file = os.path.join(filePath, fileName)

userName = input("Enter your name: ")
userAddy = input("Enter your address: ")
userPN = input("Enter your phone number: ")

with open(file, 'w') as fileHandle:
  fileHandle.write(f'{userName}, {userAddy}, {userPN}')

with open(file, 'r') as fileHandle:
  yourFile = fileHandle.read()

print(f'Your file reads: {yourFile}')
