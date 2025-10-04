
ToDo = []
Completed = []


print("""
$$$$$$  $$$  $$$$ $  $ $$$$       #                   #          
  $    $   $ $    $ $  $          #     ###           #  ###
  $    $$$$$ $$$$ $$   $$$$      ###   #   #       #### #   #
  $    $   $    $ $ $     $       #  # #   # #### #   # #   #
  $    $   $ $$$$ $  $ $$$$       ###   ###        ####  ###

------------------------------By aluminium----------------------------------      


""")
print("[GITHUB] https://github.com/aluminium65/")
    
input("\nPress Enter to access the menu.")


while True:

	print("""
Enter the the number for the option you want to select and press Enter.
    
1, View all tasks
2, Add a task
3, Remove a task
4, Add to completed
5, Quit
    """)
    
	option = input("  >> ")
	option = int(option)
    
        
	if option == 1:
    
		if len(ToDo) == 0:
			print("Your list is empty!")
        
		elif len(ToDo) > 1:
			print(f"Your list has {len(ToDo)} tasks.")
            
		elif len(ToDo) == 1:
			print('Your list has one task.')
        	
		for x in range(len(ToDo)):
			for i in ToDo:
				print("\n ",x,",",i)
        
	elif option == 2:
        
		print("Enter the task:")
		add = input("  >> ")
		ToDo.append(add)
        
	elif option == 3:
		print("Your list contains following items.")
		for x in range(len(ToDo)):
			for i in ToDo:
				print("\n ",x,",",i)
        	        
		print("Enter the number of the task you want to remove:")
		remove = input("  >> ")
		remove = int(remove)
		del ToDo[remove]
    
	elif option == 4:
		print("Your list contains following items.")
		for x in range(len(ToDo)):
			for i in ToDo:
				print("\n ",x,",",i)
        		
		print("Enter the number of the task you completed.")
		comp = input("  >> ")
		comp = int(comp)
		Completed.append(ToDo[comp])

	elif option == 5:
		print("Exiting")
		break
    
	else:
		print("Invalid Input!")
		
		
