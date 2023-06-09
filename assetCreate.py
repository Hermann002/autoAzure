# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import ClientSecretCredential
from azure.mgmt.media import AzureMediaServices


# Tenant ID for your Azure Subscription
TENANT_ID = "12f2971e-cac5-47a4-8d68-f1b22042f83e"

# Your Application Client ID of your Service Principal
CLIENT_ID = "850ab524-1d83-4a25-9f44-88368938f6fb"

# Your Service Principal secret key
CLIENT_SECRET = "3E48Q~x7KCUm1BC~IXu7hjdJVoAvf4ck5O-uJaph"


"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-media
# USAGE
    python asset_filterscreate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""



def main():
    client = AzureMediaServices(
        credential=ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET),   subscription_id="ac78f5eb-3612-400f-8319-71c0edb700ca",
        )

    response = client.assets.create_or_update(
        resource_group_name="Digiplus",
        account_name="digipluscameramedia",
        asset_name="myAsset1",
        parameters={
            "properties": {
                "description": "A documentary showing the ascent of Mount Logan",
                "storageAccountName": "digiplusstorageaccount",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/mediaservices/resource-manager/Microsoft.Media/Metadata/stable/2022-08-01/examples/assets-create.json
if __name__ == "__main__":
    main()