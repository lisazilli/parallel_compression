# Imports
import os

# Global variables
def are_fldr_same(orgl_locn, extr_locn):
    same_name_and_nbr_of_file = False
    all_files_same = False
    orgl_files = os.listdir(orgl_locn)
    extr_files = os.listdir(extr_locn)

    # Check to make sure the number of files are the same
    if orgl_files <> extr_files:   
        return False

    for file_nbr in range(0,len(orgl_files)):
        # Open both files
        if os.path.isdir(orgl_locn + orgl_files[file_nbr]) and os.path.isdir(extr_locn + extr_files[file_nbr]):
            # Recursively check this file
            if not are_fldr_same(orgl_locn + orgl_files[file_nbr] + "\\", extr_locn + extr_files[file_nbr] + "\\"):
                return False
        else:
            orgl_file = open(orgl_locn + orgl_files[file_nbr], "r")
            extr_file = open(extr_locn + extr_files[file_nbr], "r")

            # Loop to write randomly chosen number of characters
            orgl_text = orgl_file.read()
            extr_text = extr_file.read()

            if orgl_text <> extr_text:
                return False
            # Close the files
            orgl_file.close()
            extr_file.close()
    return True
print("Are folders same? " + str(are_fldr_same("OutOrgl\\", "OutExtr\\OutOrgl\\")))

    