<div class="alert alert-block alert-info" style="margin-top: 20px">
    <a href="https://cocl.us/corsera_da0101en_notebook_top">
         <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/TopAd.png" width="750" align="center">
    </a>
</div>


<a href="https://cognitiveclass.ai">
 <p align="center">
  <img src = "https://github.com/RobiDeantonio/IA-IBM/blob/master/Resources/cognitiveclass.png" width = 500> 
 </p>
</a>

<h1 align=center><font size = 5>Data Analysis with Python</font></h1>

<h1>Introduction</h1>
<h3>Welcome!</h3>

<p>
In this section, you will learn how to approach data acquisition in various ways, and obtain necessary insights from a dataset. By the end of this lab, you will successfully load the data into Jupyter Notebook, and gain some fundamental insights via Pandas Library.
</p>

<h2>Table of Contents</h2>

<div class="alert alert-block alert-info" style="margin-top: 20px">
<ol>
    <li><a href="#data_acquisition">Data Acquisition</a>
    <li><a href="#basic_insight">Basic Insight of Dataset</a></li>
</ol>

Estimated Time Needed: <strong>10 min</strong>
</div>
<hr>

<h1 id="data_acquisition">Data Acquisition</h1>
<p>
There are various formats for a dataset, .csv, .json, .xlsx  etc. The dataset can be stored in different places, on your local machine or sometimes online.<br>
In this section, you will learn how to load a dataset into our Jupyter Notebook.<br>
In our case, the Automobile Dataset is an online source, and it is in CSV (comma separated value) format. Let's use this dataset as an example to practice data reading.
<ul>
    <li>data source: <a href="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data" target="_blank">https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data</a></li>
    <li>data type: csv</li>
</ul>
The Pandas Library is a useful tool that enables us to read various datasets into a data frame; our Jupyter notebook platforms have a built-in <b>Pandas Library</b> so that all we need to do is import Pandas without installing.
</p>


```python
# import pandas library
import pandas as pd
```

<h2>Read Data</h2>
<p>
We use <code>pandas.read_csv()</code> function to read the csv file. In the bracket, we put the file path along with a quotation mark, so that pandas will read the file into a data frame from that address. The file path can be either an URL or your local file address.<br>
Because the data does not include headers, we can add an argument <code>headers = None</code>  inside the  <code>read_csv()</code> method, so that pandas will not automatically set the first row as a header.<br>
You can also assign the dataset to any variable you create.
</p>

This dataset was hosted on IBM Cloud object click <a href="https://cocl.us/DA101EN_object_storage">HERE</a> for free storage.


```python
# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)
```

After reading the dataset, we can use the <code>dataframe.head(n)</code> method to check the top n rows of the dataframe; where n is an integer. Contrary to <code>dataframe.head(n)</code>, <code>dataframe.tail(n)</code> will show you the bottom n rows of the dataframe.



```python
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
```

    The first 5 rows of the dataframe





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
      <th>20</th>
      <th>21</th>
      <th>22</th>
      <th>23</th>
      <th>24</th>
      <th>25</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>13495</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>152</td>
      <td>mpfi</td>
      <td>2.68</td>
      <td>3.47</td>
      <td>9.0</td>
      <td>154</td>
      <td>5000</td>
      <td>19</td>
      <td>26</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.0</td>
      <td>102</td>
      <td>5500</td>
      <td>24</td>
      <td>30</td>
      <td>13950</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.4</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.0</td>
      <td>115</td>
      <td>5500</td>
      <td>18</td>
      <td>22</td>
      <td>17450</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 26 columns</p>
</div>



<div class="alert alert-danger alertdanger" style="margin-top: 20px">
<h1> Question #1: </h1>
<b>check the bottom 10 rows of data frame "df".</b>
</div>


```python
# Write your code below and press Shift+Enter to execute 
df.tail(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>16</th>
      <th>17</th>
      <th>18</th>
      <th>19</th>
      <th>20</th>
      <th>21</th>
      <th>22</th>
      <th>23</th>
      <th>24</th>
      <th>25</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>195</th>
      <td>-1</td>
      <td>74</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114</td>
      <td>5400</td>
      <td>23</td>
      <td>28</td>
      <td>13415</td>
    </tr>
    <tr>
      <th>196</th>
      <td>-2</td>
      <td>103</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114</td>
      <td>5400</td>
      <td>24</td>
      <td>28</td>
      <td>15985</td>
    </tr>
    <tr>
      <th>197</th>
      <td>-1</td>
      <td>74</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114</td>
      <td>5400</td>
      <td>24</td>
      <td>28</td>
      <td>16515</td>
    </tr>
    <tr>
      <th>198</th>
      <td>-2</td>
      <td>103</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.15</td>
      <td>7.5</td>
      <td>162</td>
      <td>5100</td>
      <td>17</td>
      <td>22</td>
      <td>18420</td>
    </tr>
    <tr>
      <th>199</th>
      <td>-1</td>
      <td>74</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>wagon</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.15</td>
      <td>7.5</td>
      <td>162</td>
      <td>5100</td>
      <td>17</td>
      <td>22</td>
      <td>18950</td>
    </tr>
    <tr>
      <th>200</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114</td>
      <td>5400</td>
      <td>23</td>
      <td>28</td>
      <td>16845</td>
    </tr>
    <tr>
      <th>201</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>8.7</td>
      <td>160</td>
      <td>5300</td>
      <td>19</td>
      <td>25</td>
      <td>19045</td>
    </tr>
    <tr>
      <th>202</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>173</td>
      <td>mpfi</td>
      <td>3.58</td>
      <td>2.87</td>
      <td>8.8</td>
      <td>134</td>
      <td>5500</td>
      <td>18</td>
      <td>23</td>
      <td>21485</td>
    </tr>
    <tr>
      <th>203</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>diesel</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>145</td>
      <td>idi</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.0</td>
      <td>106</td>
      <td>4800</td>
      <td>26</td>
      <td>27</td>
      <td>22470</td>
    </tr>
    <tr>
      <th>204</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114</td>
      <td>5400</td>
      <td>19</td>
      <td>25</td>
      <td>22625</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 26 columns</p>
</div>



<div class="alert alert-danger alertdanger" style="margin-top: 20px">
<h1> Question #1 Answer: </h1>
<b>Run the code below for the solution!</b>
</div>

Double-click <b>here</b> for the solution.

<!-- The answer is below:

print("The last 10 rows of the dataframe\n")
df.tail(10)

-->

<h3>Add Headers</h3>
<p>
Take a look at our dataset; pandas automatically set the header by an integer from 0.
</p>
<p>
To better describe our data we can introduce a header, this information is available at:  <a href="https://archive.ics.uci.edu/ml/datasets/Automobile" target="_blank">https://archive.ics.uci.edu/ml/datasets/Automobile</a>
</p>
<p>
Thus, we have to add headers manually.
</p>
<p>
Firstly, we create a list "headers" that include all column names in order.
Then, we use <code>dataframe.columns = headers</code> to replace the headers by the list we created.
</p>


```python
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
```

    headers
     ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']


 We replace headers and recheck our data frame


```python
df.columns = headers
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>normalized-losses</th>
      <th>make</th>
      <th>fuel-type</th>
      <th>aspiration</th>
      <th>num-of-doors</th>
      <th>body-style</th>
      <th>drive-wheels</th>
      <th>engine-location</th>
      <th>wheel-base</th>
      <th>...</th>
      <th>engine-size</th>
      <th>fuel-system</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression-ratio</th>
      <th>horsepower</th>
      <th>peak-rpm</th>
      <th>city-mpg</th>
      <th>highway-mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>13495</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>152</td>
      <td>mpfi</td>
      <td>2.68</td>
      <td>3.47</td>
      <td>9.0</td>
      <td>154</td>
      <td>5000</td>
      <td>19</td>
      <td>26</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.0</td>
      <td>102</td>
      <td>5500</td>
      <td>24</td>
      <td>30</td>
      <td>13950</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.4</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.0</td>
      <td>115</td>
      <td>5500</td>
      <td>18</td>
      <td>22</td>
      <td>17450</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>?</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>15250</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>158</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>105.8</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>17710</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>?</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>fwd</td>
      <td>front</td>
      <td>105.8</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>18920</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>158</td>
      <td>audi</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>105.8</td>
      <td>...</td>
      <td>131</td>
      <td>mpfi</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>8.3</td>
      <td>140</td>
      <td>5500</td>
      <td>17</td>
      <td>20</td>
      <td>23875</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>?</td>
      <td>audi</td>
      <td>gas</td>
      <td>turbo</td>
      <td>two</td>
      <td>hatchback</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.5</td>
      <td>...</td>
      <td>131</td>
      <td>mpfi</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>7.0</td>
      <td>160</td>
      <td>5500</td>
      <td>16</td>
      <td>22</td>
      <td>?</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 26 columns</p>
