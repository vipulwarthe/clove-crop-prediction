provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "data_bucket" {
  bucket = "clove-mlops-data-bucket"
}

resource "aws_ecr_repository" "repo" {
  name = "clove-mlops-repo"
}