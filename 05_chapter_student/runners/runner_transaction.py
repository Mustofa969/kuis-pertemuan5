from processors.transaction_loop import Transactions 

def run_transaction_loop() -> None:
    print("=== [STUDI KASUS 1: TRANSACTION (STANDARD LOOP)] ===")
    # Inisiasi Object 
    trs: Transactions = Transactions(file_path='data/transactions.json', tax_rate=0.11)
    
    trs.load_data()
    trs.process_data()
    trs.export_to_csv(output_path='data/success_transactions_clean.csv')
    print()