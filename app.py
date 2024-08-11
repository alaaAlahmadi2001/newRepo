import streamlit as st

# Apply a global font style using custom CSS
st.markdown(
    """
    <style>
    * {
        font-family: 'Arial', sans-serif; /* Replace with your preferred font */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("##")
st.sidebar.button("Home Page")

# Header Section with Columns
col1, col2 = st.columns([2, 3])  # Adjust the ratio as needed

with col1:
    st.title("✨ **A Fresh Graduate's Quest for Success** ✨")

with col2:
    st.image("C:/Users/hp/Desktop/storyHw/job-removebg-preview.png", use_column_width=True)

# Main content with consistent font style
st.markdown("""
### Hey there!

#### I'm Alaa, a recent graduate in computer science and a data science professional. 
#### I'm on the hunt for a job that matches my qualifications and, at the same time, will set me on the path to becoming a wealthy twentysomething 💰.

#### Since I'm passionate about data science, I thought I'd take a creative approach to job hunting.  
#### You might be wondering, How, Alaa? 
#### Let me tell you 💡!!.

#### First, I searched for reliable data on job postings in Saudi Arabia.
#### Once I found the data, I made sure it included all the information I needed, and I started cleaning and analyzing it until it was perfect. 
#### It didn’t take me long; as I said, I’m a pro—just waiting for my chance to shine.

#### As a data scientist, I know that visualizations 📊 are everything. 
#### They're not just for non-tech people; even for us "🌠professional data scientists🌠" they help us see the big picture and make better decisions.


#### So, I started organizing my thoughts into questions that I could answer with the data:

""")


option = st.selectbox(

    "__Select a question to see the visualization.__",


    (
        "What proportion of job postings is attributed to each region within the kingdom?", 

        "Is there a gender preference indicated in the job postings?", 

        "What is the expected salary range for fresh graduates?", 

        "Are job opportunities predominantly targeted at individuals with experience, or is there room for fresh graduates as well?"
    )
)


if option == "What proportion of job postings is attributed to each region within the kingdom?":

    "__Riyadh has the highest job postings, followed by Makkah and the Eastern Region, with the remaining regions showing significantly fewer opportunities.__"

    st.image("C:/Users/hp/Desktop/storyHw/Q1_hw5.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

elif option == "Is there a gender preference indicated in the job postings?":

    "__Most job postings are open to both genders, with a significant number favoring males and fewer opportunities for females.__"

    st.image("C:/Users/hp/Desktop/storyHw/Q2_hw5.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

elif option == "What is the expected salary range for fresh graduates?":

    "__The majority of job salaries cluster around 4,000 SAR, with fewer opportunities offering higher salaries.__"

    st.image("C:/Users/hp/Desktop/storyHw/Q3_hw5.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

elif option == "Are job opportunities predominantly targeted at individuals with experience, or is there room for fresh graduates as well?":

    "__Over 50% of job postings are available for fresh graduates with no prior experience, making it a favorable job market for entry-level candidates.__"

    st.image("C:/Users/hp/Desktop/storyHw/Q4_hw5.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

