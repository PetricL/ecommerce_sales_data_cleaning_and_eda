# E‑Commerce Sales Data Cleaning and Exploratory Data Analysis (EDA)

## Project Overview
This project demonstrates a complete data cleaning and exploratory data analysis (EDA) workflow using Python and Pandas.  
The objective was to transform a messy e‑commerce sales dataset into a clean, analysis‑ready dataset and uncover meaningful insights through statistical analysis and visualization.

---

## Technologies Used
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## Project Structure
```text
ecommerce_data_cleaning_and_eda/
│
├── data/
│   ├── messy_ecommerce_sales_data.csv
│   └── cleaned_ecommerce_sales_data.csv
│
├── notebooks/
│   ├── cleaning.ipynb
│   └── eda.ipynb
│
├── scripts/
│   └── cleaning.py
│
├── images/
│   ├── category_distribution.png
│   ├── payment_method_distribution.png
│   ├── order_status_distribution.png
│   ├── revenue_by_category.png
│   ├── monthly_revenue_trend.png
│   ├── correlation_heatmap.png
│   └── top_5_products_by_revenue.png
│
├── README.md
└── requirements.txt
```


---

## How to Run the Project

### 1. Clone the Repository
git clone https://github.com/PetricL/ecommerce_sales_data_cleaning_and_eda.git

### 2. Install Dependencies
```bash
pip install -r requirements.txt


### 3. Run the Data Cleaning Script
scripts/cleaning.py

### 4. Open the Jupyter Notebooks
Use the notebooks below to review the complete data cleaning process and exploratory data analysis:

notebooks/cleaning.ipynb
notebooks/eda.ipynb

---

## Data Cleaning Process
The raw dataset contained multiple data quality issues that required preprocessing.

### Cleaning Tasks Performed
- Loaded and inspected the raw dataset  
- Converted Quantity and Price to numeric values  
- Removed invalid or negative entries  
- Standardized category and product names  
- Cleaned text fields (customer name, payment method, status, order ID)  
- Converted Order_Date to datetime format  
- Recalculated the Total column  
- Removed duplicate records  
- Exported the cleaned dataset  

---

## Exploratory Data Analysis (EDA)
After cleaning, exploratory analysis was performed to better understand the dataset.

### Analysis Included
- Descriptive statistics  
- Distribution analysis  
- Category‑level revenue analysis  
- Payment method and order status patterns  
- Monthly revenue trends  
- Correlation analysis  

### Visualizations
- Bar charts  
- Count plots  
- Line charts  
- Correlation heatmap  

---

## Key Findings
- The dataset is clean and well‑structured after preprocessing.  
- Books is the strongest category in both frequency and revenue.  
- Cash on Delivery is the most commonly used payment method.  
- Returned orders appear unusually often, indicating potential product or logistics issues.  
- Total revenue is influenced by both Quantity and Price, while Quantity and Price themselves show almost no correlation.  
- Monthly revenue fluctuates significantly over time, with clear periods of growth and decline.  
- **A small number of products generate a disproportionately large share of total revenue, with Shoes and Comics standing out as top performers.**

---

## Future Improvements
Potential extensions of this project include:

- Feature engineering  
- Predictive modeling  
- Customer segmentation  
- Sales forecasting  
- Interactive dashboards using Power BI or Tableau  
- Advanced statistical analysis  

---

## Author
**Lazar Petric**  
E‑Commerce Data Cleaning & Exploratory Data Analysis Project (2026)


