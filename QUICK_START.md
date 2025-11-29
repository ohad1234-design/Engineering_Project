# Quick Start Guide - Python Virtual Environment

## 🚀 Quick Commands Reference

### Run Python Scripts
```powershell
.\venv310\Scripts\python.exe your_script.py
```

### Install Packages
```powershell
.\venv310\Scripts\python.exe -m pip install package_name
```

### Check CUDA
```powershell
.\venv310\Scripts\python.exe -c "import torch; print('CUDA:', torch.cuda.is_available())"
```

### List Installed Packages
```powershell
.\venv310\Scripts\python.exe -m pip list
```

### Verify Setup
```powershell
.\venv310\Scripts\python.exe verify_setup.py
```

## 📓 For Jupyter Notebooks

1. Open `project.ipynb`
2. Click kernel selector (top-right)
3. Select: **"Python 3.10.11 (venv310)"**
4. Start coding! All packages are ready.

## 🔥 Test Your GPU

```python
import torch

# Check if CUDA is available
print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"GPU Name: {torch.cuda.get_device_name(0)}")

# Create a tensor on GPU
x = torch.randn(3, 3).cuda()
print(f"Tensor device: {x.device}")
```

## 📦 Installed Packages

- PyTorch 2.5.1+cu121 ✅
- TorchVision 0.20.1+cu121 ✅
- TorchAudio 2.5.1+cu121 ✅
- NumPy 2.1.2 ✅
- Pandas 2.3.3 ✅
- Matplotlib 3.10.7 ✅
- Pillow 11.3.0 ✅
- Ultralytics 8.3.228 ✅

## 💡 Tips

- Use full path to python.exe to avoid activation issues
- VS Code automatically uses the configured interpreter
- Restart kernel if packages aren't recognized
- Keep this venv310 folder in your project directory

For detailed instructions, see `SETUP_INSTRUCTIONS.md`
