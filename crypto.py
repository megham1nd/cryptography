coded_text = input("Enter encoded message: ")
mod_text = ""
frequency_dict = {"A": 0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
trigraph_dict = {"A":[], "B":[], "C":[], "D":[], "E":[], "F":[], "G":[], "H":[], "I":[], "J":[], "K":[], "L":[], "M":[], "N":[], "O":[], "P":[], "Q":[], "R":[], "S":[], "T":[], "U":[], "V":[], "W":[], "X":[], "Y":[], "Z":[]}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#digraph_dict = {}

for i in range(len(coded_text)):
	if coded_text[i] != " ":
		mod_text += coded_text[i]

#print(mod_text)

for i in range(len(mod_text)):
	frequency_dict[mod_text[i]] = frequency_dict.get(mod_text[i]) + 1

for i in range(len(mod_text)):	
	new_val = ""

	if (i == 0):
		new_val = "." + mod_text[i+1]
	elif (i == len(mod_text)-1):
		new_val = mod_text[i-1] + "."
	else:
		new_val = mod_text[i-1] + mod_text[i+1]

	trigraph_dict.get(mod_text[i]).append(new_val)
	trigraph_dict.get(mod_text[i]).sort()
	#print(trigraph_dict)

#print(frequency_dict)
#print(trigraph_dict)


print ("".join([str(value) + "  " if value < 10 else str(value)+ " " for key, value in frequency_dict.items()]))
print ("  ".join([key for key, value in frequency_dict.items()]))

for i in range(max(frequency_dict.values())):
	print (" ".join([trigraph_dict.get(alphabet[j])[i] if i < len(trigraph_dict.get(alphabet[j])) else "  " for j in range(len(alphabet)) ]))


