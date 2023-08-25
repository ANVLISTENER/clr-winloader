import os 

import clr

from packaging.version import parse, Version 

# Import custom package 
import mscorelib


class Package: 

 PackageName:str = ""

 lib:str = ""

 dlls:tuple = ()

 dotnet_version:str = ""

 _version = "" 

 dotnetVersionsAvailable = ()
 AvailableVersions:list = [] 

 Module = "" 

 retry:int = 0

 def __init__(self, PackageName, cwd=None, auto=True) -> None:

     

     if cwd == None: 
          self.setCwd(self.getcwd())
     else: 
          self.setCwd(cwd) 

     if auto: 
          
          self.setLib(PackageName)
          self.setVersion() 
          self.setlibFolder() 
          self.setDotnet() 
          self.setdllDir() 
          self.setdlls() 
          Module = []
          # now load the module 
          for dll in self.dlls: 
                    Module = clr.AddReference(self.dlldirectory + os.sep + dll) 
                    clr.AddReference(Module.FullName.split(",")[0]); 
          print(self.dotnet_version)
          print(self.dlls)         
          self.Module = Module
          
 def getcwd(self): 
  return os.path.dirname(__file__) 

 def setCwd(self, cwd): 
       self.cwd = cwd

 def setLib(self, PackageName): 
  self.lib = self.cwd + os.sep + PackageName 

 def setVersion(self, version=None): 
  if not self.lib: print("Library path not set"); return  
  versions = []
  if version == None: 
     AvailableVersions = []
     if os.path.exists(self.lib): 
      versions = os.listdir(self.lib) 
     #print(versions)   
     for version in versions: 
      try: 
          AvailableVersions.append(parse(version))
      except: 
          print("Error: Invalid Version") 
          exit()
     
     self.AvailableVersions = tuple(AvailableVersions)
     latest:Version = self.AvailableVersions[0]
     for version in self.AvailableVersions: 
          if version > latest: 
               latest = version 
     
     self._version = str(latest) 

  else: 
     self._version = str(version)


 def setlibFolder(self, libfolder=None): 
     if self.lib == "": print("Library Path not set"); return 
     if self._version == "": print("Library Version not set"); return 
     self.libFolder = ""
     Library = self.lib + os.sep + self._version
     result = []
     if libfolder == None: 
          try: 
               if os.path.exists(self.lib + os.sep + self._version): 
                    result = os.listdir(self.lib + os.sep + self._version) 
          except:
               print(f"ERROR: {result}")
          print(self.lib + os.sep + self._version)
          possibilities = ["lib", "Lib", "LIB", "ref"]
          for libfolder in possibilities: 
               if libfolder in result: found = True; break
               else: found = False
          if found: 
               self.libFolder = Library + os.sep + libfolder  
     else: 
               self.libFolder = Library + os.sep + libfolder 
               print(self.libFolder)
               if not os.path.exists(self.libFolder): 
                    print("Lib folder not found.")
                    exit()
               else: 
                    if bool(self.retry): 
                         self.setDotnet()
               
                    
     

 def max(versionlist, dotnettype:bool=False): 

     latest:Version = versionlist[0]

     for version in versionlist: 
          if version > latest: 
               latest = version 
          
     return latest

 def VersionsList(self, verlist): 

    VersionList:list = []
    for ver in verlist: 
     VersionList.append(parse(ver)) 

    return VersionList



 def setInstalledDotnet(self, version=None): 
     self.InstalledDotnetVersions = os.popen('dotnet --list-sdks').read().split("\n").remove("")  

     if version != None: 
          self.InstalledDotnetVersion = version 
     
     else: 

          print("Default: Setting Latest dotnet version")
          if len(self.InstalledDotnetVersions) == 1: 
               self.InstalledDotnetVersion = self.InstalledDotnetVersions[0] 

          else: 
               self.InstalledDotnetVersion = max(self.InstalledDotnetVersions) 

 def parsePackagedotnetversion(self,version):
     
     dotnettype = ""

     for character in version: 
          
          if not character.isdigit(): 
               dotnettype = dotnettype + character
          else: 
               break
     
     dotnetversion = version.replace(dotnettype, "") 

     return dotnettype, dotnetversion
        
 def setDotnet(self, version=None): 
        
     if self.lib == "": print("Library Path not set"); return 
     if self._version == "": print("Library Version not set"); return 
     if self.libFolder == "": print("Library Folder not set"); return  

     if version != None: 
          if version in os.listdir(self.libFolder): 
               self.dotnet_version = version 
               return 
          else: 
               print("ERROR: Invalid package dotnet version") 
               exit()

     self.dotnetAvailableVersionsfolder = os.listdir(self.libFolder) 
     self.dotnetAvailableVersions:list     = []
     
     dotnettypes = []
     dotnetAvailableVersions = []
     prioritydotnettypes = ["netcore", "net", "netframework", "netstandard"]
     for AvailableVersionfolder in self.dotnetAvailableVersionsfolder:
          for prioritydotnettype in prioritydotnettypes: 
               if AvailableVersionfolder.startswith(prioritydotnettype):
                    #print(AvailableVersionfolder)  
                    dotnettype, version = self.parsePackagedotnetversion(AvailableVersionfolder)
          
                    dotnetAvailableVersions.append(version)
                    if dotnettype not in dotnettypes:  
                         dotnettypes.append(dotnettype)
                    break
          

     
     self.dotnetAvailableVersions = dotnetAvailableVersions
     self.dotnetAvailableVersion = max(self.dotnetAvailableVersions) 
     
     for dotnettype in dotnettypes: 
          dotnet = dotnettype + self.dotnetAvailableVersion 
          if dotnet in self.dotnetAvailableVersionsfolder: 
               self.dotnet_version = dotnet

     #print("dotnet: ", self.libFolder)

     if not bool(self.retry): 
          self.setdllDir()
     
     # dotnetversions =  os.listdir(self.libFolder)
     
     # possibility:list = [] 
     
     # for dotnet in dotnetversions: 
     #      for dotnetversion in self.dotnetAvailableVersions:
     #           value = dotnet.replace(dotnetversion, "")
     #           if value not in possibility:       
     #                possibility.append(value) 

     # self.InstalledDotnetVersion = self.setInstalledDotnet(version=version) 


     # if "net" + max(self.dotnetAvailableVersions) in os.listdir(self.libFolder): 
     #      self.dotnetAvailableVersion = "net" + max(self.dotnetAvailableVersions)
     # else: 
     #      latest = max(self.dotnetAvailableVersions) 

     #      for dotnettype in possibility: 
     #           if dotnettype in latest: 
     #                self.dotnetAvailableVersion = dotnettype + latest
       
     #self.dotnet_version = max(self.dotnetAvailableVersions)
 
 def setdllDir(self, dlldirectory=None):

     if self.lib == "": print("Library Path not set"); return 
     if self._version == "": print("Library Version not set"); return 
     if self.libFolder == "": print("Library Folder not set"); return 
     if self.dotnet_version == "": print("dotnet_version not set"); return 
     
     if dlldirectory == None: 
          if os.path.exists(self.libFolder + os.sep + self.dotnet_version): 
               self.dlldirectory = self.libFolder + os.sep + self.dotnet_version 
          else: 
               print(f"Folder: {self.libFolder + os.sep + self.dotnet_version} does not exist. ") 

     else: 
          if not os.path.exists(dlldirectory): 
               self.dlldirectory = dlldirectory 
          
     if not bool(self.retry):
          
          self.setdlls() 
          
     # print("libdll: " + self.libFolder)

 def setdlls(self, dlls=None): 
     
     if self.lib == "": print("Library Path not set"); return 
     if self._version == "": print("Library Version not set"); return 
     if self.libFolder == "": print("Library Folder not set"); return 
     if self.dotnet_version == "": print("dotnet_version not set"); return
     if self.dlldirectory == "": print("dlldirectory not set"); return 
     
     if dlls != None: 
          if not os.path.exists(self.dlldirectory): 
               print("dll directory not exists. ") 
               exit() 
          else: 
               self.dlls = dlls 

     # print("dump" +  self.dlldirectory)
     if os.path.exists(self.dlldirectory): 
          files = os.listdir(self.dlldirectory) 
          
          
          
     else: 
          print("dlldirectory does not exist. ") 
          exit() 


     dlls = []
     for file in files: 
          if ".dll" in file: 
               dlls.append(file) 
          
     if len(dlls) == 0 and not self.retry == 1: 
          print("Retry: " + str(self.retry))
          self.retry = self.retry + 1
          self.setlibFolder("ref") 
          # # self.load()
          # self.setDotnet() 
          # self.setdllDir() 
          # self.setdlls()
          #print("hello")
     if not bool(self.retry): 
          print("Updated: " + self.dlldirectory)
          
               # not retry further 
          

     self.dlls = tuple(dlls)

     return 
 def reload(self): 
     # # self.load()
     self.setDotnet() 
     self.setdllDir() 
     self.setdlls()
     print("hello")

 def load(self): 

          import clr 

          self.setCwd(self.getcwd()) 
          self.setLib(self.PackageName)
          self.setVersion(self._version) 
          self.setlibFolder(self.lib) 
          self.setDotnet(self.dotnet_version) 
          self.setdllDir(self.dlldirectory) 
          self.setdlls(self.dlls) 
          Module = ""
          for dll in self.dlls: 
               Module = clr.AddReference(self.dlldirectory + os.sep + dll) 
               clr.AddReference(Module.FullName.split(",")[0])
               
          
          self.Module = Module
          return self
          
       
# p = Package(r"packages\microsoft.extensions.configuration.abstractions") 
# p.setCwd(r"C:\Users\712645\OneDrive - Cognizant\Desktop\Packages\packages")
# p.setLib("microsoft.extensions.configuration.abstractions") 
# p.setVersion("2.1.0")
# p.setlibFolder()

# p.setDotnet()
# p.setdllDir()
#print(p.dotnet_version)
#print(Package("pnp.framework").Module.FullName)
# import Microsoft.SharePoint.Client as pack
# Package("pnp.core")
Package(r"packages\system.text.encoding")
# Package("pnp.framework")

# print(dir(pack)) 