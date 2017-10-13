# h eisodos einai sthn morfh [[1,2,3],[1,1,1,1,1],[2,3],[4,1]],6 
inp = raw_input("Dwste thn eisodo\n")
inp
inp = inp.replace('[','')
output = inp.split("],")

for i in range(len(output)):
	output[i] = output[i].replace(']','')
total = int(output.pop()) 		#apothikeush ths teleutaias parametrou(sunolika provata) sto total 
daysum = 0 		#metavlhth apothikeushs tou athroismatos twn provatwn kathe mera
lost=0 		#sunolo xamenwn provatwn

#gia kathe mera upologizw to sunolo twn provatwn pou gurisan
for i in range(len(output)):
	day = []
	day = output[i].split(",")
	for j in range(len(day)):
		daysum += int(day[j])
	#an ta provata pou gurisan einai ligotera apo ta sunolika 
	#upologizw posa xathikan
	if daysum < total:
		lost = total - daysum
	daysum = 0

print(lost)


