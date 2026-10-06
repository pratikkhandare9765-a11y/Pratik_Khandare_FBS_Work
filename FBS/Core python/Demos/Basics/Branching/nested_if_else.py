gender = input('Enter gender (F/M):')
age = int (input('Enter age:'))

if(gender== 'F'):
    if(age >= 18):
        print('girl is eligible for marriage.')

    else:
        print('girl is not eligibal for marriage.')

else:
    if(age >= 21):
        print('boy is eligible for marriage.')   

    else:
        print('boy is not eligible for marriage.')             
        