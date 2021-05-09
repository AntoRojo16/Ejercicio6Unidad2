class FechaHora:
    __dia=0
    __mes=0
    __anio=0
    __hora=0
    __min=0
    __seg=0
    
    
    def __init__ (self,d=0,m=0,a=0,h=0,mi=0,s=0):
        self.__anio=a
        self.__mes=m
        self.__dia=d
        self.__hora=h
        self.__min=mi
        self.__seg=s
    
    def getAnio (self):
        return self.__anio
    
    def getMes (self):
        return self.__mes
    
    def getDia (self):
        return self.__dia
        
        
    def getHora (self):
        return self.__hora
    
    def getMin (self):
        return self.__min
        
    def getSeg (self):
        return self.__seg
    
        
    def __add__ (self, otraFechaHora):
        return FechaHora(self.__dia+otraFechaHora.getDia(), self.__mes+otraFechaHora.getMes(), self.__anio+otraFechaHora.getAnio(), self.__hora+otraFechaHora.getHora(), self.__min+otraFechaHora.getMin(), self.__seg+otraFechaHora.getSeg())
      
    def __sub__ (self, otraFechaHora):
        return FechaHora(self.__dia-otraFechaHora.getDia(), self.__mes-otraFechaHora.getMes(), self.__anio-otraFechaHora.getAnio(), self.__hora-otraFechaHora.getHora(), self.__min-otraFechaHora.getMin(), self.__seg-otraFechaHora.getSeg())
    
    def __gt__ (self, otraFechaHora):
        dia=otraFechaHora.getDia()
        mes=otraFechaHora.getMes()
        anio=otraFechaHora.getAnio()
        hora=otraFechaHora.getHora()
        min=otraFechaHora.getMin()
        seg=otraFechaHora.getSeg()
        return FechaHora(self.__dia>dia,
                         self.__mes>mes, 
                         self.__anio>anio,
                         self.__hora>hora,
                         self.__min>min,
                         self.__seg>seg)
    
    def bisiesto (self,anio):
        if (anio%4==0 and anio%100!=0 or anio%100==0):
            return True
        else:
            return False  
    def Mostrar (self):
        print("{}""/""{}""/""{}".format(self.__dia,self.__mes,self.__anio))
        print("{}""h, ""{}""m, ""{}""s".format(self.__hora,self.__min,self.__seg))
        
    def PonerEnHora (self,h=0,m=0,s=0):
        self.__hora=h
        self.__min=m
        self.__seg=s
        
    def verificarResta (self):
        if self.__seg<0:
            self.__seg=self.__seg+60
            self.__min=self.__min-1
        if self.__min<0:
            self.__min=self.__min+60
            self.__hora=self.__hora-1
        if self.__hora<0:
            self.__hora=self.__hora+23
            self.__dia=self.__dia-1
        if self.__dia<1:
            self.__mes=self.__mes-1
            if self.__mes<1:
                self.__mes=self.__mes+12
                self.__anio=self.__anio-1
            if (self.__mes==4)or (self.__mes==6) or (self.__mes==9) or(self.__mes==11):
                self.__dia=self.__dia+30
            if (self.__mes==1) or (self.__mes==3) or (self.__mes==5)  or (self.__mes==7) or (self.__mes==8) or (self.__mes==10):
                self.__dia=self.__dia+31
            if (self.__mes==12):
                self.__dia=self.__dia+31
            
            if self.__mes==2:
                if (self.bisiesto(self.__anio)):
                    self.__dia=self.__dia+29
                else:
                    self.__dia=self.__dia+28

        else:
            if self.__mes<1:
               self.__mes=self.__mes+12
               self.__anio=self.__anio-1
            
            
        
        
    def verificarsuma (self):
        if (self.__seg>60):
            self.__seg=self.__seg-59
            self.__min=self.__min+1
            
        if (self.__min>60):
            self.__min=self.__min-59
            self.__hora=self.__hora+1
            
        if (self.__hora>23):
            self.__hora=self.__hora-24
            self.__dia=self.__dia+1
            
            
        if(self.__mes==4)or (self.__mes==6) or (self.__mes==9) or(self.__mes==11):
            if(self.__dia>30):
                self.__dia=self.__dia-29
                self.__mes=self.__mes+1
                
        
        if (self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==12) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==11):
            if (self.__dia>31):
                if (self.__mes==12):
                   self.__anio=self.__anio+1
                   self.__mes=1
                   self.__dia=self.__dia-30
                else:
                    self.__dia=self.__dia-30
                    self.__mes=self.__mes+1
        
        if (self.__mes==2):
            if (self.bisiesto(self.__anio)):
                if (self.__dia>29):
                    self.__dia=self.__dia-28
                    self.__mes=self.__mes+1
            else:
                if self.__dia>28:
                    self.__dia=self.__dia-27
                    self.__mes=self.__mes+1
                
                


        
    def AdelantarHora (self,h=0,m=0,s=0):
        self.__hora=self.__hora+h
        self.__min=self.__min+m
        self.__seg=self.__seg+s
        
        
        if (self.__seg>60):
            self.__seg=self.__seg-59
            self.__min=self.__min+1
            
        if (self.__min>60):
            self.__min=self.__min-59
            self.__hora=self.__hora+1
            
        if (self.__hora>23):
            self.__hora=self.__hora-24
            self.__dia=self.__dia+1
            
            
        if(self.__mes==4)or (self.__mes==6) or (self.__mes==9) or(self.__mes==11):
            if(self.__dia>30):
                self.__dia=1
                self.__mes=self.__mes+1
                
        
        if (self.__mes==1) or (self.__mes==3) or (self.__mes==5) or (self.__mes==12) or (self.__mes==7) or (self.__mes==8) or (self.__mes==10) or (self.__mes==11):
            if (self.__dia>31):
                if (self.__mes==12):
                   self.__anio=self.__anio+1
                   self.__mes=1
                   self.__dia=1
                else:
                    self.__dia=1
                    self.__mes=self.__mes+1
        
        if (self.__mes==2):
            if (self.bisiesto(self.__anio)):
                if (self.__dia>29):
                    self.__dia=1
                    self.__mes=self.__mes+1
            else:
                if self.__dia>28:
                    self.__dia=1
                    self.__mes=self.__mes+1
                
                
            
        

