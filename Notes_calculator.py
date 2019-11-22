
class prueba:
########################################################
    def corte1():
        n1 = float(input("Ingrese su primer corte: "))  #METODO PARA PRIMER CORTE
        return n1
########################################################
    def corte2():
        n2 = float(input("Ingrese su segundo corte: ")) #METODO PARA SEGUNDO CORTE
        return n2
########################################################
    def corte3(x,y,z):
        n3 = ((z-x*0.30-y*0.30)/0.40)                   #METODO PARA LA NOTA DEL TERCER CORTE
        return n3
########################################################
    print("Bienvenido a su calculadora de notas: ")

    try:
        n1 = corte1()       #ASIGNACION DE VALORES DEL PRIMER CORTE
        n2 = corte2()       #ASIGNACION DE VALORES DEL SEGUNDO CORTE
    except TypeError:
        print("No hay congruencia")     #TRY POR SI INGRESA VALORES ERRONEOS
    finally:
        print("Gracias por preferirnos")
    try:
        print("Para pasar en la raya necesita (3.0): ",corte3(n1,n2,3))         #CONDICIONES
        print("Para pasar un poquito mejor (3.5): ", corte3(n1, n2, 3.5))
        print("Para pasar bien (4.0): ", corte3(n1, n2, 4))
        print("Para pasar muy bien (4.5): ", corte3(n1, n2, 4.5))
        print("Para reventarla (5.0): ", corte3(n1, n2, 5))
    except ValueError:
        print("No hay congruencia")
    finally:
        print("Enhorabuena")
