import pandas as pd
from pandas import read_excel
from datetime import datetime
import tkinter as tk

def process_data(file_path):
    # Load data
    data = pd.read_excel(file_path)
    
    # Ensure the amount is a float
    data['Invoice Amount'] = data['Invoice Amount'].apply(lambda x: float(x.replace(',', '')) if isinstance(x, str) else float(x))
    
    # Ensure the date is a date
    data['Invoice Date'] = data['Invoice Date'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y').date() if isinstance(x, str) else x.date())
    
    return data

def find_invoice_discrepancies(sap_data, portal_data):
    # Identify the invoices that are present in one dataset but not in the other
    sap_invoices = set(sap_data['INVOICE NUMBER'])
    portal_invoices = set(portal_data['INVOICE NUMBER'])

    invoices_only_in_sap = list(sap_invoices - portal_invoices)
    invoices_only_in_portal = list(portal_invoices - sap_invoices)

    # Find the invoices that are present in both but have different amounts or dates
    common_invoices = sap_invoices.intersection(portal_invoices)

    discrepant_invoices = []
    for invoice in common_invoices:
        sap_invoice_index = sap_data[sap_data['INVOICE NUMBER'] == invoice].index[0]
        portal_invoice_index = portal_data[portal_data['INVOICE NUMBER'] == invoice].index[0]
        
        sap_amount = sap_data.loc[sap_invoice_index, 'Invoice Amount']
        portal_amount = portal_data.loc[portal_invoice_index, 'Invoice Amount']
        if sap_amount != portal_amount:
            discrepant_invoices.append([invoice, "Amount", sap_amount, portal_amount])
        
        sap_date = sap_data.loc[sap_invoice_index, 'Invoice Date']
        portal_date = portal_data.loc[portal_invoice_index, 'Invoice Date']
        if sap_date != portal_date:
            discrepant_invoices.append([invoice, "Date", sap_date, portal_date])

    return invoices_only_in_sap, invoices_only_in_portal, discrepant_invoices

def display_results(invoices_only_in_sap, invoices_only_in_portal, discrepant_invoices):
    # Create a new Tkinter window
    window = tk.Tk()

    # Create a new Text widget for each list of results
    invoices_only_in_sap_widget = tk.Text(window, height=10, width=50)
    invoices_only_in_sap_widget.insert('insert', "\n".join(map(str, invoices_only_in_sap)))

    invoices_only_in_portal_widget = tk.Text(window, height=10, width=50)
    invoices_only_in_portal_widget.insert('insert', "\n".join(map(str, invoices_only_in_portal)))

    discrepant_invoices_widget = tk.Text(window, height=10, width=50)
    for invoice in discrepant_invoices:
        invoice[2] = str(invoice[2])
        invoice[3] = str(invoice[3])
        discrepant_invoices_widget.insert('insert', ", ".join(invoice) + "\n")

    # Pack the widgets
    invoices_only_in_sap_widget.pack()
    invoices_only_in_portal_widget.pack()
    discrepant_invoices_widget.pack()

    # Run the Tkinter event loop
    window.mainloop()

def main():
    sap_file_path = 'export_sap.xlsx'
    portal_file_path = 'export_portal.xlsx'
    sap_data = process_data(sap_file_path)
    portal_data = process_data(portal_file_path)
    invoices_only_in_sap, invoices_only_in_portal, discrepant_invoices = find_invoice_discrepancies(sap_data, portal_data)
    display_results(invoices_only_in_sap, invoices_only_in_portal, discrepant_invoices)

if __name__ == "__main__":
    main()
