import pandas as pd
import matplotlib.pyplot as plt

# Path to the CSV file
csv_path = 'data.csv'

try:
    # 1. Load data from CSV and read only the necessary columns to save memory
    df = pd.read_csv(csv_path, usecols=['Intl_Student_Ratio', 'Employment_Rate'])
    
    # 2. Data Cleaning: remove rows with missing values in target columns
    df = df.dropna(subset=['Intl_Student_Ratio', 'Employment_Rate'])

    # 3. Define bins and labels for categorization
    bins = [80, 85, 90, 95, 100]
    labels = ['80-84', '85-89', '90-94', '95-100']

    # 4. Use pd.cut to segment Employment_Rate into intervals
    df['Rate_Group'] = pd.cut(df['Employment_Rate'], bins=bins, labels=labels)

    # 5. Group by intervals and calculate the average International Student Ratio
    mean_intl = df.groupby('Rate_Group')['Intl_Student_Ratio'].mean()

    # 6 Visualisation
    plt.figure(figsize=(8, 5))
    mean_intl.plot(kind='bar', color='skyblue', edgecolor='black')

    plt.title('Relationship between employment and proportion of foreign students')
    plt.xlabel('Employment Rate (%)')
    plt.ylabel('Mean Intl Student Ratio')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

except FileNotFoundError:
    print(f"Error: The file {csv_path} was not found")
except Exception as e:
    print(f'An unexpected error occured: {e}')