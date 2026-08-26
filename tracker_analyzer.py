# Health App Privacy Analyzer
# Analyzes third-party trackers and SDKs found in mobile applications.

tracker_info = {
    "APPSFLYER": "Attribution / Marketing Analytics",
    "FIREBASE ANALYTICS": "Analytics",
    "GOOGLE CRASHLYTICS": "Crash Reporting",
    "ADMOB": "Advertising",
    "LOCALYTICS": "Analytics / Marketing",
    "PREBID MOBILE": "Advertising",
    "AMAZON ADVERTISEMENT": "Advertising"
}

print("Health App Tracker Analysis")
print("---------------------------")

file_name = input("Enter tracker file name: ")

try:
    with open(file_name, "r") as file:
        trackers = file.readlines()

    print("\nTracker Analysis Results")
    print("------------------------")

    known_count = 0
    total_count = 0

    for tracker in trackers:
        tracker = tracker.strip()

        if not tracker:
            continue

        total_count += 1
        tracker_key = tracker.upper()

        if tracker_key in tracker_info:
            category = tracker_info[tracker_key]
            known_count += 1
            print(f"{tracker} | Category: {category}")
        else:
            print(f"{tracker} | Category: Unclassified | Needs further review")

    print("\nSummary")
    print("-------")
    print(f"Total trackers analyzed: {total_count}")
    print(f"Known trackers identified: {known_count}")

except FileNotFoundError:
    print("Error: File not found.")