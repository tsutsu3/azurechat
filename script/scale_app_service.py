import argparse
import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.web import WebSiteManagementClient
from dotenv import load_dotenv

load_dotenv()

SID = os.environ["AZURE_SUBSCRIPTION_ID"]
GID = os.environ["AZURE_RESOURCE_GROUP_ID"]
ASP = os.environ["APP_SERVICE_PLAN"]

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["start", "end"])
args = parser.parse_args()

credential = DefaultAzureCredential()
client = WebSiteManagementClient(credential=credential, subscription_id=SID)

app_service_plan = client.app_service_plans.get(GID, ASP)
print(f"Get app service plan:\n{app_service_plan.sku}")

print("Update ...", end="")
if args.mode == "start":
    app_service_plan = client.app_service_plans.begin_create_or_update(GID, ASP, {"location": "japaneast", "sku" : {"name" : "B1"}}).result()
elif args.mode == "end":
    app_service_plan = client.app_service_plans.begin_create_or_update(GID, ASP, {"location": "japaneast", "sku" : {"name" : "F1"}}).result()
else:
    raise SystemExit
print("done.")
print(f"Update app service plan:\n{app_service_plan.sku}")