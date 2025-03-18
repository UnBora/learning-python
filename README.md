# **សេចក្តីផ្ដើមអំពី Python**  

Python គឺជា​ភាសាកូដកម្ម​ដែលមានភាពងាយស្រួលក្នុងការរៀន និងប្រើប្រាស់។ វាត្រូវបានប្រើប្រាស់យ៉ាងទូលំទូលាយក្នុង **ការអភិវឌ្ឍន៍គេហទំព័រ, ទិន្នន័យវិទ្យា, ស្វ័យប្រវត្តិកម្ម, បញ្ញាសិប្បនិម្មិត, និងវិស្វកម្មកម្មវិធី**។  

## **១. ឯកសារស្វែងយល់បន្ថែម**  
- វេបសាយផ្លូវការរបស់ Python: [https://www.python.org](https://www.python.org)  
- ចំណេះដឹង Python តាមដានតាម PEP 8: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)  

## **២. លក្ខណៈសម្បត្តិសំខាន់ៗនៃ Python**  
✅ កូដសរសេរងាយស្រួល និងអានឲ្យស្រួល  
✅ មិនចាំបាច់កំណត់ប្រភេទទិន្នន័យជាមុន (Dynamic Typing)  
✅ មានបណ្ណាល័យដ៏មានប្រយោជន៍ច្រើន (NumPy, Pandas, Flask, Django,...)  
✅ អាចប្រើបានលើ OS ច្រើន (Windows, macOS, Linux)  

## **៣. ការដំឡើង Python**  
ចំពោះអ្នកប្រើ Windows, macOS, និង Linux អ្នកអាចទាញយក Python ពី [python.org](https://www.python.org/downloads/)  
បន្ទាប់មកពិនិត្យថា Python ត្រូវបានដំឡើងដោយប្រើ​​ command៖  
```sh
python --version
```
ឬ
```sh
python3 --version
```

## **៤. សញ្ញា Syntax មូលដ្ឋាន**  
### 🟢 អថេរ (Variables)  
```python
name = "Bora"
age = 25
pi = 3.14
```

### 🟢 ប្រភេទទិន្នន័យ (Data Types)  
```python
text = "Hello"       # str (អក្សរ)
number = 10          # int (ចំនួនគត់)
decimal = 3.14       # float (ចំនួនទសភាគ)
is_python_fun = True # bool (តម្លៃត្រូវ/ខុស)
```

### 🟢 លក្ខខណ្ឌ (Conditions)  
```python
age = 18
if age >= 18:
    print("អ្នកពេញវ័យហើយ!")
else:
    print("អ្នកនៅមិនទាន់ច្បាស់ជាស្របច្បាប់នៅឡើយ។")
```

### 🟢 រង្វិលកូដ (Loops)  
```python
for i in range(5):
    print("សួស្តី", i)

n = 0
while n < 5:
    print(n)
    n += 1
```

### 🟢 អនុគមន៍ (Functions)  
```python
def greet(name):
    return f"សួស្តី {name}!"

print(greet("Bora"))
```

## **៥. ការប្រើប្រាស់បណ្ណាល័យ (Libraries)**
Python មានបណ្ណាល័យជាច្រើនសម្រាប់អភិវឌ្ឍន៍កម្មវិធី។ ឧទាហរណ៍៖  
- **NumPy/Pandas** (គណនាគណនាវិទ្យា និងទិន្នន័យវិទ្យា)  
- **Flask/Django** (អភិវឌ្ឍន៍គេហទំព័រ)  
- **Matplotlib/Seaborn** (គំនូសតាងទិន្នន័យ)  

ឧទាហរណ៍៖ **ការងាយស្រួលនៃ NumPy**  
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # គុណគ្រប់ធាតុនៃអារេដោយ 2
```

## **៦. ការចងភ្ជាប់ API (API Requests)**  
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())
```

## **៧. ការប្រើ Virtual Environment និង pip**  
**បង្កើត Virtual Environment**  
```sh
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows
```
**ដំឡើង package ជាមួយ pip**  
```sh
pip install requests
```

## **៨. ការប្រកួតកូដ Python (Coding Challenges)**  
ចង់អនុវត្តន៍? សាកល្បងលំហាត់ Python នៅលើវេបសាយដូចជា៖  
- [LeetCode](https://leetcode.com/)  
- [HackerRank](https://www.hackerrank.com/domains/tutorials/10-days-of-python)  
- [Codewars](https://www.codewars.com/)  

## **៩. បញ្ហាដែលអ្នកអាចជួបប្រទះ និងដំណោះស្រាយ**  
- **Error: `IndentationError: expected an indented block`**  
  🟢 **ដំណោះស្រាយ**: ពិនិត្យលំហូរកូដ (Spaces/Tab)  
- **Error: `ModuleNotFoundError: No module named 'numpy'`**  
  🟢 **ដំណោះស្រាយ**: ដំឡើង module នេះជាមួយ `pip install numpy`  
- **Error: `TypeError: unsupported operand type(s)`**  
  🟢 **ដំណោះស្រាយ**: ពិនិត្យប្រភេទទិន្នន័យមុនពេលគណនា  

