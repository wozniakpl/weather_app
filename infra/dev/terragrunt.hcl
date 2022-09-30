include {
  path = find_in_parent_folders()
}
terraform {
  source = "${get_parent_terragrunt_dir()}//tf_files/envs/"
}

inputs = {
  aws_region = "us-east-1"
  aws_profile = "bwdev"
  project_name = "weather-app"
  env = "dev"

  backend_variables_bucket_name = "weather-app-bckt"

}
