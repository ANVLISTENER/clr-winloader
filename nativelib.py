import os 

from datetime import datetime as date 
import time

# import custom Packages 

nativelib = r"C:\Windows\assembly" 

Libraries = os.listdir(nativelib) 

def getStandardLibrary() -> str : 
    pattern = ["NativeImages"]

    osarch = os.popen("wmic os get osarchitecture").read().split("\n")[2].split("-")[0] 

    for reqlib in Libraries: 

        if reqlib.__contains__(pattern[0]) and reqlib.__contains__(osarch): 
            found = True 
            break 
        else: 
            found = False  

    stdLibrary = nativelib + os.sep + reqlib

    if found and os.path.exists(stdLibrary): 
        pass 
    else: 
        raise Exception("Error: Standard Library not found. ") 

    return stdLibrary 
stdLibrary = getStandardLibrary() 
def Library(folder): 

    lib = {
        "Name" : "", 
        "Type" : "", 
        "Path" : "", 
        "Date Modified" : ""
        "Available Libaries"
    }


    lib["Name"] = os.path.basename(__file__) 
    lib["Type"] = "dir" if os.path.isdir(folder) else "file" 
    lib["Path"] = folder
    lib["Date Modified"] = date.strptime(time.ctime(os.path.getmtime(folder)), '%a %b %d %H:%M:%S %Y') 
    
    return lib 

def getLatest(dlllib): 

    latest = dlllib[0]["Date Modified"] 

    for lib in dlllib: 

        if lib["Date Modified"] > latest: 
            latest = lib 

    return lib 

print(getStandardLibrary()) 

def isstandardlib(lib): # not Microsoft.V9h98fh569h4

    

    for char in lib: 
      
      if  char.isdigit():    
        return False

    return True

def getStandardLibraries(): 

    global stdLibrary
    
    stdLibrary = getStandardLibrary() 

    if getStandardLibrary() and os.path.exists(getStandardLibrary()): 
        libs = os.listdir(stdLibrary) 

    else: 
        Exception("Error: Standard Library not found.")

    patterns = ["System", "Windows"] 

    stdLibraries:list = []

    for lib in libs: 

        for pattern in patterns: 
            Libobj = Library(stdLibrary + os.sep + lib)
            if lib.__contains__(pattern) and isstandardlib(lib) and lib not in stdLibraries and Libobj["Type"] == "dir": 
                stdLibraries.append(lib)
            
    
    
        
         
    
    #[[Library(stdLibrary + os.sep + lib + os.sep + libdll) for libdll in getdllLibrary(stdLibrary + os.sep + lib)] for lib in stdLibraries]

             
          
    print("Standard Libraries: ") 
    [print(lib) for lib in stdLibraries] 

def getdllLibrary(lib): 

    libdll = os.listdir(lib) 

    [Library(stdLibrary + os.sep + "System.Design" + os.sep + lib) for lib in libdll]
    
    return libdll
getStandardLibraries() 
print(getStandardLibraries())
# libdll = os.listdir(r"C:\Windows\assembly\NativeImages_v4.0.30319_64" + os.sep + "System.Design")
# # print(r"C:\Windows\assembly\NativeImages_v4.0.30319_64" + os.sep + "System" + os.sep + libdll[0])
# print(getLatest([Library(r"C:\Windows\assembly\NativeImages_v4.0.30319_64" + os.sep + "System.Design" + os.sep + lib) for lib in libdll]))