# Python Virtual Environment (`venv`) Guide

A **Python Virtual Environment (`venv`)** is a tool to create isolated environments for Python projects. It helps manage dependencies and avoid conflicts between different projects.

## **1. Creating a Virtual Environment**

```bash
python3 -m venv venv
```

This creates a `venv` directory in your project folder, which contains the virtual environment.

---

## **2. Activating the Virtual Environment**

```bash
source venv/bin/activate
```

Once activated, your terminal prompt will show `(venv)`, indicating the virtual environment is active.

---

## **3. Installing Dependencies**

After activation, install necessary packages using:

```bash
pip install package_name
```

To save installed dependencies:

```bash
pip freeze > requirements.txt
```

To install dependencies from an existing `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## **4. Deactivating the Virtual Environment**

To exit the virtual environment, run:

```bash
deactivate
```

---

## **5. Deleting the Virtual Environment**

Simply remove the `venv` directory:

```bash
rm -rf venv
```

---

## **6. Recreating a Virtual Environment**

If you need to recreate the virtual environment, delete the existing `venv` folder and run:

```bash
python3 -m venv venv
source venv/bin/activate  # (Use the appropriate activation command for your OS)
pip install -r requirements.txt
```

---

## **7. Checking the Python Version in Virtual Environment**

To confirm the Python version inside the virtual environment:

```bash
python --version
```

To verify that the virtual environment is active:

```bash
which python
```

---

## **8. Using Virtual Environments in IDEs**

- **VS Code**: Select the Python interpreter from the Command Palette (`Ctrl+Shift+P` → "Python: Select Interpreter")
- **PyCharm**: Automatically detects virtual environments and allows selection in project settings

---

## **Conclusion**

Using virtual environments ensures your Python projects remain isolated and free from dependency conflicts

---

Happy Hacking! 🎉
