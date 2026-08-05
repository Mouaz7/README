<a href="https://github.com/Mouaz7/Mouaz7">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/hero-dark.svg">
    <img width="100%" alt="Mouaz Naji — Software Engineer" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/hero-light.svg">
  </picture>
</a>

<div align="center">





</div>

> navigation --quick

<div align="center">

About • Architecture • Capabilities • Tech Stack • Projects • Education • Roadmap • Stats • Contact

</div>

> whoami

I am Mouaz Naji, a Software Engineering student at Blekinge Institute of Technology (BTH) focused on building dependable software across backend systems, AI-assisted workflows, operating-system concepts, networking and security.

I am especially interested in work where several engineering areas meet: APIs connected to automation, AI agents constrained by safety gates, concurrent systems measured for performance, and applications designed with clear architectural boundaries.

What I optimize for

Principle

What it means in practice

Reliability

Clear failure handling, observable behavior and predictable system states

Architecture

Explicit boundaries, directional dependencies and maintainable components

Security

Validation, protected credentials, review gates and least-privilege thinking

Performance

Measurement before optimization, efficient algorithms and resource awareness

Quality

Tests, readable code, documentation and repeatable development workflows

$ cat /etc/mouaz/profile.conf

NAME          = Mouaz Naji
ROLE          = Software Engineer
EDUCATION     = Software Engineering @ BTH
LOCATION      = Sweden
PRIMARY       = Backend Systems | Generative AI | System Design
SYSTEMS       = Linux | Processes | Threads | IPC | Filesystems | Networks
LANGUAGES     = Python | C++ | C | Java | TypeScript | JavaScript | Kotlin
DATA          = PostgreSQL | MySQL | MariaDB | SQLite | Firebase
TOOLS         = Git | GitHub | Docker | Bash | Android Studio | VS Code
PRINCIPLES    = Reliability | Security | Performance | Clean Architecture
OPEN_TO       = Collaboration | Open Source | Software Engineering Projects

> architecture.map

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/architecture-dark.svg">
  <img width="100%" alt="Mouaz engineering architecture map" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/architecture-light.svg">
</picture>

Engineering domains

Domain

What I work with

Key themes

Backend Systems

APIs, services, validation and authentication

Modularity, error handling, reliability

AI Engineering

LLM integrations, autonomous agents and developer automation

Orchestration, memory, evaluation, HITL

Systems Programming

Software close to the operating system

Processes, threads, synchronization, IPC

Secure Software

Controls that reduce unsafe changes

Secret handling, static checks, protected paths

Networking

Communication behavior and protocol trade-offs

TCP, UDP, throughput, packet loss

Data Engineering

Persistent state and structured data

SQL, Firebase, schemas, queries

DevOps

Repeatable delivery and operational workflows

Linux, Docker, CI/CD, observability

Software Architecture

Systems that remain understandable as they grow

Clean Architecture, interfaces, testing

> capabilities.matrix

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/capabilities-dark.svg">
  <img width="100%" alt="Mouaz capability matrix" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/capabilities-light.svg">
</picture>

The percentages are visual self-assessments, not certifications. The evidence is in the linked projects and technical work below.

> ls /tech-stack

<div align="center">

[ Languages ]

<img src="https://skillicons.dev/icons?i=python,cpp,c,java,js,ts,kotlin,bash&theme=dark" alt="Programming languages" />

[ Frontend & Mobile ]

<img src="https://skillicons.dev/icons?i=html,css,react,nextjs,vue,tailwind,androidstudio&theme=dark" alt="Frontend and mobile technologies" />

[ Backend & Data ]

<img src="https://skillicons.dev/icons?i=nodejs,express,postgres,mysql,sqlite,firebase&theme=dark" alt="Backend and data technologies" />

[ Systems, DevOps & Tools ]

<img src="https://skillicons.dev/icons?i=linux,docker,git,github,vscode,cmake&theme=dark" alt="Systems and DevOps tools" />

</div>

Engineering practices



> cat engineering_principles.yaml

