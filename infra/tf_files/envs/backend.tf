data "aws_ecr_repository" "ecr_backend_repo" {
  name = "weather-ecr-repo"
}

resource "aws_ecs_task_definition" "definition" {
    family                  = "weather-backend-task"
    task_role_arn = aws_iam_role.backend_task_role.arn
    execution_role_arn = aws_iam_role.backend_task_execution_role.arn
    network_mode = "awsvpc"
    cpu = "256"
    memory = "512"
    requires_compatibilities = ["FARGATE"]
    container_definitions = jsonencode([
        {
            name = "weather-backend"
            image = "${data.aws_ecr_repository.ecr_backend_repo.repository_url}:latest"
            essential = true
            portMappings = [
                {
                    containerPort = 8080
                    hostPort = 8080
                    protocol = "tcp"
                }
            ]
            environment = []
        }
    ])
}