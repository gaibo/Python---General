list_file = open("/workshop/contact_list.txt", "r")
output_file = open("/workshop/info.csv", "w")
for line in list_file:
	words = line.split()
	for word in words:
		if word.find("@") != -1:
			output_file.write("," + word + ",")
		elif word.find("865") != -1 or word.find("423") != -1:
			output_file.write(word + " ")
		else:
			output_file.write(word + " ")
	output_file.write("\n")
output_file.close()
list_file.close()