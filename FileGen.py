# Imports
import random
import os
import shutil

# Global variables
nbr_of_file = 1000
nbr_of_fldr_lvl = 4
nbr_of_fldr_per_lvl = 32
min_byte = 1
max_byte = 150000
otpt_locn = "OutOrgl\\"

# Clear existing data from Out directory
if os.path.exists(otpt_locn):
    shutil.rmtree(otpt_locn)

for file_nbr in range (0, nbr_of_file):
    # Choose a random number of bytes for the file:
    nbr_of_byte = random.randint(min_byte, max_byte)

    # Choose whether the file is ASCII or binary
    is_binary = random.randint(0, 1)

    # Choose if the file goes into a folder or not
    locn = otpt_locn
    
    #Pick random level
    fldr_lvl = random.randint(1, nbr_of_fldr_lvl) 
    for lvl in range(0, fldr_lvl):
        # Pick random folder number
        fldr_nbr = random.randint(0, nbr_of_fldr_per_lvl)
        locn += "Folder" + str(lvl) + "_" + str(fldr_nbr) + "\\"
    if not os.path.exists(locn):
        os.makedirs(locn)

    # Open the file
    f = open(locn + "File" + str(file_nbr + 1) + ".txt", "w+")

    # Loop to write randomly chosen number of characters
    for character in range (0, nbr_of_byte):
        if is_binary:
            f.write(chr(random.randint(0,255)))
        else:
            f.write(chr(random.randint(32,128)))

    # Close the file
    f.close()