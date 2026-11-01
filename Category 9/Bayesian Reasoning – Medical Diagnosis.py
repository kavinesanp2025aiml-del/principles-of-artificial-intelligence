# Bayesian Reasoning for Medical Diagnosis

# Prior probability
P_D = 0.10

# Probability of symptoms
P_Fever_D = 0.80
P_Cough_D = 0.70

P_Fever_NoD = 0.20
P_Cough_NoD = 0.30

# Patient symptoms
fever = True
cough = True

# Likelihood calculation
if fever and cough:
    P_S_D = P_Fever_D * P_Cough_D
    P_S_NoD = P_Fever_NoD * P_Cough_NoD

elif fever:
    P_S_D = P_Fever_D * (1 - P_Cough_D)
    P_S_NoD = P_Fever_NoD * (1 - P_Cough_NoD)

elif cough:
    P_S_D = (1 - P_Fever_D) * P_Cough_D
    P_S_NoD = (1 - P_Fever_NoD) * P_Cough_NoD

else:
    P_S_D = (1 - P_Fever_D) * (1 - P_Cough_D)
    P_S_NoD = (1 - P_Fever_NoD) * (1 - P_Cough_NoD)

# Bayes theorem
P_S = P_S_D * P_D + P_S_NoD * (1 - P_D)

P_D_S = (P_S_D * P_D) / P_S

print("Bayesian Medical Diagnosis")

print("Prior Probability:", P_D)
print("Patient has Fever:", fever)
print("Patient has Cough:", cough)

print("Probability of Disease:",
      round(P_D_S * 100, 2), "%")

if P_D_S > 0.5:
    print("Result: High possibility of disease")
else:
    print("Result: Low possibility of disease")
