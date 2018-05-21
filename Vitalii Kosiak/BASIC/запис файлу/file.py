print("File will be open or create new \n")
f = open('test.txt', 'w')

txtwrite = input("Enter text for write in file \n")
f.write(txtwrite)
f.close()
