# Theory of concurrency

This repository contains exercises for the course on the Theory of Concurrency. It comprises three tasks designed to delve into various aspects of concurrent systems and their theoretical underpinnings.

## Five philosophers

The Dining Philosophers Problem is one of the classic problems in concurrency theory. The basic formulation of the problem is as follows:

- N philosophers are seated around a circular table.

- A fork is placed between each adjacent pair of philosophers (totaling N forks).
- Each philosopher alternates between "thinking" and "eating" continuously. Each phase (thinking and eating) is finite.
- To eat, a philosopher must pick up both adjacent forks.

Designing an algorithm for the simultaneous allocation of shared resources (forks) by competing processes (philosophers) to avoid deadlock and starvation, including:

1. **Naive solution (with potential deadlock)**: Each philosopher waits for the left fork to be available, then picks it up, and similarly with the right fork.

2. **Starvation-prone solution**: Each philosopher checks if both adjacent forks are available and only then picks them up simultaneously. While free from deadlock, this solution may result in starvation if one of the neighbors is always busy eating, as both forks will never be available at the same time.
3. **Asymmetric solution**: Philosophers are numbered. Philosophers with even numbers pick up the right fork first, while those with odd numbers pick up the left fork first.
4. **Stochastic solution**: Each philosopher flips a coin before picking up forks to decide which one to pick up first (left or right), ensuring that starvation is highly unlikely.
5. **Arbiter solution**: An external arbiter (butler, waiter) ensures that at most four philosophers (in the general case, N-1) compete for forks simultaneously. Each philosopher picks up the left fork first and then the right fork. If all philosophers try to eat at once, the arbiter prevents one of them from eating until one of the philosophers finishes eating.
6. **Dining hall solution**: This solution is a modification of the arbiter version. A philosopher who cannot enter the dining hall (i.e., the arbiter does not allow them to eat) eats "in the corridor" by picking up the forks in reverse order compared to the other philosophers in the dining hall.

## Theory of Traces

Given the set of variables {x, y, z}, and the following set of actions modifying the values of these variables:

- (a) x ← x + y
- (b) y ← y + 2z
- (c) x ← 3x + z
- (d) z ← y–z

Actions can be executed concurrently with the following reservation: an action modifying the value of a variable cannot be executed concurrently with an action reading from or modifying the state of the same variable. In the language of the theory of traces: two actions are dependent if both operate on the same variable, and at least one of them modifies the value of that variable.

1. Define the dependency relations in the alphabet A = {a, b, c, d}.
2. Determine the trace defined by the word w = baadcb with respect to the above dependency relations.
3. Determine the Foata normal form of the trace [w].
4. Draw the Dependency Graph of Diekert for the word w.

## Concurrent Gaussian Elimination

Designing and implementing a parallel Gauss elimination algorithm based on information obtained from the dependency graph.

The task involves the following steps (for matrices of size N):

1. Identify indivisible tasks performed by the algorithm, name them, and build an alphabet in the sense of trace theory.
2. Construct dependency and independence relations for the alphabet, describing the Gaussian elimination algorithm.
3. Present the Gaussian elimination algorithm as a sequence of symbols from the alphabet.
4. Generate the Dependency Graph of Diekert. Transform the sequence of symbols describing the algorithm into Foata normal form.
5. Design and implement a parallel Gaussian elimination algorithm based on information obtained from the dependency graph. Pay special attention to implementing it to best reflect the dependency graph. The program should work for given matrix sizes N and input/output matrices in a format specified by the instructor. The solution may not necessarily include the need for row swapping.

## Summary

these tasks provided valuable insights into concurrency theory, including resource allocation, dependency analysis, and parallel algorithm design. Through practical exercises and implementations, we gained a deeper understanding of concurrent systems and their theoretical underpinnings.
