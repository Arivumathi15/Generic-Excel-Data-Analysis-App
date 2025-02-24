# Generic Excel Data Analysis App  

## Overview  
This is a **Streamlit-based web application** that allows users to upload an **Excel file**, select a sheet, and query the data using **LangChain's AI-powered agent**. The app leverages **OpenAI's GPT-4o** model to interpret and answer questions about the uploaded dataset.  

## Features  
- 📂 Upload **Excel files** with multiple sheets  
- 📊 **View and interact** with the selected dataset  
- 🤖 **AI-powered queries** using LangChain and OpenAI  
- ⚡ Fast and intuitive **Streamlit interface**  

## Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/excel-analysis-app.git
   cd excel-analysis-app
   ```
   
## Install dependencies:

```bash
pip install -r requirements.txt
```

## Set up your OpenAI API key:

Create a .env file in the project root and add:

  ```bash
  OPENAI_API_KEY=your_openai_api_key
  Replace your_openai_api_key with your actual API key from OpenAI.
  ```

## Run the Streamlit app:

  ```bash
  streamlit run app.py
  ```

## Usage

- Upload an Excel file via the web interface.
- Select a sheet to analyze.
- View the data in a tabular format.
- Enter a query about the dataset and get AI-powered insights.

## Dependencies

- This app requires the following Python packages:

  ```bash
  pandas  
  streamlit  
  openai  
  python-dotenv  
  langchain  
  langchain-openai  
  langchain-experimental
  ```  

## Example Queries

- What is the total sales for each category?
- Show the top 5 customers based on revenue.
- Filter data for orders placed in 2023.

## License

- This project is licensed under the MIT License.

## Contributing

- Feel free to fork this repo and submit pull requests for improvements!

## Results: 

![WhatsApp Image 2025-02-24 at 2 35 56 PM](https://github.com/user-attachments/assets/5801a18d-83e3-4259-997b-05eeba97cec4)


![WhatsApp Image 2025-02-24 at 2 36 31 PM](https://github.com/user-attachments/assets/034ab4a2-45e1-4b39-8ac9-430494cb6b11)


![WhatsApp Image 2025-02-24 at 2 37 00 PM](https://github.com/user-attachments/assets/e17679bb-c8b9-4996-b814-625401235d6d)


