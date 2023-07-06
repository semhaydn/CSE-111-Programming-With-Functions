def find_invoice_discrepancies(sap_file_path, portal_file_path):
    import pandas as pd

    # Load SAP data
    sap_data = pd.read_csv(sap_file_path)
    
    # Convert 'Amount in doc. curr.' to numeric type and take the absolute value
    sap_data['Amount in doc. curr.'] = pd.to_numeric(sap_data['Amount in doc. curr.'], errors='coerce').abs()
    
    sap_data.set_index('INVOICE NUMBER', inplace=True)

    # Load Portal data
    portal_data = pd.read_csv(portal_file_path)
    portal_data.set_index('INVOICE NUMBER', inplace=True)

    # Identify the invoices that are present in one dataset but not in the other
    sap_invoices = set(sap_data.index)
    portal_invoices = set(portal_data.index)

    invoices_only_in_sap = list(sap_invoices - portal_invoices)
    invoices_only_in_portal = list(portal_invoices - sap_invoices)

    # Find the invoices that are present in both but have different amounts or dates
    common_invoices = sap_invoices.intersection(portal_invoices)

    discrepant_invoice_list = []
    for invoice in common_invoices:
        sap_invoice = sap_data.loc[invoice]
        portal_invoice = portal_data.loc[invoice]
        if sap_invoice['Amount in doc. curr.'] != portal_invoice['Invoice Amount']:
            discrepant_invoice_list.append([invoice, "Amount", sap_invoice['Amount in doc. curr.'], portal_invoice['Invoice Amount']])
        if sap_invoice['Document Date'] != portal_invoice['Invoice Date']:
            discrepant_invoice_list.append([invoice, "Date", sap_invoice['Document Date'], portal_invoice['Invoice Date']])

    # Convert the list of discrepant invoices to a DataFrame
    discrepant_invoices = pd.DataFrame(discrepant_invoice_list, columns=["Invoice Number", "Discrepancy Type", "SAP Value", "Portal Value"])

    print(invoices_only_in_portal)
    print(invoices_only_in_sap)
    print(discrepant_invoices)

    return invoices_only_in_sap, invoices_only_in_portal, discrepant_invoices



invoices_only_in_sap, invoices_only_in_portal, discrepant_invoices = find_invoice_discrepancies('booked invoices in sap.csv', 'INCOMING INVOICE PORTAL.csv')



