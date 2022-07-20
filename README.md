<h1 align="center">Amazon Best Seller Prediction</h1>

***
# What makes an item in Amazon  a Best Seller ?

In our project we try to find out why an item is a Best Seller

## 🌟 Highlights

- Data Acquisition
- Data Handling
- Exploratory Data Analysis ( EDA )
- Supervised Learning
- Unsupervised Learning

## ℹ️ Overview

***Data Acquisition***

- Using **Selenium** we managed to scrape more the 100,000 data cells on more than 13,000 items in Amazon Both Best Seller and regular items

***Data Handling***

- With the **BeautifulSoup ( bs4 )** library we collected and arranged the data and exported the data into a .csv file
- We used various methodes in order to clean tha data : 
  - Removing duplicates 
  - Removing corrupted values 
  - Normalizing
  - Transform all data to type Float

***Exploratory Data Analysis ( EDA )***

- In oredr to analyze our DataFrame we used **seaborn** and **matplotlib** visualization libraries
  - Pie plot
  - Histogram
  - Boxplot
  - Scatter plot
  - pairplot

- Dealing with outliers using IQR variable

- Using **Chi Test** to determine if there is correlation between data features

***Supervised Learning***

- **prediction models :**
  - Logistic Regression, r2_score
  - KNN

***Unsupervised Learning***

- **prediction models :**
  - K-means, silhouette score
  - Hierarchical agglomerative clustering
  - DBSCAN

***

## 📑 Conclusion

After using Both Supervised and UnSupervised Learning we can conclude that **we can't really find out what makes an item a BestSeller for sure**. We tried to predict a
bestseller using classification, we've got a right prediction but we can't really find it exact every time. Using KNN was not so helpful also, we tried to figure what
k as number of classes we got best score for k=1. We also tried split the items into different groups using the unsupervised methods and didn't really find good
results

More information is needed on items in order to get better results

***

### ✍️ Authors
- Yaniv Lavi

✉️ [yan465@gmail.com](url)  
💿 https://github.com/yanivlav  
🖥️ https://www.linkedin.com/in/yanivlav1/  
- Stas Bratanitch

✉️ [bstasb@gmail.com](url)  
💿 https://github.com/StasBratanich  
🖥️ https://www.linkedin.com/in/stas-bratanich-computer-science/  

