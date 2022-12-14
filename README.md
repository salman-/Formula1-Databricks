# Formula1-Databricks

# How can we use this repository ?

1. Run the pipeline of Formula1-Terraform and find the created Azure Databricks and Azure Data Factory.
2. Follow instructions in ["Formula1-DataFactory" repository](https://github.com/salman-/Formula1-DataFactory) to setup the Azure Data Factory for formula1.
3. Clone this repository into Azure databricks. 
4. Setup keyvaults for values (clientId, clientSecret, tenantId, subscirptionId). The databricks use these secrets to have access to Storage-Account. If you create the keyvault using the Formula1-Terraform, these secrets are automatically added into keyvault. 
5. **Manually** give `Storage Blob Data Contributor` role to the service principal in Databricks (Azure portal -> Storae Account -> IAM -> Add Role Assignment -> Select the `Storage Blob Data Contributor`)
6. and permission to Storage account to share its blob with Azure Databricks
7. Give Databricks the Github personal token so that it can commiunicate with repo
8. Create secret scopes called `formula1-scope` via: `https://<databricks-instance>#secrets/createScope`
![Add scope to databricks](https://user-images.githubusercontent.com/4312244/206810911-853f5f46-3af8-4311-950a-79c58a7933fb.png)
9. In order to find access to from DataFactory to the Databricks, you have two main options:
  9.1. Generate an AccessToken from following path: * Open Databricks -> User Setting -> Access Token -> Click on Generate new Token* and use it linkedservice ![image](https://user-images.githubusercontent.com/4312244/207609564-135ee42f-76c9-43e0-9386-ba382ce48b3a.png)
  9.2. Alternatievly, you can select the *Managed service identity* in the linked service and it will offer a "Managed identity name", then refer to the Databricks-> IAM -> Add role -> Select your suggested "Managed identity name" and chose a contributor role to it.
  ![image](https://user-images.githubusercontent.com/4312244/207610488-46bfedfc-8aed-4095-a660-9b98440566f3.png)
[This video explains how to connect DataFactory to Databricks](https://www.youtube.com/watch?v=uk1wvsBvF34)
 