</div>



we can drop missing values along the column "price" as follows  


```python
df.dropna(subset=["price"], axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>normalized-losses</th>
      <th>make</th>
      <th>fuel-type</th>
      <th>aspiration</th>
      <th>num-of-doors</th>
      <th>body-style</th>
      <th>drive-wheels</th>
      <th>engine-location</th>
      <th>wheel-base</th>
      <th>...</th>
      <th>engine-size</th>
      <th>fuel-system</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression-ratio</th>
      <th>horsepower</th>
      <th>peak-rpm</th>
      <th>city-mpg</th>
      <th>highway-mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.00</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>13495</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.00</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>152</td>
      <td>mpfi</td>
      <td>2.68</td>
      <td>3.47</td>
      <td>9.00</td>
      <td>154</td>
      <td>5000</td>
      <td>19</td>
      <td>26</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.00</td>
      <td>102</td>
      <td>5500</td>
      <td>24</td>
      <td>30</td>
      <td>13950</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.4</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.00</td>
      <td>115</td>
      <td>5500</td>
      <td>18</td>
      <td>22</td>
      <td>17450</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>?</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.50</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>15250</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>158</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>105.8</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.50</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>17710</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>?</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>fwd</td>
      <td>front</td>
      <td>105.8</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.50</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>25</td>
      <td>18920</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>158</td>
      <td>audi</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>105.8</td>
      <td>...</td>
      <td>131</td>
      <td>mpfi</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>8.30</td>
      <td>140</td>
      <td>5500</td>
      <td>17</td>
      <td>20</td>
      <td>23875</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>?</td>
      <td>audi</td>
      <td>gas</td>
      <td>turbo</td>
      <td>two</td>
      <td>hatchback</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.5</td>
      <td>...</td>
      <td>131</td>
      <td>mpfi</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>7.00</td>
      <td>160</td>
      <td>5500</td>
      <td>16</td>
      <td>22</td>
      <td>?</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2</td>
      <td>192</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>101.2</td>
      <td>...</td>
      <td>108</td>
      <td>mpfi</td>
      <td>3.50</td>
      <td>2.80</td>
      <td>8.80</td>
      <td>101</td>
      <td>5800</td>
      <td>23</td>
      <td>29</td>
      <td>16430</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>192</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>101.2</td>
      <td>...</td>
      <td>108</td>
      <td>mpfi</td>
      <td>3.50</td>
      <td>2.80</td>
      <td>8.80</td>
      <td>101</td>
      <td>5800</td>
      <td>23</td>
      <td>29</td>
      <td>16925</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>188</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>101.2</td>
      <td>...</td>
      <td>164</td>
      <td>mpfi</td>
      <td>3.31</td>
      <td>3.19</td>
      <td>9.00</td>
      <td>121</td>
      <td>4250</td>
      <td>21</td>
      <td>28</td>
      <td>20970</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>188</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>101.2</td>
      <td>...</td>
      <td>164</td>
      <td>mpfi</td>
      <td>3.31</td>
      <td>3.19</td>
      <td>9.00</td>
      <td>121</td>
      <td>4250</td>
      <td>21</td>
      <td>28</td>
      <td>21105</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1</td>
      <td>?</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>103.5</td>
      <td>...</td>
      <td>164</td>
      <td>mpfi</td>
      <td>3.31</td>
      <td>3.19</td>
      <td>9.00</td>
      <td>121</td>
      <td>4250</td>
      <td>20</td>
      <td>25</td>
      <td>24565</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>?</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>103.5</td>
      <td>...</td>
      <td>209</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.39</td>
      <td>8.00</td>
      <td>182</td>
      <td>5400</td>
      <td>16</td>
      <td>22</td>
      <td>30760</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0</td>
      <td>?</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>103.5</td>
      <td>...</td>
      <td>209</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.39</td>
      <td>8.00</td>
      <td>182</td>
      <td>5400</td>
      <td>16</td>
      <td>22</td>
      <td>41315</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0</td>
      <td>?</td>
      <td>bmw</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>110.0</td>
      <td>...</td>
      <td>209</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.39</td>
      <td>8.00</td>
      <td>182</td>
      <td>5400</td>
      <td>15</td>
      <td>20</td>
      <td>36880</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2</td>
      <td>121</td>
      <td>chevrolet</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>88.4</td>
      <td>...</td>
      <td>61</td>
      <td>2bbl</td>
      <td>2.91</td>
      <td>3.03</td>
      <td>9.50</td>
      <td>48</td>
      <td>5100</td>
      <td>47</td>
      <td>53</td>
      <td>5151</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1</td>
      <td>98</td>
      <td>chevrolet</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>90</td>
      <td>2bbl</td>
      <td>3.03</td>
      <td>3.11</td>
      <td>9.60</td>
      <td>70</td>
      <td>5400</td>
      <td>38</td>
      <td>43</td>
      <td>6295</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0</td>
      <td>81</td>
      <td>chevrolet</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>90</td>
      <td>2bbl</td>
      <td>3.03</td>
      <td>3.11</td>
      <td>9.60</td>
      <td>70</td>
      <td>5400</td>
      <td>38</td>
      <td>43</td>
      <td>6575</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1</td>
      <td>118</td>
      <td>dodge</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>93.7</td>
      <td>...</td>
      <td>90</td>
      <td>2bbl</td>
      <td>2.97</td>
      <td>3.23</td>
      <td>9.41</td>
      <td>68</td>
      <td>5500</td>
      <td>37</td>
      <td>41</td>
      <td>5572</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1</td>
      <td>118</td>
      <td>dodge</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>93.7</td>
      <td>...</td>
      <td>90</td>
      <td>2bbl</td>
      <td>2.97</td>
      <td>3.23</td>
      <td>9.40</td>
      <td>68</td>
      <td>5500</td>
      <td>31</td>
      <td>38</td>
      <td>6377</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1</td>
      <td>118</td>
      <td>dodge</td>
      <td>gas</td>
      <td>turbo</td>
      <td>two</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>93.7</td>
      <td>...</td>
      <td>98</td>
      <td>mpfi</td>
      <td>3.03</td>
      <td>3.39</td>
      <td>7.60</td>
      <td>102</td>
      <td>5500</td>
      <td>24</td>
      <td>30</td>
      <td>7957</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1</td>
      <td>148</td>
      <td>dodge</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>93.7</td>
      <td>...</td>
      <td>90</td>
      <td>2bbl</td>
      <td>2.97</td>
      <td>3.23</td>
      <td>9.40</td>
      <td>68</td>
      <td>5500</td>
      <td>31</td>
      <td>38</td>
      <td>6229</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1</td>
      <td>148</td>
      <td>dodge</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>93.7</td>
      <td>...</td>
      <td>90</td>
      <td>2bbl</td>
      <td>2.97</td>
      <td>3.23</td>
      <td>9.40</td>
      <td>68</td>
      <td>5500</td>
      <td>31</td>
      <td>38</td>
      <td>6692</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1</td>
      <td>148</td>
      <td>dodge</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>93.7</td>
      <td>...</td>
      <td>90</td>
      <td>2bbl</td>
      <td>2.97</td>
      <td>3.23</td>
      <td>9.40</td>
      <td>68</td>
      <td>5500</td>
      <td>31</td>
      <td>38</td>
      <td>7609</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1</td>
      <td>148</td>
      <td>dodge</td>
      <td>gas</td>
      <td>turbo</td>
      <td>?</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>93.7</td>
      <td>...</td>
      <td>98</td>
      <td>mpfi</td>
      <td>3.03</td>
      <td>3.39</td>
      <td>7.60</td>
      <td>102</td>
      <td>5500</td>
      <td>24</td>
      <td>30</td>
      <td>8558</td>
    </tr>
    <tr>
      <th>28</th>
      <td>-1</td>
      <td>110</td>
      <td>dodge</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>fwd</td>
      <td>front</td>
      <td>103.3</td>
      <td>...</td>
      <td>122</td>
      <td>2bbl</td>
      <td>3.34</td>
      <td>3.46</td>
      <td>8.50</td>
      <td>88</td>
      <td>5000</td>
      <td>24</td>
      <td>30</td>
      <td>8921</td>
    </tr>
    <tr>
      <th>29</th>
      <td>3</td>
      <td>145</td>
      <td>dodge</td>
      <td>gas</td>
      <td>turbo</td>
      <td>two</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>95.9</td>
      <td>...</td>
      <td>156</td>
      <td>mfi</td>
      <td>3.60</td>
      <td>3.90</td>
      <td>7.00</td>
      <td>145</td>
      <td>5000</td>
      <td>19</td>
      <td>24</td>
      <td>12964</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>175</th>
      <td>-1</td>
      <td>65</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>102.4</td>
      <td>...</td>
      <td>122</td>
      <td>mpfi</td>
      <td>3.31</td>
      <td>3.54</td>
      <td>8.70</td>
      <td>92</td>
      <td>4200</td>
      <td>27</td>
      <td>32</td>
      <td>9988</td>
    </tr>
    <tr>
      <th>176</th>
      <td>-1</td>
      <td>65</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>102.4</td>
      <td>...</td>
      <td>122</td>
      <td>mpfi</td>
      <td>3.31</td>
      <td>3.54</td>
      <td>8.70</td>
      <td>92</td>
      <td>4200</td>
      <td>27</td>
      <td>32</td>
      <td>10898</td>
    </tr>
    <tr>
      <th>177</th>
      <td>-1</td>
      <td>65</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>102.4</td>
      <td>...</td>
      <td>122</td>
      <td>mpfi</td>
      <td>3.31</td>
      <td>3.54</td>
      <td>8.70</td>
      <td>92</td>
      <td>4200</td>
      <td>27</td>
      <td>32</td>
      <td>11248</td>
    </tr>
    <tr>
      <th>178</th>
      <td>3</td>
      <td>197</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>102.9</td>
      <td>...</td>
      <td>171</td>
      <td>mpfi</td>
      <td>3.27</td>
      <td>3.35</td>
      <td>9.30</td>
      <td>161</td>
      <td>5200</td>
      <td>20</td>
      <td>24</td>
      <td>16558</td>
    </tr>
    <tr>
      <th>179</th>
      <td>3</td>
      <td>197</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>102.9</td>
      <td>...</td>
      <td>171</td>
      <td>mpfi</td>
      <td>3.27</td>
      <td>3.35</td>
      <td>9.30</td>
      <td>161</td>
      <td>5200</td>
      <td>19</td>
      <td>24</td>
      <td>15998</td>
    </tr>
    <tr>
      <th>180</th>
      <td>-1</td>
      <td>90</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.5</td>
      <td>...</td>
      <td>171</td>
      <td>mpfi</td>
      <td>3.27</td>
      <td>3.35</td>
      <td>9.20</td>
      <td>156</td>
      <td>5200</td>
      <td>20</td>
      <td>24</td>
      <td>15690</td>
    </tr>
    <tr>
      <th>181</th>
      <td>-1</td>
      <td>?</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.5</td>
      <td>...</td>
      <td>161</td>
      <td>mpfi</td>
      <td>3.27</td>
      <td>3.35</td>
      <td>9.20</td>
      <td>156</td>
      <td>5200</td>
      <td>19</td>
      <td>24</td>
      <td>15750</td>
    </tr>
    <tr>
      <th>182</th>
      <td>2</td>
      <td>122</td>
      <td>volkswagen</td>
      <td>diesel</td>
      <td>std</td>
      <td>two</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>97.3</td>
      <td>...</td>
      <td>97</td>
      <td>idi</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.00</td>
      <td>52</td>
      <td>4800</td>
      <td>37</td>
      <td>46</td>
      <td>7775</td>
    </tr>
    <tr>
      <th>183</th>
      <td>2</td>
      <td>122</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>97.3</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>9.00</td>
      <td>85</td>
      <td>5250</td>
      <td>27</td>
      <td>34</td>
      <td>7975</td>
    </tr>
    <tr>
      <th>184</th>
      <td>2</td>
      <td>94</td>
      <td>volkswagen</td>
      <td>diesel</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>97.3</td>
      <td>...</td>
      <td>97</td>
      <td>idi</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.00</td>
      <td>52</td>
      <td>4800</td>
      <td>37</td>
      <td>46</td>
      <td>7995</td>
    </tr>
    <tr>
      <th>185</th>
      <td>2</td>
      <td>94</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>97.3</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>9.00</td>
      <td>85</td>
      <td>5250</td>
      <td>27</td>
      <td>34</td>
      <td>8195</td>
    </tr>
    <tr>
      <th>186</th>
      <td>2</td>
      <td>94</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>97.3</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>9.00</td>
      <td>85</td>
      <td>5250</td>
      <td>27</td>
      <td>34</td>
      <td>8495</td>
    </tr>
    <tr>
      <th>187</th>
      <td>2</td>
      <td>94</td>
      <td>volkswagen</td>
      <td>diesel</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>97.3</td>
      <td>...</td>
      <td>97</td>
      <td>idi</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.00</td>
      <td>68</td>
      <td>4500</td>
      <td>37</td>
      <td>42</td>
      <td>9495</td>
    </tr>
    <tr>
      <th>188</th>
      <td>2</td>
      <td>94</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>97.3</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.00</td>
      <td>100</td>
      <td>5500</td>
      <td>26</td>
      <td>32</td>
      <td>9995</td>
    </tr>
    <tr>
      <th>189</th>
      <td>3</td>
      <td>?</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>fwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.50</td>
      <td>90</td>
      <td>5500</td>
      <td>24</td>
      <td>29</td>
      <td>11595</td>
    </tr>
    <tr>
      <th>190</th>
      <td>3</td>
      <td>256</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>fwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.50</td>
      <td>90</td>
      <td>5500</td>
      <td>24</td>
      <td>29</td>
      <td>9980</td>
    </tr>
    <tr>
      <th>191</th>
      <td>0</td>
      <td>?</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>100.4</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.50</td>
      <td>110</td>
      <td>5500</td>
      <td>19</td>
      <td>24</td>
      <td>13295</td>
    </tr>
    <tr>
      <th>192</th>
      <td>0</td>
      <td>?</td>
      <td>volkswagen</td>
      <td>diesel</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>100.4</td>
      <td>...</td>
      <td>97</td>
      <td>idi</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.00</td>
      <td>68</td>
      <td>4500</td>
      <td>33</td>
      <td>38</td>
      <td>13845</td>
    </tr>
    <tr>
      <th>193</th>
      <td>0</td>
      <td>?</td>
      <td>volkswagen</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>fwd</td>
      <td>front</td>
      <td>100.4</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>9.00</td>
      <td>88</td>
      <td>5500</td>
      <td>25</td>
      <td>31</td>
      <td>12290</td>
    </tr>
    <tr>
      <th>194</th>
      <td>-2</td>
      <td>103</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.50</td>
      <td>114</td>
      <td>5400</td>
      <td>23</td>
      <td>28</td>
      <td>12940</td>
    </tr>
    <tr>
      <th>195</th>
      <td>-1</td>
      <td>74</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.50</td>
      <td>114</td>
      <td>5400</td>
      <td>23</td>
      <td>28</td>
      <td>13415</td>
    </tr>
    <tr>
      <th>196</th>
      <td>-2</td>
      <td>103</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.50</td>
      <td>114</td>
      <td>5400</td>
      <td>24</td>
      <td>28</td>
      <td>15985</td>
    </tr>
    <tr>
      <th>197</th>
      <td>-1</td>
      <td>74</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>wagon</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.50</td>
      <td>114</td>
      <td>5400</td>
      <td>24</td>
      <td>28</td>
      <td>16515</td>
    </tr>
    <tr>
      <th>198</th>
      <td>-2</td>
      <td>103</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.15</td>
      <td>7.50</td>
      <td>162</td>
      <td>5100</td>
      <td>17</td>
      <td>22</td>
      <td>18420</td>
    </tr>
    <tr>
      <th>199</th>
      <td>-1</td>
      <td>74</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>wagon</td>
      <td>rwd</td>
      <td>front</td>
      <td>104.3</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.15</td>
      <td>7.50</td>
      <td>162</td>
      <td>5100</td>
      <td>17</td>
      <td>22</td>
      <td>18950</td>
    </tr>
    <tr>
      <th>200</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.50</td>
      <td>114</td>
      <td>5400</td>
      <td>23</td>
      <td>28</td>
      <td>16845</td>
    </tr>
    <tr>
      <th>201</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>8.70</td>
      <td>160</td>
      <td>5300</td>
      <td>19</td>
      <td>25</td>
      <td>19045</td>
    </tr>
    <tr>
      <th>202</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>173</td>
      <td>mpfi</td>
      <td>3.58</td>
      <td>2.87</td>
      <td>8.80</td>
      <td>134</td>
      <td>5500</td>
      <td>18</td>
      <td>23</td>
      <td>21485</td>
    </tr>
    <tr>
      <th>203</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>diesel</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>145</td>
      <td>idi</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.00</td>
      <td>106</td>
      <td>4800</td>
      <td>26</td>
      <td>27</td>
      <td>22470</td>
    </tr>
    <tr>
      <th>204</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.50</td>
      <td>114</td>
      <td>5400</td>
      <td>19</td>
      <td>25</td>
      <td>22625</td>
    </tr>
  </tbody>
</table>
<p>205 rows × 26 columns</p>
</div>



Now, we have successfully read the raw dataset and add the correct headers into the data frame.

 <div class="alert alert-danger alertdanger" style="margin-top: 20px">
<h1> Question #2: </h1>
<b>Find the name of the columns of the dataframe</b>
</div>


```python
# Write your code below and press Shift+Enter to execute 
df.columns
```




    Index(['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
           'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
           'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',
           'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',
           'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
           'highway-mpg', 'price'],
          dtype='object')



Double-click <b>here</b> for the solution.

<!-- The answer is below:

print(df.columns)

-->

<h2>Save Dataset</h2>
<p>
Correspondingly, Pandas enables us to save the dataset to csv  by using the <code>dataframe.to_csv()</code> method, you can add the file path and name along with quotation marks in the brackets.
</p>
<p>
    For example, if you would save the dataframe <b>df</b> as <b>automobile.csv</b> to your local machine, you may use the syntax below:
</p>
df.to_csv("automobile.csv", index=False)
 We can also read and save other file formats, we can use similar functions to **`pd.read_csv()`** and **`df.to_csv()`** for other data formats, the functions are listed in the following table:


<h2>Read/Save Other Data Formats</h2>



| Data Formate  | Read           | Save             |
| ------------- |:--------------:| ----------------:|
| csv           | `pd.read_csv()`  |`df.to_csv()`     |
| json          | `pd.read_json()` |`df.to_json()`    |
| excel         | `pd.read_excel()`|`df.to_excel()`   |
| hdf           | `pd.read_hdf()`  |`df.to_hdf()`     |
| sql           | `pd.read_sql()`  |`df.to_sql()`     |
| ...           |   ...          |       ...        |

<h1 id="basic_insight">Basic Insight of Dataset</h1>
<p>
After reading data into Pandas dataframe, it is time for us to explore the dataset.<br>
There are several ways to obtain essential insights of the data to help us better understand our dataset.
</p>

<h2>Data Types</h2>
<p>
Data has a variety of types.<br>
The main types stored in Pandas dataframes are <b>object</b>, <b>float</b>, <b>int</b>, <b>bool</b> and <b>datetime64</b>. In order to better learn about each attribute, it is always good for us to know the data type of each column. In Pandas:
</p>


```python
df.dtypes
```




    symboling              int64
    normalized-losses     object
    make                  object
    fuel-type             object
    aspiration            object
    num-of-doors          object
    body-style            object
    drive-wheels          object
    engine-location       object
    wheel-base           float64
    length               float64
    width                float64
    height               float64
    curb-weight            int64
    engine-type           object
    num-of-cylinders      object
    engine-size            int64
    fuel-system           object
    bore                  object
    stroke                object
    compression-ratio    float64
    horsepower            object
    peak-rpm              object
    city-mpg               int64
    highway-mpg            int64
    price                 object
    dtype: object



returns a Series with the data type of each column.


```python
# check the data type of data frame "df" by .dtypes
print(df.dtypes)
```

<p>
As a result, as shown above, it is clear to see that the data type of "symboling" and "curb-weight" are <code>int64</code>, "normalized-losses" is <code>object</code>, and "wheel-base" is <code>float64</code>, etc.
</p>
<p>
These data types can be changed; we will learn how to accomplish this in a later module.
</p>

<h2>Describe</h2>
If we would like to get a statistical summary of each column, such as count, column mean value, column standard deviation, etc. We use the describe method:
dataframe.describe()
This method will provide various summary statistics, excluding <code>NaN</code> (Not a Number) values.


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>wheel-base</th>
      <th>length</th>
      <th>width</th>
      <th>height</th>
      <th>curb-weight</th>
      <th>engine-size</th>
      <th>compression-ratio</th>
      <th>city-mpg</th>
      <th>highway-mpg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.834146</td>
      <td>98.756585</td>
      <td>174.049268</td>
      <td>65.907805</td>
      <td>53.724878</td>
      <td>2555.565854</td>
      <td>126.907317</td>
      <td>10.142537</td>
      <td>25.219512</td>
      <td>30.751220</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.245307</td>
      <td>6.021776</td>
      <td>12.337289</td>
      <td>2.145204</td>
      <td>2.443522</td>
      <td>520.680204</td>
      <td>41.642693</td>
      <td>3.972040</td>
      <td>6.542142</td>
      <td>6.886443</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.000000</td>
      <td>86.600000</td>
      <td>141.100000</td>
      <td>60.300000</td>
      <td>47.800000</td>
      <td>1488.000000</td>
      <td>61.000000</td>
      <td>7.000000</td>
      <td>13.000000</td>
      <td>16.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>94.500000</td>
      <td>166.300000</td>
      <td>64.100000</td>
      <td>52.000000</td>
      <td>2145.000000</td>
      <td>97.000000</td>
      <td>8.600000</td>
      <td>19.000000</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>97.000000</td>
      <td>173.200000</td>
      <td>65.500000</td>
      <td>54.100000</td>
      <td>2414.000000</td>
      <td>120.000000</td>
      <td>9.000000</td>
      <td>24.000000</td>
      <td>30.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.000000</td>
      <td>102.400000</td>
      <td>183.100000</td>
      <td>66.900000</td>
      <td>55.500000</td>
      <td>2935.000000</td>
      <td>141.000000</td>
      <td>9.400000</td>
      <td>30.000000</td>
      <td>34.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.000000</td>
      <td>120.900000</td>
      <td>208.100000</td>
      <td>72.300000</td>
      <td>59.800000</td>
      <td>4066.000000</td>
      <td>326.000000</td>
      <td>23.000000</td>
      <td>49.000000</td>
      <td>54.000000</td>
    </tr>
  </tbody>
</table>
</div>



<p>
This shows the statistical summary of all numeric-typed (int, float) columns.<br>
For example, the attribute "symboling" has 205 counts, the mean value of this column is 0.83, the standard deviation is 1.25, the minimum value is -2, 25th percentile is 0, 50th percentile is 1, 75th percentile is 2, and the maximum value is 3.
<br>
However, what if we would also like to check all the columns including those that are of type object.
<br><br>

You can add an argument <code>include = "all"</code> inside the bracket. Let's try it again.
</p>


```python
# describe all the columns in "df" 
df.describe(include = "all")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symboling</th>
      <th>normalized-losses</th>
      <th>make</th>
      <th>fuel-type</th>
      <th>aspiration</th>
      <th>num-of-doors</th>
      <th>body-style</th>
      <th>drive-wheels</th>
      <th>engine-location</th>
      <th>wheel-base</th>
      <th>...</th>
      <th>engine-size</th>
      <th>fuel-system</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression-ratio</th>
      <th>horsepower</th>
      <th>peak-rpm</th>
      <th>city-mpg</th>
      <th>highway-mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>205.000000</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205.000000</td>
      <td>...</td>
      <td>205.000000</td>
      <td>205</td>
      <td>205</td>
      <td>205</td>
      <td>205.000000</td>
      <td>205</td>
      <td>205</td>
      <td>205.000000</td>
      <td>205.000000</td>
      <td>205</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>NaN</td>
      <td>52</td>
      <td>22</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>3</td>
      <td>2</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>8</td>
      <td>39</td>
      <td>37</td>
      <td>NaN</td>
      <td>60</td>
      <td>24</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>187</td>
    </tr>
    <tr>
      <th>top</th>
      <td>NaN</td>
      <td>?</td>
      <td>toyota</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>mpfi</td>
      <td>3.62</td>
      <td>3.40</td>
      <td>NaN</td>
      <td>68</td>
      <td>5500</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>?</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>NaN</td>
      <td>41</td>
      <td>32</td>
      <td>185</td>
      <td>168</td>
      <td>114</td>
      <td>96</td>
      <td>120</td>
      <td>202</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>94</td>
      <td>23</td>
      <td>20</td>
      <td>NaN</td>
      <td>19</td>
      <td>37</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.834146</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>98.756585</td>
      <td>...</td>
      <td>126.907317</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>10.142537</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>25.219512</td>
      <td>30.751220</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.245307</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.021776</td>
      <td>...</td>
      <td>41.642693</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.972040</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.542142</td>
      <td>6.886443</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86.600000</td>
      <td>...</td>
      <td>61.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>13.000000</td>
      <td>16.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>94.500000</td>
      <td>...</td>
      <td>97.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8.600000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19.000000</td>
      <td>25.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>1.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>97.000000</td>
      <td>...</td>
      <td>120.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24.000000</td>
      <td>30.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>2.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>102.400000</td>
      <td>...</td>
      <td>141.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.400000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.000000</td>
      <td>34.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120.900000</td>
      <td>...</td>
      <td>326.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>23.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>49.000000</td>
      <td>54.000000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>11 rows × 26 columns</p>
