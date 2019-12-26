import matplotlib.pyplot as plt
import numpy as np
# v 4 5 6 8
# e 5 8 9 11
x = [20, 40, 54, 88]

# Time Complexity : O(V.E)
y_bellman = [20, 40, 54, 88]
# Time Complexity : O(V2.log V + V.E)
y_Johnson = [29.632, 57.474, 82.013, 145.797]

#  xticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
plt.xticks(x, ("G(4,5)", 'G(5,8)', 'G(6,9)', 'G(8,11)'))
plt.plot(x, y_bellman, 'v:  ',  ms='4.5', label='Bellman Ford')
plt.plot(x, y_Johnson, 'o-',  ms='4.5', label="Johnson's Algorithm")
plt.xlabel('Reference range for G(V,E)')
plt.ylabel('Time complexity Function')
plt.title("Bellman Ford vs Johnson's Algorithm")
plt.legend()
plt.show()
