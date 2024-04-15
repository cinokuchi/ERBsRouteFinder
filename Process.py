from ComponentDict import *
from Locations import routeAsString
import json
import os.path

def procThreeZoneRoutesHelper(currRoute, numRemainingItems, leftoverList, startingItem, itemList, newThreeZoneRoutes):
	newLeftoverList = leftoverList.copy()
	for itemEntry in itemList:
		itemName = itemEntry[0]
		itemCount = itemEntry[1]
		locSet = itemEntry[2]
		if startingItem and startingItem == itemName:
			startingItem = None
			itemCount -= 1
			if itemCount == 0:
				continue
		if locSet & currRoute:
			continue
		numRemainingItems += itemCount
		if numRemainingItems > 2:
			break
		newLeftoverList.append((itemName, itemCount, locSet))
	if numRemainingItems <= 2:
		newThreeZoneRoutes.append((currRoute, numRemainingItems, newLeftoverList, startingItem))

def procWeaponThreeZoneRoutes(rawThreeZoneRoutes, newThreeZoneRoutes, weaponTuple):
	for route in rawThreeZoneRoutes:
		procThreeZoneRoutesHelper(route, 0, [], weaponTuple[0], weaponTuple[1], newThreeZoneRoutes)

def procThreeZoneRoutes(threeZoneRoutes, newThreeZoneRoutes,itemList):
	for routeEntry in threeZoneRoutes:
		procThreeZoneRoutesHelper(routeEntry[0], routeEntry[1], routeEntry[2], routeEntry[3], itemList, newThreeZoneRoutes)

def procFourZoneRoutesHelper(currRoute, startingItem, itemList, newFourZoneRoutes):
	saveRoute = True
	for itemEntry in itemList:
		itemName = itemEntry[0]
		itemCount = itemEntry[1]
		locSet = itemEntry[2]
		if startingItem and startingItem == itemName:
			startingItem = None
			itemCount -= 1
			if itemCount == 0:
				continue
		if not locSet & currRoute:
			saveRoute = False
			break
	if saveRoute:
		newFourZoneRoutes.append((currRoute, startingItem))

def procWeaponFourZoneRoutes(rawFourZoneRoutes, newFourZoneRoutes, weaponTuple):
	for route in rawFourZoneRoutes:
		procFourZoneRoutesHelper(route, weaponTuple[0], weaponTuple[1], newFourZoneRoutes)

def procFourZoneRoutes(fourZoneRoutes, newFourZoneRoutes,itemList):
	for routeEntry in fourZoneRoutes:
		procFourZoneRoutesHelper(routeEntry[0], routeEntry[1], itemList, newFourZoneRoutes)

def getItemListFromEquipMap(equipMap):
	itemList = []
	for itemName, itemCount in equipMap.items():
		itemList.append((itemName, itemCount, componentDict[itemName]))
	return itemList

def readEquipDir(dirName):
	equipDirPath = "./equipment/" + dirName + "/"
	equipDict = {}
	for equipFileName in os.listdir(equipDirPath):
		if os.path.isfile(equipDirPath + equipFileName):
			equipName = os.path.splitext(equipFileName)[0]
			with open(equipDirPath + equipFileName, 'r') as f:
				itemMap = json.load(f)
			equipDict[equipName] = getItemListFromEquipMap(itemMap)
	return equipDict

def readWeaponDir():
	weaponDirPath = "./equipment/weapon/"
	weaponDict = {}
	for weaponFileName in os.listdir(weaponDirPath):
		if os.path.isfile(weaponDirPath + weaponFileName):
			weaponName = os.path.splitext(weaponFileName)[0]
			with open(weaponDirPath + weaponFileName, 'r') as f:
				weaponPair = json.load(f)
			weaponDict[weaponName] = (startingItemDict[weaponPair[0]], getItemListFromEquipMap(weaponPair[1]))
	return weaponDict

def printThreeZoneRoutes(threeZoneRoutes):
	for routeEntry in threeZoneRoutes:
		print('\t' + routeAsString(routeEntry[0]))
		if routeEntry[2]:
			print("\t\tremainingItems: ", end = '')
			for itemEntry in routeEntry[2]:
				print(itemEntry[0], end = ", ")
		print()

def printFourZoneRoutes(fourZoneRoutes):
	for routeEntry in fourZoneRoutes:
		print('\t'+routeAsString(routeEntry[0]))
	print()
