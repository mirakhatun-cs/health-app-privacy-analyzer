# Health App Privacy Analyzer
# Identifies potentially privacy-sensitive Android permissions.

sensitive_permissions = {
    "CAMERA",
    "RECORD_AUDIO",
    "ACCESS_FINE_LOCATION",
    "ACCESS_COARSE_LOCATION",
    "READ_CONTACTS",
    "READ_PHONE_STATE",
    "GET_ACCOUNTS",
    "READ_EXTERNAL_STORAGE"
}

print("Health App Privacy Analysis")
print("---------------------------")

file_name = input("Enter permission file name: ")

try:
    with open(file_name, "r") as file:
        permissions = file.readlines()

    print("\nAnalysis Results")
    print("----------------")

    for permission in permissions:
        permission = permission.strip().upper()

        if permission in sensitive_permissions:
            print(f"{permission}: Privacy-sensitive")
        else:
            print(f"{permission}: Not classified as privacy-sensitive")

except FileNotFoundError:
    print("Error: File not found.")

