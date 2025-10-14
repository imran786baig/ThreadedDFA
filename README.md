# DFA Multithreading and Multiprocessing Comparison

## 📘 Overview
This project analyzes the performance difference between **multithreading** and **multiprocessing** in running a **Deterministic Finite Automaton (DFA)** program.  
The goal is to determine which approach executes faster under varying loads.

---

## ⚙️ Objective
To measure the **execution time** of a DFA program using:
- **5, 10, and 15 threads** (Multithreading)
- **5, 10, and 15 processes** (Multiprocessing)

---

## 🧩 Methodology
1. The DFA program was executed multiple times.
2. Each run used different numbers of threads and processes.
3. The total time taken for execution was recorded for comparison.

---

## 📊 Results

### Multithreading
- Completed tasks faster.
- Shared memory efficiently.
- Minimal overhead in communication between threads.

### Multiprocessing
- Slower execution time.
- Each process used separate memory space.
- Increased memory usage and context switching overhead.

---

## 🧠 Comparison Summary
| Method | Memory Usage | Execution Speed | Efficiency |
|--------|---------------|----------------|-------------|
| **Multithreading** | Low | Fast | High |
| **Multiprocessing** | High | Slow | Moderate |

- **Multithreading** outperformed **multiprocessing** because the DFA tasks were lightweight and benefited from shared memory.
- **Multiprocessing** was slower since each process ran independently, requiring more system resources.

---

## 🏁 Conclusion
For lightweight tasks like DFA simulations:
- **Multithreading** is the better choice due to its speed and efficient memory sharing.
- **Multiprocessing** is useful for CPU-heavy or isolated tasks, but not optimal for this DFA scenario.

**In summary:**  
> Multithreading works faster and more efficiently for DFA-based programs with light workloads.
