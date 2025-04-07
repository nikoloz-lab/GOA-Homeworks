def age_in_days(year, month, day, ref_year, ref_month, ref_day):
    """
    Calculate age in days from the birth date (year, month, day) to the reference date (ref_year, ref_month, ref_day).
    """
    # Create date objects for birth date and reference date
    birth_date = date(year, month, day)
    reference_date = date(ref_year, ref_month, ref_day)
    
    # Calculate the difference in days
    days_difference = (reference_date - birth_date).days
    
    # Return the result
    return f"You are {days_difference} days old"