# car
# help - either lower or upper case you get this lists of commands -
# help - start - to start the car
        #- to stop the car
        # - to exit 

command = ""
while True:
   command = input (">").lower()
   if command == "start":
      print ("start the car")
   elif command == "stop":
      print ("stop the car")
   elif command == 'help':
      print("""
 start =     start the car
 stop = to stop the car
 quit = to quit the system
      """)
   elif command == 'quit':
      quit
   else:
      print("press help for more guidance!")
      break


