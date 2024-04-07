# step 1
beatles = []
print("Step 1:", beatles)

# step 2
for member in ['John Lennon', 'Paul McCartney', 'George Harrison']:
    beatles.append(member)
print("Step 2:", beatles)

# step 3
for member in ['Stu Sutcliffe', 'Pete Best']:
    beatles.append(member)
print("Step 3:", beatles)

# step 4
del beatles[-2]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0,'Ringo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
