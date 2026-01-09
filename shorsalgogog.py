import math
import random
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import QFT


#GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Quantum Period Finder
def quantum_period_finding():
    n = 4  # number of counting qubits

    qc = QuantumCircuit(n, n)

    # sted1: superposition
    for i in range(n):
        qc.h(i)

    # step2: inverse QFT
    qc.append(QFT(n, inverse=True), range(n))

    # Step 3: Measure
    qc.measure(range(n), range(n))

    backend = Aer.get_backend("aer_simulator")
    result = execute(qc, backend, shots=1024).result()
    counts = result.get_counts()

    # Most frequent result
    measured = max(counts, key=counts.get)
    value = int(measured, 2)

    if value == 0:
        return None

    return 2**n // value

# Shor Algorithm 
def shors_algorithm(N):
    while True:
        a = random.randint(2, N - 1)

        # step1: Classical check
        g = gcd(a, N)
        if g > 1:
            return g, N // g

        # Step 2: Quantum period finding
        r = quantum_period_finding()

        if r and r % 2 == 0:
            x = pow(a, r // 2, N)
            p = gcd(x - 1, N)
            q = gcd(x + 1, N)

            if p > 1 and q > 1:
                return p, q


# Run
N = 21 ()
factors = shors_algorithm(N)

print("Number:", N)
print("Factors:", factors)
