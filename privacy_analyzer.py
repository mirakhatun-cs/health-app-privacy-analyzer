# Health App Privacy Analyzer
# Analyzes Android permissions and groups them by privacy-related category.

permission_info = {
    "CAMERA": ("Camera / Media", True),
    "RECORD_AUDIO": ("Microphone", True),
    "ACCESS_FINE_LOCATION": ("Location", True),
    "ACCESS_COARSE_LOCATION": ("Location", True),
    "READ_CONTACTS": ("Contacts", True),
    "READ_PHONE_STATE": ("Device / Phone Information", True),
    "GET_ACCOUNTS": ("Accounts", True),
    "READ_EXTERNAL_STORAGE": ("Storage", True),

    "INTERNET": ("Network", False),
    "WAKE_LOCK": ("System", False)
}

print("Health App Privacy Analysis")
print("---------------------------")

file_name = input("Enter permission file name: ")

try:
    with open(file_name, "r") as file:
        permissions = file.readlines()

    print("\nAnalysis Results")
    print("----------------")

    sensitive_count = 0
    total_count = 0

    for permission in permissions:
        permission = permission.strip().upper()

        # Skip empty lines
        if not permission:
            continue

        total_count += 1

        if permission in permission_info:
            category, is_sensitive = permission_info[permission]

            if is_sensitive:
                sensitive_count += 1
                status = "Privacy-sensitive"
            else:
                status = "Not classified as privacy-sensitive"

            print(
                f"{permission} | Category: {category} | {status}"
            )

        else:
            print(
                f"{permission} | Category: Unclassified | Needs further review"
            )

    print("\nSummary")
    print("-------")
    print(f"Total permissions analyzed: {total_count}")
    print(f"Privacy-sensitive permissions identified: {sensitive_count}")

except FileNotFoundError:
    print("Error: File not found.")