# Week10--Advanced-Python-Library-with-Comprehensive-Testing
A production-ready Python library showcasing advanced concepts like decorators, generators, context managers, and metaclasses. Includes pytest-based testing (90%+ coverage), type hints, modular architecture, and real-world examples for scalable and efficient development.

## 📌 Project Overview

This project is a **custom-built Advanced Python Library** designed to demonstrate powerful Python programming concepts and professional development practices. It showcases the use of **decorators, generators, context managers, and metaclasses** along with **comprehensive testing, type hints, and modular architecture**.

The library focuses on writing clean, reusable, and efficient code suitable for real-world applications.

---

## 🎯 Features

*  Advanced decorators (retry, cache, timer)
*  Generator-based data processing pipelines
*  Context managers for safe resource handling
*  Plugin system using metaclasses
*  Type hints for better code quality
*  90%+ test coverage using pytest
*  Modular and scalable project structure
*  Error handling with custom exceptions

---

## 🛠️ Tech Stack

* Python 3.x
* pytest (testing)
* mypy (type checking)
* black (code formatting)

---

## 📂 Project Structure

```
week10-advanced-library/
│── src/my_advanced_lib/
│   ├── core/
│   │   ├── decorators.py
│   │   ├── generators.py
│   │   ├── context_managers.py
│   │   └── metaclasses.py
│   ├── utils/
│   │   ├── validators.py
│   │   └── serializers.py
│   ├── exceptions.py
│   └── __init__.py
│
│── tests/
│── examples/
│── docs/
│── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/week10-advanced-library.git
cd week10-advanced-library
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements-dev.txt
```

### 5️⃣ Install Project

```bash
pip install -e .
```

---

## 🚀 Usage Example

### 🔹 Decorators

```python
from my_advanced_lib.core.decorators import retry, Cache, timer

cache = Cache(ttl=60)

@retry(max_attempts=3)
@timer
@cache
def fetch_data():
    return {"data": "sample"}

print(fetch_data())
```

---

### 🔹 Generators

```python
from my_advanced_lib.core.generators import batch_generator

data = range(10000)

for batch in batch_generator(iter(data), batch_size=1000):
    print(len(batch))
```

---

### 🔹 Context Manager

```python
from my_advanced_lib.core.context_managers import FileManager

with FileManager("test.txt", "w") as f:
    f.write("Hello World")
```

---

### 🔹 Metaclass Plugin System

```python
from my_advanced_lib.core.metaclasses import PluginMeta

print(PluginMeta.registry)
```

---

## 🧪 Testing

### Run Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=my_advanced_lib
```

### ✔ Results

* All test cases passed
* Achieved 90%+ code coverage

---

## 📊 Key Concepts Used

* Decorators (function enhancement)
* Generators (memory-efficient processing)
* Context Managers (resource safety)
* Metaclasses (class customization)
* Type Hints (better readability & reliability)

---

## 📈 Future Enhancements

* Add CLI interface
* Integrate REST API
* Publish on PyPI
* Add performance benchmarking
* Improve plugin system

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

