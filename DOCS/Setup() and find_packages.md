v2025-07-19
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

## Basic Packaging Workflow (Beginner-Friendly)

Now that we understand what `setuptools` is, and why we use the `setup()` and `find_packages()` functions — along with their parameters — it’s time to create a **basic packaging workflow**.

This guide will walk you through how to:
- Package your project code
- Reuse it in other projects
- Share it via **GitHub**
- Or even publish it on **PyPI**
#### **Step 1: Import Required Tools**
Start by importing the necessary components from the `setuptools` module — specifically, `setup()` and `find_packages()`:

```python
from setuptools import setup, find_packages
```

#### **Step 2: Define Metadata with `setup()`**
In this step, we define our package using the `setup()` function. Here, we provide important metadata like the package name, version, author, etc.
```python
setup(
    name="your_package_name",
    version="0.0.0",  # Version of your package
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description about the package",
    url="https://github.com/your-username/your-repo",  # GitHub repo link

    packages=find_packages(include=['module_folder', 'module_folder.*']),  # Folder with your code

    install_requires=[
        'beautifulsoup4==4.13.4',
        'emoji==2.14.1',
        'matplotlib==3.10.3',
        'numpy==2.3.2',
        'pandas==2.3.1',
        'selenium==4.34.2',
        'textblob==0.19.0',
        'undetected-chromedriver==3.5.5'
    ]
)

```
You can change or add fields based on your specific package.
#### **Step 3: Install the Package in Editable Mode**
After defining the package metadata in your `setup.py` file, save the file and open your terminal.  
Navigate to the project root directory (where `setup.py` is located), and run the following command:
```python
pip install -e .
```
This installs your package in **editable mode**, which creates a symbolic link to your source code.  
It allows any changes you make to the codebase to reflect immediately without needing to reinstall the package.
This is especially useful during development, as it speeds up your workflow and eliminates the need for repeated installations.

**Pro Tip (Explanation for Beginners):**
`pip install -e .`  
The `-e` stands for "editable". This means your package is installed as a link, so any code changes you make will be immediately reflected without needing reinstallation.

#### **Step 4: Test the Package with a Simple Import**
Once your package has been installed in **editable mode**, the next step is to test whether the installation was successful.

**Instructions:**

1. Open your terminal or any Python interpreter (e.g., IDLE, Jupyter Notebook, or Python shell).
2. Run the following command:
    ```
    import your_package_name
    ```

3. If the import runs **without any errors**, your package is successfully installed and ready for use.

Tip: You can now access any modules, functions, or classes defined in your package just like you would with any third-party library.

You can even add a **quick test** to check a specific function:
```python
from your_package_name.module_name import some_function

result = some_function()
print(result)
```
This confirms both the import and functionality of your code.

**Note:** Replace `your_package_name` with the **name of the folder** that contains your `__init__.py` file and other module files.  
This folder is considered the root of your package and must follow Python’s packaging structure.

#### **Step 5:Install Your Package from GitHub in Another Project**

**Overview**
You can install your custom Python package directly from a GitHub repository using `pip`. This is useful when you want to **reuse your package in other projects** without publishing it to PyPI.

**Requirements**
- Your package must be pushed to a GitHub repository and include a valid `setup.py` file.
- Git must be installed on your system.
- The repository should be **public**, or you must configure authentication for private repos.

**Installation Steps**
 1. Ensure your package repository is pushed to GitHub. Your project should contain the following at minimum:
 ```
 your-repo/
├── setup.py
└── your_package/
    └── __init__.py
```
 2. In the project where you want to use this package, open a terminal and run:
 ```
 pip install git+https://github.com/your-username/your-repo-name.git
```
3. Verify the installation by importing your package:
  ```
  import your_package_name
```

This is a simple, beginner-friendly workflow for creating a Python package from your project, so you can:
- Reuse it across multiple projects
- Share it with others via **GitHub**
- Or even publish it on **PyPI** for global access

It covers everything from defining your `setup.py`, organizing your package structure, installing it in editable mode, testing it, and using it in other projects.

Ideal for new developers who want to turn their Python code into a reusable and shareable package.
## 🧠Summary

- ✅ `setup()` helps package your code so it can be installed like any Python library.

- ✅ `find_packages()` searches for all folders containing `__init__.py`, making packaging easier.

- ✅ `install_requires` tells Python which libraries must be installed with your package.
