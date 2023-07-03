coded_text = input("Enter double keyword polyalphabetic encoded message: ")
alpha = int(input("Search up to: "))

mod_text = ""
ic_list = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(coded_text)):
	if coded_text[i] != " ":
		mod_text += coded_text[i]

for i in range(4, alpha+1):
	freq_dict = {"A": 0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
	ic = 0

	for j in range(0, len(mod_text), i):
		freq_dict[mod_text[j]] = freq_dict.get(mod_ text[j]) + 1

	for j in range(len(alphabet)):
		ic += freq_dict.get(alphabet[j])*(freq_dict.get(alphabet[j])-1)
	ic /= (sum(freq_dict.values()))*(sum(freq_dict.values())-1)	
	ic_list.append(ic)

for i in range(0, len(ic_list)):
	print("IC for a {} alphabet encoding: {}".format(i+4, round(ic_list[i], 3)))


select = int(input("Select encoding scheme to continue: "))
group_freq = [{"A": 0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0} for _ in range(select)]
group_list = [[] for _ in range(select)]

rounded_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(mod_text)):
	group = i % select
	group_freq[group][mod_text[i]] = group_freq[group].get(mod_text[i]) + 1

print(" ")
for i in range(select):
	print(" ".join([rounded_alphabet[i] for i in range(52)]))
	for j in range(max(group_freq[i].values())):
		print(" ".join(["X" if j < group_freq[i].get(rounded_alphabet[k]) else " " for k in range(len(rounded_alphabet))]))
	print(" ")

final_map = ""
final_array = []
def mapping():
	global final_map
	global final_array
	map = input("Map: ")
	if map != "DONE":
		final_array = []
		for i in range(len(map)):
			print(" ".join([rounded_alphabet[k+alphabet.find(map[i])] for k in range(26)]))
			final_array.append(rounded_alphabet[alphabet.find(map[i]):alphabet.find(map[i])+26])
		final_map = map
		mapping()
mapping()
print(" ".join([alphabet[i] for i in range(26)]))

collapsed_code = ""
for i in range(0, len(mod_text)):
	group = i % select
	collapsed_code += alphabet[final_array[group].find(mod_text[i])]
print(collapsed_code)

	

