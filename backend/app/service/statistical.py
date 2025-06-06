# from datetime import datetime, timedelta
# from sqlalchemy import func
# from sqlalchemy.orm import Session
# from app.models import Passenger, Booking, Flight


# def get_ticket_count_by_period(db: Session, period: str = "day"):
#     """
#     Calculate total ticket count for different time periods

#     :param db: Database session
#     :param period: 'day', 'week', 'month', or 'year'
#     :return: Total number of tickets
#     """
#     # Get the current date
#     now = datetime.now()

#     # Base query to count passengers through bookings
#     query = db.query(func.count(Passenger.passenger_id))

#     # Apply time-based filtering based on the period
#     if period == 'day':
#         # Trả về số vé theo từng giờ trong ngày
#         hourly_counts = {}
#         for hour in range(24):
#             start_time = now.replace(hour=hour, minute=0, second=0, microsecond=0)
#             end_time = start_time + timedelta(hours=1)
#             count = (
#                 query.join(Booking, Passenger.booking_id == Booking.booking_id)
#                 .join(Flight, Booking.flight_id == Flight.flight_id)
#                 .filter(
#                     Flight.estimated_departure_time >= start_time,
#                     Flight.estimated_departure_time < end_time
#                 )
#                 .scalar()
#             )
#             hourly_counts[f"{hour}:00"] = count or 0
#         return hourly_counts
    
#     elif period == 'week':
#         # Trả về số vé theo từng ngày trong tuần
#         daily_counts = {}
#         start_of_week = now - timedelta(days=now.weekday())  # Thứ 2 đầu tuần
#         for i in range(7):
#             day_start = start_of_week + timedelta(days=i)
#             day_start = day_start.replace(hour=0, minute=0, second=0, microsecond=0)
#             day_end = day_start + timedelta(days=1)
#             count = (
#                 query.join(Booking, Passenger.booking_id == Booking.booking_id)
#                 .join(Flight, Booking.flight_id == Flight.flight_id)
#                 .filter(
#                     Flight.estimated_departure_time >= day_start,
#                     Flight.estimated_departure_time < day_end
#                 )
#                 .scalar()
#             )
#             day_name = day_start.strftime("%A")
#             daily_counts[day_name] = count or 0
#         return daily_counts
    
#     elif period == 'month':
#         # Trả về tổng số vé theo từng tuần trong tháng
#         weekly_counts = {}
#         start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

#         for week in range(4):  # Giả định chia thành 4 tuần
#             week_start = start_of_month + timedelta(days=week * 7)
#             week_end = week_start + timedelta(days=7)

#             # Nếu tuần cuối vượt quá ngày cuối tháng, giới hạn đến ngày cuối tháng
#             if week == 3:  # Tuần cuối cùng
#                 next_month = (start_of_month + timedelta(days=32)).replace(day=1)
#                 week_end = next_month

#             count = (
#                 query.join(Booking, Passenger.booking_id == Booking.booking_id)
#                 .join(Flight, Booking.flight_id == Flight.flight_id)
#                 .filter(
#                     Flight.estimated_departure_time >= week_start,
#                     Flight.estimated_departure_time < week_end,
#                 )
#                 .scalar()
#             )
#             weekly_counts[f"week_{week + 1}"] = count or 0
#         return weekly_counts

#     elif period == "year":
#         # Trả về tổng số vé cho từng tháng của năm
#         result = {}
#         for month in range(1, 13):
#             month_start = now.replace(
#                 month=month, day=1, hour=0, minute=0, second=0, microsecond=0
#             )
#             if month == 12:
#                 month_end = datetime(now.year + 1, 1, 1)
#             else:
#                 month_end = now.replace(month=month + 1, day=1)
#             count = (
#                 query.join(Booking, Passenger.booking_id == Booking.booking_id)
#                 .join(Flight, Booking.flight_id == Flight.flight_id)
#                 .filter(
#                     Flight.estimated_departure_time >= month_start,
#                     Flight.estimated_departure_time < month_end,
#                 )
#                 .scalar()
#             )
#             result[f"month_{month}"] = count or 0
#         return result

#     else:
#         raise ValueError("Invalid period. Choose 'day', 'week', 'month', or 'year'.")

#     # Execute and return the count
#     return query.scalar()


# # Example usage functions
# def get_daily_ticket_count(db: Session):
#     """Get total tickets for today"""
#     return get_ticket_count_by_period(db, "day")


# def get_weekly_ticket_count(db: Session):
#     """Get total tickets for this week"""
#     return get_ticket_count_by_period(db, "week")


# def get_monthly_ticket_count(db: Session):
#     """Get total tickets for this month"""
#     return get_ticket_count_by_period(db, "month")


