# UNICODE

* Python 2:
    ```python
    type('text') # OUTPUT: str
    type(u'text') # OUTPUT: unicode
    ```
* Python 3:
    ```python
    type('text') # OUTPUT: str
    type(u'text') # OUTPUT: str
    ```
## Conversion between string and bytes(Python3):

> **str.encode():**



Convert string into bytes.

Default format: utf-8

```python
##−∗−coding :  utf−8−∗−
>>> 'খ'.encode('utf-8')
b'\xe0\xa6\x96'
```
```python
##−∗−coding :  utf−16−∗−
>>> 'খ'.encode('utf-16')
b'\xff\xfe\x96\t'
```
```python
##−∗−coding :  utf−32−∗−
>>> 'খ'.encode('utf-32')
b'\xff\xfe\x00\x00\x96\t\x00\x00'

```
> bytes.decode()

Convert bytes into string.

Default format: utf-8

```python
##−∗−coding :  utf−8−∗−
>>> b'\xe0\xa6\x96'.decode('utf-8')
'খ'
```
```python
##−∗−coding :  utf−16−∗−
>>> b'\xff\xfe\x96\t'.decode('utf-16')
'খ'
```
```python
##−∗−coding :  utf−32−∗−
>>> b'\xff\xfe\x00\x00\x96\t\x00\x00'.decode('utf-32')
'খ'

```