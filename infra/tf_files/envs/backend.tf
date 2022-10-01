data "aws_ecr_repository" "ecr_backend_repo" {
  name = "weather-ecr-repo"
}

resource "aws_ecs_task_definition" "backend_task_definition" {
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

data "aws_ecs_task_definition" "backend_task_definition_name" {
    task_definition = aws_ecs_task_definition.backend_task_definition.family
    depends_on = [
        aws_ecs_task_definition.backend_task_definition
    ]
}

resource "aws_security_group" "backend_security_group" {
    name = "weather-backend-sg"
    description = "Weather backend security group"
    vpc_id = aws_vpc.main.id
}

resource "aws_ecs_cluster" "weather-cluster" {
  name = "${var.project_name}-${var.env}-ecs-cluster"
  tags = local.common_tags
}


resource "aws_ecs_service" "backend_service" {
    name = "weather-backend-service"
    cluster = aws_ecs_cluster.weather-cluster.id
    task_definition = data.aws_ecs_task_definition.backend_task_definition_name.arn
    desired_count = 1
    launch_type = "FARGATE"
    network_configuration {
        subnets = aws_subnet.main.*.id
        security_groups = [aws_security_group.backend_security_group.id]
        assign_public_ip = true
    }
    depends_on = [
        aws_ecs_task_definition.backend_task_definition
    ]
}