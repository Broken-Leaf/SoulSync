import os
import sys
from pathlib import Path

def load_env_file(env_path=None):
    """
    Load environment variables from a .env file
    
    Args:
        env_path: Path to the .env file. If None, will look for .env in the project root.
    """
    if env_path is None:
        # Try to find the project root by looking for .env or .env.example
        current_path = Path.cwd()
        while current_path != current_path.parent:
            if (current_path / ".env").exists() or (current_path / ".env.example").exists():
                env_path = current_path / ".env"
                break
            current_path = current_path.parent
    
    if env_path is None or not Path(env_path).exists():
        print(f"Warning: .env file not found at {env_path}")
        return False
    
    try:
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if not line or line.startswith('#'):
                    continue
                
                # Parse key-value pairs
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # Remove quotes if present
                    if value and value[0] == value[-1] and value[0] in ('"', "'"):
                        value = value[1:-1]
                    
                    # Set environment variable if not already set
                    if key and not os.environ.get(key):
                        os.environ[key] = value
        return True
    except Exception as e:
        print(f"Error loading .env file: {e}")
        return False

# Load environment variables when this module is imported
load_env_file()