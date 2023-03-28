# Py-Boost custom losses

The repository for final project at [ML course](https://github.com/adasegroup/ML2023_lectures) at Skoltech - "Several custom losses implementation for the median regression task in Py-Boost".

Modern gradient boosting toolkits are very complex and are written in low-level programming languages. As a result, 
1) It is hard to customize them to suit one’s needs 
2) New ideas and methods are not easy to implement 
3) It is difficult to understand how they work. 

[Py-boost](https://github.com/sb-ai-lab/Py-Boost) is a Python-based gradient boosting library which aims at overcoming the aforementioned problems. Py-boost can be easily customized. In this project we implemented several custom losses for the median regression task and compared resulls on different datasets.

## Installation 

```bash
git clone https://github.com/dalibra/Py-Boost-custom-losses.git
```
On local machine:
```bash
pip install -r requirements.txt
```
In google colab:
```
pip install py-boost==0.4.1
```

## Usage
All the losses are implenented in `utils.py` as separate classes. You can find the execution in `experiments.ipynb`.
## Datasets:
- [Allstate Claims Severity](https://www.kaggle.com/competitions/allstate-claims-severity/data)
- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
- [Life Expectancy](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)
- [Car Price Prediction Challenge](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge?select=car_price_prediction.csv)


## Results
ЧЕ ТО ТАМ ЧЕ ТО ТАМ

### Allstate

<table>
<thead>
  <tr>
    <th> </th>
    <th>Pseudo Huber</th>
    <th>Huber</th>
    <th>MSLE</th>
    <th>MAE</th>
    <th>LogCosh</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Test loss</b></td>
    <td><b>1139</b></td>
    <td><b>1139</b></td>
    <td><b>1140</b></td>
    <td>1915</td>
    <td>1152</td>
  </tr>
</tbody>
</table>

<p align="center"><img src="pics/allstate.png" width="800" /></p>

### House Prices

<table>
<thead>
  <tr>
    <th> </th>
    <th>Pseudo Huber</th>
    <th>Huber</th>
    <th>MSLE</th>
    <th>MAE</th>
    <th>LogCosh</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Test loss</b></td>
    <td>22818</td>
    <td>58577</td>
    <td><b>16914</b></td>
    <td>62387</td>
    <td>60336</td>
  </tr>
</tbody>
</table>

<p align="center"><img src="pics/house_prices.png" width="800" /></p>

### Life Expectancy

<table>
<thead>
  <tr>
    <th> </th>
    <th>Pseudo Huber</th>
    <th>Huber</th>
    <th>MSLE</th>
    <th>MAE</th>
    <th>LogCosh</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Test loss</b></td>
    <td>1.17</td>
    <td>1.16</td>
    <td><b>1.13</b></td>
    <td>1.20</td>
    <td>1.34</td>
  </tr>
</tbody>
</table>

<p align="center"><img src="pics/life_expectancy.jpg" width="800" /></p>

### Car Price Prediction Challenge

<table>
<thead>
  <tr>
    <th> </th>
    <th>Pseudo Huber</th>
    <th>Huber</th>
    <th>MSLE</th>
    <th>MAE</th>
    <th>LogCosh</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>Test loss</b></td>
    <td>5872</td>
    <td>5941</td>
    <td><b>5868</b></td>
    <td>12691</td>
    <td>6892</td>
  </tr>
</tbody>
</table>

<p align="center"><img src="pics/car price.jpg" width="800" /></p>

### Dependence on delta for each dataset

<p align="center"><img src="pics/delta_allstate.jpg" width="800" /></p>

<p align="center"><img src="pics/delta_house_prices.png" width="700" /></p>

<p align="center"><img src="pics/delta_life_expectancy.jpg" width="800" /></p>

<p align="center"><img src="pics/delta_car_price.jpg" width="800" /></p>


## Team 13:
- Danil Ivanov
- Stas Pyatkin
- Bari Khairullin
- Dmitriy Kornilov
- Danil Gusak
