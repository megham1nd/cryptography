coded_text = input("Enter double keyword polyalphabetic encoded message: ")
mod_text = ""

four_alpha = {"A": 0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
five_alpha = {"A": 0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
six_alpha = {"A": 0, "B":0, "C":0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}

four_val = 0
five_val = 0
six_val = 0

ic_list = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(coded_text)):
	if coded_text[i] != " ":
		mod_text += coded_text[i]

for i in range(0, len(mod_text), 4):
	four_alpha[mod_text[i]] = four_alpha.get(mod_text[i]) + 1
for i in range(len(alphabet)):
	four_val += four_alpha.get(alphabet[i])*(four_alpha.get(alphabet[i])-1)
four_val /= (sum(four_alpha.values()))*(sum(four_alpha.values())-1)

for i in range(0, len(mod_text), 5):
	five_alpha[mod_text[i]] = five_alpha.get(mod_text[i]) + 1
for i in range(len(alphabet)):
	five_val += five_alpha.get(alphabet[i])*(five_alpha.get(alphabet[i])-1)
five_val /= (sum(five_alpha.values()))*(sum(five_alpha.values())-1)

for i in range(0, len(mod_text), 6):
	six_alpha[mod_text[i]] = six_alpha.get(mod_text[i]) + 1
for i in range(len(alphabet)):
	six_val += six_alpha.get(alphabet[i])*(six_alpha.get(alphabet[i])-1)
six_val /= (sum(six_alpha.values()))*(sum(six_alpha.values())-1)


print("IC for a 4 alphabet encoding: " + str(round(four_val,3)))
print("IC for a 5 alphabet encoding: " + str(round(five_val,3)))
print("IC for a 6 alphabet encoding: " + str(round(six_val,3)))