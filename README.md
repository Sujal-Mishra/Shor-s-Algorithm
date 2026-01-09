# Shor-s-Algorithm
# Shor’s Algorithm (Beginner-Friendly Quantum Implementation)

This repository contains a **simple and educational implementation of Shor’s Algorithm** using **Qiskit**.  
The goal of this project is to demonstrate the **core idea behind Shor’s algorithm**—period finding using quantum computing—rather than providing a fully optimized or scalable solution.

This implementation is designed for **beginners** who are learning quantum computing concepts.

---

## 📌 What This Project Does

- Uses **quantum circuits** built with Qiskit
- Demonstrates **quantum superposition** and **Quantum Fourier Transform (QFT)**
- Combines **quantum period finding** with **classical GCD logic**
- Factors **small composite numbers** (e.g., 15, 21)
- Runs on a **quantum simulator**, not real hardware

---

## ⚠️ Important Note

This is a **simplified and educational version** of Shor’s Algorithm.

- It is **not suitable for large numbers**
- It does **not break real encryption**
- Quantum advantage appears only on large-scale quantum hardware

---

## 🧠 Algorithm Overview

1. Randomly choose a number `a`
2. Check `gcd(a, N)` using classical computation
3. Use a **quantum circuit with QFT** to estimate the period `r`
4. Convert the period into factors using classical math

---

## 🛠️ Requirements

### Python Version
- Python 3.8 or higher

### Required Modules

| Module | Purpose |
|------|--------|
| `math` | Mathematical operations |
| `random` | Random number selection |
| `qiskit` | Quantum circuit framework |
| `qiskit-aer` | Quantum simulator backend |

---

## 📦 Installation

Install the required dependencies using:

```bash
pip install qiskit qiskit-aer
