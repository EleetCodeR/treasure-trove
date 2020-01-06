# ==========/ FOR : INTRA-PACKAGE REFERENCES section /===============

# from ecommerce.customer import contact  # Absolute import
# from ..customer import contact  # Relative import

# contact.contact_customer()
# ==========/--------------------------- /===============

#
#
#
#
#

# ==========/ FOR : EXECUTING MODULE AS SCRIPT section /===============
print("Sales initialized.", __name__)
# NOTE:
# when this module ("sales.py") is loaded from app.py output is :

# Ecommerce initialized. (was written inside __init__ of ecommerce)
# Sales initialized. ecommerce.shopping.sales

# when this module is executed directly as sales.py output is:

# Sales initialized. __main__

# NOTE:
# observe that name of the module (__name__) is different in both the cases. (ecommerce.shopping.sales - from app.py , __main__ - from sales.py)
# It is because the name of the module that starts our program execution is always __main__
# ==========/--------------------------- /===============
#
#
#
#

# ==========/starter CODE FOR sales.py /=================


def calc_tax():
    pass


def calc_shipping():
    pass


# ==========/--------------------------- /=================
#
#
#
#

# ==========/ FOR : EXECUTING MODULE AS SCRIPT section /===============
# NOTE:
if __name__ == "__main__":
    # any initialization code.
    print("Sales started.")
    calc_tax()
# By writing code like above, we can use this module as a script, as well as a reusable-module that we can import into another module.
# above code (one inside IF ) will not be executed if this module is imported into another modules. as it's __name__ will be different.
# ==========/--------------------------- /==============================
