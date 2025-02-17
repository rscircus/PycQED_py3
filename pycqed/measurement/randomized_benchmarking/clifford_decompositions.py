'''
5 primitives decomposition of the single qubit clifford group as per
Asaad et al. arXiv:1508.06676

In this decomposition the Clifford group is represented by 5 primitive gates
that are consecutively applied. (Note that X90 occurs twice in this list).
-X90-Y90-X90-mX180-mY180-

Note: now that I think some more about it this way of representing the 5
primitives decomposition may not be the most useful one.
'''

from copy import deepcopy


Five_primitives_decomposition = [[]]*(24)
# explictly reversing order because order of operators is order in time
Five_primitives_decomposition[0] = ['I']
Five_primitives_decomposition[1] = ['Y90', 'X90']
Five_primitives_decomposition[2] = ['X90', 'Y90', 'mX180']
Five_primitives_decomposition[3] = ['mX180']
Five_primitives_decomposition[4] = ['Y90', 'X90', 'mY180']
Five_primitives_decomposition[5] = ['X90', 'Y90', 'mY180']
Five_primitives_decomposition[6] = ['mY180']
Five_primitives_decomposition[7] = ['Y90', 'X90', 'mX180', 'mY180']
Five_primitives_decomposition[8] = ['X90', 'Y90']
Five_primitives_decomposition[9] = ['mX180', 'mY180']
Five_primitives_decomposition[10] = ['Y90', 'X90', 'mX180']
Five_primitives_decomposition[11] = ['X90', 'Y90', 'mX180', 'mY180']

Five_primitives_decomposition[12] = ['Y90',  'mX180']
Five_primitives_decomposition[13] = ['X90', 'mX180']
Five_primitives_decomposition[14] = ['X90', 'Y90', 'X90', 'mY180']
Five_primitives_decomposition[15] = ['Y90', 'mY180']
Five_primitives_decomposition[16] = ['X90']
Five_primitives_decomposition[17] = ['X90', 'Y90', 'X90']
Five_primitives_decomposition[18] = ['Y90', 'mX180', 'mY180']
Five_primitives_decomposition[19] = ['X90',  'mY180']
Five_primitives_decomposition[20] = ['X90', 'Y90', 'X90', 'mX180', 'mY180']
Five_primitives_decomposition[21] = ['Y90']
Five_primitives_decomposition[22] = ['X90', 'mX180', 'mY180']
Five_primitives_decomposition[23] = ['X90', 'Y90', 'X90', 'mX180']

'''
Gate decomposition decomposition of the clifford group as per
Eptstein et al. Phys. Rev. A 89, 062321 (2014)
'''
XY_gate_decomposition = [[]]*(24)
# explictly reversing order because order of operators is order in time
XY_gate_decomposition[0] = ['I']
XY_gate_decomposition[1] = ['Y90', 'X90']
XY_gate_decomposition[2] = ['mX90', 'mY90']
XY_gate_decomposition[3] = ['X180']
XY_gate_decomposition[4] = ['mY90', 'mX90']
XY_gate_decomposition[5] = ['X90', 'mY90']
XY_gate_decomposition[6] = ['Y180']
XY_gate_decomposition[7] = ['mY90', 'X90']
XY_gate_decomposition[8] = ['X90', 'Y90']
XY_gate_decomposition[9] = ['X180', 'Y180']
XY_gate_decomposition[10] = ['Y90', 'mX90']
XY_gate_decomposition[11] = ['mX90', 'Y90']

XY_gate_decomposition[12] = ['Y90', 'X180']
XY_gate_decomposition[13] = ['mX90']
XY_gate_decomposition[14] = ['X90', 'mY90', 'mX90']
XY_gate_decomposition[15] = ['mY90']
XY_gate_decomposition[16] = ['X90']
XY_gate_decomposition[17] = ['X90', 'Y90', 'X90']
XY_gate_decomposition[18] = ['mY90', 'X180']
XY_gate_decomposition[19] = ['X90', 'Y180']
XY_gate_decomposition[20] = ['X90', 'mY90', 'X90']
XY_gate_decomposition[21] = ['Y90']
XY_gate_decomposition[22] = ['mX90', 'Y180']
XY_gate_decomposition[23] = ['X90', 'Y90', 'mX90']

# assigning to this variable for legacy reasons
gate_decomposition = XY_gate_decomposition
epstein_efficient_decomposition = XY_gate_decomposition

