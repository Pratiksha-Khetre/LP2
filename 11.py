# Expert System for Hospitals and Medical Facilities

def medical_expert_system():

    print("======================================")
    print("   HOSPITAL EXPERT SYSTEM")
    print("======================================")

    name = input("Enter Patient Name: ")

    print("\nAnswer with yes or no.\n")

    fever = input("Do you have fever? ").lower()
    cough = input("Do you have cough? ").lower()
    headache = input("Do you have headache? ").lower()
    stomach = input("Do you have stomach pain? ").lower()

    print("\n===== MEDICAL REPORT =====")

    # Rules for diagnosis
    if fever == "yes" and cough == "yes":
        print("Possible Disease: Flu or Viral Infection")
        print("Suggested Doctor: General Physician")

    elif fever == "yes" and headache == "yes":
        print("Possible Disease: Migraine or Fever")
        print("Suggested Doctor: Neurologist")

    elif stomach == "yes":
        print("Possible Disease: Stomach Infection")
        print("Suggested Doctor: Gastroenterologist")

    else:
        print("No major disease detected.")
        print("Stay healthy and take rest.")

    print(f"\nThank You {name} for using the Expert System.")


# Function Call
medical_expert_system()