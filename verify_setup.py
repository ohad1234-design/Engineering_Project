"""
Verification script for Python virtual environment setup
Tests all required packages and CUDA availability
"""

import sys
print("=" * 60)
print("PYTHON ENVIRONMENT VERIFICATION")
print("=" * 60)

# Python version
print(f"\n1. Python Version: {sys.version}")
print(f"   Executable: {sys.executable}")

# Test PyTorch and CUDA
print("\n2. PyTorch & CUDA:")
try:
    import torch
    print(f"   ✓ PyTorch: {torch.__version__}")
    print(f"   ✓ CUDA Available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"   ✓ CUDA Version: {torch.version.cuda}")
        print(f"   ✓ GPU Count: {torch.cuda.device_count()}")
        print(f"   ✓ GPU Name: {torch.cuda.get_device_name(0)}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test torchvision
print("\n3. TorchVision:")
try:
    import torchvision
    print(f"   ✓ TorchVision: {torchvision.__version__}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test torchaudio
print("\n4. TorchAudio:")
try:
    import torchaudio
    print(f"   ✓ TorchAudio: {torchaudio.__version__}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test NumPy
print("\n5. NumPy:")
try:
    import numpy as np
    print(f"   ✓ NumPy: {np.__version__}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test Pandas
print("\n6. Pandas:")
try:
    import pandas as pd
    print(f"   ✓ Pandas: {pd.__version__}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test Matplotlib
print("\n7. Matplotlib:")
try:
    import matplotlib
    print(f"   ✓ Matplotlib: {matplotlib.__version__}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test Pillow
print("\n8. Pillow (PIL):")
try:
    from PIL import Image
    import PIL
    print(f"   ✓ Pillow: {PIL.__version__}")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Test Ultralytics (YOLO)
print("\n9. Ultralytics (YOLO):")
try:
    from ultralytics import YOLO
    import ultralytics
    print(f"   ✓ Ultralytics: {ultralytics.__version__}")
except Exception as e:
    print(f"   ✗ Error: {e}")

print("\n" + "=" * 60)
print("VERIFICATION COMPLETE!")
print("=" * 60)
