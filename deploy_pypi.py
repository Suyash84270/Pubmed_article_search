
import os
import subprocess
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the PyPI token from environment variables
token = os.getenv('TWINE_PASSWORD')

if not token:
    print("Error: TWINE_PASSWORD not set in .env or environment variables.")
else:
    # Use Twine to publish the package to TestPyPI
    try:
        result = subprocess.run(
            ['python', '-m', 'twine', 'upload', '--repository', 'testpypi', 'dist/*'],
            check=True
        )
        print("Module uploaded successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during upload: {e}")
