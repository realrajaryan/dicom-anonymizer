###############################################################################
# MIT License
#
# Copyright (c) 2021-2022 Raj Aryan Singh
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
###############################################################################

# imports
import python, os
    
# Function that anonymizes the DICOM file
# headers, by replacing the appropriate
# fields with an empty string and then writes
# it in the "anonymized" folder in the same 
# directory as of the file.
def anonymize(path, file_identifier='1'):
    dicInfo = pydicom.read_file(path)
    
    dicInfo.ReferringPhysicianName = ''
    dicInfo.InstitutionName = ''
    dicInfo.InstitutionAddress = ''
    dicInfo.InstitutionalDepartmentName = ''
    dicInfo.ManufacturerModelName = ''
    dicInfo.Manufacturer = ''
    dicInfo.AccessionNumber = ''
    dicInfo.StationName = ''
    dicInfo.PatientBirthDate = ''
    dicInfo.PatientAge = ''
    dicInfo.PatientID = ''
    dicInfo.PatientSex = ''
    dicInfo.PatientName = ''
    dicInfo.PatientPosition = ''
    dicInfo.PatientWeight = ''
    dicInfo.SeriesDescription = ''
    dicInfo.StudyDescription = ''
    dicInfo.AcquisitionDate = ''
    dicInfo.StudyDate = ''
    dicInfo.SeriesDate = ''
    dicInfo.StudyTime = ''
    dicInfo.SeriesTime = ''
    dicInfo.ContentDate = ''
    dicInfo.AcquisitionDateTime = ''
    dicInfo.StudyID = ''
    dicInfo.ImplementationVersionName = ''
    dicInfo.InstanceCreationDate = ''
    dicInfo.InstanceCreationTime = ''
    dicInfo.SoftwareVersions = ''
    dicInfo.ProtocolName = ''
    del dicInfo[(0x0002,0x0000):(0x0003,0x0000)]
    
    out_dir = os.path.join(os.path.dirname(path), 'anonymized')
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    dicInfo.save_as(os.path.join(out_dir, f"OUT_{file_identifier}.dcm"))
    return

# Input validation for main menu
# recrusive function only stops 
# when their is a valid input.
def read_valid_option(prompt):
    print(prompt)
    user_in = input()
    if user_in == 'quit':
        return
    if user_in=='1' or user_in=='2':
        return user_in
    else:
        print("Please select a valid option! i.e. 1 or 2")
        user_in = read_valid_option(prompt)
        return user_in

# Validates file path input and
# calls the anonymize function. 
# File Identifier is an identifier
# string the user would like to have
# attached in the output file's
# name i.e OUT_SomeIdentifier.dcm
def read_valid_file():
    print("Please enter the file's path:")
    file_in = str(input())
    if file_in == 'quit':
        return
    print("Please enter file identifier:")
    identifier_in = str(input())
    if identifier_in == 'quit':
        return
    try:
        anonymize(file_in, identifier_in)
        print(f"File successfully anonymized and saved as OUT_{identifier_in}.dcm!")
        return
    except Exception as e:
        print(e)
        print("Please input a valid dicom file!")
        read_valid_file()
        
# Validates folder path and finds
# all DICOM files by iterating 
# through all files in the dir
# and calls the anonmymize function
# on each of the dicom files.
def read_valid_folder():
    print("Please enter the folder's path:")
    folder_in = str(input())
    try:
        files_list = os.listdir(folder_in)
        count = 0
        for file in files_list:
            if file.lower().endswith('dcm') or file.lower().endswith('ima'):
                anonymize(os.path.join(folder_in, file), str(count))
                count += 1
        print(f"All files successfully anonymized!")        
    except:
        print("Please enter a valid folder path!")
        read_valid_folder()

# Main function calls the input 
# validation functions and builds the
# Text Based Interface.
def main():
    prompt = "DICOM File Anonymizer\n==================================\nOptions\n1) Anonymize a file\n2) Anonymize all files in a folder\n** Input 'quit' at any time to quit! **\nChoose an option to continue:"
    opt_chosen = read_valid_option(prompt)
    if opt_chosen == '1':
        read_valid_file()
    elif opt_chosen == '2':
        read_valid_folder()
    print("==================================\nThank You For Using DICOM Anonymizer!")    
    
if __name__ == '__main__':
     main()