# def get_yearly_ticket_count(db: Session):
#     """Get total tickets for this year"""
#     return get_ticket_count_by_period(db, "year")


# def get_ticket_count_details(db: Session):
#     """
#     Get ticket counts for different time periods

#     :param db: Database session
#     :return: Dictionary with ticket counts
#     """
#     print("Getting ticket count details")
#     return {
#         "daily": get_daily_ticket_count(db),
#         "weekly": get_weekly_ticket_count(db),
#         "monthly": get_monthly_ticket_count(db),
#         "yearly": get_yearly_ticket_count(db),
#     }

# def get_cancelled_ticket_count_by_period(db: Session, period: str = "day"):
#     """
#     Calculate total cancelled tickets for different time periods

#     :param db: Database session
#     :param period: 'day', 'week', 'month', or 'year'
#     :return: Total number of cancelled tickets
#     """
#     # Get the current date
#     now = datetime.now()

#     # Base query to count cancelled bookings
#     query = db.query(func.count(Booking.booking_id)).filter(Booking.cancelled == True)

#     if period == "day":
#         # Trả về số vé bị hủy theo từng giờ trong ngày
#         hourly_counts = {}
#         for hour in range(24):
#             start_time = now.replace(hour=hour, minute=0, second=0, microsecond=0)
#             end_time = start_time + timedelta(hours=1)
#             count = (
#                 query.filter(
#                     Booking.booking_date >= start_time,
#                     Booking.booking_date < end_time,
#                 )
#                 .scalar()
#             )
#             hourly_counts[f"{hour}:00"] = count or 0
#         return hourly_counts

#     elif period == "week":
#         # Trả về số vé bị hủy theo từng ngày trong tuần
#         daily_counts = {}
#         start_of_week = now - timedelta(days=now.weekday())  # Thứ 2 đầu tuần
#         for i in range(7):
#             day_start = start_of_week + timedelta(days=i)
#             day_start = day_start.replace(hour=0, minute=0, second=0, microsecond=0)
#             day_end = day_start + timedelta(days=1)
#             count = (
#                 query.filter(
#                     Booking.booking_date >= day_start,
#                     Booking.booking_date < day_end,
#                 )
#                 .scalar()
#             )
#             day_name = day_start.strftime("%A")
#             daily_counts[day_name] = count or 0
#         return daily_counts

#     elif period == "month":
#         # Trả về số vé bị hủy theo từng tuần trong tháng
#         weekly_counts = {}
#         start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

#         for week in range(4):  # Giả định chia thành 4 tuần
#             week_start = start_of_month + timedelta(days=week * 7)
#             week_end = week_start + timedelta(days=7)

#             # Nếu tuần cuối vượt quá ngày cuối tháng, giới hạn đến ngày cuối tháng
#             if week == 3:
#                 next_month = (start_of_month + timedelta(days=32)).replace(day=1)
#                 week_end = next_month

#             count = (
#                 query.filter(
#                     Booking.booking_date >= week_start,
#                     Booking.booking_date < week_end,
#                 )
#                 .scalar()
#             )
#             weekly_counts[f"week_{week + 1}"] = count or 0
#         return weekly_counts

#     elif period == "year":
#         # Trả về số vé bị hủy cho từng tháng của năm
#         result = {}
#         for month in range(1, 13):
#             month_start = now.replace(
#                 month=month, day=1, hour=0, minute=0, second=0, microsecond=0
#             )
#             if month == 12:
#                 month_end = datetime(now.year + 1, 1, 1)
#             else:
#                 month_end = now.replace(month=month + 1, day=1)
#             count = (
#                 query.filter(
#                     Booking.booking_date >= month_start,
#                     Booking.booking_date < month_end,
#                 )
#                 .scalar()
#             )
#             result[f"month_{month}"] = count or 0
#         return result

#     else:
#         raise ValueError("Invalid period. Choose 'day', 'week', 'month', or 'year'.")



from datetime import datetime, timedelta
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models import Passenger, Booking, Flight


