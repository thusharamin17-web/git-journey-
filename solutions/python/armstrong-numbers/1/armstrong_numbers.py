def is_armstrong_number(number):
    arm_check=0
    original=number
    num=number
    str_num=str(number)
    l=len(str_num)
    while num>0:
        rem=num%10
        arm_check+=rem**l
        num=num//10
    return arm_check==original
        
    
