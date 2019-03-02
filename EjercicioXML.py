from lxml import etree
def listar_armadura(doc):
	lista=doc.xpath("//Champion/armorBase/text()")
	return lista
def contar_campeones(doc):
    lista=doc.xpath("count(//Champion/name/text())")
    return lista
def pediryestadisticas(doc):
    indicador=False
    campeon=str(input("Dime el campeón que analizar. "))
    lista=doc.xpath("//Champion/name/text()")
    listaE=doc.xpath("//Champion/estadisticas")
    for campeones in lista:
        if campeon==campeones:
            indicador=True
    if indicador:
        print("Campeon detectado.")
        input("Pulse Enter para continuar.")
        print(listaE)
    else:
        print("Ese campeon no esta en nuestra base de datos.")
opciones='''1.Listar Armaduras
2.Contar Campeones
3.Pedir Campeones y dar estadisticas
4.Pedir Habilidad
5.Guia de campeon
0.Salir'''
doc=etree.parse('LeagueOfLegends.xml')
opcion=int
while opcion!=0:
    print(opciones)
    opcion=int(input("Dime la opción. "))
    if opcion==1:
        for armadura in listar_armadura(doc):
            print(armadura)
    elif opcion==2:
        print("Hay",int(contar_campeones(doc)),"campeones en nuestro documento.")
    elif opcion==3:
        pediryestadisticas(doc)
    elif opcion==4:
        provincia=str(input("Dime el nombre de la provincia. "))
        for nombre in poblaciones(provincia,doc):
           print (nombre)
    elif opcion==5:
        localidad=str(input("Dime el nombre de la localidad. "))
        for nombre in poblaciones(localidad,doc):
            print(nombre)
    elif opcion==0:
        print("Fin del programa.")

