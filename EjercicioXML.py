from lxml import etree
import webbrowser
def listar_armadura(doc):
    listaC=doc.xpath("//Champion/name/text()")
    lista=doc.xpath("//Champion/estadisticas/armorBase/text()")
    return zip(listaC,lista)
def contar_campeones(doc):
    lista=doc.xpath("count(//Champion/name/text())")
    return lista
def pediryestadisticas(doc):
    indicador=False
    campeon=str(input("Dime el campeón que analizar. "))
    listavar=['range','moveSpeed','armorBase','armorLevel','manaBase','manaLevel','criticalChanceBase','criticalChanceLevel','manaRegenBase','manaRegenLevel','healthRegenBase','healthRegenLevel','magicResistBase','magicResistLevel','healthBase','healthLevel','attackBase','attackLevel','ratingDefense','ratingMagic','ratingDifficulty','ratingAttack']
    lista=doc.xpath("//Champion/name/text()")
    listaE=doc.xpath("//Champion/estadisticas/range/text()")
    for campeones in lista:
        if campeon==campeones:
            indicador=True
    if indicador:
        print("Campeon detectado.")
        input("Pulse Enter para continuar.")
        for var in listavar:
            print(var,end="")
            dic=doc.xpath("//Champion[name='%s']/estadisticas/%s/text()"%(campeon,var))
            for estadisticas in dic:
                print("-->",estadisticas)
    else:
        print("Ese campeon no esta en nuestra base de datos.")
def pedirhabilidad(doc):
    habilidad=str(input("Dime la habilidad. "))
    lista=doc.xpath("//Champion/abilities/Ability/name/text()")
    indicador=False
    for habilidades in lista:
        if habilidad==habilidades:
            indicador=True
    if indicador:
        print("Habilidad detectada.")
        input("Presione Enter para averiguar de que campeon se trata.")
        dic=doc.xpath("//Champion/abilities/Ability[name='%s']/../../name/text()"%habilidad)
        for champion in dic:
            print(champion)
    else:
        print("Esa habilidad no esta en nuestra base de datos.")

def guiacampeon(doc):
    campeon=str(input("Dime el campeon que esté en nuestra base de datos. "))
    lista=doc.xpath("//Champion/name/text()")
    for campeones in lista:
         if campeon==campeones:
            indicador=True
    if indicador:
        print("Campeon detectado.")
        input("Pulse Enter para continuar.")
        webbrowser.open_new("https://euw.op.gg/champion/%s"%campeon) 
    else:
        print("Este campeon no esta en nuestra base de datos.")
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
        for listas in listar_armadura(doc):
            print(listas[0],"--->",listas[1])
    elif opcion==2:
        print("Hay",int(contar_campeones(doc)),"campeones en nuestro documento.")
    elif opcion==3:
        pediryestadisticas(doc)
        #Ejemplo Darius,Ziggs,Anivia
    elif opcion==4:
        pedirhabilidad(doc)
        #Ejemplo Spinning Axe,Courage,Quickdraw
    elif opcion==5:
        guiacampeon(doc)
    elif opcion==0:
        print("Fin del programa.")

