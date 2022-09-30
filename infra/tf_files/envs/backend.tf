data "aws_ecr_repository" "ecr_backend_repo" {
  name = "weather-ecr-repo"
}

resource "aws_ecs_task_definition" "backend_task" {
  family                   = "weather-backend-task"
  requires_compatibilities = ["FARGATE"]
    network_mode             = "awsvpc"
    cpu                      = "256"
    memory                   = "512"
    task_role_arn = aws_iam_role.backend_task_role.arn
    execution_role_arn = aws_iam_role.backend_task_execution_role.arn
    tags = local.common_tags
    container_definitions = <<DEFINITION
[
    {
        "name": "weather-backend",
        "image": "${data.aws_ecr_repository.ecr_backend_repo.repository_url}:latest",
        "memory": 512,
        "essential": true,
        "portMappings": [
            {
                "containerPort": 9000,
                "hostPort": 9000,
                "protocol": "tcp"
            }
        ],
        "environmentFiles": [
            {
                "type": "s3",
                "value": "${var.backend_variables_bucket_name}/${var.env}.env"
            }
        ],
        "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
                "awslogs-group": "weather-backend",
                "awslogs-region": "us-east-1",
                "awslogs-stream-prefix": "weather-backend"
            }
        }
    }
]
DEFINITION
}