architecture:
  - separate responsibilities before adding features
  - keep dependencies explicit and directional
  - design interfaces around behavior, not implementation details

reliability:
  - handle failure as a normal system state
  - prefer observable workflows over silent automation
  - add limits, deduplication and auditability to autonomous systems

security:
  - validate inputs and protect credentials
  - use least privilege and protected paths
  - keep humans in control of high-impact decisions

quality:
  - test behavior, not only individual functions
  - keep code readable enough to review under pressure
  - optimize after measuring, not before understanding

> ls /projects --sort=impact

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/projects-dark.svg">
  <img width="100%" alt="Mouaz selected projects" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/projects-light.svg">
</picture>

<details open>
<summary><b>▶ Auto-Healing AI DevOps Platform — Bachelor Thesis Project</b></summary>

A self-healing CI/CD research prototype that detects failed builds, compresses and analyses logs, generates candidate fixes, runs quality and security checks, opens a pull request and notifies a human reviewer.

Aspect

Detail

Stack

Python · LLMs · GitHub · Jenkins · Slack · Docker

Architecture

Six-agent pipeline coordinated through an orchestrator and specialized services

Safety

Enforced human review, protected paths, secret scanning and regression blocking

Quality

Bandit, Pylint, syntax validation, retry limits and audit logging

Repository

Mouaz7/auto-healing-devops-platform

</details>

<details>
<summary><b>▶ Campus360 — Hybrid Campus Navigation</b></summary>

An Android application that combines outdoor maps and indoor floor plans with search, favorites, localization and secure Firebase authentication.

Aspect

Detail

Stack

Kotlin · Android · Firebase · Google Maps

Architecture

MVVM with Clean Architecture boundaries

Features

Hybrid navigation, smart search, favorites, dark mode and localization

Repository

Mouaz7/Campus360

</details>

<details>
<summary><b>▶ PongPal — Slack, Web and IoT Booking Ecosystem</b></summary>

An internal Softhouse project connecting a web application, Slack commands, Firebase services and Raspberry Pi camera control for booking and match tracking.

Aspect

Detail

Stack

React · TypeScript · Slack API · Firebase · Python · Raspberry Pi

Integrations

Bookings, match results, leaderboards, statistics and table status

Repository

Mouaz7/PongPal-Showcase

</details>

<details>
<summary><b>▶ Chess Game — Modern C++ and SFML</b></summary>

A graphical chess application with legal move validation, special rules, timers, history tracking and a Chess.com-inspired interface.

Aspect

Detail

Stack

C++20 · SFML 3.0 · vcpkg · Visual Studio

Design

Abstract piece hierarchy, polymorphism, RAII and smart pointers

Rules

Castling, en passant, promotion, checkmate, stalemate and draw conditions

Repository

Mouaz7/chess-game

</details>

<details>
<summary><b>▶ Concurrency Systems — POSIX and Operating-System Concepts</b></summary>

A systems-programming collection demonstrating concurrency, synchronization, IPC and page-replacement algorithms in C.

Aspect

Detail

Stack

C · Linux · POSIX Threads

Concurrency

pthreads, mutexes, semaphores and parallel matrix multiplication

IPC

Shared memory and System V message queues

Memory

FIFO, LRU and Optimal page-replacement algorithms

Repository

Mouaz7/Concurrency-Systems

</details>

<details>
<summary><b>▶ OS Filesystem — FAT-Based Virtual Storage</b></summary>

A simulated filesystem with a command shell, hierarchical directories, permission flags, path resolution and virtual block storage.

Aspect

Detail

Stack

C++ · Linux · Make

Architecture

Interactive shell → filesystem core → disk I/O layer

Features

Files, directories, permissions, path resolution and formatting

Repository

Mouaz7/Os_filesystem

</details>

<details>
<summary><b>▶ C++ Transport System — OOP and Persistence</b></summary>

A terminal-based transport-management application for shuttles, passenger groups and time-constrained schedules.

Aspect

Detail

Stack

C++ · Visual Studio

Design

