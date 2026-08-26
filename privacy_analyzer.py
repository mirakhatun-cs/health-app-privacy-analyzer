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

permissions = [
    "CAMERA",
    "INTERNET",
    "RECORD_AUDIO",
    "ACCESS_FINE_LOCATION",
    "WAKE_LOCK"
]

print("Health App Privacy Analysis")
print("---------------------------")

for permission in permissions:
    if permission in sensitive_permissions:
        print(f"{permission}: Privacy-sensitive")
    else:
        print(f"{permission}: Not classified as privacy-sensitive")
