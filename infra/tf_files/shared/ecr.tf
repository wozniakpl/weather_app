resource "aws_ecr_repository" "ecr_backend_repo" {
  name = "weather-ecr-repo"
  tags = local.common_tags
}