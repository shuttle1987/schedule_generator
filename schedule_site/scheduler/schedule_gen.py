"""Generate a schedule with the given staff in the database"""

__all__ = ['InfeasibleSchedule', 'generate_schedule']

class InfeasibleSchedule(Exception):
    """Exception for infeasibility related errors"""

def generate_schedule():
    """Attempts to generate a schedule for the given set of staff and requirements"""
    #would use a solver such as logilab https://www.logilab.org/852
    #or some other suitable constraint satisfaction solver library
    raise NotImplementedError
