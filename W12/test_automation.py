import pytest
from pandas import DataFrame
from datetime import date
from automation import process_data, find_invoice_discrepancies

def test_process_data():
    # Create a sample DataFrame for testing
    data = {
        'INVOICE NUMBER': ['INV-001', 'INV-002'],
        'Invoice Date': ['01/01/2023', date(2023, 2, 1)],
        'Invoice Amount': ['100.5', 200],
        'Currency': ['USD', 'EUR']
    }
    df = DataFrame(data)
    df.to_excel('test_data.xlsx', index=False)

    # Process the data
    processed_data = process_data('test_data.xlsx')

    # Check the data types and values
    assert processed_data['Invoice Amount'].dtype == float
    assert processed_data['Invoice Date'].dtype == object  # Datetime is considered as object
    assert processed_data.loc[0, 'Invoice Amount'] == 100.5
    assert processed_data.loc[0, 'Invoice Date'] == date(2023, 1, 1)

def test_find_invoice_discrepancies():
    # Create a sample DataFrame for testing
    data_sap = {
        'INVOICE NUMBER': ['INV-001', 'INV-002', 'INV-003'],
        'Invoice Date': [date(2023, 1, 1), date(2023, 2, 1), date(2023, 3, 1)],
        'Invoice Amount': [100.5, 200, 300],
        'Currency': ['USD', 'EUR', 'GBP']
    }
    data_portal = {
        'INVOICE NUMBER': ['INV-001', 'INV-002', 'INV-004'],
        'Invoice Date': [date(2023, 1, 2), date(2023, 2, 1), date(2023, 4, 1)],
        'Invoice Amount': [100.5, 200, 400],
        'Currency': ['USD', 'EUR', 'GBP']
    }
    sap_data = DataFrame(data_sap)
    portal_data = DataFrame(data_portal)

    # Find the discrepancies
    invoices_only_in_sap, invoices_only_in_portal, discrepant_invoices = find_invoice_discrepancies(sap_data, portal_data)

    # Check the discrepancies
    assert invoices_only_in_sap == ['INV-003']
    assert invoices_only_in_portal == ['INV-004']
    assert discrepant_invoices == [['INV-001', 'Date', date(2023, 1, 1), date(2023, 1, 2)]]

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])