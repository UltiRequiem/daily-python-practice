NUMBER_LIST = [12, 67, 98, 34]
  
print("The original list is : " + str(NUMBER_LIST))
  
RESULT = list(map(lambda i: sum(int(char) for char in str(i)), NUMBER_LIST))
      
print ("List Integer Summation : " + str(RESULT))
