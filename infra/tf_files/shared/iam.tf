resource "aws_iam_user" "user" {
  name = "weather-dev-user"
  path = "/"
}

resource "aws_iam_access_key" "user_key" {
  user = aws_iam_user.user.name
}

resource "aws_iam_policy" "user_policy_ecr" {
  name = "${var.project_name}-${var.env}-userPolicyEcr"
  path = "/"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["ecr:*"]
        Effect   = "Allow"
        Resource = ["arn:aws:ecr:*:*:repository/*"]
      },
      {
        Action   = ["ecr:GetAuthorizationToken"]
        Effect   = "Allow"
        Resource = ["*"]
      }
    ]
  })
}
resource "aws_iam_user_policy_attachment" "user_policy_ecr" {
  user       = aws_iam_user.user.name
  policy_arn = aws_iam_policy.user_policy_ecr.arn
}


output "user_id" {
  value       = aws_iam_access_key.user_key.id
}

output "user_secret" {
  value       = aws_iam_access_key.user_key.secret
  sensitive   = true
}
