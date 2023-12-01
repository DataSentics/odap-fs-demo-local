# ODAP feature store demo

Demo repositories offer an easy way of testing ODAP framework functionalities on any Databricks workspace while showcasing many of features built into the framework.

All the freamework components are described in the documentation which is available [here](https://www.notion.so/datasentics/ODAP-Use-Case-Framework-f6ed0a95140d48c69b642b568c6db85f).

## Datasets

The demo leverages Databricks datasets which are available on the platform by default ([databricks-datasets](https://docs.databricks.com/en/dbfs/databricks-datasets.html#databricks-datasets-databricks-datasets)). The datasets are then slightly modified and saved as tables into the catalog as a part of the demo setup. 

The original datasets are: 
* people - Information about people including names, birth information and salary.
* bike sharing - Information about bike sharing stations including weather conditions and stations usage. 

## Entities

Two different entities (each based on a different original dataset) are defined. Each entity has its configuration that defines its feature orchestration details which enables operating with multiple entities within the same repository. This can be done by defining which configuration file is used as mentioned in the [How to use](#how-to-use) chapter.

## Repositories

At the moment, there are two distinct publically available repositories that operate with identical datasets. This allows mocking an orchestration from multiple sources while having a single orchestration entry point.

### Global 
The repository is available on [GitHub](https://github.com/DataSentics/odap-fs-demo-global). It contains definitions of features that are expected to be orchestrated from a different (local) repository. Besides that, it is also setup so that the included features can be standalone orchestrated from within the repository if needed. 

### Local

The repository is available on [GitHub](https://github.com/DataSentics/odap-fs-demo-local). It is the main repository that also serves as an entry point for the orchestration. It contains definitions of features that are expected to be orchestrated from within the repository, together with the ones stored in a global one. By default, it orchestrates features from both repositories all together. 

---

## How to use

This is a step-by-step guide on how to deploy the demo to Databricks and run an orchestration. 

### Step 1 - Clone repositories

*Note:* If this is the first time of cloning from Github, you have to configure the git credentials. To do that, please follow an [official Databricks guide](https://docs.databricks.com/en/repos/get-access-tokens-from-git-provider.html).

Clone both repositories to the root of your Databricks repos. This can be done via HTTPS by navigating to *Workspace* > *Repos* > *Add* > *Repo*:

* odap-fs-demo-local: `https://github.com/DataSentics/odap-fs-demo-local.git`

* odap-fs-demo-global: `https://github.com/DataSentics/odap-fs-demo-global.git`

It is essential to enter correct names for each of the cloned repositories as they are referenced in the default configuration files:

### Step 2 - Prepare datasets 

* Navigate to the `data/init_source_tables` in the [local](https://github.com/DataSentics/odap-fs-demo-local) repository.

* Run the notebook by clicking the `Run all` button in the notebook UI.

The demo expects default Databricks datasets to be available on DBFS. 

### Step 3 - Setup clusters

It is necessary to setup one cluster per [entity](#entities). The clusters can have arbitrary name but it is recommended to include the entity names as a good practice. The configuration of each cluster should be the same with an exception of environment variables (see below). You can create a new cluster by navigating to *Compute* > *Create Compute*.  

Recommended settings (common): 
* **cluster type:** Single node (sufficient for the demo)

* **DBR:** 12.2 LTS ML, important to select the ML version

* **node type:** Standard_DS3_v2, or any other cheap node type

To configure each cluster for a particular entity, an environment variable with a path to a config file has to be added. In the cluster edit mode, navigate to *Advanced options* > *Spark* > *Environment variables* and add the following variables for given entities: 

* person: `ODAP_CONFIG_PATH="_config/config-person.yaml"`

* station: `ODAP_CONFIG_PATH="_config/config-station.yaml"`

To finish the creation of a cluster, click on *Create compute*. 

### Step 4 - Modify configuration (optional)

Before running the orchestration, you can modify its default configuration for each entity. A detailed guide on how to setup feature orchestration can be found in the [ODAP documentation](https://www.notion.so/datasentics/Configuring-calculation-1caba3bde82f48b4ab7e1ac6cc420e49).

### Step 5 - Run the orchestration

* Go to the orchestration notebook that is stored at `orchestration/features_orchestrator` in the [local](https://github.com/DataSentics/odap-fs-demo-local) repository. 

* Attach a cluster that is setup for an entity you want to orchestrate the features for. 

* Run the notebook by clicking the `Run all` button in the notebook UI.

The notebook run will automatically create all the necesarry tables and calculate the defined features from both repositories.
