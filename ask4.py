import urllib2,sys,json,requests

town = raw_input("Dwste thn prwth polh: \n")
tomeisPrwths = [] #  edw 8a krathsoume to rate gia ka8e category
tomeisDeuterhs = []# twn 2 polewn mas
EvaluationPrwths = 0 #  teliko rate ths ka8e polhs
EvaluationDeuterhs = 0

'''
firstTown = urllib2.urlopen('https://api.teleport.org/api/urban_areas/slug:%s/scores/'%town)
town1 = firstTown.read()
data = json.loads(town1)
test = town1.split("{")
firstTotal  = 0.0

final_evaluation =""
tmpRate = "0"

for j in range(16,33):
	housing  = str(test[j])
	house = str(housing.split(",")[2])	
	for i in range(18,len(house)-2):
		tmpRate += house[i]
	print 'pros8etw: ',float(tmpRate)
	firstTotal += (float(tmpRate))
	print j,' = ', tmpRate,' ',housing  # tmpRate h ajiologisi ths category,housing olh h protash
	tmpRate = ""

omg =  str(test[32]).split(":")
print 'Evaluation: ', omg[len(omg)-1]
'''
#function gia ton upologismo tou rating ths kathe polhs. To flag an einai 1 gemizei ton 
#pinaka me tis ba8mologies apo ka8e kathgoria gia thn prwth polh an einai 2 gia thn deuterh polh.
#Epistrefei thn sunolikh ajiologisi pou pairnei apo to api, ka8ws kai gemizei tous pinakes
#me tis ba8mologies gia ka8e kathgoria.
def getEvaluation(townName,flag):
	tmpRate = "0"
	firstTown = urllib2.urlopen('https://api.teleport.org/api/urban_areas/slug:%s/scores/'%townName)
	town1 = firstTown.read()
	data = json.loads(town1)
	test = town1.split("{")

	for j in range(16,33):
		housing = str(test[j])
		house = str(housing.split(",")[2])
		for i in range(18,len(house)-2):
			tmpRate += house[i]
		#print 'to tmp rate einai', tmpRate
		if( flag is 1):
			tomeisPrwths.append(tmpRate)	
		if(flag is 2):
			tomeisDeuterhs.append(tmpRate)
		tmpRate=""

	omg = str(test[32]).split(":")			
	return omg[len(omg)-1]	

#getEvaluation(town)

EvaluationPrwths = getEvaluation(town,1)
town2 = raw_input("Dwste thn deuterh polh: \n")
EvaluationDeuterhs = getEvaluation(town2,2)

if ( str(town) == str(town2)):
	print 'dwsate 2 idies poleis. H ajiologisi tous einai: ',EvaluationPrwths
	sys.exit()

if( EvaluationDeuterhs < EvaluationPrwths):  # Sugkrisei gia na tupwsei pia exei megalutero score
	print 'h polh ',town,' yperterei ths polhs ',town2,' me score:{',EvaluationPrwths,' enadi{',EvaluationDeuterhs
elif EvaluationDeuterhs > EvaluationPrwths:
	print 'h polh ',town2,' yperterei ths polhs ',town,' me score:{',EvaluationDeuterhs,' enadi{',EvaluationPrwths
else:
	print 'oi 2 poleis einai isajies'	

uperteriPrwti = 0
uperteriDeuteri=0

#Gia to erwthma se posous tomeis uperterei h ka8e polh sugkrinoume ka8e 8esh apo tous pinakes pou periexoun to rate ths
#ka8e kathgorias kai aujanoume tous metrhtes upertereiPrwti/uperteriDeuteri analoga me to apotelesma ths sugkrishs.
for i in range(len(tomeisDeuterhs)):
	if tomeisPrwths[i]>tomeisDeuterhs[i]:
		uperteriPrwti+=1
	elif tomeisDeuterhs[i]>tomeisPrwths:
		uperteriDeuteri+=1

print 'h polh ',town,' uperterei se ',uperteriPrwti,' apo tous 17 tomeis. '
print 'h polh ',town2,' uperterei se ',uperteriDeuteri,' apo tous 17 tomeis. '


'''
starting with 16 till 
16 housing
17 cost of living
18 Startups
19 Venture Capital
20 Travel connectivity
21 Commute
22 Buisiness Freedom
23 Safety
24 Healthcare
25 Education
26 Enviromental
27 Economy
28 Taxation
29 Internet Access
30 Leisure
31 Tolerance
32 Outdoors
'''