inp = raw_input("Dwste thn eisodo\n")
inp

inp = inp.replace('[','')
inp = inp.replace(']','')
inp = inp.split(',')
count = 0 
hmax = int(inp[0])
output = []


for i in range(len(inp)):
	count = count + 1
	#elegxw an eimai sto teleutaio 10lepto ths wras
	#kai vriskw to megisto
	if count == 6:
		#an einai h trexousa timh thn apothikeuw
		if int(inp[i]) > hmax:
			hmax = int(inp[i])
		#prosthiki ths megisths timhs gia kathe wra 
		#ston pinaka output
		output.append(hmax)
		count = 0
		hmax = int(inp[i])
	#sugkrinw thn trexousa timh me thn ews twra megisth
	#an einai megaluterh thn krataw
	if int(inp[i]) > hmax:
		hmax = int(inp[i])

		

print "[('4:00pm',", output[0],"), ('5:00pm',",output[1],"), ('6:00pm',",output[2],"), ('7:00pm',",output[3],")]"