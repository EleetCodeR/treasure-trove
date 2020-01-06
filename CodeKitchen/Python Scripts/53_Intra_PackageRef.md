# Intra-Pacakge References :

## Importing from Sibling Packages:
We often need to import a module/method from a sibling package, in that case intra-package references are used.
for eg., 
Here in our case we have created a "customer" subpackage (inside "ecommerce") , from which we will try to import "contact" module into "sales" module.

For this we can use Absolute-import or Relative-import: (Now inside "sales.py" we write...),
### Absolute-import : 
~~~~
from ecommerce.customer import contact
~~~~
### Relative-import :
~~~~
from ..customer import contact
~~~~

Absolute Import should preferred over Relative , however if there is an n-tiered project and import becomes too noisy with complex layers (too many dot operators) , relative import becomes suitable.
See sales.py file INTRA-PACKAGE REFERENCES section.

### NOTE:
One dot = current package (shopping) (here intellisense shows all modules/subpackages of current package).
Another dot = come outside current package (now in ecommerce) (here intellisense shows all modules/subpackges of toplevel package of current file).
