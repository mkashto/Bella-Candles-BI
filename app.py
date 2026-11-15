
import streamlit as st
import pandas as pd
import altair as alt

# إعداد الصفحة
st.set_page_config(
    page_title="بيلا للشموع المعطرة",
    page_icon="🕯️",
    layout="centered"
)

# تنسيق الصفحة
st.markdown("""
<style>
.stApp {
    direction: rtl;
    background-color: white;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    direction: rtl;
    text-align: right;
}

h1, h2, h3, p, label {
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

# عنوان المشروع
st.title("🕯️ بيلا للشموع المعطرة")
st.subheader("لوحة تحليل المبيعات")
st.write("مرحباً بك في متجر بيلا للشموع المعطرة.")

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
df["الأرباح"] = df["الكمية"] * (
    df["السعر"] - df["التكلفة"]
)

# حساب المؤشرات
total_sales = df["إجمالي المبيعات"].sum()
total_profit = df["الأرباح"].sum()
total_quantity = df["الكمية"].sum()

best_product = df.groupby("المنتج")["الكمية"].sum().idxmax()

# عرض المؤشرات
st.header("مؤشرات أداء المتجر")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "إجمالي المبيعات",
    str(total_sales) + " ر.س"
)

col2.metric(
    "إجمالي الأرباح",
    str(total_profit) + " ر.س"
)

col3.metric(
    "الكمية المباعة",
    total_quantity
)

col4.metric(
    "الأكثر مبيعاً",
    best_product
)

st.divider()

# تحليل المبيعات
st.header("تحليل المبيعات")

# المبيعات حسب المنتج
st.subheader("المبيعات حسب المنتج")

sales = df.groupby(
    "المنتج",
    as_index=False
)["إجمالي المبيعات"].sum()

chart1 = alt.Chart(sales).mark_bar(
    color="#1976D2"
).encode(
    x=alt.X(
        "المنتج:N",
        title="المنتج",
        sort=None,
        axis=alt.Axis(labelAngle=0)
    ),
    y=alt.Y(
        "إجمالي المبيعات:Q",
        title="إجمالي المبيعات بالريال",
        scale=alt.Scale(domainMin=0)
    )
).properties(
    width=650,
    height=300
)

st.altair_chart(
    chart1,
    use_container_width=False
)

# الأرباح حسب المنتج
st.subheader("الأرباح حسب المنتج")

profits = df.groupby(
    "المنتج",
    as_index=False
)["الأرباح"].sum()

chart2 = alt.Chart(profits).mark_bar(
    color="#1976D2"
).encode(
    x=alt.X(
        "المنتج:N",
        title="المنتج",
        sort=None,
        axis=alt.Axis(labelAngle=0)
    ),
    y=alt.Y(
        "الأرباح:Q",
        title="الأرباح بالريال",
        scale=alt.Scale(domainMin=0)
    )
).properties(
    width=650,
    height=300
)

st.altair_chart(
    chart2,
    use_container_width=False
)

st.divider()

# جدول تفاصيل المبيعات
st.header("تفاصيل المبيعات")

st.dataframe(
    df,
    hide_index=True,
    use_container_width=True
)
