import matplotlib.pyplot as plt
import pandas as pd

# ==========================================
# 1. تحميل واستكشاف البيانات (Data Loading & Exploration)
# ==========================================
file_path = "E-Commerce Sales.csv"
data = pd.read_csv(file_path)

# عرض الصفوف الأولى والأخيرة وعينة عشوائية
print("=== الصفوف الأولى (Head) ===")
print(data.head())

print("\n=== الصفوف الأخيرة (Tail) ===")
print(data.tail())

print("\n=== عينة عشوائية (Sample) ===")
print(data.sample(5))

print("\n=== معلومات البيانات وأنوع الأعمدة ===")
data.info()

print("\n=== الإحصاءات الوصفية ===")
print(data.describe())

# ==========================================
# 2. معالجة التواريخ (Datetime Processing)
# ==========================================
data["Date"] = pd.to_datetime(data["Date"])

data["day"] = data["Date"].dt.day
data["year"] = data["Date"].dt.year
data["quarter"] = data["Date"].dt.quarter
data["month_name"] = data["Date"].dt.month_name()
data["day_name"] = data["Date"].dt.day_name()
data["day_short"] = data["Date"].dt.day_name().str[:3]

# ==========================================
# 3. تنظيف البيانات والتحويل الرقمي (Data Cleaning)
# ==========================================
# تنظيف سعر الوحدة Unit Price
data["Unit Price"] = (
    data["Unit Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
    .astype(float)
)
print(f"\nنوع بيانات Unit Price: {data['Unit Price'].dtype}")

# تنظيف تكلفة الوحدة Unit Cost
data["Unit Cost"] = (
    data["Unit Cost"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
    .astype(float)
)
print(f"نوع بيانات Unit Cost: {data['Unit Cost'].dtype}")

# ==========================================
# 4. حساب المؤشرات المالية (KPIs Calculation)
# ==========================================
data["Total_Sales"] = data["Quantity"] * data["Unit Price"]
data["Total_Cost"] = data["Quantity"] * data["Unit Cost"]
data["Profit"] = data["Total_Sales"] - data["Total_Cost"]

print("\n=== معلومات البيانات بعد إضافة المؤشرات ===")
data.info()

print("\n=== القيم الفريدة لجنس العملاء ===")
print(data["Customer Gender"].unique())

# ==========================================
# 5. التصور البياني (Data Visualization)
# ==========================================
plt.figure(figsize=(6, 6))
data["Customer Gender"].value_counts().plot(
    kind="pie", autopct="%1.1f%%", startangle=90
)
plt.title("Customer Gender Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# ==========================================
# 6. التجميع والجدولة المحورية (Aggregation & Pivoting)
# ==========================================
# تجميع المبيعات حسب فئة المنتج وترتيبها
category_sales = (
    data.groupby("Product Category")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
print("\n=== إجمالي المبيعات حسب فئة المنتج ===")
print(category_sales)

# الجدول المحوري Pivot Table
category_pivot = data.pivot_table(
    index="Product Category", values="Total_Sales", aggfunc="sum"
)
print("\n=== الجدول المحوري للمبيعات ===")
print(category_pivot)

# ==========================================
# 7. حفظ البيانات المعدلة واستدعاؤها (Export & Reload)
# ==========================================
cleaned_file_path = "newfile.csv"
data.to_csv(cleaned_file_path, index=False)

# قراءة الملف المنظف
data_2 = pd.read_csv(cleaned_file_path)
print("\n=== عينة من الملف الجديد ===")
print(data_2.sample(3))

# حذف عمود الفهرس الإضافي في حال وجوده
if "Unnamed: 0" in data_2.columns:
    data_2 = data_2.drop(columns=["Unnamed: 0"])

# ==========================================
# 8. التصفية المتقدمة (Advanced Filtering)
# ==========================================
print("\n=== معاملات دولة فرنسا فقط ===")
print(data_2[data_2["Country"] == "France"].head())

print("\n=== العملاء الذين أعمارهم أكبر من 30 ===")
print(data_2[data_2["Customer Age"] > 30].head())

print("\n=== تصفية مركبة (فرنسا + عمر > 30 + دبابات Bikes) ===")
filtered_data = data_2[
    (data_2["Country"] == "France")
    & (data_2["Customer Age"] > 30)
    & (data_2["Product Category"] == "Bikes")
]
print(filtered_data)