def get_ticket_statistics_by_period(db: Session, period: str = "day"):
    """
    Get ticket statistics (bought and cancelled) for different time periods.

    :param db: Database session
    :param period: 'day', 'week', 'month', or 'year'
    :return: Dictionary containing ticket_bought and ticket_cancelled counts
    """
    # Get the current date
    now = datetime.now()

    # Base queries
    ticket_bought_query = db.query(func.count(Passenger.passenger_id))
    ticket_cancel_query = db.query(func.count(Passenger.passenger_id))

    if period == "day":
        # Số liệu theo giờ trong ngày
        hourly_stats = {}
        for hour in range(24):
            start_time = now.replace(hour=hour, minute=0, second=0, microsecond=0)
            end_time = start_time + timedelta(hours=1)
            ticket_bought = (
                ticket_bought_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= start_time,
                    Flight.estimated_departure_time < end_time,
                    Booking.cancelled == False
                )
                .scalar()
            )
            ticket_cancel = (
                ticket_cancel_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= start_time,
                    Flight.estimated_departure_time < end_time,
                    Booking.cancelled == True
                )
                .scalar()
            )
            hourly_stats[f"{hour}:00"] = {
                "tickets_bought": ticket_bought or 0,
                "tickets_canceled": ticket_cancel or 0,
            }
        return hourly_stats

    elif period == "week":
        # Số liệu theo ngày trong tuần
        daily_stats = {}
        start_of_week = now - timedelta(days=now.weekday())  # Thứ 2 đầu tuần
        for i in range(7):
            day_start = start_of_week + timedelta(days=i)
            day_start = day_start.replace(hour=0, minute=0, second=0, microsecond=0)
            day_end = day_start + timedelta(days=1)
            ticket_bought = (
                ticket_bought_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= day_start,
                    Flight.estimated_departure_time < day_end,
                    Booking.cancelled == False
                )
                .scalar()
            )
            ticket_cancel = (
                ticket_cancel_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= day_start,
                    Flight.estimated_departure_time < day_end,
                    Booking.cancelled == True
                )
                .scalar()
            )
            day_name = day_start.strftime("%A")
            daily_stats[day_name] = {
                "tickets_bought": ticket_bought or 0,
                "tickets_canceled": ticket_cancel or 0,
            }
        return daily_stats

    elif period == "month":
        # Số liệu theo tuần trong tháng
        weekly_stats = {}
        start_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        for week in range(4):  # Giả định chia thành 4 tuần
            week_start = start_of_month + timedelta(days=week * 7)
            week_end = week_start + timedelta(days=7)

            if week == 3:  # Tuần cuối cùng
                next_month = (start_of_month + timedelta(days=32)).replace(day=1)
                week_end = next_month

            ticket_bought = (
                ticket_bought_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= week_start,
                    Flight.estimated_departure_time < week_end,
                    Booking.cancelled == False
                )
                .scalar()
            )
            ticket_cancel = (
                ticket_cancel_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= week_start,
                    Flight.estimated_departure_time < week_end,
                    Booking.cancelled == True
                )
                .scalar()
            )
            weekly_stats[f"week_{week + 1}"] = {
                "tickets_bought": ticket_bought or 0,
                "tickets_canceled": ticket_cancel or 0,
            }
        return weekly_stats

    elif period == "year":
        # Số liệu theo tháng trong năm
        monthly_stats = {}
        for month in range(1, 13):
            month_start = now.replace(
                month=month, day=1, hour=0, minute=0, second=0, microsecond=0
            )
            if month == 12:
                month_end = datetime(now.year + 1, 1, 1)
            else:
                month_end = now.replace(month=month + 1, day=1)
            ticket_bought = (
                ticket_bought_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= month_start,
                    Flight.estimated_departure_time < month_end,
                    Booking.cancelled == False
                )
                .scalar()
            )
            ticket_cancel = (
                ticket_cancel_query
                .join(Booking, Passenger.booking_id == Booking.booking_id)
                .join(Flight, Booking.flight_id == Flight.flight_id)
                .filter(
                    Flight.estimated_departure_time >= month_start,
                    Flight.estimated_departure_time < month_end,
                    Booking.cancelled == True
                )
                .scalar()
            )
            monthly_stats[f"month_{month}"] = {
                "tickets_bought": ticket_bought or 0,
                "tickets_canceled": ticket_cancel or 0,
            }
        return monthly_stats

    else:
        raise ValueError("Invalid period. Choose 'day', 'week', 'month', or 'year'.")


# Example usage functions
# Example usage functions
def get_daily_ticket_count(db: Session):
    """Get total tickets for today"""
    return get_ticket_statistics_by_period(db, "day")


def get_weekly_ticket_count(db: Session):
    """Get total tickets for this week"""
    return get_ticket_statistics_by_period(db, "week")


def get_monthly_ticket_count(db: Session):
    """Get total tickets for this month"""
    return get_ticket_statistics_by_period(db,"month")


def get_yearly_ticket_count(db: Session):
    """Get total tickets for this year"""
    return get_ticket_statistics_by_period(db, "year")


def get_ticket_count_details(db: Session):
    """
    Get ticket counts for different time periods

    :param db: Database session
    :return: Dictionary with ticket counts
    """
    print("Getting ticket count details")
    return {
        "daily": get_daily_ticket_count(db),
        "weekly": get_weekly_ticket_count(db),
        "monthly": get_monthly_ticket_count(db),
        "yearly": get_yearly_ticket_count(db),
    }
