from simuq.aais.qmachine_factory import QMachineFactory
from simuq.qmachine import *


class HeisenbergQMachineFactory(QMachineFactory):
    @staticmethod
    def generate_qmachine(n=3, E=None, *args, **kwargs):
        mach = QMachine()
        ql = [qubit(mach) for i in range(n)]

        if E == None:
            link = [(i, j) for i in range(n) for j in range(i + 1, n)]
        else:
            link = E

        for i in range(n):
            L = mach.add_signal_line()

            ins1 = L.add_instruction('native', 'L{}_X_Y'.format(i))
            amp = ins1.add_local_variable()
            phase = ins1.add_local_variable(lower_bound=-2 * 3.1415926, upper_bound=2 * 3.1415926)
            ins1.set_ham(amp * (Expression.cos(phase) * ql[i].X
                                + Expression.sin(phase) * ql[i].Y))

            ins2 = L.add_instruction('derived', 'L{}_Z'.format(i))
            amp = ins2.add_local_variable()
            ins2.set_ham(amp * ql[i].Z)

        for (q0, q1) in link:
            L = mach.add_signal_line()

            ins = L.add_instruction('derived', 'L{}{}_XX'.format(q0, q1))
            amp = ins.add_local_variable()
            ins.set_ham(amp * ql[q0].X * ql[q1].X)

            ins = L.add_instruction('derived', 'L{}{}_YY'.format(q0, q1))
            amp = ins.add_local_variable()
            ins.set_ham(amp * ql[q0].Y * ql[q1].Y)

            ins = L.add_instruction('derived', 'L{}{}_ZZ'.format(q0, q1))
            amp = ins.add_local_variable()
            ins.set_ham(amp * ql[q0].Z * ql[q1].Z)

        return mach
