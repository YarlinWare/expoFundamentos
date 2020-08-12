from xml.dom import minidom

doc = minidom.parse("ejemplo.xml")
empleados = doc.getElementsByTagName("empleado")

def registro_completo():
    for empleado in empleados:
        #Obtener una lista de nodos y sus atributos
        sid = empleado.getAttribute("id")
        username = empleado.getElementsByTagName("username")[0]
        password = empleado.getElementsByTagName("password")[0]
        print("************ Empleado", sid ," ************")
        print("id:%s " % sid)
        print("username:%s" % username.firstChild.data)
        print("password:%s" % password.firstChild.data)
    print(" ")

def registro(id_registro):
    # Encontrar nodo específico del documento XML
    nombre = doc.getElementsByTagName("nombre")[id_registro]
    print(nombre.firstChild.data)

valor = int(input('Ingrese el id del registro: '))
registro(valor)
registro_completo()