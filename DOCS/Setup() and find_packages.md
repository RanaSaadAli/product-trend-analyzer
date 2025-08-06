2025-07-19
#setuptools #setupPy 

# 📦 Understanding `setup()` and `find_packages()` in `setuptools`


## 🔧 What is `setuptools`?

`setuptools` is a Python library used to **package and distribute Python projects**. It provides tools to create a `setup.py` file, which lets you turn your code into a reusable and installable Python package.

---

## ⚙️ What is the `setup()` Function?

The `setup()` function is the core of your `setup.py` file. It contains **metadata and configuration** about your project. This metadata tells Python how to install and handle your package.

Once your project has a `setup.py` file, you (or others) can install your package locally or even publish it on PyPI for global use.
### 🔑 Common Arguments in `setup()`

- **`name`**: The name of your package (e.g., `'cleancsv'`).

- **`version`**: Version of your package written in `MAJOR.MINOR.PATCH` format, e.g., `'0.0.1'`.

- **`author`**: The name of the package author.

- **`author_email`**: The email of the package author.

- **`install_requires`**: A list of external libraries your package needs to run (like `pandas`, `numpy`, etc.).

- **`packages`**: Specifies which modules and packages should be included when installing. This is where `find_packages()` is used.

---

## 📁 What is `find_packages()`?

`find_packages()` is a helper function from `setuptools` that automatically finds all Python packages (i.e., folders containing an `__init__.py` file).

Instead of manually listing each subpackage, `find_packages()` finds them all and includes them in the package installation process.

```python

from setuptools import setup, find_packages

  

setup(

    name="cleancsv",

    version="0.0.1",

    author="Your Name",

    author_email="your.email@example.com",

    packages=find_packages(),

    install_requires=[

        "pandas",

        "numpy"

    ]

)

```

#### **Scenario 1**
The `find_packages()` function detects all folders with an `__init__.py` file and includes them in your package. But if you want to include only a specific folder, you can use the `include` parameter to limit what gets packaged. So if I want the `find_packages()` function to include only the modules inside a specific folder, I can use the `include` parameter. This tells Python exactly which folders (or packages) should be included when building the package.
For example if my Python modules are located in a folder named `packages`, and I want the `find_packages()` function to include only this specific folder — and not pick up modules from other projects or folders — then I will use the `include` parameter in `find_packages()` to restrict it accordingly.

```python
find_packages(include=['packages', 'packages.*'])
```

**Explanation:**

- `'packages'` includes the **main package itself** (i.e., the `packages/` folder, if it has an `__init__.py`).

- `'packages.*'` includes any **sub-packages** inside `packages/`, like `packages.utils`, `packages.models`, etc.

#### **Scenario 2**

Now, in another scenario, if we want to exclude certain specific folders from our packages while including all the others, we can use the `exclude` parameter in `find_packages()` to achieve that.

```python
packages=find_packages(exclude=['excluded_folder', 'excluded_folder.*'])
```
This tells setuptools:
- "Find all packages, **except** anything named `excluded_folder` or its sub-packages."

**Example Folder Structure:**
```
your_project/
├── core/
│   └── __init__.py
├── utils/
│   └── __init__.py
├── tests/
│   └── __init__.py
```
Now if you run:
```python
find_packages(exclude=['tests', 'tests.*'])
```
The result will include:

- `core`

- `utils`

And it will exclude:

- `tests`

#### **Note**
**What the `*` means (in plain terms):**

- `'tests'` → skips the folder named `tests` itself (e.g., `tests/__init__.py`)
    
- `'tests.*'` → skips **everything inside `tests/`**, like:

    - `tests.unit`
        
    - `tests.integration`
        
    - `tests.helpers.logging`  
        and so on.


It works like a wildcard that matches all submodules or subpackages under `tests`.

#### **Scenario 3**
In a third scenario, if we want the `setup.py` file to not start from the current directory, but instead begin searching for packages from another specific folder (which contains the modules with `__init__.py`), we can use the `where` parameter in `find_packages()`.

Example Structure:
```
your_project/
├── setup.py
├── source/
│   ├── mypackage/
│   │   ├── __init__.py
│   │   └── module.py
```
Here, `mypackage` is **inside the `source/` folder**, and not directly in the root where `setup.py` is.

**Solution:**

You tell `find_packages()` to look **in the `source/` directory** like this:
```python
from setuptools import setup, find_packages

setup(
    name='your_project',
    version='0.1',
    packages=find_packages(where='source'),
    package_dir={'': 'source'},  # Tells setuptools that packages live inside 'source/'
)
```

#### Explanation of package_dir={'': 'source'}:

- The empty string `''` means “root package”.
    
- `'source'` is the **folder where your real packages are located**.
    
- You're telling Python:

	 “Look inside the `source/` folder to find the packages you’re installing.”
    
**Summary of Key Parameters:**

`include` 
Include only specific packages (whitelist).        

 `exclude` 
Exclude specific packages (blacklist).  

`where` 
Start package discovery from a different folder.

---
## 📦 What is `install_requires`?

The `install_requires` argument lists all third-party libraries that your package depends on. When someone installs your package, Python will automatically install these dependencies.

> ✅ Think of it like a built-in `requirements.txt` for your package!

---
## 🧠 Summary

- ✅ `setup()` helps package your code so it can be installed like any Python library.

- ✅ `find_packages()` searches for all folders containing `__init__.py`, making packaging easier.

- ✅ `install_requires` tells Python which libraries must be installed with your package.

## How to Test Your Package Locally

Once your `setup.py` and package structure are ready, you can install your package locally to test it:
```python
pip install .
```
This tells pip to install the current folder as a package.