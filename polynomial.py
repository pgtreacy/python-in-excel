
import nitroplot as plt
import numpy as np


active_sheet("polynomial")


# create 50 equally spaced points between -10 and 10
x = np.linspace(-10, 10, 50)

# A # indicates a comment
# Add a # to the start of a line for the line to be ignored
# Remove a # fr the line to be executed
# Add/remove the # from each equation below to see each one plotted

# calculate the y value for each element of the x vector
y = 3*x**2 + 4*x + 2

#y = 2*x**3 - 3*x**2 + 4*x + 2

#y = np.sin(x)


fig, ax = plt.subplots()
ax.plot(x, y)
plt.graph()
