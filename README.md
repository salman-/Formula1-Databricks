# Formula1-Databricks

### Ingestion

### Transform

## Load


# How can we use this repository ?

1. After running the pipeline of Formula1-Terraform, you can find a Azure Databricks under your resource group.
2. Setup the Azure Data Factory for formula1 using the "Formula1-DataFactory" repository.
3. Clone this repository into Azure databricks
4. Setup keyvaults for values (clientId, clientSecret, tenantId, subscirptionId) so that databricks can have access to other services such as Storage-Account
5. Give proper role and permission to Storage account to share its blob with Azure Databricks
6. Give Databricks the Github personal token so that it can commiunicate with repo
4. Create secret scopes called `formula1-scope` via: `https://<databricks-instance>#secrets/createScope`

