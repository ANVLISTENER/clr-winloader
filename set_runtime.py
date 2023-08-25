from clr_loader import get_coreclr
from pythonnet import set_runtime # no module named pythonnet (requires pythonnet >=v3)

def load(): 

	rt = get_coreclr(runtime_config = "Config.json")
	set_runtime(rt)