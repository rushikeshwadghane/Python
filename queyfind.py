all_tables = set([
    "tbl_credit_note_mst",
    "tbl_credit_note_details",
    "tbl_credit_note_details_history",
    "tbl_credit_note_mst_history",
    "tbl_credit_note_sub_details",
    "tbl_credit_note_sub_details_history",
    "tbl_employee_expense_booking_mst",
    "tbl_employee_expense_booking_details",
    "tbl_expense_booking_mst",
    "tbl_expense_booking_details_history",
    "tbl_expense_booking_mst_history",
    "tbl_fpc_farmer_bill_mst",
    "tbl_fpc_farmer_bill_mst_history",
    "tbl_grn_mst",
    "tbl_grn_details",
    "tbl_grn_mst_history",
    "tbl_inventory_mst",
    "tbl_inventory_details",
    "tbl_inventory_details_history",
    "tbl_inventory_mst_history",
    "tbl_inventory_summary_details",
    "tbl_inventory_summary_details_history",
    "tbl_invoice_mst",
    "tbl_invoice_details",
    "tbl_invoice_details_history",
    "tbl_invoice_mst_history",
    "tbl_lot_creation_details",
    "tbl_lot_creation_details_history",
    "tbl_lot_creation_mst",
    "tbl_lot_creation_mst_history",
    "tbl_payable_ledger",
    "tbl_payment_details",
    "tbl_payment_details_history",
    "tbl_payment_mst_history",
    "tbl_purchase_booking_details",
    "tbl_purchase_booking_details_history",
    "tbl_purchase_order",
    "tbl_purchase_order_details",
    "tbl_qc_mst",
    "tbl_qc_details",
    "tbl_receipt_mst",
    "tbl_recept_accounting",
    "tbl_receipt_details",
    "tbl_receipt_details_history",
    "tbl_receipt_mst_history",
    "tbl_receivable_ledger",
    "tbl_sales_order_mst",
    "tbl_sales_order_details_history",
    "tbl_sales_order_mst_history",
    "tbl_purchase_booking_mst",
    "tbl_purchase_booking_mst_history",
    "tbl_debit_note_mst",
    "tbl_debit_note_mst_history",
    "tbl_allocation_details",
    "tbl_allocation_mst",
    "tbl_credit_note_accounting",
    "tbl_credit_note_accounting_history",
    "tbl_debit_note_accounting",
    "tbl_debit_note_accounting_history",
    "tbl_debit_note_details",
    "tbl_debit_note_details_history",
    "tbl_debit_note_sub_details",
    "tbl_debit_note_sub_details_history",
    "tbl_dispatch_note_details",
    "tbl_dispatch_note_details_history",
    "tbl_dispatch_note_mst",
    "tbl_dispatch_note_mst_history",
    "tbl_dispatch_quality_parameter_details",
    "tbl_dispatch_quality_parameter_details_history",
    "tbl_employee_expense_booking_accounting",
    "tbl_employee_expense_booking_accounting_history",
    "tbl_employee_expense_booking_details_history",
    "tbl_employee_expense_booking_mst_history",
    "tbl_expense_booking_accounting",
    "tbl_expense_booking_accounting_history",
    "tbl_expense_booking_details",
    "tbl_fpc_farmer_bill_details",
    "tbl_fpc_farmer_bill_details_history",
    "tbl_gate_pass_details",
    "tbl_gate_pass_details_history",
    "tbl_gate_pass_mst",
    "tbl_gate_pass_mst_history",
    "tbl_grn_details_history",
    "tbl_inventory_accounting",
    "tbl_inventory_accounting_history",
    "tbl_invoice_accounting",
    "tbl_invoice_accounting_history",
    "tbl_journal_details",
    "tbl_journal_details_history",
    "tbl_journal_mst",
    "tbl_journal_mst_history",
    "tbl_ledger",
    "tbl_ledger_history",
    "tbl_payable_ledger_history",
    "tbl_payment_accounting",
    "tbl_payment_accounting_history",
    "tbl_purchase_accounting",
    "tbl_purchase_accounting_history",
    "tbl_payment_mst",
    "tbl_purchase_booking_sub_details",
    "tbl_purchase_booking_sub_details_history",
    "tbl_purchase_order_details_history",
    "tbl_purchase_order_history",
    "tbl_qc_details_history",
    "tbl_qc_mst_history",
    "tbl_qc_quality_parameter_details",
    "tbl_qc_quality_parameter_details_history",
    "tbl_receipt_accounting_history",
    "tbl_receivable_ledger_history",
    "tbl_so_quality_parameter_details",
    "tbl_so_quality_parameter_details_history",
    "tbl_stock_adjustment_accounting",
    "tbl_stock_adjustment_accounting_history",
    "tbl_stock_adjustment_details",
    "tbl_stock_adjustment_details_history",
    "tbl_stock_adjustment_mst",
    "tbl_stock_adjustment_mst_history",
    "tbl_stock_transfer_accounting",
    "tbl_stock_transfer_accounting_history",
    "tbl_stock_transfer_details",
    "tbl_stock_transfer_details_history",
    "tbl_stock_transfer_mst",
    "tbl_stock_transfer_mst_history"
])