Encapsulation, inheritance, polymorphism and modular managers

Persistence

File streams for shuttles, passengers and schedules

Repository

Mouaz7/Cpp-TransportSystem

</details>

<details>
<summary><b>▶ Network UDP/TCP Analysis — Protocol Behavior</b></summary>

Python senders and receivers used to study delivery behavior at different packet rates.

Aspect

Detail

Stack

Python · TCP · UDP

Measurements

Packet rate, throughput, ordering and loss

Analysis

UDP loss under load versus TCP ordering and retransmission

Repository

Mouaz7/network-udp-tcp-analysis

</details>

> cat education.log

Software Engineering @ BTH

FOUNDATION
├── Programming in Python, C, C++ and Java
├── Algorithms and Data Structures
├── Object-Oriented Design
└── Computational Problem Solving

SYSTEMS
├── Operating Systems
├── Processes, Threads and IPC
├── Computer Networks
├── Embedded and Assembly Programming
└── Performance and Resource Management

SOFTWARE ENGINEERING
├── Requirements Engineering
├── Software Architecture and Design Patterns
├── Verification, Validation and Testing
├── Team-Based Development
└── Maintainability and Quality

DATA, SECURITY AND AI
├── Database Technology
├── Security and Cryptography
├── Artificial Intelligence
├── Generative AI Integrations
└── Safe Automation and Human Control

> engineering.roadmap

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/roadmap-dark.svg">
  <img width="100%" alt="Mouaz engineering roadmap" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/roadmap-light.svg">
</picture>

Areas I am deepening

Distributed systems and service-to-service communication.

Cloud-native deployment, observability and production operations.

Advanced backend performance and database optimization.

AI agent evaluation, trust and controlled autonomy.

Security engineering integrated throughout the development lifecycle.

> ps aux | grep current-work

Process

State

Description

backend.systems

RUNNING

Designing APIs and modular application services

ai.devtools

RUNNING

Exploring AI-assisted repair, orchestration and evaluation

cloud.devops

LEARNING

Improving deployment, automation and infrastructure knowledge

security.practice

ACTIVE

Applying secure defaults, quality gates and review controls

performance.lab

ACTIVE

Measuring concurrency, networking and algorithmic behavior

open.source

READY

Looking for useful projects and collaborative engineering work

> git stats --user Mouaz7

<div align="center">

<img height="175" src="https://github-readme-stats.vercel.app/api?username=Mouaz7&show_icons=true&hide_border=true&bg_color=05080B&title_color=E6C87A&text_color=EAFEF7&icon_color=35F2C1" alt="Mouaz GitHub statistics" />
<img height="175" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mouaz7&layout=compact&hide_border=true&bg_color=05080B&title_color=E6C87A&text_color=EAFEF7" alt="Most used languages" />

<br/>

<img src="https://streak-stats.demolab.com?user=Mouaz7&hide_border=true&background=05080B&ring=35F2C1&fire=E6C87A&currStreakLabel=61E7E2&sideLabels=EAFEF7&currStreakNum=EAFEF7&sideNums=EAFEF7&dates=8DB8AA" alt="GitHub contribution streak" />

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=Mouaz7&bg_color=05080B&color=8DB8AA&line=35F2C1&point=E6C87A&area=true&area_color=35F2C1&hide_border=true&custom_title=Contribution%20Matrix">
  <img width="100%" alt="Mouaz contribution graph" src="https://github-readme-activity-graph.vercel.app/graph?username=Mouaz7&bg_color=F4F7F5&color=5E7B70&line=0F8B6D&point=A66F00&area=true&area_color=0F8B6D&hide_border=true&custom_title=Contribution%20Matrix">
</picture>

> cat /personal/interests.txt

<div align="center">



</div>

> connect --with Mouaz

<div align="center">

I am interested in conversations and collaborations around backend engineering, system design, AI-assisted development, security, performance and open-source software.

<br/>



<br/>

mouaz@engineering:~$ echo "Build carefully. Measure honestly. Improve continuously."

</div>
