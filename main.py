from Locations import *
from Process import *
import os

FULL_ROUTES_DIR = "lastRun/"
THREE_ZONE_FULL_ROUTES_PATH = FULL_ROUTES_DIR + "threeZone.txt"
FOUR_ZONE_FULL_ROUTES_PATH = FULL_ROUTES_DIR + "fourZone.txt"

def main():
	if not os.path.exists(FULL_ROUTES_DIR):
		os.makedirs(FULL_ROUTES_DIR)
	try:
		os.remove(THREE_ZONE_FULL_ROUTES_PATH)
	except OSError:
		pass
	try:
		os.remove(FOUR_ZONE_FULL_ROUTES_PATH)
	except OSError:
		pass
	
		
	# prepEquipDicts
	weaponDict = readWeaponDir()
	chestDict = readEquipDir("chest")
	headDict = readEquipDir("head")
	armDict = readEquipDir("arm")
	bootDict = readEquipDir("boot")
	accDict = readEquipDir("accessory")

	# partial process threeZoneRoutes:
	for weaponName, weaponTuple in weaponDict.items():
		weaponThreeZoneRoutes = []
		procWeaponThreeZoneRoutes(THREE_ZONE_LIST,weaponThreeZoneRoutes,weaponTuple)
		if not weaponThreeZoneRoutes:
			continue
		for chestName, chestList in chestDict.items():
			chestThreeZoneRoutes = []
			procThreeZoneRoutes(weaponThreeZoneRoutes,chestThreeZoneRoutes,chestList)
			if not chestThreeZoneRoutes:
				continue
			for headName, headList in headDict.items():
				headThreeZoneRoutes = []
				procThreeZoneRoutes(chestThreeZoneRoutes,headThreeZoneRoutes,headList)
				if not headThreeZoneRoutes:
					continue
				for armName, armList in armDict.items():
					armThreeZoneRoutes = []
					procThreeZoneRoutes(headThreeZoneRoutes,armThreeZoneRoutes,armList)
					if not armThreeZoneRoutes:
						continue
					for bootName, bootList in bootDict.items():
						bootThreeZoneRoutes = []
						procThreeZoneRoutes(armThreeZoneRoutes,bootThreeZoneRoutes,bootList)
						if not bootThreeZoneRoutes:
							continue
						for accName, accList in accDict.items():
							accThreeZoneRoutes = []
							procThreeZoneRoutes(bootThreeZoneRoutes,accThreeZoneRoutes,accList)
							if accThreeZoneRoutes:
								with open(THREE_ZONE_FULL_ROUTES_PATH, 'a') as f:
									hasBeenPrinted = False
									for routeEntry in accThreeZoneRoutes:
										if not hasBeenPrinted:
											hasBeenPrinted = True
											f.write("===================================\n")
											f.write(weaponName + ", "
													+ chestName + ", "
													+ headName + ", "
													+ armName + ", "
													+ bootName + ", "
													+ accName + '\n')
										f.write('\t' + routeAsString(routeEntry[0]) + '\n')
										if routeEntry[2]:
											f.write("\t\tremainingItems: ")
											for itemEntry in routeEntry[2]:
												f.write(itemEntry[0] + ", ")
										f.write('\n')

	# partial process fourZoneRoutes:
	for weaponName, weaponTuple in weaponDict.items():
		weaponFourZoneRoutes = []
		procWeaponFourZoneRoutes(FOUR_ZONE_LIST,weaponFourZoneRoutes,weaponTuple)
		if not weaponFourZoneRoutes:
			continue
		for chestName, chestList in chestDict.items():
			chestFourZoneRoutes = []
			procFourZoneRoutes(weaponFourZoneRoutes,chestFourZoneRoutes,chestList)
			if not chestFourZoneRoutes:
				continue
			for headName, headList in headDict.items():
				headFourZoneRoutes = []
				procFourZoneRoutes(chestFourZoneRoutes,headFourZoneRoutes,headList)
				if not headFourZoneRoutes:
					continue
				for armName, armList in armDict.items():
					armFourZoneRoutes = []
					procFourZoneRoutes(headFourZoneRoutes,armFourZoneRoutes,armList)
					if not armFourZoneRoutes:
						continue
					for bootName, bootList in bootDict.items():
						bootFourZoneRoutes = []
						procFourZoneRoutes(armFourZoneRoutes,bootFourZoneRoutes,bootList)
						if not bootFourZoneRoutes:
							continue
						for accName, accList in accDict.items():
							accFourZoneRoutes = []
							procFourZoneRoutes(bootFourZoneRoutes,accFourZoneRoutes,accList)
							if accFourZoneRoutes:
								with open(FOUR_ZONE_FULL_ROUTES_PATH, 'a') as f:
									hasBeenPrinted = False
									for routeEntry in accFourZoneRoutes:
										if not hasBeenPrinted:
											hasBeenPrinted = True
											f.write("===================================\n")
											f.write(weaponName + ", "
													+ chestName + ", "
													+ headName + ", "
													+ armName + ", "
													+ bootName + ", "
													+ accName + '\n')
										f.write('\t' + routeAsString(routeEntry[0]) + '\n')

if __name__ == "__main__":
    main()