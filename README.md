# ERIVN-ISM_simulation
# ERIVN-ISM Simulation

This repository contains the **Python implementation of the Empirical Rule Interval-Valued Neutrosophic Interpretive Structural Modeling (ERIVN-ISM) simulation**, designed for academic research and decision modeling. The simulation compares the **ERIVN-ISM** methodology with the **traditional Fuzzy ISM (FISM)** approach through large-scale Monte Carlo-style replications.

## **Overview**
The simulation automates the following processes:
- **Generation of synthetic expert opinions** based on predefined linguistic scales.
- **Transformation of expert opinions** into respective **Fuzzy ISM (FISM) and ERIVN-ISM** decision matrices.
- **Conversion of neutrosophic numbers** using the **Empirical Rule (mean ± standard deviation)** to obtain Interval-Valued Neutrosophic Numbers (IVNNs).
- **Application of the deneutrosophication operator** to transform neutrosophic values into crisp values.
- **Threshold computation and reachability matrix generation** for both models.
- **Computation of Dice-Sørensen Similarity (DSS)** to evaluate structural similarity.
- **Visualization of DSS distribution** using **boxplots**.

## **Features**
- Fully automated **Monte Carlo-style** simulation.
- Supports **customizable replication settings**.
- Provides **statistical insights and visualization** for validation.
- Written in **Python**, ensuring flexibility and reproducibility.

## **Installation**
To run the simulation, ensure that you have **Python 3.7+** installed along with the required dependencies. You can install the necessary libraries using:

```bash
pip install numpy matplotlib
```

## **Usage**
Clone the repository and navigate to the directory:

```bash
git clone [GITHUB_REPOSITORY_URL]
cd ERIVN-ISM-Simulation
```

Run the Python script:

```bash
python erivn_ism_simulation.py
```

The script will prompt you for the **number of replications** and generate a **boxplot visualization** of Dice-Sørensen Similarity scores.

## **Example Output**
After execution, the program will display a **boxplot** showing the similarity distribution between ERIVN-ISM and FISM models. The output includes:
- **Mean Dice-Sørensen Similarity**
- **Standard Deviation of DSS**
- **Total number of replications**

A sample output visualization is provided in **Figure 4.1** of the accompanying research paper.

## **License**
This simulation is provided for **academic and research purposes only**. If you use this work in your research, please cite the corresponding paper.

## **Contributions**
Contributions are welcome! Feel free to **open an issue** or submit a **pull request** if you have any improvements.

## **Contact**
For any inquiries regarding the simulation, methodology, or implementation, please contact **[Your Email or GitHub Username]**.

