import subprocess
import os

def run_docker():
    # Set the image name
    image_name = "my_django_app"
    
    # Build the Docker image
    print("Building Docker image...")
    try:
        subprocess.run(["docker", "build", "-t", image_name, "."], check=True)
    except subprocess.CalledProcessError:
        print("Failed to build Docker image.")
        return

    # Run the Docker container
    print("Running Docker container...")
    try:
        print("Django app is running on http://localhost:8000/")
        subprocess.run(["docker", "run", "-p", "8000:8000", image_name], check=True)
    except subprocess.CalledProcessError:
        print("Failed to run Docker container.")
        return
    
  

if __name__ == "__main__":
    run_docker()
