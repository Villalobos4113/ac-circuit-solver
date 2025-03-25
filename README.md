# Python Project: AC Circuit Equation Solver

## Overview

Alternating Current (AC) circuits play a crucial role in electrical engineering, powering everything from household appliances to industrial machinery. Solving AC circuit equations accurately is essential for designing efficient electrical systems. This project provides a Python script that simplifies the analysis and solution of AC circuit equations involving resistors, capacitors, inductors, and complex impedances.

## Motivation

Solving AC circuit equations manually can be cumbersome and error-prone, especially when dealing with complex numbers and phasor representations. This script aims to automate and simplify these calculations, improving accuracy and efficiency for students, engineers, and hobbyists involved in electrical circuit design.

## Problem to Solve

The primary goal of this project is to assist users in quickly and accurately solving AC circuit equations by:

- Calculating impedances (Z) of resistors, inductors, and capacitors.
- Solving for currents, voltages, and power in series and parallel AC circuits.
- Handling complex arithmetic automatically (phasor calculations).

By automating these tasks, the project enhances accuracy and reduces the time spent on circuit analysis.

## Features

- **Impedance Calculation:** Compute impedance for resistors, capacitors, and inductors automatically.
- **Complex Arithmetic:** Efficiently handle phasor (complex number) calculations.
- **Circuit Analysis:** Solve equations for currents, voltages, and power in AC circuits.
- **Interactive CLI:** User-friendly command-line interface for easy interaction.

## Installation

### Prerequisites

Ensure Python 3.x is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Setting Up a Virtual Environment (Recommended)

1. Create a virtual environment:
   ```bash
   python3 -m venv venv/
   ```
2. Activate the environment:
   - **Windows**:
     ```bash
     PS> venv\Scripts\activate
     ```
   - **Linux or Mac**:
     ```bash
     $ source venv/bin/activate
     ```

### Installing Dependencies

Install required packages:
```bash
pip install -r requirements.txt
```

To add installed packages to `requirements.txt`:
```bash
pip freeze > requirements.txt
```

## Usage

### Running the AC Circuit Solver

1. Navigate to the project directory:
   ```bash
   cd ac-circuit-solver
   ```
2. Ensure the virtual environment is activated.
3. Run the main script:
   ```bash
   python main.py
   ```
4. Follow the prompts to input circuit details and obtain solutions.

## Example Usage

```bash
python main.py
```

Sample interaction:

```
To be add soon
```

## Project Structure

```bash
ac-circuit-solver/
│
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Authors

- Fernando Villalobos Betancourt [@Villalobos4113](https://www.github.com/Villalobos4113)

## License

This project is under the MIT License - see [LICENSE](https://choosealicense.com/licenses/mit/) for details.

