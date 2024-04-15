# ERBsRouteFinder
 ---
 Usage
 ---
 For each folder in "equipment/\*", enter the "ignore" directory and move any items you want to consider up one directory. Then open a terminal, navigate to the root project directory and run "python3 main.py".

 This will generate two files, "lastRun/threeZone.txt" and "lastRun/fourZone.txt",
 containing all possible builds that can be completed in three zones plus 2 buys and all possible
 builds that can be completed in four zones with 0 buys respectively.
 
 Re-running the tool will overwrite "lastRun/threeZone.txt" and "lastRun/fourZone.txt" if they
 already exist. Renaming or moving the files will preserve them.


 ---
 Adding items
 ---
 The RouteFinder as provided does not contain every item.
 Adding items is simple - each item file is a json file mapping component names to the number
 of said components required for the completed item. Make sure to double check the spelling and
 capitalization of component names.

 ---
 The route finder is old
 ---
 I created this route finder in 2022 and promptly lost interest in ERBs.
 Any changes to the map or existing items will break the route finder.
 You may fix any existing item json files yourself.
 Fixing map zones is more involved - you will have to create new enumerations for the locations
 and regenerate all of the threezone/fourzone combinations under Locations.py,
 then also go to the ComponentDict and redo all of the locations for the components.
