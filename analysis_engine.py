
from mobsf_parser import parse_mobsf_report

PERMISSION_INFO = {
    "CAMERA": ("Camera / Media", True),
    "RECORD_AUDIO": ("Microphone", True),
    "ACCESS_FINE_LOCATION": ("Location", True),
    "ACCESS_COARSE_LOCATION": ("Location", True),
    "READ_CONTACTS": ("Contacts", True),
    "READ_PHONE_STATE": ("Device / Phone Information", True),
    "GET_ACCOUNTS": ("Accounts", True),
    "READ_EXTERNAL_STORAGE": ("Storage", True),
    "INTERNET": ("Network", False),
    "WAKE_LOCK": ("System", False),
}

TRACKER_INFO = {
    "APPSFLYER": "Attribution / Marketing Analytics",
    "FIREBASE ANALYTICS": "Analytics",
    "GOOGLE CRASHLYTICS": "Crash Reporting",
    "ADMOB": "Advertising",
    "LOCALYTICS": "Analytics / Marketing",
    "PREBID MOBILE": "Advertising",
    "AMAZON ADVERTISEMENT": "Advertising",
}


def analyze_report(report):
    parsed = parse_mobsf_report(report)

    permissions = []
    for name in parsed["permissions"]:
        category, sensitive = PERMISSION_INFO.get(
            name.upper(), ("Unclassified", None)
        )
        permissions.append({
            "name": name,
            "category": category,
            "privacy_sensitive": sensitive,
            "evidence": "Declared permission in supplied report",
        })

    trackers = []
    for name in parsed["trackers"]:
        category = TRACKER_INFO.get(name.upper(), "Unclassified")
        trackers.append({
            "name": name,
            "category": category,
            "recognized": category != "Unclassified",
            "evidence": "SDK indicator in supplied report",
        })

    return {
        "app_name": parsed["app_name"],
        "package_name": parsed["package_name"],
        "permissions": permissions,
        "trackers": trackers,
        "summary": {
            "total_permissions": len(permissions),
            "sensitive_permissions": sum(
                p["privacy_sensitive"] is True for p in permissions
            ),
            "total_trackers": len(trackers),
            "recognized_trackers": sum(
                t["recognized"] for t in trackers
            ),
        },
    }


if __name__ == "__main__":
    example = {
        "app_name": "Sample Health App",
        "package_name": "com.example.health",
        "permissions": {
            "android.permission.CAMERA": {},
            "android.permission.RECORD_AUDIO": {},
            "android.permission.INTERNET": {},
        },
        "trackers": ["AppsFlyer", "Firebase Analytics"],
    }

    import json
    print(json.dumps(analyze_report(example), indent=2))
