from random import randint

UPPER_CASE="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER_CASE=UPPER_CASE.lower()
SPECIAL_CHARACTERS="!@#$%^&*(){}[]?\|><~`+-_,."
NUMBERS="0123456789"
ALL=UPPER_CASE+ LOWER_CASE+SPECIAL_CHARACTERS+NUMBERS

def generate_password(length,sequence):

    #Generates the password by taking the length and sequence
    
    temp_password=""
    
    for i in range(length):
        num=randint(0,len(sequence)-1)
        temp_password+=sequence[num]
        
    return temp_password

def get_input(text):

    #Get user input and validate that it is a positive integer.

    while True:
        
        try:
            value=int(input(text))
            if value <0:
                print("\nPlease enter a positive number")
            else:
                return value
        except:
            print("\nInvalid input. Please enter a valid number!!")
            
    
def main():
    
    print("\t\t*** Welcome to  Random Password Generator ***\n")

    password_length=get_input("\nEnter the length of your password you want to generate: ")
    
    password=""


    if password_length<=0:
        print("Password Length should be greater than Zero")
        return
    
    nums=get_input("\nHow many numbers do you want in the password : ")
    num_upper=get_input("\nHow many uppercase charatcers do you want in the password : ")
    num_lower=get_input("\nHow many lowercase charatcers do you want in the password : ")
    num_special=get_input("\nHow many special charatcers do you want in the password :  ")

    total_chars=nums+num_upper+num_lower+num_special

    if total_chars > password_length:
        print("\nTotal characters exceed Password length!!")
        print("\nPassword length:",password_length,".The length you given for the characters is",total_chars)
        return
    
    password+=generate_password(nums,NUMBERS)
    password+=generate_password(num_upper,UPPER_CASE)
    password+=generate_password(num_lower,LOWER_CASE)
    password+=generate_password(num_special,SPECIAL_CHARACTERS)
          
    if password_length-total_chars>0:
            password+=generate_password(password_length-total_chars,ALL)

    print("\nGenerated Password:",password)


if __name__ == "__main__":
    main()


      


