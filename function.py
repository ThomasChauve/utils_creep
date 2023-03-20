import math

def area_tronc_cyl(Dlarge,Dsmall):
    '''
    This function compute the surface and the mass to applied on the sample for the experiment
    :param Dlarge: circle diameter (unit millimeter) (see schematic)
    :type Dlarge: float
    :param Dsmall: smaller larger (unit millimeter) (see schematic)
    :type Dsmall: float
    '''

    r=Dlarge/2 #larger radius of the circle.
    h=Dsmall-r #smaller radius of the sample.
    f=Dlarge-Dsmall #deflection
    alpha=2*math.acos(h/r).real
    #print(alpha*360/(2*cmath.pi))
    
    #Determination of the area of the bot/top surface of the sample. (in mm²)
    Ac=math.pi*pow(r,2) #Area of a circle
    As=Ac*alpha/(2*math.pi) #Area of the circular sector alpha
    At=1/2*pow(r,2)*math.sin(alpha).real #Area of the isosceles triangle in the circle
    A1=As-At #Area of the segment circle

    Af=Ac-A1#Final area wanted
    return Af

def theor_weight(AreaSample,stress=0.8):
    '''
    This function compute the mass to applied on the sample for the experiment
    :param AreaSample: Area of the sample (unit millimeter²) 
    :type AreaSample: float
    :param stress: stress applied on the sample (in MPa)
    :type stress: float
    '''
    Mth=(stress*AreaSample-22.38)/(0.14) #Etallonage à revoir
    return Mth