import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings 
warnings.filterwarnings("ignore")  # ->ignorar os erros que aparecem no site

st.set_page_config(page_title= "Trabalho",page_icon=":bookmark_tabs:", layout="wide")  #->Titulo da aba no navegador

# {=======================Título=========================}
st.title("Desenvolvimento de um Medidor de Desgaste de Furo de Lança de Convertedores LD")
st.markdown('<style>div.block-container{padding-top:1rem;}</style> ',unsafe_allow_html=True)

# {=======================Dowload de arquivo=========================}
fl = st.file_uploader(":file_folder: Uploud a file", type=(["csv","txt","xlsx","xls"]))

if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename, encoding = 'ISO-8859-1')
else:
    os.chdir(r"C:\Users\julia\OneDrive\Documentos\IFES\PROJETO_WRL\SITE")
    df = pd.read_csv("Superstore.csv", encoding = 'ISO-8859-1')

# {=======================Seleção de Datas=========================}
col1, col2 = st.columns((2))
df["Order Date"] = pd.to_datetime(df["Order Date"])

startDate = pd.to_datetime(df["Order Date"]).min()
endDate = pd.to_datetime(df["Order Date"]).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Data de início", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("Data final", endDate))

    df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)]. copy()

# {=======================Barra de seleção=========================}
st.sidebar.header("Seja bem-vindo")
region = st.sidebar.multiselect("Região:", df["Region"].unique())
if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

state = st.sidebar.multiselect("Estado:", df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df["State"].isin(state)]

city = st.sidebar.multiselect("Cidade:", df3["City"].unique())

# {=======================Filtro baseado na região, estado e cidade=========================}

if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df = df[df["State"].isin(state)]
elif state and city:
    filtered_df = df3[df["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df = df3[df["Region"].isin(region) & df3["City"].isin(city)]
elif region and state:
    filtered_df = df3[df["Region"].isin(region) & df3["State"].isin(state)]
elif city:
    filtered_df = df3[df3["City"].isin(city)]
else:
    filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]

category_df = filtered_df.groupby(by = ["Category"], as_index = False)["Sales"].sum()

# {=======================Primeiros gráficos=========================}

with col1:
    st.subheader("Categorias de venda")
    fig = px.bar(category_df, x = "Category",y= "Sales", text = ['${:,.2f}'.format(x) for x in category_df["Sales"]], template = "seaborn")
    st.plotly_chart(fig, use_container_width=True, height = 200)

with col2:
    st.subheader("Regiões de venda")
    fig = px.pie(filtered_df, values = "Sales", names = "Region", hole = 0.5, )
    fig.update_traces(text = filtered_df["Region"],textposition = "outside")
    st.plotly_chart(fig, use_container_width=True)

# {=======================Dowload dos dados filtrados=========================}

cl1,cl2 = st.columns(2)
with cl1:
    with st.expander("Category_ViewData"):
        st.write(category_df.style.background_gradient(cmap = "Greens"))
        csv = category_df.to_csv(index = False).encode('utf-8')
        st.download_button("Dowload Data", data = csv, file_name = "Categoria.csv", mime= "Text/csv", help = "Click here :computer:")

with cl2:
    with st.expander("Region_ViewData"):
        region = filtered_df.groupby(by = "Region", as_index = False)["Sales"].sum()
        st.write(region.style.background_gradient(cmap = "Greens"))
        csv = category_df.to_csv(index = False).encode('utf-8')
        st.download_button("Dowload Data", data = csv, file_name = "Região.csv", mime= "Text/csv", help = "Click here :computer:")

filtered_df["month_year"] = filtered_df["Order Date"]. dt.to_period("M")
st.subheader('Analize de tempos')

linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x="month_year", y = "Sales", labels={"Sales":"Montante"}, height = 500, width= 1000, template="gridon")
st.plotly_chart(fig2, use_container_width=True)

with st.expander("View Data of TimeSeries:"):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv", mime ='text/csv')

 