from models import Transaction


def calculate_income(transactions):
    return sum(t.amount for t in transactions if t.type == "income")

def calculate_expense(transactions):
    return sum(t.amount for t in transactions if t.type == "expense")

def calculate_balance(transactions):
    income=calculate_income(transactions)
    expense=calculate_expense(transactions)
    return income-expense

def category_breakdown(transactions):
    breakdown = {}

    for t in transactions:
        breakdown[t.category] = breakdown.get(t.category, 0) + t.amount

    return breakdown

def monthly_summary(transactions):
    summary = {}

    for t in transactions:
        month = t.date.strftime("%Y-%m")
        summary[month] = summary.get(month, 0) + t.amount

    return summary


def recent_activity(transactions, limit=5):
    return sorted(transactions, key=lambda x: x.date, reverse=True)[:limit]