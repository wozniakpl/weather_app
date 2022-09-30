include {
  path = find_in_parent_folders()
}
terraform {
  source = "${get_parent_terragrunt_dir()}//tf_files/shared/"
}

inputs = {
  aws_region  = "us-east-1"
  aws_profile = "bwdev"
  project_name = "weather-app"
  env          = "shared"
}
