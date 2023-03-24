# Py-Boost custom losses

The repository for final project at [ML course](https://github.com/adasegroup/ML2023_lectures) at Skoltech - "Several custom losses implementation for the median regression task in Py-Boost".


## Datasets:
- [Allstate Claims Severity](https://www.kaggle.com/competitions/allstate-claims-severity/data)
- [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
- [Life Expectancy](https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who)
- [Car Price Prediction Challenge](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge?select=car_price_prediction.csv)

## Results
че то там че то там

### Allstate

<table>
<thead>
  <tr>
    <th></th>
    <th>AE Reconstruct</th>
    <th>AE Raw Decode</th>
    <th><b>AE + W2GN</b></th>
    <th><a href="https://github.com/joeylitalien/celeba-gan-pytorch">WGAN</a></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><b>FID Score</b></td>
    <td>23.35</td>
    <td>86.66</td>
    <td><b>43.35</b></td>
    <td>45.23</td>
  </tr>
</tbody>
</table>

<p align="center"><img src="pics/allstate.png" width="800" /></p>

### House Prices
<p align="center"><img src="pics/house_prices.jpg" width="800" /></p>

### Life Expectancy
<p align="center"><img src="pics/life_expectancy.jpg" width="800" /></p>

### Car Price Prediction Challenge
<p align="center"><img src="pics/car price.jpg" width="800" /></p>




## Team 13:
- Danil Ivanov
- Stas Pyatkin
- Bari Khairullin
- Dmitriy Kornilov
- Danil Gusak
