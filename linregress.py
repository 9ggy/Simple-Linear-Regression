import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import random

def linregress(X: np.array ,Y: np.array, color: str = 'r'):

  # Function to calculate r-squared given the sets of numbers, the slope, and the y intercept.
  def rsquared(X: np.array,Y: np.array, slope: int, yint: int):
    y_mean = mean(Y)
    y_hat = [yint + (slope * x) for x in X]
    rsquared = round(sum([(y - y_mean)**2 for y in y_hat]) / sum([(y - y_mean)**2 for y in Y]), ndigits=14)
    return rsquared

  # Mathematical stuff
    # Mean data.
  x_mean = mean(X)
  y_mean = mean(Y)
  x_mean_list, y_mean_list = [(x - x_mean) for x in X], [(y - y_mean) for y in Y]

    # Initializing variables that are used for finding both the slope and y-intercept.
  x_squared = sum([x**2 for x in x_mean_list])
  x_y_mult = sum([x*y for x,y in zip(x_mean_list,y_mean_list)])

    # Calculating slope and y-intercept.
  slope = x_y_mult / x_squared
  y_int = y_mean - (slope * x_mean)

  def plot(x,y):
    fig = plt.figure()
    ax = fig.add_subplot()

    # Aesthetic purposes
    ax.set_xlabel('Independant')
    ax.set_ylabel('Dependant')
    ax.grid(color='0.8')  
    fig.suptitle('Linear Regression')

    # Plot the base scatter plot.
    ax.plot(x, y, 'o', color = color)

    # Abline function
    axes = fig.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = np.array(y_int + slope * x_vals)

    # Plot the regression line on top of the base scatter plot
    ax.plot(x_vals, y_vals, '-')
    plt.show()


  rs = rsquared(X,Y, slope, y_int)
  print(f"Slope: {slope} \n Y-Intercept: {y_int} \n R-Squared: {rs}")
  plot(X,Y)
  return slope, y_int, rs
