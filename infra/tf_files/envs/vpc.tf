resource "aws_vpc" "main" {
  cidr_block = cidrsubnet("172.16.0.0/12", 11, random_integer.cidr_seed.result)

  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = merge(
    {
      "Name" = "${var.project_name}@${var.env}"
    },
    local.common_tags
  )
}

resource "random_integer" "cidr_seed" {
  min = 0
  max = 2047
}

resource "aws_subnet" "main" {
  count  = 1
  vpc_id = aws_vpc.main.id

  availability_zone = "us-east-1a"
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 2, count.index)

  tags = local.common_tags
}

resource "aws_subnet" "second" {
    count  = 1
    vpc_id = aws_vpc.main.id

    availability_zone = "us-east-1b"
    cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 2, count.index + 1)

    tags = local.common_tags
}