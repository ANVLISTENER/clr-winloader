import os 

# Import the Pythonnet module 

import clr 

data:dict = {"Name" : "", 
             "Type" : "" 
            }

Modules:list = [] 
NotLoaded:list = []  
NotImported:list = [] 

LoadedLibraries:list = []
NotLoadedLibraries:list = []

def Import(lib): 
    
    globals()[lib] = __import__(lib, fromlist=[""]) 

def getLibraryData(lib, libtype): 

    data["Name"] = lib 
    data["Type"] = libtype 

    return data

stdlibs = open("mscorelib.conf").read().split("\n")


for stdlib in stdlibs: 
    
    libtype:str = "Standard Library " 

    try: 
    
        globals()[stdlib.strip()] = __import__(stdlib.strip(), fromlist=[""]) 
        
    except: 

        data = getLibraryData(stdlib.strip(), libtype)
        NotImported.append(data)
        print(f"Not Imported({data['Type']}): ", data['Name'])
        
    Modules.append(stdlib.strip())

def ImportAdditionalModules(): 

    global AddnModules

    type:str = "Additional Module"

    AddnModules = open("coredependency.txt").read().split("\n")

    for AddModule in AddnModules: 
        Module = AddModule.split(",")[0] 

        try: 

            lib = clr.AddReference(Module) 
        

        except: 
            data = getLibraryData(lib.FullName.split(",")[0], libtype)
            NotLoaded.append(data)
            print(f"Not Loaded({data['Type']}): ", data['Name'])
        
        try: 
            globals()[Module] = __import__(Module, fromlist=[""]) 

        except: 
            data = getLibraryData(lib.FullName.split(",")[0], libtype)
            NotImported.append(data)
            print(f"Not Imported({data['Type']}): ", data['Name'])

        Modules.append(Module)

def ImportSystemLibraries(): 

    libtype:str = "System.* Library"

    SystemLibraries = open("SystemLibraries.txt").read().split("\n") 
    
    for systemlib in SystemLibraries: 
        
        try: 
            lib = clr.AddReference(systemlib) 
        
        except: 
            data = getLibraryData(lib.FullName.split(",")[0], libtype)
            NotLoaded.append(data)
            print(f"Not Loaded({data['Type']}): ", data['Name']) 

        try: 
            globals()[lib.FullName.split(",")[0]] = __import__(lib.FullName.split(",")[0], fromlist=[""]) 

        except: 
            data = getLibraryData(lib.FullName.split(",")[0], libtype)
            NotImported.append(data)
            print(f"Not Imported({data['Type']}): ", data['Name'])

        Modules.append(lib.FullName.split(",")[0])

ImportSystemLibraries()
ImportAdditionalModules() 

def loadedModules(): 

    for stdlib in stdlibs: 
        Modules.append(stdlib.strip()) 

    for AddnModule in AddnModules: 
        Modules.append(AddnModule.split(",")[0])

    return Modules



def isLoaded(lib):

    return (lib in globals()) or (lib in locals()) 

def getLoadedModules(): 

    for lib in Modules: 
        if isLoaded(lib): 
            LoadedLibraries.append(lib)
        else: 
            NotLoadedLibraries.append(lib)
    




print(clr.AddReference("System.ObjectModel"))  
import System.ObjectModel     