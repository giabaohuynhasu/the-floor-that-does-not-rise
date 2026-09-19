---
title: "Thinker: Leonard Kleinrock (1975) & William Massey (1985) — Workload Processes"
type: thinker
role: mathematical-foundation
citekey: "@Kleinrock1975, @Massey1985"
tags:
  - queueing-systems
  - workload-process
  - time-dependent
---

# Leonard Kleinrock & William Massey: The Workload Process V(t)

## 1. Intellectual Profile
- **Scholars**: Leonard Kleinrock (UCLA, father of packet switching) & William A. Massey (Princeton University).
- **Key Works**:
  - Kleinrock, L. (1975). *Queueing Systems, Volume 1: Theory*. Wiley-Interscience.
  - Massey, W. A. (1985). "Asymptotic analysis of the time dependent M/M/1 queue." *Mathematics of Operations Research*, 10(2), 305–327.
- **Core Contribution**: Defined the virtual waiting time / workload process $V(t)$, representing the total unfinished work in a queueing system at time $t$, and formulated the asymptotic expansion of queues driven by non-stationary arrival rates.

## 2. Dialectical Role in Our Framework: FOUNDATIONAL PILLAR
Kleinrock's $V(t)$ is the central mathematical object of our paper:
$$V(t) = F(t) - D(t)$$
Each technological reset event adds a jump requirement $\delta_k$, raising $F(t)$ and restarting the diffusion clock. Massey's time-dependent queueing analysis allows us to model time-varying arrival rates $\lambda(t)$ without assuming steady-state stationarity, proving that transient stability cannot be maintained when arrival growth rates outpace service scaling.

## 3. Typed Graph Edges
- `[[Kleinrock_Massey_Time_Dependent]] ────[ THEORETICAL | DIRECTLY_SUPPORTED ]────► [[CLAIM_T2_Workload_Divergence]]`
- `[[Kleinrock_Massey_Time_Dependent]] ────[ MECHANISTIC | DIRECTLY_SUPPORTED ]────► [[Huynh_2026_Floor_That_Does_Not_Rise]]`
