import string
import random


print("""

%%%%  %%%  %%%% %%%%         %%%%% %%%%% %   %
%  % %   % %    %           %      %     %%  %
%%%% %%%%% %%%% %%%% ###### %   %% %%%%% % % %
%    %   %    %    %        %    % %     %  %%
%    %   % %%%% %%%%         %%%%% %%%%% %   %

--------------------By aluminium------------------------

""")



print("The Aluminium Password Generator.")
print("\n[GITHUB] https://github.com/aluminium65/")
input("\n Press Enter to continue.")

print("\n Enter the length, you want your password of, in numeric characters. (i.e:4,6,23)")

while True:

	try:
		LenPass = input("  >> ")
		LenPass = int(LenPass)
		break
    
	except ValueError:
		print("The value must be numeric.")
        
        

print("\n Do you want to include numbers?(press \"y\" for Yes, \"n\" for No.)")
num_choice = input("  >> ")


print("\n Do you want to include symbols?(press \"y\" for Yes, \"n\" for No.)")
sym_choice = input("  >> ")


char = list(string.ascii_letters)


if num_choice == 'y':
	char.extend(string.digits)
	
if sym_choice == 'y':
	char.extend(string.punctuation)


def generator(length, list):
	
	Final = []
	for x in range(length):
		list_element = random.choice(list)
		Final.append(list_element)
		
	return Final


Output1 = generator(LenPass, char)
Output = "".join(Output1)


print(f"Here is your secure Password: {Output}")

