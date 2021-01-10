'''
CAD.CurvesFromLayerName 28/12/2020
Goal: Get dynamo curves from an import instance and a layer name.
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
'''
# bibliotecas
import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import Options #Clave para acceder a las opciones de geometría del cad
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion) #Clave para convertir a curvas de dynamo
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument #Necesitamos acceder al documento
#inputs
cad = UnwrapElement(IN[0]) #Necesita un ImportInstance
capa = IN[1] #Necesita un string
curvas, solidos, salida = [], [], []
#mainbody
geOpt = cad.get_Geometry(Options()) #Accedemos a las opciones de geometría
geCur = [g.GetInstanceGeometry() for g in geOpt] #Obtenemos todas las geometrías almacenadas en una lista que almacena todo
for g in geCur[0]: #Separamos los solidos del resto de geometrías (los solidos son sombreados en autocad)
	if str(g.GetType()) != "Autodesk.Revit.DB.Solid":
		curvas.append(g)
	else:
		pass
graId = [c.GraphicsStyleId for c in curvas] #Busco el id del estilo grafico de las curvas que esta vinculado a la capa de cad
graEl = [doc.GetElement(id) for id in graId] #Conocido el id busco el elemento
grNam = [s.GraphicsStyleCategory.Name for s in graEl] #Busco el nombre de la capa de cada geometria
for n,c in zip(grNam,curvas):
	if capa == n:
		salida.append(c.ToProtoType()) #Convierto las curvas de revit a curvas de dynamo
	else:
		pass
#output
OUT = salida
