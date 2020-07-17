import json

CRITICAL = 0
MEDIUM = 1
HIGH = 0

f = open('ECR_scan.json', )
test = json.loads(f)


resource = test["resources"][0]

finding_severity_counts = test["detail"]["finding-severity-counts"]

if "CRITICAL" in finding_severity_counts:
    critical_count = finding_severity_counts["CRITICAL"]
    if critical_count > CRITICAL:
        print("Resource {} has {} critical findings".format(resource, critical_count))
        
if "MEDIUM" in finding_severity_counts:
    medium_count = finding_severity_counts["MEDIUM"]
    if medium_count > MEDIUM:
        print("Resource {} has {} medium findings".format(resource, medium_count))
        
if "HIGH" in finding_severity_counts:
    high_count = finding_severity_counts["HIGH"]
    if high_count > HIGH:
        print("Resource {} has {} high findings".format(resource, high_count))
        