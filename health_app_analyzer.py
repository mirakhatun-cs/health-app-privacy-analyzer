# Health App Privacy & Security Analyzer
# Combines permission and tracker analysis into one report.

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

tracker_info = {
    "APPSFLYER": "Attribution / Marketing Analytics",
    "FIREBASE ANALYTICS": "Analytics",
    "GOOGLE CRASHLYTICS": "Crash Reporting",
    "ADMOB": "Advertising",
    "LOCALYTICS": "Analytics / Marketing",
    "PREBID MOBILE": "Advertising",
    "AMAZON ADVERTISEMENT": "Advertising"
}

print("Health App Privacy & Security Report")
print("====================================")

permission_file = input("Enter permission file name: ")
tracker_file = input("Enter tracker file name: ")

try:
    with open(permission_file, "r") as file:
        permissions = file.readlines()

    with open(tracker_file, "r") as file:
        trackers = file.readlines()

    print("\nPermission Findings")
    print("-------------------")

    sensitive_count = 0
    permission_count = 0

    for permission in permissions:
        permission = permission.strip().upper()

        if not permission:
            continue

        permission_count += 1

        if permission in permission_info:
            category, is_sensitive = permission_info[permission]

            if is_sensitive:
                sensitive_count += 1
                status = "Privacy-sensitive"
            else:
                status = "Not classified as privacy-sensitive"

            print(f"{permission} | {category} | {status}")
        else:
            print(f"{permission} | Unclassified | Needs further review")

    print("\nTracker Findings")
    print("----------------")

    tracker_count = 0
    known_tracker_count = 0

    for tracker in trackers:
        tracker = tracker.strip()

        if not tracker:
            continue

        tracker_count += 1
        tracker_key = tracker.upper()

        if tracker_key in tracker_info:
            known_tracker_count += 1
            print(f"{tracker} | {tracker_info[tracker_key]}")
        else:
            print(f"{tracker} | Unclassified | Needs further review")

    print("\nSummary")
    print("-------")
    print(f"Total permissions analyzed: {permission_count}")
    print(f"Privacy-sensitive permissions identified: {sensitive_count}")
    print(f"Total trackers analyzed: {tracker_count}")
    print(f"Known trackers identified: {known_tracker_count}")

except FileNotFoundError:
    print("Error: One or more input files could not be found.")