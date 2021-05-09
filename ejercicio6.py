from FechaHoraseis import FechaHora
def bisiesto (anio):
    if (anio%4==0 and anio%100!=0 or anio%100==0):
        return True
    else:
        return False
def valiadarHora (hora,min,seg):

    if (hora in range(24)):
        if min in range(60):
            if seg in range(60):
                return True
            else:
                print("los datos ingresados son incorrectos,seg")
                return False
        else:
            print("los datos ingresados son incorrectos,min")
            return False
    else:
        print("los datos ingresados son incorrectos,hora")
        return False

def validar (dia,mes, anio,hora,min,seg):
    if (anio in range(2022)):
        if (mes in range(13)):
            if (mes==4 or mes==6 or mes==9 or mes==11):
                if dia in range(31):
                    if (valiadarHora(hora,min,seg)):
                        return True
                    else:
                        print("los datos ingresados son incorrectos, hora")
                        return False
                else:
                    print("los datos ingresados son incorrectos, se ingreso un dia incorrecto")
                    return False
            else:
                if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
                    if dia in range(32):
                        if (valiadarHora(hora,min,seg)==True):
                            return True
                        else:
                            print("los datos ingresados son incorrectos")
                            return False
                    else:
                        print("los datos ingresados son incorrectos")
                        return False
                else:
                    if mes==2:
                        if bisiesto(anio):
                            if dia in range(30):
                                if (valiadarHora(hora,min,seg)==True):
                                    return True
                                else:
                                    print("los datos ingresados son incorrectos")
                                    return False
                            else:
                                print("los datos ingresados son incorrectos")
                                return False
                        else:
                            if dia in range(29):
                                if (valiadarHora(hora,min,seg)==True):
                                    return True
                                else:
                                    print("los datos ingresados son incorrectos")
                                    return False
                            else:
                                print("los datos ingresados son incorrectos")
                                return False 
    else:
        return False
    
    
def test ():
    d=int(input("Ingrese Dia, de fecha 1: "))
    mes=int(input("Ingrese Mes, fecha 1: "))

    a=int(input("Ingrese Año de fecha 1: "))

    h=int(input("Ingrese Hora de fecha 1: "))

    m=int(input("Ingrese Minutos de fecha 1: "))

    s=int(input("Ingrese Segundos de fecha 1: "))
    if validar(d,mes,a,h,m,s):
        r1= FechaHora(d,mes,a,h, m, s)
        d1=int(input("Ingrese Dia, de fecha 2: "))
        mes1=int(input("Ingrese Mes, fecha 2: "))

        a1=int(input("Ingrese Año de fecha 2: "))

        h1=int(input("Ingrese Hora de fecha 2: "))

        m1=int(input("Ingrese Minutos de fecha 2: "))

        s1=int(input("Ingrese Segundos de fecha 2: "))
        if validar(d1,mes1,a1,h1,m1,s1):
            r2= FechaHora(d1,mes1,a1,h1, m1, s1)
            
            print("Suma de Fecha y Horas")
            r3=r1+r2
            r3.verificarsuma()
            r3.Mostrar()
            print("Resta de de Fcha y Hora")
            r4=r1-r2
            r4.verificarResta()
            r4.Mostrar()
            print("Comparar si r1 es mayor que r2")
            r5=r1>r2
            if (r5.getAnio()):
                print("r1 es mayor que r2")
        
        else:
            print("ERROR")
        
        
    else:
        print("ERROR")
    
        

if __name__=="__main__":
    test()
    
