import json
import os
import re

dir = os.path.dirname(os.path.realpath(__file__)) + '/Contacts.json'

try:
	with open(dir,"r") as f:
		contacts = json.load(f)
except Exception:
	with open(dir,"w") as f:
		contacts = {}

contacts = dict(contacts)

print("""
 ####  ###  ##    # #####  ###   #### #####     ###   ###   ###  #  #
#     #   # # #   #   #   #   # #       #       #  # #   # #   # # #
#     #   # #  #  #   #   ##### #       #       ###  #   # #   # ##
#     #   # #   # #   #   #   # #       #       #  # #   # #   # # #
 ####  ###  #    ##   #   #   #  ####   #       ###   ###   ###  #  #
""")

print("\n[GITHUB] https://github.com/aluminium65/")

input("\nPress Enter to access Menu.")

	
while True:
	
	print(
		"""
Enter the number of option you want to select and press Enter:

1, View all Contacts
2, Add new Contact
3, Delete Contact
4, Search Contact
5, Exit
	"""
	)
	try:
		option = input("  >> ")
		option = int(option)
		
	except ValueError:
		print("\nThe option must be numeric!")
	
	if option == 1:
		if len(contacts) == 0:
			print("\nYour contact list is empty.")
			print("Please add some contacts.")
		else:
			print("All Contacts: \n")
			for x in contacts.keys():
				y = contacts[x]
				print(f" {x} : {y}")
				
	
	elif option == 2:
		print("\nType the name of contact:")
		name = input("  >> ")
		
		print("Enter the Phone number:")
		number = input("  >> ")
		
		contacts[name] = number
	
	
	elif option == 3:
		print("\nEnter the name of contact you want to delete.")
		for x in contacts.keys():
			y = contacts[x]
			print(f"{x} : {y}")
					
		name = input("\n  >> ")
		del contacts[name]
	
	
	elif option == 4:
		print("\nEnter the name of contact:")
		name = input("  >> ")
		name = str(name)
		print("")

		if name == "":
			print("No name was Given!")
		
		else:
			search_result = []
			for x in contacts.keys():
				if re.search(name, x, re.IGNORECASE):
					search_result.append(x)

			if len(search_result) > 0:
				print("Here are the matches: \n")
				for loop_search in search_result:
					print(loop_search)
	
		
			if len(search_result) == 0:
				print("No matches Found!")

	
	elif option == 5:
		print("\nExiting...")
		break
	
	
	else:
		print("\nInvalid Input!")
					

with open(dir,"w") as f:
	json.dump(contacts, f, indent=4)
