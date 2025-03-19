import numpy as np
import random
import matplotlib.pyplot as plt


def erivn_fism_simulation():
    replications = int(input("Enter the number of replications: "))
    DSS = []

    for w in range(replications):
        z = random.randint(5, 20)  # Number of experts
        x = random.randint(10, 30)  # Number of factors

        # Initialize matrices
        rndmat = np.zeros((x, x, z), dtype=int)
        FExpert = np.zeros((x, x, z), dtype=object)
        ERIVNExpert = np.zeros((x, x, z), dtype=object)
        FDec = np.zeros((x, x), dtype=object)
        ERIVNDec = np.zeros((x, x), dtype=object)
        FCrispDec = np.zeros((x, x))
        ERIVNCrispDec = np.zeros((x, x))
        FIRM = np.zeros((x, x), dtype=int)
        ERIVNIRM = np.zeros((x, x), dtype=int)

        # Fill rndmat and initialize expert opinions
        for t in range(z):
            for i in range(x):
                for j in range(x):
                    rndmat[i, j, t] = random.randint(0, 4) if i != j else 4

                    # Fuzzy ISM expert opinions
                    FExpert[i, j, t] = {
                        0: {"Le": 0, "Mi": 0, "Ri": 0.25},
                        1: {"Le": 0, "Mi": 0.25, "Ri": 0.5},
                        2: {"Le": 0.25, "Mi": 0.5, "Ri": 0.75},
                        3: {"Le": 0.5, "Mi": 0.75, "Ri": 1.0},
                        4: {"Le": 0.75, "Mi": 1.0, "Ri": 1.0},
                    }[rndmat[i, j, t]]

                    # ERIVN-ISM expert opinions (SVNN format - corrected)
                    ERIVNExpert[i, j, t] = {
                        0: {"T": 0.1, "I": 0.8, "F": 0.9},
                        1: {"T": 0.35, "I": 0.6, "F": 0.7},
                        2: {"T": 0.5, "I": 0.4, "F": 0.45},
                        3: {"T": 0.8, "I": 0.2, "F": 0.15},
                        4: {"T": 0.9, "I": 0.1, "F": 0.1},
                    }[rndmat[i, j, t]]

        # Aggregate expert decisions
        for i in range(x):
            for j in range(x):
                Fl, Fm, Fr = 0, 0, 0
                T_values, I_values, F_values = [], [], []

                for t in range(z):
                    Fl += FExpert[i, j, t]["Le"]
                    Fm += FExpert[i, j, t]["Mi"]
                    Fr += FExpert[i, j, t]["Ri"]

                    T_values.append(ERIVNExpert[i, j, t]["T"])
                    I_values.append(ERIVNExpert[i, j, t]["I"])
                    F_values.append(ERIVNExpert[i, j, t]["F"])

                # Compute Fuzzy ISM Decision
                FDec[i, j] = {"Le": Fl / z, "Mi": Fm / z, "Ri": Fr / z}
                FCrispDec[i, j] = (FDec[i, j]["Le"] + 2 * FDec[i, j]["Mi"] + FDec[i, j]["Ri"]) / 4

                # Compute IVNN Bounds
                T_mean, I_mean, F_mean = np.mean(T_values), np.mean(I_values), np.mean(F_values)
                T_std, I_std, F_std = np.std(T_values, ddof=1), np.std(I_values, ddof=1), np.std(F_values, ddof=1)

                T_L, T_U = max(0, T_mean - T_std), min(1, T_mean + T_std)
                I_L, I_U = max(0, I_mean - I_std), min(1, I_mean + I_std)
                F_L, F_U = max(0, F_mean - F_std), min(1, F_mean + F_std)

                ERIVNDec[i, j] = {"T": [T_L, T_U], "I": [I_L, I_U], "F": [F_L, F_U]}

                # Deneutrosophication operator
                numerator = (T_L + T_U + (1 - F_L) + (1 - F_U) + (T_L * T_U) + np.sqrt(abs((1 - F_L) * (1 - F_U)))) / 6
                denominator = ((1 - (I_L + I_U) / 2) * np.sqrt(abs((1 - I_L) * (1 - I_U)))) / 2

                ERIVNCrispDec[i, j] = numerator * denominator if denominator != 0 else 0

        # Compute thresholds
        ERIVNThreshold = np.mean(ERIVNCrispDec)
        FuzzyThreshold = np.mean(FCrispDec)

        # Generate binary reachability matrices
        ERIVNIRM = (ERIVNCrispDec >= ERIVNThreshold).astype(int)
        FIRM = (FCrispDec >= FuzzyThreshold).astype(int)
        np.fill_diagonal(ERIVNIRM, 1)
        np.fill_diagonal(FIRM, 1)

        # Compute Dice-Sørensen similarity
        JaccA = np.sum(ERIVNIRM)
        JaccB = np.sum(FIRM)
        Joint = np.sum(np.logical_and(ERIVNIRM, FIRM))
        DSS.append(2 * Joint / (JaccA + JaccB) if (JaccA + JaccB) != 0 else 0)

    # Generate boxplot with additional data
    plt.boxplot(DSS, vert=True, patch_artist=True, showmeans=True, meanline=True)
    plt.title("Dice-Sørensen Similarity Boxplot")
    plt.ylabel("DSS")
    plt.xticks([1], ["Simulation Results"])
    for i, value in enumerate(DSS):
        plt.scatter(1, value, alpha=0.6, color="blue", label="Data Points" if i == 0 else "")
    mean_dss = np.mean(DSS)
    std_dss = np.std(DSS, ddof=1)
    plt.text(1.1, mean_dss, f"Mean: {mean_dss:.2f}", color="red")
    plt.text(1.1, mean_dss - std_dss, f"SD: {std_dss:.2f}", color="green")
    plt.text(1.1, min(DSS), f"Replications: {len(DSS)}", color="blue")
    plt.legend()
    plt.show()

    return np.mean(DSS), np.std(DSS, ddof=1)


# Example usage
average_dss, standard_error = erivn_fism_simulation()
print(f"Average DSS: {average_dss}")
print(f"Standard Error: {standard_error}")
