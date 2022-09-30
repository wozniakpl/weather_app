data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com", "application-autoscaling.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "backend_task_role" {
  name               = "${var.project_name}-${var.env}-ecs-backend-task-rl"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
  tags               = local.common_tags
}

resource "aws_iam_role" "backend_task_execution_role" {
  name               = "${var.project_name}-${var.env}-ecs-backend-execution-rl"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
  tags               = local.common_tags
}
