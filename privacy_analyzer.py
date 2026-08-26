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

user_input = input(
    "Enter Android permissions separated by commas: "
)

permissions = user_input.split(",")

print("\nAnalysis Results")
print("----------------")

for permission in permissions:
    permission = permission.strip().upper()

    if permission in sensitive_permissions:
        print(f"{permission}: Privacy-sensitive")
    else:
        print(f"{permission}: Not classified as privacy-sensitive")