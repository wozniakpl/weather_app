remote_state {
  backend = "s3"

  config = {
    encrypt = false
    bucket  = "weather-app-bckt"
    key     = "terraform/${path_relative_to_include()}.tfstate"
    region  = "us-east-1"
  }
}
