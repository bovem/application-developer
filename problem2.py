import os 
import re 

# Updated Code
def updateVersion(filename, regex, replacement_string):
    filename = os.path.join(os.environ["SourcePath"], "develop", "global", "src", filename)

    #os.chmod(filename, 755)

    # Read contents of the file and replace content matching regex
    # with replacement_string
    with open(filename, "r") as f: 
        file_content = f.read()
        new_content = re.sub(regex, replacement_string, file_content)

    # Write the new contents to the file
    with open(filename, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    updateVersion("SConstruct", "point\=[\d]+", "point={}".format(os.environ["BuildNum"]))
    updateVersion("VERSION", "ADLMSDK_VERSION_POINT=[\d]+", "ADLMSDK_VERSION_POINT={}".format(os.environ["BuildNum"]))

# Earlier Version of code
# def updateSconstruct(): 
#     # "Update the build number in the SConstruct file" 
#     os.chmod(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct"), 0755) 
#     fin = open(os.path.join(os.environ["SourcePath"]z,"develop","global","src","SConstruct"), 'r')
#     fout = open(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1"), 'w') 
#     for line in fin: 
#         line=re.sub("point\=[\d]+","point="+os.environ["BuildNum"],line) 
#         fout.write(line) 
# 
#     fin.close() 
#     fout.close() 
#     os.remove(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct")) 
#     os.rename(os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1"), os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct")) 
# 
# # VERSION file interesting line 
# # ADLMSDK_VERSION_POINT=6 
# def updateVersion(): 
#     # "Update the build number in the VERSION file"
#     os.chmod(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"), 0755) 
#     fin = open(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION"), 'r') 
#     fout = open(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION1"), 'w') 
#     for line in fin: 
#         line=re.sub("ADLMSDK_VERSION_POINT=[\d]+","ADLMSDK_VERSION_POINT="+os.environ["BuildNum"],line) 
#         fout.write(line) 
#     fin.close() 
#     fout.close() 
#     os.remove(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION")) 
#     os.rename(os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION1"), os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION")) 

# def main(): 
#     updateSconstruct() 
#     updateVersion() 
# 
# main()
