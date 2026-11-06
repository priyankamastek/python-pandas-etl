# To execute the code of this file
# in project directory, on CMD: uv run python -m foundation.function_dates


from datetime import datetime, date, timedelta

# Common date formats seen in source files (CSV, APIs, legacy systems)
KNOWN_FORMATS = ['%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%m/%d/%Y', '%Y%m%d', '%d-%b-%Y']


# Parse a date string that may arrive in different formats
# Returns None when the value cannot be parsed (bad record)
def parse_date(date_str, formats=KNOWN_FORMATS):
    if date_str is None or str(date_str).strip() == '':
        return None
    for fmt in formats:
        try:
            return datetime.strptime(str(date_str).strip(), fmt).date()
        except ValueError:
            continue
    return None


# Convert any supported date string to the standard ISO format (YYYY-MM-DD)
def standardize_date(date_str):
    parsed = parse_date(date_str)
    if parsed is None:
        return None
    return parsed.strftime('%Y-%m-%d')


# Number of days between two dates (end - start)
def days_between(start_date, end_date):
    return (end_date - start_date).days


# Calculate age in completed years as of a given date (default: today)
def calculate_age(birth_date, as_of=None):
    if as_of is None:
        as_of = date.today()
    age = as_of.year - birth_date.year
    # Subtract one year if the birthday has not happened yet this year
    if (as_of.month, as_of.day) < (birth_date.month, birth_date.day):
        age = age - 1
    return age


# Count working days (Mon-Fri) between two dates, both inclusive
# Optional holidays list is excluded from the count
def business_days_between(start_date, end_date, holidays=None):
    if holidays is None:
        holidays = []
    count = 0
    current = start_date
    while current <= end_date:
        # weekday(): Monday = 0 ... Sunday = 6
        if current.weekday() < 5 and current not in holidays:
            count = count + 1
        current = current + timedelta(days=1)
    return count


# First and last day of the month - useful for monthly partitions / reports
def month_start_end(any_date):
    month_start = any_date.replace(day=1)
    # Jump to next month, then step back one day
    next_month = (month_start + timedelta(days=32)).replace(day=1)
    month_end = next_month - timedelta(days=1)
    return month_start, month_end


# Return the quarter label for a date, e.g. '2026-Q4'
def get_quarter(any_date):
    quarter = (any_date.month - 1) // 3 + 1
    return f'{any_date.year}-Q{quarter}'


# Build the list of dates for an incremental / backfill load window
def generate_date_range(start_date, end_date):
    dates = []
    current = start_date
    while current <= end_date:
        dates.append(current)
        current = current + timedelta(days=1)
    return dates


# Build a partition path for a data lake, e.g. 'sales/year=2026/month=10/day=29'
def partition_path(base, any_date):
    return f'{base}/year={any_date.year}/month={any_date.month:02d}/day={any_date.day:02d}'


# Check whether a record is older than N days (data retention / stale check)
def is_stale(record_date, max_age_days, as_of=None):
    if as_of is None:
        as_of = date.today()
    return days_between(record_date, as_of) > max_age_days


# Runs only when this file is executed directly, not when it is imported
if __name__ == "__main__":
    # Parse dates arriving in mixed formats
    raw_dates = ['2026-10-29', '29/10/2026', '20261029', '29-Oct-2026', 'bad-date', '']
    for raw in raw_dates:
        print(raw, '->', standardize_date(raw))

    start = date(2026, 10, 1)
    end = date(2026, 10, 31)
    print("Days between:", days_between(start, end))
    print("Business days:", business_days_between(start, end, holidays=[date(2026, 10, 2)]))

    print("Age:", calculate_age(date(1995, 12, 15), as_of=date(2026, 10, 29)))
    print("Month start/end:", month_start_end(date(2024, 2, 10)))
    print("Quarter:", get_quarter(date(2026, 10, 29)))

    print("Load window:", generate_date_range(date(2026, 10, 27), date(2026, 10, 29)))
    print("Partition:", partition_path('sales', date(2026, 10, 29)))
    print("Is stale:", is_stale(date(2026, 9, 1), max_age_days=30, as_of=date(2026, 10, 29)))
