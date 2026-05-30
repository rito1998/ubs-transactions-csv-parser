from pathlib import Path

from ubs_transactions_csv_parser import AccountExportData


def _load_test_export_data() -> AccountExportData:
	csv_path = Path(__file__).with_name("test_transactions.csv")
	return AccountExportData.from_csv(csv_path)


def test_parse_transactions_count() -> None:
	export_data = _load_test_export_data()
	assert len(export_data.transactions) == 3


def test_transactions_are_unique() -> None:
	export_data = _load_test_export_data()
	assert len(export_data.transactions) == len(set(export_data.transactions))
