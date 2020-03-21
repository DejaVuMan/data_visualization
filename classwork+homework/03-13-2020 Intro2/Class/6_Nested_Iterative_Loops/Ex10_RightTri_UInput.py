# This program creates a right triangle with the letter A of increasing width per line. the limit is 10.
def pypart(n): 
      
    # outer loop to handle number of rows (vertical)
    # n in this case 
    for i in range(0, n): 
      
        # inner loop to handle number of columns (horizontal)
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing letter A 
            print("A",end="") 
       
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = input("How many lines would you like your triangle to have?")
n = int(n)
pypart(n) 