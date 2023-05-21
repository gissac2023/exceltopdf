import pandas as pd
import glob
from fpdf import FPDF

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    #FPDF.add_page(orientation="L", format="A4")
    #col1, col2, col3 in FPDF.cell():

