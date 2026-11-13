
import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(
    page_title="بيلا للشموع المعطرة",
    page_icon="🕯️",
    layout="wide"
)

# تنسيق الصفحة
st.markdown("""
<style>

/* اتجاه الصفحة من اليمين إلى اليسار */
.stApp {
    direction: rtl;
    background-color: #FAF7F2;
}

.block-container {
    direction: rtl;
    text-align: right;
    padding-top: 2rem;
}

/* تنسيق العناوين والنصوص */
h1, h2, h3, p, label {
    text-align: right;
}

/* تنسيق مربعات المؤشرات */
div[data-testid="stMetric"] {
    background-color: #F1E5D8;
    border: 1px solid #D8BFA8;
    border-radius: 15px;
    padding: 20px;
    text-align: right;
    direction: rtl;
}

/* تنسيق أرقام المؤشرات */
div[data-testid="stMetricValue"] {
    color: #704B3A;
    font-size: 25px;
}

/* تنسيق القائمة الجانبية */
section[data-testid="stSidebar"] {
    direction: rtl;
    text-align: right;
    background-color: #F3E8DE;
}

</style>
""", unsafe_allow_html=True)

# عنوان المشروع
st.title("🕯️ بيلا للشموع المعطرة")
st.subheader("لوحة ذكاء الأعمال وتحليل المبيعات")
st.write("مرحباً بك في لوحة تحليل مبيعات متجر بيلا.")

st.divider()

# بيانات المبيعات
data = {
    "المنتج": [
        "شمعة الفانيلا",
        "شمعة اللافندر",
        "شمعة الورد",
        "شمعة الياسمين",
        "شمعة الفانيلا",
        "شمعة اللافندر",
        "شمعة الورد",
        "شمعة الياسمين"
    ],

    "الكمية": [20, 15, 12, 10, 18, 14, 16, 11],

    "السعر": [45, 50, 55, 48, 45, 50, 55, 48],

    "التكلفة": [20, 22, 25, 21, 20, 22, 25, 21]
}

# إنشاء جدول البيانات
df = pd.DataFrame(data)

# حساب إجمالي المبيعات
df["إجمالي المبيعات"] = df["الكمية"] * df["السعر"]

# حساب الأرباح
df["الأرباح"] = df["الكمية"] * (df["السعر"] - df["التكلفة"])

# القائمة الجانبية
st.sidebar.title("قائمة المتجر")

products = st.sidebar.multiselect(
    "اختاري المنتج",
    df["المنتج"].unique(),
    default=df["المنتج"].unique()
)

# تصفية المنتجات
filtered_df = df[df["المنتج"].isin(products)]

# حساب المؤشرات
total_sales = filtered_df["إجمالي المبيعات"].sum()
total_profit = filtered_df["الأرباح"].sum()
total_quantity = filtered_df["الكمية"].sum()

# تحديد المنتج الأكثر مبيعاً
if len(filtered_df) > 0:
    best_product = filtered_df.groupby("المنتج")["الكمية"].sum().idxmax()
else:
    best_product = "لا يوجد"

# عرض المؤشرات
st.header("مؤشرات أداء المتجر")

col1, col2, col3, col4 = st.columns(4)

col1.metric("إجمالي المبيعات", str(total_sales) + " ر.س")
col2.metric("إجمالي الأرباح", str(total_profit) + " ر.س")
col3.metric("الكمية المباعة", total_quantity)
col4.metric("الأكثر مبيعاً", best_product)

st.divider()

# تحليل المبيعات
st.header("تحليل المبيعات")

if len(filtered_df) > 0:

    st.subheader("المبيعات حسب المنتج")

    sales = filtered_df.groupby("المنتج")["إجمالي المبيعات"].sum()
    st.bar_chart(sales)

    st.subheader("الأرباح حسب المنتج")

    profits = filtered_df.groupby("المنتج")["الأرباح"].sum()
    st.bar_chart(profits)

else:
    st.info("يرجى اختيار منتج واحد على الأقل.")

st.divider()

# جدول تفاصيل المبيعات
st.header("تفاصيل المبيعات")

st.dataframe(
    filtered_df,
    hide_index=True,
    use_container_width=True
)
