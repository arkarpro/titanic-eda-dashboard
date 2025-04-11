import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------------------#
# Load CSV with caching and loading spinner
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/arkarpro/titanic-eda-dashboard/main/Titanic.csv")

with st.spinner("🔄 Loading data... Please wait."):
    df = load_data()
#--------------------------------------------------------------------------------------#
# Dashboard Title
st.markdown(
    "<h1 style='color:blue; font-size: 36px; text-align: left;'>Titanic EDA Dashboard</h1>", 
    unsafe_allow_html=True
)
st.info("Titanic EDA Dashboard သည် သင်ကြားမှုဆိုင်ရာ အလိုက် လေ့ကျင့်သောဖိုင်ဖြစ်ပါသဖြင့် အခြေခံသင်ကြားမှုများကို လေ့လာသင်ကြားခြင်းကို လက်တွေ့မျှဝေသော လေ့ကျင့်ခန်းတစ်ခုသာဖြစ်ပါသည်။")
st.markdown("""
    - **ယခုလေ့ကျင့်ခန်းမှာ** ခရီးသည်များ၏ *အမျိုးအစား*၊ *အသက်အုပ်စု* နှင့် *အသက်ရှင်/သေဆုံးမှု* အခြေအနေများကို သုံးသပ်သွားမှာ ဖြစ်ပါတယ်။
    - **မှတ်ချက်။ ။** ယခုလေ့ကျင့်ခန်းကို သင်ကြားမှု အခန်းအလိုက် တဆင့်စီ update ပြုလုပ်သွားမည်ဖြစ်ပါသည်။
""")

st.info("Titanic သင်္ဘောကြီး ခရီးသည်အချက်အလက်များ")
st.markdown("""
    - ခရီးသည် စုစုပေါင်း **၈၉၁** ဦး ပါဝင်သည်။
    - **အမျိုးသား ၅၇၇** ဦးနှင့် **အမျိုးသမီး ၃၁၄** ဦး ပါဝင်သည်။
    - ယခုလေ့ကျင့်ခန်းတွင်၊ 
        - အသက်အုပ်စု
        - စီးနင်းလိုက်ပါလာသည့် အတန်း (P class)
        - ကျား/မ
        - ရှင်သန်/သေဆုံးမှုများ
    ကို စုစည်းသုံးသပ်သွားကြမှာ ဖြစ်ပါတယ်။
""")

#--------------------------------------------------------------------------------------#
# add one blank line here
st.text("")  # Blank line
st.text("")  # Blank line
st.text("")  # Blank line
#--------------------------------------------------------------------------------------#
total_passengers_sex= df.Sex.value_counts() # prepare passenger table
st.markdown("#### Total Passengers by Gender") #show subtitle
st.markdown("""
    ##### 💡 Idea  
    - ခရီးသွား အမျိုးသား၊ အမျိုးသမီး အရေအတွက်ကို အချက်အလက်အားဖြင့် ဒေါင်းလုတ်ချနိုင်ရန် ဘယ်ဘက်တွင် ဇယားဖြင့် ဖော်ပြထားပြီးတော့၊  
    - အချက်အလက်ကို အလွယ်မြင်သာစေရန် ညာဘက်တွင် Bar Chart ဖြင့်​ဖော်ပြကြမယ်။
""")
st.text("")  # Blank line

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
st.markdown("#### Survived and Not-Survived Passengers")
st.markdown("""
    ##### 💡 Idea  
    - အသက်ရှင်သန်ကျန်ရစ်သူ စာရင်းကို ကျား၊မ အလိုက်ဖော်ပြခြင်းဖြင့် အလွယ်တကူနှိုင်းယှဉ်နိုင်နိုင်အောင်ပြင်ဆင်မယ်။ 
    - ဒီတစ်ခါ အခြေခံ Pie chart လေးကို ရိုးရှင်းစွာထည့်မယ်။
""")
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
st.markdown("#### နောက်ရက်များမှာ ဆက်လက် လေ့လာကြရင်း အဆင့်မြှင့်ကြမယ်နော် Bye!")
