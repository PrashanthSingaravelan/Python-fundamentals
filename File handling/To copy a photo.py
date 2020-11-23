f1=open("My pic.JPG","wb")
f2=open("Passport size photo.jpg","rb")

for i in f2:
    f1.write(i)