#Author: Faith Elledge
#Grithub_user: Elledgef
#Date: 5/4
#Description:

def find_median(numbers):
    numbers.sort()
    if len(numbers) % 2==1:
        return numbers[len(numbers)//2]
    else:
        return (numbers[len(numbers)//2] + numbers[(len(numbers)-1)//2])/2