</div>



<p>
Now, it provides the statistical summary of all the columns, including object-typed attributes.<br>
We can now see how many unique values, which is the top value and the frequency of top value in the object-typed columns.<br>
Some values in the table above show as "NaN", this is because those numbers are not available regarding a particular column type.<br>
</p>

<div class="alert alert-danger alertdanger" style="margin-top: 20px">
<h1> Question #3: </h1>

<p>
You can select the columns of a data frame by indicating the name of  each column, for example, you can select the three columns as follows:
</p>
<p>
    <code>dataframe[[' column 1 ',column 2', 'column 3']]</code>
</p>
<p>
Where "column" is the name of the column, you can apply the method  ".describe()" to get the statistics of those columns as follows:
</p>
<p>
    <code>dataframe[[' column 1 ',column 2', 'column 3'] ].describe()</code>
</p>

Apply the  method to ".describe()" to the columns 'length' and 'compression-ratio'.
</div>


```python
# Write your code below and press Shift+Enter to execute 
df[['length','compression-ratio']].describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>length</th>
      <th>compression-ratio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>205.000000</td>
      <td>205.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>174.049268</td>
      <td>10.142537</td>
    </tr>
    <tr>
      <th>std</th>
      <td>12.337289</td>
      <td>3.972040</td>
    </tr>
    <tr>
      <th>min</th>
      <td>141.100000</td>
      <td>7.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>166.300000</td>
      <td>8.600000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>173.200000</td>
      <td>9.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>183.100000</td>
      <td>9.400000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>208.100000</td>
      <td>23.000000</td>
    </tr>
  </tbody>
</table>
</div>



Double-click <b>here</b> for the solution.

<!-- The answer is below:

df[['length', 'compression-ratio']].describe()

-->


<h2>Info</h2>
Another method you can use to check your dataset is:
dataframe.info
It provide a concise summary of your DataFrame.


```python
# look at the info of "df"
df.info
```




    <bound method DataFrame.info of      symboling normalized-losses         make fuel-type aspiration  \
    0            3                 ?  alfa-romero       gas        std   
    1            3                 ?  alfa-romero       gas        std   
    2            1                 ?  alfa-romero       gas        std   
    3            2               164         audi       gas        std   
    4            2               164         audi       gas        std   
    5            2                 ?         audi       gas        std   
    6            1               158         audi       gas        std   
    7            1                 ?         audi       gas        std   
    8            1               158         audi       gas      turbo   
    9            0                 ?         audi       gas      turbo   
    10           2               192          bmw       gas        std   
    11           0               192          bmw       gas        std   
    12           0               188          bmw       gas        std   
    13           0               188          bmw       gas        std   
    14           1                 ?          bmw       gas        std   
    15           0                 ?          bmw       gas        std   
    16           0                 ?          bmw       gas        std   
    17           0                 ?          bmw       gas        std   
    18           2               121    chevrolet       gas        std   
    19           1                98    chevrolet       gas        std   
    20           0                81    chevrolet       gas        std   
    21           1               118        dodge       gas        std   
    22           1               118        dodge       gas        std   
    23           1               118        dodge       gas      turbo   
    24           1               148        dodge       gas        std   
    25           1               148        dodge       gas        std   
    26           1               148        dodge       gas        std   
    27           1               148        dodge       gas      turbo   
    28          -1               110        dodge       gas        std   
    29           3               145        dodge       gas      turbo   
    ..         ...               ...          ...       ...        ...   
    175         -1                65       toyota       gas        std   
    176         -1                65       toyota       gas        std   
    177         -1                65       toyota       gas        std   
    178          3               197       toyota       gas        std   
    179          3               197       toyota       gas        std   
    180         -1                90       toyota       gas        std   
    181         -1                 ?       toyota       gas        std   
    182          2               122   volkswagen    diesel        std   
    183          2               122   volkswagen       gas        std   
    184          2                94   volkswagen    diesel        std   
    185          2                94   volkswagen       gas        std   
    186          2                94   volkswagen       gas        std   
    187          2                94   volkswagen    diesel      turbo   
    188          2                94   volkswagen       gas        std   
    189          3                 ?   volkswagen       gas        std   
    190          3               256   volkswagen       gas        std   
    191          0                 ?   volkswagen       gas        std   
    192          0                 ?   volkswagen    diesel      turbo   
    193          0                 ?   volkswagen       gas        std   
    194         -2               103        volvo       gas        std   
    195         -1                74        volvo       gas        std   
    196         -2               103        volvo       gas        std   
    197         -1                74        volvo       gas        std   
    198         -2               103        volvo       gas      turbo   
    199         -1                74        volvo       gas      turbo   
    200         -1                95        volvo       gas        std   
    201         -1                95        volvo       gas      turbo   
    202         -1                95        volvo       gas        std   
    203         -1                95        volvo    diesel      turbo   
    204         -1                95        volvo       gas      turbo   
    
        num-of-doors   body-style drive-wheels engine-location  wheel-base  ...  \
    0            two  convertible          rwd           front        88.6  ...   
    1            two  convertible          rwd           front        88.6  ...   
    2            two    hatchback          rwd           front        94.5  ...   
    3           four        sedan          fwd           front        99.8  ...   
    4           four        sedan          4wd           front        99.4  ...   
    5            two        sedan          fwd           front        99.8  ...   
    6           four        sedan          fwd           front       105.8  ...   
    7           four        wagon          fwd           front       105.8  ...   
    8           four        sedan          fwd           front       105.8  ...   
    9            two    hatchback          4wd           front        99.5  ...   
    10           two        sedan          rwd           front       101.2  ...   
    11          four        sedan          rwd           front       101.2  ...   
    12           two        sedan          rwd           front       101.2  ...   
    13          four        sedan          rwd           front       101.2  ...   
    14          four        sedan          rwd           front       103.5  ...   
    15          four        sedan          rwd           front       103.5  ...   
    16           two        sedan          rwd           front       103.5  ...   
    17          four        sedan          rwd           front       110.0  ...   
    18           two    hatchback          fwd           front        88.4  ...   
    19           two    hatchback          fwd           front        94.5  ...   
    20          four        sedan          fwd           front        94.5  ...   
    21           two    hatchback          fwd           front        93.7  ...   
    22           two    hatchback          fwd           front        93.7  ...   
    23           two    hatchback          fwd           front        93.7  ...   
    24          four    hatchback          fwd           front        93.7  ...   
    25          four        sedan          fwd           front        93.7  ...   
    26          four        sedan          fwd           front        93.7  ...   
    27             ?        sedan          fwd           front        93.7  ...   
    28          four        wagon          fwd           front       103.3  ...   
    29           two    hatchback          fwd           front        95.9  ...   
    ..           ...          ...          ...             ...         ...  ...   
    175         four    hatchback          fwd           front       102.4  ...   
    176         four        sedan          fwd           front       102.4  ...   
    177         four    hatchback          fwd           front       102.4  ...   
    178          two    hatchback          rwd           front       102.9  ...   
    179          two    hatchback          rwd           front       102.9  ...   
    180         four        sedan          rwd           front       104.5  ...   
    181         four        wagon          rwd           front       104.5  ...   
    182          two        sedan          fwd           front        97.3  ...   
    183          two        sedan          fwd           front        97.3  ...   
    184         four        sedan          fwd           front        97.3  ...   
    185         four        sedan          fwd           front        97.3  ...   
    186         four        sedan          fwd           front        97.3  ...   
    187         four        sedan          fwd           front        97.3  ...   
    188         four        sedan          fwd           front        97.3  ...   
    189          two  convertible          fwd           front        94.5  ...   
    190          two    hatchback          fwd           front        94.5  ...   
    191         four        sedan          fwd           front       100.4  ...   
    192         four        sedan          fwd           front       100.4  ...   
    193         four        wagon          fwd           front       100.4  ...   
    194         four        sedan          rwd           front       104.3  ...   
    195         four        wagon          rwd           front       104.3  ...   
    196         four        sedan          rwd           front       104.3  ...   
    197         four        wagon          rwd           front       104.3  ...   
    198         four        sedan          rwd           front       104.3  ...   
    199         four        wagon          rwd           front       104.3  ...   
    200         four        sedan          rwd           front       109.1  ...   
    201         four        sedan          rwd           front       109.1  ...   
    202         four        sedan          rwd           front       109.1  ...   
    203         four        sedan          rwd           front       109.1  ...   
    204         four        sedan          rwd           front       109.1  ...   
    
         engine-size  fuel-system  bore  stroke compression-ratio horsepower  \
    0            130         mpfi  3.47    2.68              9.00        111   
    1            130         mpfi  3.47    2.68              9.00        111   
    2            152         mpfi  2.68    3.47              9.00        154   
    3            109         mpfi  3.19    3.40             10.00        102   
    4            136         mpfi  3.19    3.40              8.00        115   
    5            136         mpfi  3.19    3.40              8.50        110   
    6            136         mpfi  3.19    3.40              8.50        110   
    7            136         mpfi  3.19    3.40              8.50        110   
    8            131         mpfi  3.13    3.40              8.30        140   
    9            131         mpfi  3.13    3.40              7.00        160   
    10           108         mpfi  3.50    2.80              8.80        101   
    11           108         mpfi  3.50    2.80              8.80        101   
    12           164         mpfi  3.31    3.19              9.00        121   
    13           164         mpfi  3.31    3.19              9.00        121   
    14           164         mpfi  3.31    3.19              9.00        121   
    15           209         mpfi  3.62    3.39              8.00        182   
    16           209         mpfi  3.62    3.39              8.00        182   
    17           209         mpfi  3.62    3.39              8.00        182   
    18            61         2bbl  2.91    3.03              9.50         48   
    19            90         2bbl  3.03    3.11              9.60         70   
    20            90         2bbl  3.03    3.11              9.60         70   
    21            90         2bbl  2.97    3.23              9.41         68   
    22            90         2bbl  2.97    3.23              9.40         68   
    23            98         mpfi  3.03    3.39              7.60        102   
    24            90         2bbl  2.97    3.23              9.40         68   
    25            90         2bbl  2.97    3.23              9.40         68   
    26            90         2bbl  2.97    3.23              9.40         68   
    27            98         mpfi  3.03    3.39              7.60        102   
    28           122         2bbl  3.34    3.46              8.50         88   
    29           156          mfi  3.60    3.90              7.00        145   
    ..           ...          ...   ...     ...               ...        ...   
    175          122         mpfi  3.31    3.54              8.70         92   
    176          122         mpfi  3.31    3.54              8.70         92   
    177          122         mpfi  3.31    3.54              8.70         92   
    178          171         mpfi  3.27    3.35              9.30        161   
    179          171         mpfi  3.27    3.35              9.30        161   
    180          171         mpfi  3.27    3.35              9.20        156   
    181          161         mpfi  3.27    3.35              9.20        156   
    182           97          idi  3.01    3.40             23.00         52   
    183          109         mpfi  3.19    3.40              9.00         85   
    184           97          idi  3.01    3.40             23.00         52   
    185          109         mpfi  3.19    3.40              9.00         85   
    186          109         mpfi  3.19    3.40              9.00         85   
    187           97          idi  3.01    3.40             23.00         68   
    188          109         mpfi  3.19    3.40             10.00        100   
    189          109         mpfi  3.19    3.40              8.50         90   
    190          109         mpfi  3.19    3.40              8.50         90   
    191          136         mpfi  3.19    3.40              8.50        110   
    192           97          idi  3.01    3.40             23.00         68   
    193          109         mpfi  3.19    3.40              9.00         88   
    194          141         mpfi  3.78    3.15              9.50        114   
    195          141         mpfi  3.78    3.15              9.50        114   
    196          141         mpfi  3.78    3.15              9.50        114   
    197          141         mpfi  3.78    3.15              9.50        114   
    198          130         mpfi  3.62    3.15              7.50        162   
    199          130         mpfi  3.62    3.15              7.50        162   
    200          141         mpfi  3.78    3.15              9.50        114   
    201          141         mpfi  3.78    3.15              8.70        160   
    202          173         mpfi  3.58    2.87              8.80        134   
    203          145          idi  3.01    3.40             23.00        106   
    204          141         mpfi  3.78    3.15              9.50        114   
    
         peak-rpm city-mpg highway-mpg  price  
    0        5000       21          27  13495  
    1        5000       21          27  16500  
    2        5000       19          26  16500  
    3        5500       24          30  13950  
    4        5500       18          22  17450  
    5        5500       19          25  15250  
    6        5500       19          25  17710  
    7        5500       19          25  18920  
    8        5500       17          20  23875  
    9        5500       16          22      ?  
    10       5800       23          29  16430  
    11       5800       23          29  16925  
    12       4250       21          28  20970  
    13       4250       21          28  21105  
    14       4250       20          25  24565  
    15       5400       16          22  30760  
    16       5400       16          22  41315  
    17       5400       15          20  36880  
    18       5100       47          53   5151  
    19       5400       38          43   6295  
    20       5400       38          43   6575  
    21       5500       37          41   5572  
    22       5500       31          38   6377  
    23       5500       24          30   7957  
    24       5500       31          38   6229  
    25       5500       31          38   6692  
    26       5500       31          38   7609  
    27       5500       24          30   8558  
    28       5000       24          30   8921  
    29       5000       19          24  12964  
    ..        ...      ...         ...    ...  
    175      4200       27          32   9988  
    176      4200       27          32  10898  
    177      4200       27          32  11248  
    178      5200       20          24  16558  
    179      5200       19          24  15998  
    180      5200       20          24  15690  
    181      5200       19          24  15750  
    182      4800       37          46   7775  
    183      5250       27          34   7975  
    184      4800       37          46   7995  
    185      5250       27          34   8195  
    186      5250       27          34   8495  
    187      4500       37          42   9495  
    188      5500       26          32   9995  
    189      5500       24          29  11595  
    190      5500       24          29   9980  
    191      5500       19          24  13295  
    192      4500       33          38  13845  
    193      5500       25          31  12290  
    194      5400       23          28  12940  
    195      5400       23          28  13415  
    196      5400       24          28  15985  
    197      5400       24          28  16515  
    198      5100       17          22  18420  
    199      5100       17          22  18950  
    200      5400       23          28  16845  
    201      5300       19          25  19045  
    202      5500       18          23  21485  
    203      4800       26          27  22470  
    204      5400       19          25  22625  
    
    [205 rows x 26 columns]>



<p>
Here we are able to see the information of our dataframe, with the top 30 rows and the bottom 30 rows.
<br><br>
And, it also shows us the whole data frame has 205 rows and 26 columns in total.
</p>

<h1>Excellent! You have just completed the  Introduction  Notebook!</h1>

<div class="alert alert-block alert-info" style="margin-top: 20px">

    <p><a href="https://cocl.us/corsera_da0101en_notebook_bottom"><img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/Images/BottomAd.png" width="750" align="center"></a></p>
</div>


<h3>About the Authors:</h3>

This notebook was written by <a href="https://www.linkedin.com/in/mahdi-noorian-58219234/" target="_blank">Mahdi Noorian PhD</a>, <a href="https://www.linkedin.com/in/joseph-s-50398b136/" target="_blank">Joseph Santarcangelo</a>, Bahare Talayian, Eric Xiao, Steven Dong, Parizad, Hima Vsudevan and <a href="https://www.linkedin.com/in/fiorellawever/" target="_blank">Fiorella Wenver</a> and <a href=" https://www.linkedin.com/in/yi-leng-yao-84451275/ " target="_blank" >Yi Yao</a>.

<p><a href="https://www.linkedin.com/in/joseph-s-50398b136/" target="_blank">Joseph Santarcangelo</a> is a Data Scientist at IBM, and holds a PhD in Electrical Engineering. His research focused on using Machine Learning, Signal Processing, and Computer Vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.</p>

<hr>
<p>Copyright &copy; 2018 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href="https://cognitiveclass.ai/mit-license/">MIT License</a>.</p>
