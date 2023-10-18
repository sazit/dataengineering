terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.7.0"
    }
  }

  backend "azurerm" {
    resource_group_name  = "rg-dev-ause-dataengineering"
    storage_account_name = "sadevausedataeng01"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
    use_oidc             = true
  }
}

provider "azurerm" {
  features {}
  use_oidc = true
}

resource "azurerm_resource_group" "rg-dev-ause-dataengineering-01" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_data_factory" "adf-dev-ause-api-integration-01" {
  name                = "adf-dev-ause-api-integration-01"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
}
