


file = open('C:/Users/user01/Desktop/f1.txt').read()




file1 = open('C:/Users/user01/Desktop/f2.txt','w')
file1.write(file)

file1.close()



'''




if file.mode=='w':
    print(file.read())
    
else:
    file1=open('C:/Users/user01/Desktop/f3.txt','w+')
    file1.write('hello this is WRITE MODE')
    print('file in read mode')
    '''