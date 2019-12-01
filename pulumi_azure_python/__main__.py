import pulumi
from pulumi_azure import core, storage, appservice

# Create an Azure Resource Group
location = pulumi.config.get_config('location')
print(location)

resource_group = core.ResourceGroup('my_pulumi_resource_group', location=location)

# Create an Azure resource (Storage Account)
account = storage.Account('storage',
                          # The location for the storage account will be derived automatically from the resource group.
                          resource_group_name=resource_group.name,
                          account_tier='Standard',
                          account_replication_type='LRS')


# play around with some resource groups and maybe a function?
appService = appservice.Plan("appServicePlan", resource_group_name=resource_group.name, sku= {"tier" : "free", "size" : "F1"})


example_function = appservice.FunctionApp(
    "MyTestFunction",
    resource_group_name=resource_group.name,
    app_service_plan_id=appService.id,
    app_settings={"runtime": "python"},
    storage_connection_string=account)


# Export the connection string for the storage account
pulumi.export('connection_string', account.primary_connection_string)
