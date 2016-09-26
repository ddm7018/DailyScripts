import sys, keyring

print sys.argv[1], sys.argv[2],  sys.argv[3]

keyring.set_password("system","myphoneemail",sys.argv[1])
keyring.set_password("system","email", sys.argv[2])
keyring.set_password("system",sys.argv[2], sys.argv[3])