from azure.identity import ClientSecretCredential
from azure.mgmt.media import AzureMediaServices

# Tenant ID for your Azure Subscription
TENANT_ID = "12f2971e-cac5-47a4-8d68-f1b22042f83e"

# Your Application Client ID of your Service Principal
CLIENT_ID = "850ab524-1d83-4a25-9f44-88368938f6fb"

# Your Service Principal secret key
CLIENT_SECRET = "3E48Q~x7KCUm1BC~IXu7hjdJVoAvf4ck5O-uJaph"

# Your Azure Subscription ID
#SUBSCRIPTION_ID = "ac78f5eb-3612-400f-8319-71c0edb700ca"

# Your Resource Group name
#RESOURCE_GROUP_NAME = "Digiplus"

# Your Azure Media Service account name
#ACCOUNT_NAME = "digipluscameramedia"

#credentials = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)

# The Azure Media Services Client
#client = AzureMediaServices(credentials, SUBSCRIPTION_ID)

# Now that you are authenticated, you can manipulate the entities.
# For example, list assets in your Media Services account
#assets = client.assets.list(RESOURCE_GROUP_NAME, ACCOUNT_NAME)

def main():
    client = AzureMediaServices(
        credential=ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET),
        subscription_id="ac78f5eb-3612-400f-8319-71c0edb700ca",
    )

    response = client.live_events.begin_start(
        resource_group_name="Digiplus",
        account_name="digipluscameramedia",
        live_event_name="digiplusstream",
    ).result()
    print(response)


# x-ms-original-file: specification/mediaservices/resource-manager/Microsoft.Media/Streaming/stable/2022-08-01/examples/liveevent-start.json
if __name__ == "__main__":
    main()