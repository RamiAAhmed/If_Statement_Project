# Q8
bill = int(input('Please Enetr your consumption in units '))
if bill<=100:
    print ('Total Bill Amount is Rs00')
elif 100<bill<=200:
    bill_1=bill-100
    print ('Total Bill Amount is ', bill_1*5)
else:
    bill_2=bill-200
    print ('Total Bill Amount is ', 500+bill_2*10)   

# Q1
marks = int(input('Please Enetr your Marks '))
if marks> 90:
    print('Your Grade is A')
elif 90>=marks>80:
    print('Your Grade is B')
elif 80>=marks>=60:
    print('Your Grade is C')
elif 60>marks:
    print('Your Grade is D')

# Q2
bike_cost = int(input('Please Enetr the bike cost price '))
if bike_cost<=50000:
    print ('Road Tax is', bike_cost*.05)
elif 50000<bike_cost<=100000:
    print ('Road Tax is', bike_cost*.1)
else:
    print ('Road Tax is', bike_cost*.15)

# Q5
a = int(input('Enter First Number ')) 
b=  int(input('Enter Second Number ')) 
print(' First Number is Lrager') if a>b else print(' Second Number is Lrager')    

# Q6
number = int(input('Enter a Number ')) 
print(' Positive Number') if number>=0 else print('Negative Number') 

# Q7
num_1,num_2,num_3 = int(input('Enter first Number ')),int(input('Enter second Number ')),int(input('Enter third Number '))
if num_1>num_2 and num_1>num_3:
    print('The Lragest number is first number; equal to', num_1)
elif num_2>num_1 and num_2>num_3:
    print('The Lragest number is second number; equal to', num_2)
else:
    print('The Lragest number is third number; equal to', num_3)    

# Q8
percentage = int(input('Please Enetr your percentage '))
if percentage>100 or percentage<0:
    print('Not Valid')
elif percentage> 80:
    print('Your Grade is A+')
elif 80>=percentage>60:
    print('Your Grade is A')
elif 60>=percentage>50:
    print('Your Grade is B+')
elif 50>=percentage>45:
    print('Your Grade is B')
elif 45>=percentage>25:
    print('Your Grade is C')
else:
    print('Your Grade is D')   
