import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------------#
# Load CSV
df = pd.read_csv("https://raw.githubusercontent.com/arkarpro/titanic-eda-dashboard/refs/heads/main/Titanic.csv")
#--------------------------------------------------------------------------------------#
# Dashboard Title
st.markdown(
    "<h1 style='color:blue; font-size: 36px; text-align: left;'>Titanic EDA Dashboard</h1>", 
    unsafe_allow_html=True
)
st.info("Titanic သင်္ဘောကြီး ခရီးသည်အချက်အလက်များ")
st.markdown("""
    - ခရီးသည် စုစုပေါင်း **၈၉၁** ဦး ပါဝင်သည်။
    - **အမျိုးသား ၅၇၇** ဦးနှင့် **အမျိုးသမီး ၃၁၄** ဦး ပါဝင်သည်။
    - ယခုလေ့ကျင့်ခန်းတွင်၊ 
        - အသက်အုပ်စု
        - စီးနင်းလိုက်ပါလာသည့် အတန်း (P class)
        - ကျား/မ
        - ရှင်သန်/သေဆုံးမှုများ
    ကို စုစည်းသုံးသပ်သွားမှာ ဖြစ်ပါတယ်။
""")
st.info("Titanic ခရီးသည်များအနက် ၈၉၁ ဦး ပါဝင်ပြီး၊ ယင်းအနက် ၅၇၇ ဦးမှာ အမျိုးသားဖြစ်သည်။")
st.markdown("""
    - **ယခုလေ့ကျင့်ခန်းမှာ** ခရီးသည်များ၏ *အမျိုးအစား*၊ *အသက်အုပ်စု* နှင့် *အသက်ရှင်/သေဆုံးမှု* အခြေအနေများကို သုံးသပ်သွားမှာ ဖြစ်ပါတယ်။
""")
#--------------------------------------------------------------------------------------#
# add one blank line here
st.text("")  # Blank line
st.text("")  # Blank line
st.text("")  # Blank line
#--------------------------------------------------------------------------------------#
total_passengers_sex= df.Sex.value_counts() # prepare passenger table
st.markdown("##### Total Passengers by Gender") #show subtitle
col01, col02 = st.columns(2) # to defind columns
with col01:
    st.markdown("**Count of Passengers**") #show subtitle
    st.dataframe(total_passengers_sex, height=100, width=250) # Show Total Passengers
with col02: # Bar chart in right size
    st.markdown("**Bar Chart**")
    fig, ax = plt.subplots(figsize=(1, 1), dpi=200)  # High DPI for clarity
    ax.bar(total_passengers_sex.index, total_passengers_sex.values, color=["skyblue", "salmon"])
    ax.set_title("Total Passengers by Gender", fontsize=6)
    ax.set_xlabel("Gender", fontsize=5)
    ax.set_ylabel("Total", fontsize=5)
    ax.tick_params(axis='both', which='both', length=0, labelsize=4)
    ax.spines["top"].set_visible(False)     # အပေါ်ဘောင်ဖျောက်
    ax.spines["right"].set_visible(False)   # ညာဘောင်ဖျောက်
    ax.spines["bottom"].set_visible(False)  # အောက်ဘောင်ဖျောက်
    ax.spines["left"].set_visible(False)    # ဘယ်ဘောင်ဖျောက်
    st.pyplot(fig)        # Show in Streamlit
#--------------------------------------------------------------------------------------#
st.text("-------------------------------------------------------------------------------")  # add a line
st.text("")  # Blank line
st.text("")  # Blank line
#--------------------------------------------------------------------------------------#
survived_status = df['Survived'].value_counts() # Prepare data

# Subtitle
st.markdown("##### Survived and Not-Survived Passengers")
# Columns
col1, col2 = st.columns(2)
# Styled box (left side)
with col1:
    st.markdown("** Count Table**")
    st.dataframe(survived_status, height=100, width=250)  # small height, just enough for 2 rows
# Pie chart (right side)
with col2:
    st.markdown("** Pie Chart**")
    fig, ax = plt.subplots(figsize=(1.5, 1.5), dpi=200)  # Higher DPI for clear labels
    ax.pie(survived_status, labels=["Not-Survived", "Survived"], autopct="%0.2f%%", shadow=True,
           colors=["red", "green"], textprops={'fontsize': 6})  # Clearer pie labels
    st.pyplot(fig)
st.text("-------------------------------------------------------------------------------")  # add a line
#--------------------------------------------------------------------------------------#