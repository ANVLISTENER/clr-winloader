import os 

from Package import Package

cwd = os.path.dirname(__file__) 

Packages = os.listdir(cwd + os.sep + "packages") 
print(Packages) 

def getDependencies(dll)  -> list: 
    
    dependencies = []

    lib = fr'{dll}'

    cmd = fr'.\Getdependencies.exe  "{lib}"' 
    
    output = os.popen(cmd).read().split("\n") 
    
    return [dependency.split(",")[0] for dependency in output].remove('')

    




def setDependencies(): 
    for package in Packages: 
        if os.path.isdir(cwd + os.sep + "packages" + os.sep + package):
            print(cwd + os.sep + "packages" + os.sep + package) 
            #print("hello")
            Package(fr"packages\{package}")
    
    
k = getDependencies(r"C:\Users\712645\OneDrive - Cognizant\Desktop\Packages\microsoft.sharepointonline.csom\16.1.23814.12000\lib\net45\Microsoft.SharePoint.Client.dll") 
print("Dependencies: " + str(k))
#p = Package(r"packages\microsoft.extensions.configuration.abstractions") 
#print(p.Module.FullName.split(",")[0])
# Package(r"pnp.framework") 
# import PnP.Framework
#print(Package("pnp.framework").Module.FullName.split(",")[0]) c
Package("pnp.core")
Package("pnp.framework")
Package("microsoft.sharepointonline.csom")
import Microsoft.SharePoint.Client

print("hello") 