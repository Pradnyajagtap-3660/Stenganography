# import cv2
# import os
# import string

# img = cv2.imread("mypic.jpg") # Replace with the correct image path

# msg = input("Enter secret message:")
# password = input("Enter a passcode:")

# d = {}
# c = {}

# for i in range(255):
#     d[chr(i)] = i
#     c[i] = chr(i)

# m = 0
# n = 0
# z = 0

# for i in range(len(msg)):
#     img[n, m, z] = d[msg[i]]
#     n = n + 1
#     m = m + 1
#     z = (z + 1) % 3

# cv2.imwrite("encryptedImage.jpg", img)
# os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

# message = ""
# n = 0
# m = 0
# z = 0

# pas = input("Enter passcode for Decryption")
# if password == pas:
#     for i in range(len(msg)):
#         message = message + c[img[n, m, z]]
#         n = n + 1
#         m = m + 1
#         z = (z + 1) % 3
#     print("Decryption message:", message)
# else:
#     print("YOU ARE NOT auth")


import cv2
import os

# Load imagey
img = cv2.imread("Stenography-main/mypic.jpg")


# Check if image is loaded
if img is None:
    print("Error: Could not load image. Check the file path!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# ASCII Mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

n, m, z = 0, 0, 0

# Encode message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through BGR channels

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the encrypted image on Windows

# Decryption
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")