# The fixed length decomposition
epstein_fixed_length_decomposition = deepcopy(XY_gate_decomposition)
for el in epstein_fixed_length_decomposition:
    for i in range(3-len(el)):
        el.append('I')
'''
Gate decomposition decomposition of the clifford group as per
McKay et al. Phys. Rev. A 96, 022330 (2017)
'''
HZ_gate_decomposition = [[]]*(24)
# explictly reversing order because order of operators is order in time
HZ_gate_decomposition[0] = ['Z0']
HZ_gate_decomposition[1] = ['X90', 'Z90']
HZ_gate_decomposition[2] = ['mZ90', 'mX90']
HZ_gate_decomposition[3] = ['X180']
HZ_gate_decomposition[4] = ['mZ90', 'mX90', 'Z90', 'mX90']
HZ_gate_decomposition[5] = ['mZ90', 'mX90', 'Z180']
HZ_gate_decomposition[6] = ['mZ90', 'X180', 'Z90']
HZ_gate_decomposition[7] = ['mZ90', 'mX90', 'Z90', 'X90']
HZ_gate_decomposition[8] = ['X90', 'mZ90', 'X90', 'Z90']
HZ_gate_decomposition[9] = ['Z180']
HZ_gate_decomposition[10] = ['Z180', 'X90', 'Z90']
HZ_gate_decomposition[11] = ['Z90', 'mX90']

HZ_gate_decomposition[12] = ['Z90', 'X90', 'Z90']
HZ_gate_decomposition[13] = ['mX90']
HZ_gate_decomposition[14] = ['Z90']
HZ_gate_decomposition[15] = ['mZ90', 'mX90', 'Z90']
HZ_gate_decomposition[16] = ['X90']
HZ_gate_decomposition[17] = ['X180', 'Z90']
HZ_gate_decomposition[18] = ['mZ90', 'mX90', 'Z90', 'X180']
HZ_gate_decomposition[19] = ['X90', 'mZ90', 'X180', 'Z90']
HZ_gate_decomposition[20] = ['mX90', 'Z180', 'X90', 'Z90']
HZ_gate_decomposition[21] = ['mZ90', 'X90', 'Z90']
HZ_gate_decomposition[22] = ['mX90', 'mZ90', 'X180', 'Z90']
HZ_gate_decomposition[23] = ['mZ90']
# HZ_gate_decomposition = [[]]*(24)
# # explictly reversing order because order of operators is order in time
# HZ_gate_decomposition[0] = ['I']
# HZ_gate_decomposition[1] = ['X90', 'Z90']
# HZ_gate_decomposition[2] = ['mZ90', 'mX90']
# HZ_gate_decomposition[3] = ['X180']
# HZ_gate_decomposition[4] = ['mZ90', 'mX90', 'Z90', 'mX90']
# HZ_gate_decomposition[5] = ['mZ90', 'mX90', 'Z180']
# HZ_gate_decomposition[6] = ['mZ90', 'X180', 'Z90']
# HZ_gate_decomposition[7] = ['mZ90', 'mX90', 'Z90', 'X90']
# HZ_gate_decomposition[8] = ['X90', 'mZ90', 'X90', 'Z90']
# HZ_gate_decomposition[9] = ['mZ180']
# HZ_gate_decomposition[10] = ['mZ180', 'X90', 'Z90']
# HZ_gate_decomposition[11] = ['Z90', 'mX90']
#
# HZ_gate_decomposition[12] = ['Z90', 'X90', 'Z90']
# HZ_gate_decomposition[13] = ['mX90']
# HZ_gate_decomposition[14] = ['Z90']
# HZ_gate_decomposition[15] = ['mZ90', 'mX90', 'Z90']
# HZ_gate_decomposition[16] = ['X90']
# HZ_gate_decomposition[17] = ['X180', 'Z90']
# HZ_gate_decomposition[18] = ['mZ90', 'mX90', 'Z90', 'X180']
# HZ_gate_decomposition[19] = ['X90', 'mZ90', 'X180', 'Z90']
# HZ_gate_decomposition[20] = ['mX90', 'Z180', 'X90', 'Z90']
# HZ_gate_decomposition[21] = ['mZ90', 'X90', 'Z90']
# HZ_gate_decomposition[22] = ['mX90', 'mZ90', 'X180', 'Z90']
# HZ_gate_decomposition[23] = ['mZ90']

