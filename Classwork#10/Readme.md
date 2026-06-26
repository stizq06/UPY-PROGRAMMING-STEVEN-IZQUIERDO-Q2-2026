# Git/GitHub Repository

This repository contains Python-based implementations, developed as part of the Programming course (Q2-2026). The objective of this assignment is to establish a professional development environment using Git for version control and GitHub for remote collaboration.

## Project Description

The included Python script (`school_management_system.py`) is a text-based tool that simulates a role-based login system for school administration. 

The program utilizes Python dictionaries to manage user credentials and academic records, employing `while` loops and `if/elif/else` decision flows to grant specific access based on three roles:
* **Student:** Can view their own grades, automatically calculating which subjects are approved (>= 8.0) and which are pending.
* **Professor:** Can view the list of students and continuously update their grades in a loop until an empty username is entered.
* **Coordinator:** Has read-only access to view all registered professors and students, including a formatted matrix of all academic records.

The code is cleanly structured into **INPUT**, **PROCESS**, and **OUTPUT** sections to maintain readability and order.

## Environment & Tools

* **Language:** Python 3.x
* **Version Control:** Git
* **Hosting Platform:** GitHub
* **Modeling Tools:** Mermaid (for Flowchart generation)

## How to Run the Program

1. Ensure you have Python installed on your system.
2. Clone this repository or download the source files.
3. Navigate to the project directory `Classwork-10-School-Management-System` and execute the script:

```bash
python school_management_system.py