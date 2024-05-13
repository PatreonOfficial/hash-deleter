# Hash Deleter
Deletes files in a directory based on *identical* file hashes.

# How to run:
 ## (S)etup:
  Select the folder of your source files (Might be relative or absolute)
  > E.g.  
  > Absoulute: "C://yourFolderStructure/directory"  
  > Relative: "directory"
 
 ## (A)uto:
  Tries to automatically find identical files and deletes them  
  This uses the before defined directory


 ## (M)anual:
  Manually add a files hash by its name and deletes all files with the same hash  
  This uses the before defined directory
  
  >E.g.  
  > "TotallyLegitFile.jpeg"

 ## (H)elp
  Displays some help that might be usefull  

# INFO
Files are not immediately deleted, they are moved to "/delme/"