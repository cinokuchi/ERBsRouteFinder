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