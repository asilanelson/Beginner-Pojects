# car
# help - either lower or upper case you get this lists of commands -
# help - start - to start the car
        #- to stop the car
        # - to exit 
started = False
command = ""
while True:
   command = input (">").lower()
   if command == "start":
      if started:
         print("car already started") 
      else:
         started = True
         print ("start the car")
   elif command == "stop":
      if not started:
         print (" the car is already stopped")
      else:
         started = False
         print(" stop the car")
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


