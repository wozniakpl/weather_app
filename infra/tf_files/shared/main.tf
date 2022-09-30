provider "aws" {
  region = var.aws_region
}

terraform {
  backend "s3" {}
  required_version = ">= 0.12.0"
}

variable "aws_region" {
  type        = string
}

variable "project_name" {
  type        = string
}

variable "env" {
  type        = string
}

locals {
  common_tags = {
    environment = var.env
    project     = var.project_name
    provisioner = "terraform"
  }
}
