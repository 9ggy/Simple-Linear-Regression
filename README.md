# Simple-Linear-Regression

This was my approach at writing a linear regression algorithm. It calculates the best fitting line from two sets: X and Y. The function returns the slope and y intercept of the best fitting line, along with the R² value of the line. 

The less the data is correlated, the more the line will be pointing "downwards"

# Examples


<details closed>
  <summary> 1) A simple, low volume set of x and y corrdinates with a visible amount of correlation: </summary>
  <br>
  
   ## Data:
   ```py
    x = np.array([i for i in range(1,6)])
    y = np.array([1,2,5,6,7])
   ```
  ## Produces:
  ```
    Slope: 1.6 
    Y-Intercept: -0.8000000000000007 
    R-Squared: 0.94814814814815
  ```
  
  <h2 align = 'center'>Visualization</h2>
  
  <div align = 'center'>
    <img src='https://user-images.githubusercontent.com/84878036/150583778-9ef40ef0-ff66-49b8-a420-6f0286e9a7bd.png'>
  </div>
</details>

<details closed>
  <summary> 2) Bigger data with a the only correlation being a random number between 1 and 70 being added to each x element </summary>
  <br>
  
   ##### *Note in this instance you wont get the same exact data, this is beause of nature of the data we are using here.*
  
   ## Data:
   ```py
    x = np.array([x for x in range(1,40)])
    y = np.array([y + random.randint(1,70) for y in x])
   ```
  ## Produces:
  ```
    Slope: 1.2161943319838058 
    Y-Intercept: 29.676113360323885 
    R-Squared: 0.30895964256062
  ```
  <h2 align = 'center'>Visualization</h2>
  
  <div align = 'center'>
    <img src='https://user-images.githubusercontent.com/84878036/150585576-15434b94-7d49-47fe-95dc-b3c7d0fd9f29.png'>
  </div>
</details>

<details closed>
  <summary> 3) Large data with a small amount of correlation (it looks highly correlated because of the amount of data) </summary>
  <br>
  
   ##### *Note in this instance you wont get the same exact data, this is beause of nature of the data we are using here.*
  
   ## Data:
   ```py
    x = np.array([x for x in range(1,1000)])
    y = np.array([y + random.randint(100,1000) for y in x])
   ```
  ## Produces:
  ```
    Slope: 1.0101869444594895 
    Y-Intercept: 539.9065277702553 
    R-Squared: 0.55485407861745
  ```
  <h2 align = 'center'>Visualization</h2>
  
  <div align = 'center'>
    <img src='https://user-images.githubusercontent.com/84878036/150587307-0d4f6bca-7375-4a1f-867b-66450571ac2b.png'>
  </div>
</details>

<details closed>
  <summary> 4) Same model as number 3, this time with less total data points </summary>
  <br>
  
   ##### *Note in this instance you wont get the same exact data, this is beause of nature of the data we are using here.*
  
   ## Data:
   ```py
    x = np.array([x for x in range(1,20)])
    y = np.array([y + random.randint(100,1000) for y in x])
   ```
  ## Produces:
  ```
    Slope: 0.22456140350877193 
    Y-Intercept: 590.2456140350877 
    R-Squared: 2.244129053e-05
  ```
  <h2 align = 'center'>Visualization</h2>
  
  <div align = 'center'>
    <img src='https://user-images.githubusercontent.com/84878036/150588076-1974f57a-30aa-4d50-925a-b0b580e1b73e.png'>
  </div>
</details>

<details closed>
  <summary> 5) negative correlation </summary>
  <br>
  
   ##### *Note in this instance you wont get the same exact data, this is beause of nature of the data we are using here.*
  
   ## Data:
   ```py
    x = [1,2,3,4,5]
    y = [random.randint(1,1000) for i in range(5)]
   ```
  ## Produces:
  ```
    Slope: -142.4 
    Y-Intercept: 891.2 
    R-Squared: 0.3621364841021
  ```
  <h2 align = 'center'>Visualization</h2>
  
  <div align = 'center'>
    <img src='https://user-images.githubusercontent.com/84878036/150590384-5025edeb-a642-4ee8-bf4b-7268c9667915.png'>
  </div>
</details>
