from set_runtime import load

load() 

import os 

import clr 

PnPFrameworkdll = "PnP.Framework.dll" 
PnPCoredll = "PnP.Core.dll" 
MicrosoftSharePointClient = "Microsoft.SharePoint.Client.dll"

PnPFrameworkpwd = os.path.dirname(__file__) + os.sep + r"pnp.framework\1.13.0\lib\net7.0"
PnPCorepwd = os.path.dirname(__file__) + os.sep + r"pnp.core\1.10.0\lib\net7.0"

def getLib(pwd, dll): 
 return pwd + os.sep + dll 

if os.path.exists(getLib(PnPFrameworkpwd, PnPFrameworkdll)): 
 clr.AddReference(getLib(PnPFrameworkpwd, PnPFrameworkdll))
 clr.AddReference(getLib(PnPCorepwd, PnPCoredll))

else: 
 print("path does not exist") 
 exit() 

CoreModule = os.path.basename(getLib(PnPCorepwd, PnPCoredll))
FwrkModule = os.path.basename(getLib(PnPFrameworkpwd, PnPFrameworkdll)) 

clr.AddReference("PnP.Framework")
clr.AddReference("PnP.Core") 


import PnP.Core
import PnP.Framework 


