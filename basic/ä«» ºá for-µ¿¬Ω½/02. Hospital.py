period = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7
for a in range(1, period + 1):
    patient = int(input())
    if a % 3 == 0 and treated_patients < untreated_patients:
        doctors += 1
    if patient <= doctors:
        treated_patients += patient
    else:
        treated_patients += doctors
        untreated_patients += patient - doctors
print(f"Treated patients: {treated_patients}.\n"
      f"Untreated patients: {untreated_patients}.")