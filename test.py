from simuq.solver import generate_as

#from systems.heis5 import qs
#from systems.single_x import qs
#from systems.annealing import qs

#from aais.ibm7 import mach

#generate_as(FloquetQS, FluxSCMach)
#generate_as(qs, mach, 1)




from systems.mis import qs
from aais.rydberg import Rydberg as mach

generate_as(qs, mach, 1, 1e-1)