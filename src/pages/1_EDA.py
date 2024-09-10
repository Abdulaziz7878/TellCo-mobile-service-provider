import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data from the xlsx file
def load_data(uploaded_file):
    """
    Load data from an Excel file.

    Args:
        uploaded_file (streamlit.uploaded_file_manager.UploadedFile): The uploaded Excel file.

    Returns:
        pandas.DataFrame: The loaded data.
    """
    try:
        data = pd.read_csv(uploaded_file)
        return data
    except Exception as e:
        st.error("Error loading data: " + str(e))
        return None

df = load_data(r"C:\Users\Abdulaziz\Desktop\10 Academy\TellCo mobile service provider\notebooks\cleand-data.csv")

def display_data_preview(data):
    """
    Display the first few rows of the data.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.title("EDA Page")
    st.header("Data Preview")
    st.write(data.head())

display_data_preview(df)

def display_data_types(data):
    """
    Display the data types of each column.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Data Types")
    st.write(data.dtypes)

display_data_types(df)

def display_summary_statistics(data):
    """
    Display the summary statistics of the data.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Summary Statistics")
    st.write(data.describe())

display_summary_statistics(df)

def display_distribution(data, column_name):
    """
    Display the distribution of a column.

    Args:
        data (pandas.DataFrame): The data to display.
        column_name (str): The name of the column to display.
    """
    st.header(f"Distribution of {column_name}")
    fig = px.bar(data[column_name].value_counts())
    st.plotly_chart(fig, use_container_width=True)

def eda_page(data):
    """
    Display the exploratory data analysis page.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.title("Exploratory Data Analysis")

    analysis_options = {
        "Data Types": display_data_types,
        "Summary Statistics": display_summary_statistics,
        "Distribution": display_distribution,
    }

def main():
    """
    The main function.
    """

if __name__ == "__main__":
    main()