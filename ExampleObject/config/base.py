#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Class Father '''
class Muestra(object):
    # Constructor
    '''
    * args y ** kwargs le permiten pasar una cantidad variable de argumentos a una función. 
    Lo que significa la variable aquí es que usted no sabe de antemano cuántos argumentos 
    puede pasar a su función por parte del usuario, por lo que en este caso utiliza estas 
    dos palabras clave.
    Fuente: https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
    '''
    def __init__(self, **kwargs):
        self.codigoEspectro = kwargs['codigoEspectro']
        self.spatialReference = kwargs.get('spatialReference', 84)
        """self.descripcion = kwargs['descripcion']
        self.fecha = kwargs['fecha']
        self.codidgoMuestra = kwargs['codigoMuestra']
        self.proyecto = kwargs['proyecto']
        self.equipo = kwargs['equipo']
        self.fuente =  kwargs['fuente']
        self.direccion = kwargs['direccion']
        self.nota = kwargs['nota']
        self.este = kwargs['este']
        self.datum = kwargs['datum']
        self.zona = kwargs['zona']
        self.region = kwargs['region']
        self.provincia = kwargs['provincia']
        self.distrito = kwargs['distrito']
        self.cuadrangulo = kwargs['cuadrangulo']
        self.lugar = kwargs['lugar']
        self.responsable = kwargs['responsable']"""

    # Getter @property. Es decorador que que al llamar la funcion lo trata como  atributo
    @property
    def getCodigoEspectro(self):
        return self.codigoEspectro
    
    """
    @getCodigoEspectro.settter
    def getCodigoEspect(self, val):
        return self.codigoEspectro = val
    """

    @property
    def getSpatialReference(self):
        return self.spatialReference

    """
        @classmethod. Existe para recibir como primer argumento el 
        tipo(es decir, la clase) del objeto que ha llamado al metodo.
        Usamos cuando trabajamos con la clase  y queremos volver un 
        objeto de la misma clase.
    """
    @classmethod
    def fision(cls):
        h1 = cls(codigoEspectro = "CD Espectro - UNO", spatialReference=10)
        h2 = cls(codigoEspectro = "CD Espectro - DOS", spatialReference=20)
        return h1, h2
    """
        Los metodos de clase(class methods) pueden visualizarse como una 
        variante de los metodos normales: sí reciben  un primer argumento,
        pero la referencia no es al objeto que llama al método(self), sino
        a la clase de dicho objeto(cls, por convencion).
    """
    def spatialReferenceType(self):
        tipo1 = Muestra(codigoEspectro='Espectro 1', spatialReference=42)
        tipo2 = Muestra(codigoEspectro='Espectro 2', spatialReference=69)
        return tipo1.getSpatialReference , tipo2.getSpatialReference

    """
        Usar type(self) es inevitable cuando necesitamos crear objetos de la misma
        clase  y acceder a atributos del objeto que llama al metodo.
    """
    # type()
    def objetoDeLaMismaClase(self):
        cls = type(self)
        ascendencia = ", hijo de " + self.codigoEspectro
        h1 = cls(codigoEspectro ="Primogenico" + ascendencia)
        h2 = cls(codigoEspectro ="Benjamin" + ascendencia)
        return h1, h2

''' Class Mother '''
class MuestraFirmaEspectral(Muestra):
    # Constructor
    def __init__(self, codigoEspectro, spatialReference ,condPorcentajeNubosidad , condTipoNubosidad, condAtmosferica):
        ''' Inicializando la clase padre e hijo'''
        super(MuestraFirmaEspectral, self).__init__(codigoEspectro=codigoEspectro , spatialReference=spatialReference)
        self.condPorcentajeNubosidad = condPorcentajeNubosidad
        self.condTipoNubosidad = condTipoNubosidad
        self.condAtmosferica = condAtmosferica
        
    # Getter workspaceGeoDataBase.
    @property
    def pathWork(self):
        return self.pathWorkGeoDataBase

    """
        @staticmethod. Usamos cuando el metodo trabaja con la clase, no con sus objetos. No hace uso 
        de ningún atributo de ningún objeto, pero la dejamos dentro porque su lógica pertenece 
        conceptualmente a calculadora.     
    """
    @staticmethod
    def suma(x,y):
        return x + y

''' Se llega crear la clase persona para realizar las pruebas de GETTER y SETTER '''
class Persona():
    '''
        En Python todos los campos deberian ser publico.

        Los Getter y Setter son innecesario si no se adiciona
        alguna logica en sus atributos.

        
    '''
    # Constructor
    def __init__(self, **kwargs):
        self.documentoIdentidad = kwargs['documentoIdentidad']
        self.nombres = kwargs.get('nombres',None)
        self.apellidos = kwargs.get('apellidos',None)
        self.edad = kwargs.get('edad', None)
        self._direccion = kwargs.get('direccion', None)
   
    # Getter/Setter documentoIdentidad
    def get_DocumentoIdentidad(self):
        return self.documentoIdentidad
    
    def set_DocumentoIdentidad(self, documentoIdentidad):
        self.documentoIdentidad = documentoIdentidad

    def del_DocumentoIdentidad(self):
        self.documentoIdentidad = None

    '''Argumentos nombrados - DocumentoIdentidad'''
    personaDNI =  property(get_DocumentoIdentidad, set_DocumentoIdentidad, del_DocumentoIdentidad,"DNI")

    # Getter/Setter nombre
    def get_Nombres(self):
        return self.nombres
    
    def set_Nombres(self, nombre):
        self.nombres = nombres

    def del_Nombres(self):
        self.nombres = None

    '''Argumentos nombrados - Nombre'''
    personaNombres =  property(get_Nombres, set_Nombres, del_Nombres,"Nombres")

    # Getter/Setter  apellidos
    def get_Apellidos(self):
        return self.apellidos
    
    def set_Apellidos(self, nombre):
        self.apellidos = apellidos

    def del_Apellidos(self):
        self.apellidos = None

    '''Argumentos nombrados - Apellidos'''
    personaApellidos =  property(get_Apellidos, set_Apellidos, del_Apellidos,"Apellidos")

    # Getter/Setter edad
    def get_Edad(self):
        return self.edad
    
    def set_Edad(self, edad):
        self.edad = edad

    def del_Edad(self):
        self.edad = None

    '''Argumentos nombrados - Nombre'''
    personaEdad =  property(get_Edad, set_Edad, del_Edad,"Edad")