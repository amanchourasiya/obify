# Obify - Python's answer to Java Collections Framework

This is python library that provides functionalities similar to collections framework in Java.
A counter to the utility of this library can be made that python already has collections module that pretty much handles and provides all the functionality similar to 
java collections but python in build collections is missing some key fuctionalities 
e.g. Java provides some libraries such as heap or Priority Queue that can work in objects but there is no such think in python , we only have heap or queue that only work on 
some primitive data types that can be comapred by any arithmatic operator.

So this library provides the feature to use these data structures such as Heap or Priority Queue with our own objects.

## Getting Started

This library has been published on PyPy so can be installed by Pip.
```
pip install obify
```

### Prerequisites

The only requiement for the object to use these data structures is that it should have a function named 'compare_to' which should look like this

```
def compare_to(self,node):
    if self.data < node.data:
        return -1
    elif self.data > node.data:
        return 1
    else:
        return 0
```

This function should return -1 if the self is less than the compared node and 1 of its greater that compared node and 0 for equal nodes

### This library can be used following way

```python
from obify import heap

class Node():
    def __init__(self, data):
        self.data = data

    def compare(self, node):
        if self.data < node.data:
            return -1
        elif self.data > node.data:
            return 1
        else:
            return 0

def test_heap():
    h = heap.MinHeap()
    h.insert(Node(12))
    h.insert(Node(2))
    h.insert(Node(20))
    h.remove()
    h.insert(Node(0))
```

## Built With Technologies

* [Python](https://python.org/) -Open source programming/scripting language. 


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Aman Chourasiya** - *Project setup ,PyPy deployment* - [Aman Chourasiya](https://github.com/amanchourasiya)
* **Anuj Chourasiya** - *Bugfixing* - [Anuj Chourasiya](https://github.com/anuj-chourasiya)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments




