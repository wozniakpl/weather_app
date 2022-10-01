resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "${var.project_name}-${var.env}-rds-subnet-group"
  subnet_ids = concat(aws_subnet.main.*.id, aws_subnet.second.*.id)
  tags       = local.common_tags
}

resource "aws_security_group" "rds_security_group" {
  name        = "${var.project_name}-${var.env}-rds-sg"
  description = "RDS security group"
  vpc_id      = aws_vpc.main.id
  tags        = local.common_tags
}

resource "aws_db_instance" "rds_instance" {
  identifier              = "${var.project_name}-${var.env}-rds-instance"
  allocated_storage       = 20
  engine                  = "postgres"
  engine_version          = "12.11"
  instance_class          = "db.t2.micro"
  db_name                 = "postgres"
  username                = "postgres"
  password                = "postgres" // TODO
  db_subnet_group_name    = aws_db_subnet_group.rds_subnet_group.name
  vpc_security_group_ids  = [aws_security_group.rds_security_group.id]
  skip_final_snapshot     = true
  publicly_accessible     = false
  backup_retention_period = 0
  tags                    = local.common_tags
}