delete_query_text = """
DELETE FROM tbl_credit_note_details_history;
DELETE FROM tbl_credit_note_mst_history;
DELETE FROM tbl_credit_note_sub_details_history;
DELETE FROM tbl_debit_note_mst_history;
DELETE FROM tbl_debit_note_details_history;
DELETE FROM tbl_debit_note_sub_details_history;
DELETE FROM tbl_dispatch_note_details_history;
DELETE FROM tbl_dispatch_note_mst_history;
DELETE FROM tbl_dispatch_quality_parameter_details_history;
DELETE FROM tbl_employee_expense_booking_accounting_history;
DELETE FROM tbl_employee_expense_booking_details_history;
DELETE FROM tbl_employee_expense_booking_mst_history;
DELETE FROM tbl_expense_booking_accounting_history;
DELETE FROM tbl_expense_booking_details_history;
DELETE FROM tbl_expense_booking_mst_history;
DELETE FROM tbl_fpc_farmer_bill_mst_history;
DELETE FROM tbl_fpc_farmer_bill_details_history;
DELETE FROM tbl_gate_pass_details_history;
DELETE FROM tbl_gate_pass_mst_history;
DELETE FROM tbl_grn_details_history;
DELETE FROM tbl_grn_mst_history;
DELETE FROM tbl_inventory_accounting_history;
DELETE FROM tbl_inventory_details_history;
DELETE FROM tbl_inventory_mst_history;
DELETE FROM tbl_inventory_summary_details_history;
DELETE FROM tbl_invoice_accounting_history;
DELETE FROM tbl_invoice_details_history;
DELETE FROM tbl_invoice_mst_history;
DELETE FROM tbl_journal_details_history;
DELETE FROM tbl_journal_mst_history;
DELETE FROM tbl_ledger_history;
DELETE FROM tbl_payable_ledger_history;
DELETE FROM tbl_payment_accounting_history;
DELETE FROM tbl_payment_details_history;
DELETE FROM tbl_payment_mst_history;
DELETE FROM tbl_purchase_accounting_history;
DELETE FROM tbl_purchase_booking_details_history;
DELETE FROM tbl_purchase_booking_mst_history;
DELETE FROM tbl_purchase_booking_sub_details_history;
DELETE FROM tbl_purchase_order_details_history;
DELETE FROM tbl_purchase_order_history;
DELETE FROM tbl_qc_details_history;
DELETE FROM tbl_qc_mst_history;
DELETE FROM tbl_qc_quality_parameter_details_history;
DELETE FROM tbl_receipt_accounting_history;
DELETE FROM tbl_receipt_details_history;
DELETE FROM tbl_receipt_mst_history;
DELETE FROM tbl_receivable_ledger_history;
DELETE FROM tbl_sales_order_details_history;
DELETE FROM tbl_sales_order_mst_history;
DELETE FROM tbl_so_quality_parameter_details_history;
DELETE FROM tbl_stock_adjustment_accounting_history;
DELETE FROM tbl_stock_adjustment_details_history;
DELETE FROM tbl_stock_adjustment_mst_history;
DELETE FROM tbl_stock_transfer_accounting_history;
DELETE FROM tbl_stock_transfer_details_history;
DELETE FROM tbl_stock_transfer_mst_history;
DELETE FROM tbl_credit_note_accounting;
DELETE FROM tbl_debit_note_accounting;
DELETE FROM tbl_employee_expense_booking_accounting;
DELETE FROM tbl_expense_booking_accounting;
DELETE FROM tbl_inventory_accounting;
DELETE FROM tbl_invoice_accounting;
DELETE FROM tbl_journal_details;
DELETE FROM tbl_journal_mst;
DELETE FROM tbl_payment_accounting;
DELETE FROM tbl_purchase_accounting;
DELETE FROM tbl_receipt_accounting;
DELETE FROM tbl_stock_adjustment_accounting;
DELETE FROM tbl_stock_transfer_accounting;
DELETE FROM tbl_credit_note_sub_details;
DELETE FROM tbl_debit_note_sub_details;
DELETE FROM tbl_purchase_booking_sub_details;
DELETE FROM tbl_inventory_summary_details;
DELETE FROM tbl_qc_quality_parameter_details;
DELETE FROM tbl_so_quality_parameter_details;
DELETE FROM tbl_dispatch_quality_parameter_details;
DELETE FROM tbl_credit_note_details;
DELETE FROM tbl_debit_note_details;
DELETE FROM tbl_dispatch_note_details;
DELETE FROM tbl_employee_expense_booking_details;
DELETE FROM tbl_expense_booking_details;
DELETE FROM tbl_fpc_farmer_bill_details;
DELETE FROM tbl_gate_pass_details;
DELETE FROM tbl_grn_details;
DELETE FROM tbl_inventory_details;
DELETE FROM tbl_invoice_details;
DELETE FROM tbl_lot_creation_details;
DELETE FROM tbl_payment_details;
DELETE FROM tbl_purchase_booking_details;
DELETE FROM tbl_purchase_order_details;
DELETE FROM tbl_qc_details;
DELETE FROM tbl_receipt_details;
DELETE FROM tbl_sales_order_mst;
DELETE FROM tbl_stock_adjustment_details;
DELETE FROM tbl_stock_transfer_details;
DELETE FROM tbl_credit_note_mst;
DELETE FROM tbl_debit_note_mst;
DELETE FROM tbl_dispatch_note_mst;
DELETE FROM tbl_employee_expense_booking_mst;
DELETE FROM tbl_expense_booking_mst;
DELETE FROM tbl_fpc_farmer_bill_mst;
DELETE FROM tbl_gate_pass_mst;
DELETE FROM tbl_grn_mst;
DELETE FROM tbl_inventory_mst;
DELETE FROM tbl_invoice_mst;
DELETE FROM tbl_lot_creation_mst;
DELETE FROM tbl_payment_mst;
DELETE FROM tbl_purchase_booking_mst;
DELETE FROM tbl_purchase_order;
DELETE FROM tbl_qc_mst;
DELETE FROM tbl_receipt_mst;
DELETE FROM tbl_allocation_details;
DELETE FROM tbl_allocation_mst;
DELETE FROM tbl_credit_note_accounting_history;
DELETE FROM tbl_sales_order_mst;
DELETE FROM tbl_sales_order_mst;
DELETE FROM tbl_sales_order_mst;
DELETE FROM tbl_sales_order_mst;
DELETE FROM tbl_sales_order_mst;
"""

import re

# Extract table names from delete query using regex
used_tables = set(re.findall(r"DELETE FROM (\w+);", delete_query_text))

# Find tables that were not used in delete query
missing_tables = all_tables - used_tables

print("Missing tables in the DELETE script:")
for table in sorted(missing_tables):
    print(table)
