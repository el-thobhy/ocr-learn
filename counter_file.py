import os
import sys
import site

packages_dir = site.getsitepackages()[0] + "/"

total = 0
for pkg in os.listdir(packages_dir):
    path = os.path.join(packages_dir, pkg)
    if os.path.isdir(path):
        size = sum(os.path.getsize(os.path.join(dp,f)) for dp, dn, filenames in os.walk(path) for f in filenames)
        size_mb = size / (1024 * 1024)  # Convert to MB
        print(f"{pkg:<40}: {size_mb:.2f} MB")
        total += size

print(f"\nTotal size of installed packages: {total / (1024 * 1024):.2f} MB")
sys.exit(0 if total > 0 else 1)