from Locations import *

startingItemDict = {
	"dagger":"kitchenKnife",
	"twoHandedSword":"rustySword",
	"axe":"hatchet",
	"dualSwords":"twinBlades",
	#Note - twinBlades are a starting item, but not a base component
	#(builds out of rustySword and kitchenKnife)
	#This would cause problems, but thankfully only dualSword type weapons
	#build out of twinblades, so we're fine
	"hammer":"hammer",
	"glove":"cottonGlove"
}

componentDict = {
	"alcohol": SCHOOL | HOSPITAL | FACTORY,
	"bamboo": ARCHERYRANGE | FOREST | CEMETERY | POND | TEMPLE,
	"bandage": ALLEY | SCHOOL | HOSPITAL | DOCK,
	"battery": DOCK | AVENUE | FACTORY,
	"bikeHelmet": BEACH | SCHOOL | CHAPEL | POND,
	"binoculars": ALLEY | HOTEL | BEACH | FACTORY,
	"box": POND | CHAPEL | DOCK,
	"bracelet": ALLEY | UPTOWN | POND,
	"branch": ALL_LOCATIONS,
	"brassKnuckles": FOREST | CEMETERY,
	"buddhistScripture": TEMPLE,
	"can": BEACH | AVENUE | SCHOOL,
	"carbonatedWater": BEACH | HOTEL | UPTOWN,
	"cloth": HOTEL | AVENUE | TEMPLE,
	"cottonGloves": HOTEL | HOSPITAL,
	"cross": ALLEY | CHAPEL,
	"fabricArmor": ARCHERYRANGE | TEMPLE | FOREST | CEMETERY,
	"fan": FOREST | AVENUE | CHAPEL,
	"feather": FOREST | CEMETERY | TEMPLE,
	"fedorova": HOTEL | UPTOWN | FACTORY,
	"flower": UPTOWN | FOREST | CEMETERY | POND,
	"fountainPen": UPTOWN | AVENUE | SCHOOL,
	"gemstone": BEACH | FOREST | POND | TEMPLE,
	"glassBottle": AVENUE | CHAPEL | DOCK,
	"glue": ALLEY | HOSPITAL | FACTORY,
	"gunpowder": ARCHERYRANGE | TEMPLE | CEMETERY,
	"hammer": BEACH | ALLEY | POND,
	"hairband": CEMETERY | AVENUE | TEMPLE,
	"hat": ARCHERYRANGE | SCHOOL | POND,
	"hatchet": BEACH | POND | FACTORY,
	"healingPotion": ALL_LOCATIONS,
	"holyGrail": CHAPEL,
	"ice": HOTEL | CEMETERY | HOSPITAL,
	"ironBall": ARCHERYRANGE | FOREST | FACTORY,
	"ironOre": HOTEL | FOREST | CEMETERY,
	"kitchenKnife": DOCK | HOTEL | TEMPLE,
	"laserPointer": SCHOOL | UPTOWN | HOSPITAL,
	"leather": ALL_LOCATIONS,
	"lighter": DOCK | FACTORY | SCHOOL | ALLEY,
	"monksRobe": ARCHERYRANGE | TEMPLE,
	"mousetrap": BEACH | CEMETERY | POND,
	"nail": ARCHERYRANGE | AVENUE | FACTORY,
	"needle": ALLEY | HOTEL | HOSPITAL,
	"oil": ARCHERYRANGE | UPTOWN | FACTORY | AVENUE,
	"orientalHerb": FOREST | POND | TEMPLE,
	"paper": ARCHERYRANGE | TEMPLE | CHAPEL,
	"pianoWire": BEACH | UPTOWN | HOTEL | CHAPEL,
	"pickaxe": BEACH | FOREST | CEMETERY | POND,
	"playingCards": HOTEL | AVENUE,
	"razor": HOSPITAL | CHAPEL | SCHOOL,
	"ribbon": SCHOOL | UPTOWN | POND,
	"rubber": ALLEY | ARCHERYRANGE | DOCK,
	"runningShoes": ALLEY | ARCHERYRANGE | UPTOWN,
	"rustySword": DOCK | ARCHERYRANGE | CHAPEL,
	"scrapMetal": DOCK | HOTEL | HOSPITAL | FACTORY,
	"scissors": ALLEY | SCHOOL | HOSPITAL,
	"shortCrossbow": POND | DOCK | CHAPEL,
	"shortRod": DOCK | CHAPEL | POND,
	"slippers": SCHOOL | AVENUE | DOCK,
	"stallionMedal": ALLEY | TEMPLE | BEACH,
	"steelChain": BEACH | CEMETERY | ALLEY,
	"stone": ALL_LOCATIONS,
	"tights": FOREST | AVENUE | HOSPITAL,
	"turtleShell": BEACH | DOCK | POND,
	"twinBlades": ALL_LOCATIONS, #technically rustySword and kitcheKnife, but the only time you need twinBlades, you need exactly one and spawn with them
	"waltherPpk": HOTEL | BEACH | FACTORY,
	"watch": HOTEL | AVENUE | UPTOWN,
	"water": ALL_LOCATIONS,
	"wetsuit": BEACH | DOCK | ALLEY,
	"windbreaker": HOTEL | UPTOWN | SCHOOL
}
