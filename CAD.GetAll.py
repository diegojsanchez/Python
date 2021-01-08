'''
CAD.GetAll 21/12/2020
diegojsanchez@gmail.com #masalladedynamo
'''
# bibliotecas
import clr 
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector, ImportInstance
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
#mainbody
ins = FilteredElementCollector(doc).OfClass(ImportInstance).ToElements() # Para obtener las instancias de los elementos importados
nombre = [x.Category.Name for x in ins]
#output
OUT = ins, nombre