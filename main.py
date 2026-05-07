from abc import ABC, abstractmethod

class Arxitektor(ABC):
    @abstractmethod
    def loyihalash(self):
        pass

class GoogleArxitektor(Arxitektor):
    def loyihalash(self):
        return "Google loyihalarini loyihalashmoqda"

class MetaArxitektor(Arxitektor):
    def loyihalash(self):
        return "Meta loyihalarini loyihalashmoqda"

arxitektor = GoogleArxitektor()
print(arxitektor.loyihalash())

arxitektor = MetaArxitektor()
print(arxitektor.loyihalash())
```

```python
# @abstractmethod qiladi:
# - Bir classdan inherit qilingan subclasslarda implementatsiyani talab qiladi.
# - Agar subclassda @abstractmethod metodni implementatsiya qilmagan bo'lsa, Python hata chiqaradi.
