
import json
from pathlib import Path


def parse_mobsf_report(report):
    """Extract available findings from a MobSF JSON report."""

    permissions_data = report.get("permissions", {})
    permissions = []

    if isinstance(permissions_data, dict):
        for name in permissions_data:
            permissions.append(name.split(".")[-1])

    elif isinstance(permissions_data, list):
        for item in permissions_data:
            if isinstance(item, str):
                permissions.append(item.split(".")[-1])
            elif isinstance(item, dict):
                name = item.get("permission") or item.get("name")
                if name:
                    permissions.append(str(name).split(".")[-1])

    trackers_data = report.get("trackers", [])
    trackers = []

    if isinstance(trackers_data, list):
        for item in trackers_data:
            if isinstance(item, str):
                trackers.append(item)
            elif isinstance(item, dict):
                name = item.get("name")
                if name:
                    trackers.append(str(name))

    elif isinstance(trackers_data, dict):
        trackers = list(trackers_data.keys())

    return {
        "app_name": report.get("app_name", "Unknown App"),
        "package_name": report.get("package_name", "Unknown"),
        "permissions": sorted(set(permissions)),
        "trackers": sorted(set(trackers)),
        "permission_count": len(set(permissions)),
        "tracker_count": len(set(trackers))
    }


def load_mobsf_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        report = json.load(file)

    if not isinstance(report, dict):
        raise ValueError("Expected a MobSF JSON object.")

    return parse_mobsf_report(report)


if __name__ == "__main__":
    sample = {
        "app_name": "Sample Health App",
        "package_name": "com.example.health",
        "permissions": {
            "android.permission.CAMERA": {},
            "android.permission.RECORD_AUDIO": {},
            "android.permission.INTERNET": {}
        },
        "trackers": ["AppsFlyer", "Firebase Analytics"]
    }

    result = parse_mobsf_report(sample)
    print(json.dumps(result, indent=2))
