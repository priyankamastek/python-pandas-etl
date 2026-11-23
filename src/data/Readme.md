import pandas as pd

class OrderProcessor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load(self):
        """Load order data"""
        self.df = pd.read_csv(self.file_path)

    def remove_duplicates(self):
        """Remove duplicate orders"""
        self.df.drop_duplicates(inplace=True)

    def standardize_status(self):
        """Convert status values to lowercase and remove extra spaces"""
        self.df["status"] = self.df["status"].str.strip().str.lower()

    def standardize_country(self):
        """Standardize country names"""
        self.df["country"] = self.df["country"].str.strip().str.title()

        self.df["country"] = self.df["country"].replace({
            "Uk": "United Kingdom",
            "United Kingdom": "United Kingdom"
        })

    def fill_missing_customer_ids(self):
        """Replace missing customer IDs"""
        self.df["customer_id"] = self.df["customer_id"].fillna("UNKNOWN")

    def convert_order_date(self):
        """Parse different date formats"""
        self.df["order_date"] = pd.to_datetime(
            self.df["order_date"],
            errors="coerce"
        )

    def clean_unit_price(self):
        """Remove currency symbols and convert to numeric"""
        self.df["unit_price"] = (
            self.df["unit_price"]
            .astype(str)
            .str.replace("£", "", regex=False)
        )

        self.df["unit_price"] = pd.to_numeric(
            self.df["unit_price"],
            errors="coerce"
        )

    def clean_quantity(self):
        """Convert quantity to numeric"""
        self.df["quantity"] = pd.to_numeric(
            self.df["quantity"],
            errors="coerce"
        )

    def get_invalid_orders(self):
        """Find bad-quality records"""

        return self.df[
            (self.df["quantity"] <= 0) |
            (self.df["unit_price"].isna()) |
            (self.df["order_date"].isna())
        ]

    def calculate_order_value(self):
        """Create new business metric"""

        self.df["order_value"] = (
            self.df["quantity"] *
            self.df["unit_price"]
        )

    def get_shipped_orders(self):
        """Return shipped orders only"""

        return self.df[
            self.df["status"] == "shipped"
        ]

    def summary(self):

        print(f"Total Orders : {len(self.df)}")
        print(f"Columns : {len(self.df.columns)}")
        print(f"Duplicates : {self.df.duplicated().sum()}")



# Inheritance
Inheritance allows us to create specialised data-processing classes that reuse common ETL logic from a parent class while adding source-specific business rules.

