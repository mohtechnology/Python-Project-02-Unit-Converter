try:
  print("1 - Length \n2 - Temperature")
  choise = int(input("Enter Your Choise : ")) # 1 - length, 2 - temperature
  
  # code for length
  if choise == 1:
    length = float(input("Enter Your Length in meter : "))
    print("1 - Kilometer \n2 - Feet")
    # taking choise as an input
    length_choise = int(input("Enter Your Choise : ")) # 1 - Kilometer, 2 - feet
    if length_choise == 1:
      print(f"{length / 1000} Kilometer")
    elif length_choise == 2:
      print(f"{length * 3.28084} Feet")
    else:
      print('INVALID CHOISE')
  
  # code for temperature
  elif choise == 2:
    temp = float(input("Enter your temperature in celcius : "))
    print(f"{(temp * 9/5) + 32} Fahrenheit")
  
  else:
    print('INVALID CHOISE')

except:
  print('PLEASE TRY AGAIN')
